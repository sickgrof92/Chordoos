import { Redirect, router, useLocalSearchParams } from 'expo-router';
import { useEffect, useMemo, useRef, useState } from 'react';
import { AccessibilityInfo, Animated, Easing, Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Character } from '../characters/Character.tsx';
import { Pod } from '../components/Pod.tsx';
import { Button, RarityPill } from '../components/ui.tsx';
import { haptic, play } from '../feedback.ts';
import { CHARACTER_BY_ID, RARITIES } from '../game/characters.ts';
import { openSurprise } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts } from '../theme.ts';

const HINTS = ['Tap to open!', 'Keep tapping!', 'Almost there!'];
const CONFETTI_COLORS = ['#FFE14D', '#7CFFB2', '#FF8FD8', '#53F3FF', '#FFFFFF', '#FF8A3D'];

export default function Reveal() {
  const params = useLocalSearchParams<{ kid: string; char: string; isNew: string; count: string }>();
  const { kid: getKid, state, saveKid } = useFamily();
  const insets = useSafeAreaInsets();
  const { width, height } = useWindowDimensions();
  const [stage, setStage] = useState(0);
  const [reduceMotion, setReduceMotion] = useState(false);

  const shake = useRef(new Animated.Value(0)).current;
  const pop = useRef(new Animated.Value(0)).current;
  const spin = useRef(new Animated.Value(0)).current;
  const flash = useRef(new Animated.Value(0)).current;

  const ch = CHARACTER_BY_ID[params.char];
  const kid = getKid(params.kid);
  const sound = state.settings?.sound ?? true;
  const cost = state.settings?.cost ?? 3;
  const rarity = ch?.rarity ?? 0;
  const rc = RARITIES[rarity].color;

  useEffect(() => {
    AccessibilityInfo.isReduceMotionEnabled().then(setReduceMotion).catch(() => {});
  }, []);

  useEffect(() => {
    if (stage < 3) return;
    const loop = Animated.loop(Animated.timing(spin, { toValue: 1, duration: 14000, easing: Easing.linear, useNativeDriver: true }));
    loop.start();
    return () => loop.stop();
  }, [stage, spin]);

  const confetti = useMemo(
    () =>
      Array.from({ length: reduceMotion ? 0 : 48 }, (_, i) => ({
        x: Math.random() * width,
        delay: Math.random() * 400,
        dur: 1600 + Math.random() * 1800,
        rot: Math.random() * 720,
        color: i % 6 === 0 ? rc : CONFETTI_COLORS[i % CONFETTI_COLORS.length],
        v: new Animated.Value(0),
      })),
    [width, rc, reduceMotion],
  );

  if (!ch || !kid) return <Redirect href="/" />;

  const tap = () => {
    const next = stage + 1;
    setStage(next);
    if (next < 3) {
      haptic.crack();
      play('crack', sound);
      shake.setValue(0);
      Animated.sequence(
        [1, -1, 0.7, -0.5, 0].map((v) => Animated.timing(shake, { toValue: v, duration: 70, useNativeDriver: true })),
      ).start();
      return;
    }
    haptic.success();
    play(rarity >= 3 ? 'revealBig' : 'reveal', sound);
    flash.setValue(1);
    Animated.timing(flash, { toValue: 0, duration: 700, useNativeDriver: true }).start();
    pop.setValue(0);
    Animated.spring(pop, { toValue: 1, useNativeDriver: true, friction: 5, tension: 80 }).start();
    confetti.forEach((p) =>
      Animated.timing(p.v, { toValue: 1, duration: p.dur, delay: p.delay, easing: Easing.in(Easing.quad), useNativeDriver: true }).start(),
    );
  };

  const again = () => {
    const r = openSurprise(kid, cost);
    if (!r) return;
    saveKid(r.kid);
    router.replace({ pathname: '/reveal', params: { kid: kid.id, char: r.character.id, isNew: r.isNew ? '1' : '0', count: String(r.count) } });
  };

  const rotate = shake.interpolate({ inputRange: [-1, 1], outputRange: ['-10deg', '10deg'] });
  const spinDeg = spin.interpolate({ inputRange: [0, 1], outputRange: ['0deg', '360deg'] });
  const charSize = Math.min(260, width * 0.66);

  return (
    <View style={[st.wrap, { paddingTop: insets.top + 20, paddingBottom: insets.bottom + 20 }]}>
      {stage < 3 ? (
        <Pressable onPress={tap} accessibilityRole="button" accessibilityLabel="Tap the surprise pod to open it" style={st.center}>
          <Animated.View
            style={{
              transform: [{ rotate }],
              shadowColor: stage >= 2 ? rc : 'transparent',
              shadowOpacity: 0.9,
              shadowRadius: 26,
              shadowOffset: { width: 0, height: 0 },
            }}
          >
            <Pod size={Math.min(220, width * 0.58)} color={stage >= 2 ? rc : '#FF6B4A'} cracks={stage} />
          </Animated.View>
          <Text style={st.hint}>{HINTS[stage]}</Text>
        </Pressable>
      ) : (
        <View style={st.center}>
          <Animated.View style={[st.rays, { borderColor: rc, transform: [{ rotate: spinDeg }] }]}>
            {Array.from({ length: 12 }, (_, i) => (
              <View key={i} style={[st.ray, { backgroundColor: rc, transform: [{ rotate: `${i * 30}deg` }] }]} />
            ))}
          </Animated.View>
          <Animated.View style={{ transform: [{ scale: pop.interpolate({ inputRange: [0, 1], outputRange: [0.2, 1] }) }], opacity: pop }}>
            <Character id={ch.id} size={charSize} />
          </Animated.View>
          <RarityPill rarity={rarity} big center />
          {params.isNew === '1' ? (
            <Text style={st.newTag}>NEW!</Text>
          ) : (
            <Text style={st.dupe}>You have {params.count} of these</Text>
          )}
          <Text style={st.name}>{ch.name}</Text>
          <Text style={st.flavor}>
            <Text style={{ fontFamily: fonts.bodyBold }}>{ch.style}</Text> · {ch.flavor}
          </Text>
          <View style={{ flexDirection: 'row', gap: 12, marginTop: 8, flexWrap: 'wrap', justifyContent: 'center' }}>
            <Button title="Yay!" kind="primary" big onPress={() => router.back()} />
            {kid.stars >= cost ? <Button title="Open another" big onPress={again} /> : null}
          </View>
        </View>
      )}

      {confetti.map((p, i) => (
        <Animated.View
          key={i}
          pointerEvents="none"
          style={[
            st.confetti,
            {
              left: p.x,
              backgroundColor: p.color,
              opacity: stage >= 3 ? 1 : 0,
              transform: [
                { translateY: p.v.interpolate({ inputRange: [0, 1], outputRange: [-30, height + 40] }) },
                { rotate: p.v.interpolate({ inputRange: [0, 1], outputRange: ['0deg', `${p.rot}deg`] }) },
              ],
            },
          ]}
        />
      ))}
      <Animated.View pointerEvents="none" style={[StyleSheet.absoluteFill, { backgroundColor: '#fff', opacity: flash }]} />
    </View>
  );
}

const st = StyleSheet.create({
  wrap: { flex: 1, backgroundColor: colors.night, alignItems: 'center', justifyContent: 'center', paddingHorizontal: 20 },
  center: { alignItems: 'center', justifyContent: 'center', gap: 12, maxWidth: 440, width: '100%' },
  hint: { fontFamily: fonts.display, fontSize: 28, color: '#fff', marginTop: 12 },
  rays: { position: 'absolute', top: -60, width: 420, height: 420, alignItems: 'center', justifyContent: 'center', opacity: 0.18 },
  ray: { position: 'absolute', width: 18, height: 420, borderRadius: 9 },
  newTag: { fontFamily: fonts.display, fontSize: 20, color: '#1B1530', backgroundColor: '#7CFFB2', paddingHorizontal: 14, borderRadius: 99, overflow: 'hidden', transform: [{ rotate: '-4deg' }] },
  dupe: { fontFamily: fonts.bodyBold, fontSize: 15, color: '#1B1530', backgroundColor: '#E5E0FF', paddingHorizontal: 12, paddingVertical: 2, borderRadius: 99, overflow: 'hidden' },
  name: { fontFamily: fonts.display, fontSize: 40, color: '#fff' },
  flavor: { fontFamily: fonts.body, fontSize: 16, color: '#E5E0FF', textAlign: 'center', maxWidth: 340 },
  confetti: { position: 'absolute', top: 0, width: 10, height: 16, borderRadius: 3 },
});

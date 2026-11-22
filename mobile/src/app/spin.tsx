import { Redirect, router, useLocalSearchParams } from 'expo-router';
import { useEffect, useMemo, useRef, useState } from 'react';
import { AccessibilityInfo, Animated, Easing, StyleSheet, Text, useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Button, Squish } from '../components/ui.tsx';
import { Wheel } from '../components/Wheel.tsx';
import { haptic, play } from '../feedback.ts';
import { canSpin, landingAngle, MIN_SLIVERS, spin, type Sliver } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts } from '../theme.ts';

const CONFETTI_COLORS = ['#FFE14D', '#7CFFB2', '#FF8FD8', '#53F3FF', '#FFFFFF', '#FF8A3D'];

export default function Spin() {
  const params = useLocalSearchParams<{ kid: string }>();
  const { kid: getKid, state, saveKid } = useFamily();
  const insets = useSafeAreaInsets();
  const { width, height } = useWindowDimensions();
  const kid = getKid(params.kid);
  const sound = state.settings?.sound ?? true;

  // The wheel as drawn. It stays as it was during a spin, even though the kid is saved straight away.
  const [shown, setShown] = useState<Sliver[]>(kid?.wheel ?? []);
  const [phase, setPhase] = useState<'ready' | 'spinning' | 'won'>('ready');
  const [won, setWon] = useState<Sliver | null>(null);
  const [reduceMotion, setReduceMotion] = useState(false);
  const rotation = useRef(new Animated.Value(0)).current;
  const pop = useRef(new Animated.Value(0)).current;
  const flash = useRef(new Animated.Value(0)).current;
  const lastTick = useRef(0);

  useEffect(() => {
    AccessibilityInfo.isReduceMotionEnabled().then(setReduceMotion).catch(() => {});
  }, []);

  // A click each time a slice boundary passes the pointer.
  useEffect(() => {
    const n = Math.max(shown.length, 1);
    const id = rotation.addListener(({ value }) => {
      const tick = Math.floor(value / (360 / n));
      if (tick !== lastTick.current) {
        lastTick.current = tick;
        play('tap', sound);
        haptic.tap();
      }
    });
    return () => rotation.removeListener(id);
  }, [rotation, shown.length, sound]);

  const confetti = useMemo(
    () =>
      Array.from({ length: reduceMotion ? 0 : 48 }, (_, i) => ({
        x: Math.random() * width,
        delay: Math.random() * 400,
        dur: 1600 + Math.random() * 1800,
        rot: Math.random() * 720,
        color: CONFETTI_COLORS[i % CONFETTI_COLORS.length],
        v: new Animated.Value(0),
      })),
    [width, reduceMotion, won],
  );

  useEffect(() => {
    if (phase !== 'won') return;
    confetti.forEach((p) =>
      Animated.timing(p.v, { toValue: 1, duration: p.dur, delay: p.delay, easing: Easing.in(Easing.quad), useNativeDriver: true }).start(),
    );
  }, [phase, confetti]);

  if (!kid) return <Redirect href="/" />;

  const go = () => {
    const r = spin(kid);
    if (!r) return;
    const wheel = kid.wheel;
    setShown(wheel);
    saveKid(r.kid);
    setPhase('spinning');
    haptic.bump();
    rotation.setValue(0);
    lastTick.current = 0;
    const target = landingAngle(r.index, wheel.length, reduceMotion ? 1 : 5, Math.random() * 2 - 1);
    Animated.timing(rotation, {
      toValue: target,
      duration: reduceMotion ? 1200 : 4800,
      easing: Easing.out(Easing.cubic),
      useNativeDriver: true,
    }).start(() => {
      setWon(r.sliver);
      setPhase('won');
      haptic.success();
      play('revealBig', sound);
      flash.setValue(1);
      Animated.timing(flash, { toValue: 0, duration: 700, useNativeDriver: true }).start();
      pop.setValue(0);
      Animated.spring(pop, { toValue: 1, useNativeDriver: true, friction: 5, tension: 80 }).start();
    });
  };


  const size = Math.min(width - 40, height * 0.55, 440);
  const ready = phase === 'ready' && canSpin(kid);

  return (
    <View style={[st.wrap, { paddingTop: insets.top + 14, paddingBottom: insets.bottom + 20 }]}>
      <View style={st.head}>
        <Squish label="Back" onPress={() => router.back()} disabled={phase === 'spinning'} style={st.back}>
          <Text style={st.backText}>‹</Text>
        </Squish>
        <Text style={st.title} numberOfLines={1}>{kid.name}'s wheel</Text>
      </View>

      <View style={st.center}>
        <Wheel wheel={shown} size={size} rotation={rotation} />
        {phase === 'ready' ? (
          ready ? (
            <Button title="SPIN!" kind="primary" big onPress={go} style={{ minWidth: 200 }} />
          ) : (
            <Text style={st.sub}>
              The wheel needs {MIN_SLIVERS} slices to spin. Buy {MIN_SLIVERS - kid.wheel.length} more in the prize shop.
            </Text>
          )
        ) : phase === 'spinning' ? (
          <Text style={st.sub}>Spinning…</Text>
        ) : null}
      </View>

      {phase === 'won' && won ? (
        <View style={[StyleSheet.absoluteFill, st.winWrap]}>
          <Animated.View style={[st.winCard, { opacity: pop, transform: [{ scale: pop.interpolate({ inputRange: [0, 1], outputRange: [0.4, 1] }) }] }]}>
            <Text style={st.youWon}>You won!</Text>
            <Text style={{ fontSize: 84 }}>{won.icon}</Text>
            <Text style={st.prize}>{won.name}</Text>
            <Text style={st.hint}>Show a grown-up to get your prize. Your wheel starts fresh now.</Text>
            <View style={{ flexDirection: 'row', gap: 12, flexWrap: 'wrap', justifyContent: 'center' }}>
              <Button title="Yay!" kind="primary" big onPress={() => router.back()} />
            </View>
          </Animated.View>
        </View>
      ) : null}

      {confetti.map((p, i) => (
        <Animated.View
          key={i}
          pointerEvents="none"
          style={[
            st.confetti,
            {
              left: p.x,
              backgroundColor: p.color,
              opacity: phase === 'won' ? 1 : 0,
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
  wrap: { flex: 1, backgroundColor: colors.night, paddingHorizontal: 20 },
  head: { flexDirection: 'row', alignItems: 'center', gap: 12, maxWidth: 760, width: '100%', alignSelf: 'center' },
  back: { width: 48, height: 48, borderRadius: 24, backgroundColor: '#2A2343', alignItems: 'center', justifyContent: 'center' },
  backText: { fontFamily: fonts.display, fontSize: 30, color: '#fff', marginTop: -4 },
  title: { flex: 1, fontFamily: fonts.display, fontSize: 26, color: '#fff' },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 26 },
  sub: { fontFamily: fonts.bodyBold, fontSize: 18, color: '#E5E0FF', textAlign: 'center', maxWidth: 340 },
  winWrap: { alignItems: 'center', justifyContent: 'center', backgroundColor: 'rgba(20,15,38,0.72)', padding: 20 },
  winCard: { backgroundColor: colors.surface, borderRadius: 32, padding: 26, alignItems: 'center', gap: 8, width: '100%', maxWidth: 400, borderWidth: 4, borderColor: colors.star },
  youWon: { fontFamily: fonts.display, fontSize: 24, color: colors.accent },
  prize: { fontFamily: fonts.display, fontSize: 34, lineHeight: 38, color: colors.ink, textAlign: 'center' },
  hint: { fontFamily: fonts.body, fontSize: 16, color: colors.muted, textAlign: 'center', marginBottom: 8 },
  confetti: { position: 'absolute', top: 0, width: 10, height: 16, borderRadius: 3 },
});

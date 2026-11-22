import { Redirect, router, useLocalSearchParams } from 'expo-router';
import { useEffect, useRef, useState } from 'react';
import { Animated, Pressable, ScrollView, StyleSheet, Text, useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Avatar, Body, Button, H2, Points, Squish } from '../../components/ui.tsx';
import { sliverColor, Wheel } from '../../components/Wheel.tsx';
import { haptic, play } from '../../feedback.ts';
import { buySliver, canSpin, isDone, MAX_SLIVERS, MIN_SLIVERS, pendingWins, refundSliver, toggleTask, type Prize } from '../../game/rules.ts';
import { useFamily } from '../../state/family.tsx';
import { colors, fonts, shadow } from '../../theme.ts';

export default function KidScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const { kid: getKid, state, today, saveKid } = useFamily();
  const insets = useSafeAreaInsets();
  const { width } = useWindowDimensions();
  const [tab, setTab] = useState<'tasks' | 'shop'>('tasks');
  const [note, setNote] = useState<string | null>(null);
  const pointScale = useRef(new Animated.Value(1)).current;
  const wiggle = useRef(new Animated.Value(0)).current;

  const kid = getKid(id);
  const settings = state.settings;
  const ready = !!kid && canSpin(kid);

  useEffect(() => {
    if (!ready) return;
    const loop = Animated.loop(
      Animated.sequence([
        Animated.delay(1200),
        Animated.timing(wiggle, { toValue: 1, duration: 90, useNativeDriver: true }),
        Animated.timing(wiggle, { toValue: -1, duration: 120, useNativeDriver: true }),
        Animated.timing(wiggle, { toValue: 0, duration: 110, useNativeDriver: true }),
      ]),
    );
    loop.start();
    return () => loop.stop();
  }, [ready, wiggle]);

  useEffect(() => {
    if (!note) return;
    const t = setTimeout(() => setNote(null), 2200);
    return () => clearTimeout(t);
  }, [note]);

  if (!kid || !settings) return <Redirect href="/" />;
  const { tasks, prizes } = settings;
  const left = tasks.filter((t) => !isDone(kid, t, today));
  const waiting = pendingWins(kid);
  const need = Math.max(0, MIN_SLIVERS - kid.wheel.length);

  const bump = () =>
    Animated.sequence([
      Animated.spring(pointScale, { toValue: 1.3, useNativeDriver: true, speed: 40 }),
      Animated.spring(pointScale, { toValue: 1, useNativeDriver: true, speed: 20 }),
    ]).start();

  const onTask = (taskId: string) => {
    const task = tasks.find((t) => t.id === taskId);
    if (!task) return;
    const r = toggleTask(kid, task, today);
    if (r.change === 'blocked') {
      haptic.warn();
      setNote('Those points were already spent on the wheel.');
      return;
    }
    saveKid(r.kid);
    if (r.change === 'done') {
      play('ding', settings.sound);
      haptic.success();
      setNote(`+${task.points} ★ Nice job!`);
      bump();
    }
  };

  const onBuy = (p: Prize) => {
    const r = buySliver(kid, p);
    if (!r.ok) {
      haptic.warn();
      setNote(r.reason === 'full' ? `Your wheel is full (${MAX_SLIVERS} slices). Spin it first!` : `You need ${p.cost - kid.points} more points.`);
      return;
    }
    saveKid(r.kid);
    play('ding', settings.sound);
    haptic.success();
    const n = r.kid.wheel.length;
    setNote(n < MIN_SLIVERS ? `${p.name} added! ${MIN_SLIVERS - n} more to spin.` : `${p.name} added to your wheel!`);
  };

  const rotate = wiggle.interpolate({ inputRange: [-1, 1], outputRange: ['-10deg', '10deg'] });

  return (
    <View style={{ flex: 1 }}>
      <ScrollView contentContainerStyle={[st.page, { paddingTop: insets.top + 10, paddingBottom: insets.bottom + 40 }]}>
        <View style={st.head}>
          <Squish label="Back" onPress={() => router.back()} style={st.back}>
            <Text style={st.backText}>‹</Text>
          </Squish>
          <Avatar color={kid.color} name={kid.name} size={52} />
          <H2 style={{ flex: 1 }}>{kid.name}</H2>
          <Points value={kid.points} scale={pointScale} />
        </View>

        <Squish label={ready ? 'Spin the wheel' : 'Your wheel'} onPress={() => (ready ? router.push({ pathname: '/spin', params: { kid: kid.id } }) : setTab('shop'))} style={st.wheelCard}>
          <Animated.View style={{ transform: [{ rotate }] }}>
            <Wheel wheel={kid.wheel} size={width < 400 ? 112 : 136} />
          </Animated.View>
          <View style={{ flex: 1, gap: 8 }}>
            <Text style={st.wheelTitle}>{ready ? 'Your wheel is ready!' : 'Your prize wheel'}</Text>
            <View style={st.pips} accessibilityLabel={`${Math.min(kid.wheel.length, MIN_SLIVERS)} of ${MIN_SLIVERS} slices`}>
              {Array.from({ length: MIN_SLIVERS }, (_, i) => (
                <View key={i} style={[st.pip, i < kid.wheel.length && { backgroundColor: sliverColor(kid.wheel, i), borderColor: colors.ink }]} />
              ))}
              {kid.wheel.length > MIN_SLIVERS ? <Text style={st.more}>+{kid.wheel.length - MIN_SLIVERS}</Text> : null}
            </View>
            {ready ? (
              <View pointerEvents="none">
                <Button title="Spin it!" kind="primary" big onPress={() => {}} />
              </View>
            ) : (
              <Body muted>
                {kid.wheel.length === 0 ? 'Buy prizes in the shop to fill your wheel.' : `Add ${need} more prize${need > 1 ? 's' : ''} to spin.`}
              </Body>
            )}
          </View>
        </Squish>

        {waiting.length ? (
          <View style={st.waiting}>
            <Text style={st.waitTitle}>Prizes you won 🎉</Text>
            <Body style={{ fontSize: 15 }}>{waiting.map((w) => `${w.icon} ${w.name}`).join('   ')}</Body>
            <Body muted style={{ fontSize: 14 }}>Show a grown-up to get them.</Body>
          </View>
        ) : null}

        <View style={st.tabs} accessibilityRole="tablist">
          {(['tasks', 'shop'] as const).map((t) => (
            <Pressable key={t} accessibilityRole="tab" accessibilityState={{ selected: tab === t }} onPress={() => setTab(t)} style={[st.tab, tab === t && st.tabOn]}>
              <Text style={[st.tabText, tab === t && { color: colors.bg }]}>{t === 'tasks' ? `Tasks${left.length ? ` (${left.length})` : ''}` : 'Prize shop'}</Text>
            </Pressable>
          ))}
        </View>

        {tab === 'tasks' ? (
          <View style={{ gap: 10 }}>
            {tasks.map((t) => {
              const done = isDone(kid, t, today);
              return (
                <Squish key={t.id} silent label={`${t.name}, ${done ? 'done' : 'not done'}`} onPress={() => onTask(t.id)} style={[st.row, done && st.rowDone]}>
                  <Text style={st.icon}>{t.icon}</Text>
                  <View style={{ flex: 1 }}>
                    <Text style={[st.rowName, done && st.rowNameDone]}>{t.name}</Text>
                    <Body muted style={{ fontSize: 14 }}>+{t.points} ★ · {t.repeat === 'once' ? 'One time' : 'Every day'}</Body>
                  </View>
                  <View style={[st.chk, done && st.chkOn]}>{done ? <Text style={st.chkMark}>✓</Text> : null}</View>
                </Squish>
              );
            })}
            {tasks.length === 0 ? <Body muted style={st.empty}>No tasks yet. Ask a grown-up to add some.</Body> : null}
            {tasks.length > 0 && left.length === 0 ? <Body style={st.empty}>You finished everything today. Amazing work!</Body> : null}
          </View>
        ) : (
          <View style={{ gap: 10 }}>
            <Body muted>Each prize you buy becomes a slice of your wheel. Buy the same one again to make it likelier.</Body>
            {[...prizes].sort((a, b) => a.cost - b.cost).map((p) => {
              const afford = kid.points >= p.cost;
              const have = kid.wheel.filter((w) => w.prizeId === p.id).length;
              return (
                <View key={p.id} style={st.row}>
                  <Text style={st.icon}>{p.icon}</Text>
                  <View style={{ flex: 1 }}>
                    <Text style={st.rowName}>{p.name}</Text>
                    <Body muted style={{ fontSize: 14 }}>
                      {p.cost} ★{have ? ` · ${have} on your wheel` : ''}
                    </Body>
                  </View>
                  <Button title={afford ? 'Buy' : `${p.cost - kid.points} more`} kind={afford ? 'primary' : 'plain'} disabled={!afford} onPress={() => onBuy(p)} />
                </View>
              );
            })}
            {prizes.length === 0 ? <Body muted style={st.empty}>No prizes yet. Ask a grown-up to add some.</Body> : null}

            {kid.wheel.length ? (
              <View style={{ gap: 8, marginTop: 8 }}>
                <H2>On your wheel ({kid.wheel.length})</H2>
                {kid.wheel.map((s, i) => (
                  <View key={s.id} style={st.slice}>
                    <View style={[st.swatch, { backgroundColor: sliverColor(kid.wheel, i) }]} />
                    <Text style={{ fontSize: 22 }}>{s.icon}</Text>
                    <Text style={[st.rowName, { flex: 1, fontSize: 16 }]} numberOfLines={1}>{s.name}</Text>
                    <Button
                      title={`Undo +${s.cost}★`}
                      onPress={() => {
                        saveKid(refundSliver(kid, s.id));
                        setNote(`Took ${s.name} off. You got ${s.cost} points back.`);
                      }}
                    />
                  </View>
                ))}
              </View>
            ) : null}
          </View>
        )}
      </ScrollView>

      {note ? (
        <View pointerEvents="none" style={[st.toast, { bottom: insets.bottom + 20 }]}>
          <Text style={st.toastText}>{note}</Text>
        </View>
      ) : null}
    </View>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 16, maxWidth: 760, width: '100%', alignSelf: 'center' },
  head: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  back: { width: 48, height: 48, borderRadius: 24, backgroundColor: colors.surface, borderWidth: 2, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  backText: { fontFamily: fonts.display, fontSize: 30, color: colors.ink, marginTop: -4 },
  wheelCard: { flexDirection: 'row', alignItems: 'center', gap: 16, backgroundColor: colors.surface, borderRadius: 28, borderWidth: 2, borderColor: colors.line, padding: 16, ...shadow },
  wheelTitle: { fontFamily: fonts.displayBold, fontSize: 20, color: colors.ink },
  pips: { flexDirection: 'row', flexWrap: 'wrap', gap: 6, alignItems: 'center' },
  pip: { width: 26, height: 26, borderRadius: 8, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.tile },
  more: { fontFamily: fonts.bodyBold, fontSize: 15, color: colors.muted },
  waiting: { backgroundColor: '#FFF6DB', borderRadius: 20, borderWidth: 2, borderColor: colors.star, padding: 14, gap: 4 },
  waitTitle: { fontFamily: fonts.displayBold, fontSize: 18, color: colors.ink },
  tabs: { flexDirection: 'row', backgroundColor: colors.surface, borderRadius: 999, borderWidth: 2, borderColor: colors.line, padding: 4 },
  tab: { flex: 1, minHeight: 46, borderRadius: 999, alignItems: 'center', justifyContent: 'center' },
  tabOn: { backgroundColor: colors.ink },
  tabText: { fontFamily: fonts.bodyBold, fontSize: 16, color: colors.ink },
  row: { flexDirection: 'row', alignItems: 'center', gap: 14, backgroundColor: colors.surface, borderRadius: 20, borderWidth: 2, borderColor: colors.line, paddingHorizontal: 14, paddingVertical: 12, minHeight: 74, ...shadow },
  rowDone: { backgroundColor: colors.tile, shadowOpacity: 0, elevation: 0 },
  icon: { fontSize: 30, width: 44, textAlign: 'center' },
  rowName: { fontFamily: fonts.bodyBold, fontSize: 18, color: colors.ink },
  rowNameDone: { textDecorationLine: 'line-through', color: colors.muted },
  chk: { width: 44, height: 44, borderRadius: 22, borderWidth: 3, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  chkOn: { backgroundColor: colors.good, borderColor: colors.good },
  chkMark: { color: '#fff', fontSize: 24, fontFamily: fonts.bodyBold },
  empty: { textAlign: 'center', padding: 18, borderRadius: 20, borderWidth: 2, borderStyle: 'dashed', borderColor: colors.line },
  slice: { flexDirection: 'row', alignItems: 'center', gap: 10, backgroundColor: colors.surface, borderRadius: 16, borderWidth: 2, borderColor: colors.line, padding: 8 },
  swatch: { width: 14, alignSelf: 'stretch', borderRadius: 6 },
  toast: { position: 'absolute', alignSelf: 'center', backgroundColor: colors.ink, borderRadius: 99, paddingHorizontal: 20, paddingVertical: 12, maxWidth: '90%' },
  toastText: { color: colors.bg, fontFamily: fonts.bodyBold, fontSize: 16, textAlign: 'center' },
});

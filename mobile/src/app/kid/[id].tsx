import { Redirect, router, useLocalSearchParams } from 'expo-router';
import { useEffect, useRef, useState } from 'react';
import { Animated, Modal, Pressable, ScrollView, StyleSheet, Text, useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Character } from '../../characters/Character.tsx';
import { Pod } from '../../components/Pod.tsx';
import { Avatar, Body, Button, H2, RarityPill, StarCount, Squish } from '../../components/ui.tsx';
import { haptic, play } from '../../feedback.ts';
import { CHARACTER_BY_ID, CHARACTERS, RARITIES, type Rarity } from '../../game/characters.ts';
import { isDone, openSurprise, ownedCount, toggleTask } from '../../game/rules.ts';
import { useFamily } from '../../state/family.tsx';
import { colors, fonts, shadow } from '../../theme.ts';

export default function KidScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const { kid: getKid, state, today, saveKid } = useFamily();
  const insets = useSafeAreaInsets();
  const { width } = useWindowDimensions();
  const [tab, setTab] = useState<'tasks' | 'collection'>('tasks');
  const [detail, setDetail] = useState<string | null>(null);
  const [note, setNote] = useState<string | null>(null);
  const starScale = useRef(new Animated.Value(1)).current;
  const wiggle = useRef(new Animated.Value(0)).current;

  const kid = getKid(id);
  const settings = state.settings;
  const cost = settings?.cost ?? 3;
  const ready = !!kid && kid.stars >= cost;

  useEffect(() => {
    if (!ready) return;
    const loop = Animated.loop(
      Animated.sequence([
        Animated.delay(900),
        Animated.timing(wiggle, { toValue: 1, duration: 90, useNativeDriver: true }),
        Animated.timing(wiggle, { toValue: -1, duration: 120, useNativeDriver: true }),
        Animated.timing(wiggle, { toValue: 0.6, duration: 110, useNativeDriver: true }),
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
  const tasks = settings.tasks;
  const left = tasks.filter((t) => !isDone(kid, t, today));

  const bumpStars = () =>
    Animated.sequence([
      Animated.spring(starScale, { toValue: 1.3, useNativeDriver: true, speed: 40 }),
      Animated.spring(starScale, { toValue: 1, useNativeDriver: true, speed: 20 }),
    ]).start();

  const onTask = (taskId: string) => {
    const task = tasks.find((t) => t.id === taskId);
    if (!task) return;
    const r = toggleTask(kid, task, today);
    if (r.change === 'blocked') {
      haptic.warn();
      setNote('Those stars were already used for a surprise.');
      return;
    }
    saveKid(r.kid);
    if (r.change === 'done') {
      play('ding', settings.sound);
      haptic.success();
      setNote(`+${task.stars} ★ Nice job!`);
      bumpStars();
    }
  };

  const onOpen = () => {
    const r = openSurprise(kid, cost);
    if (!r) return;
    saveKid(r.kid);
    router.push({ pathname: '/reveal', params: { kid: kid.id, char: r.character.id, isNew: r.isNew ? '1' : '0', count: String(r.count) } });
  };

  const rotate = wiggle.interpolate({ inputRange: [-1, 1], outputRange: ['-8deg', '8deg'] });
  const tileW = Math.floor((Math.min(width, 760) - 32 - 10 * 2) / 3);

  return (
    <View style={{ flex: 1 }}>
      <ScrollView contentContainerStyle={[st.page, { paddingTop: insets.top + 10, paddingBottom: insets.bottom + 40 }]}>
        <View style={st.head}>
          <Squish label="Back" onPress={() => router.back()} style={st.back}>
            <Text style={st.backText}>‹</Text>
          </Squish>
          <Avatar color={kid.color} name={kid.name} size={52}>
            {kid.buddy && kid.collection[kid.buddy] ? <Character id={kid.buddy} size={50} /> : undefined}
          </Avatar>
          <H2 style={{ flex: 1 }}>{kid.name}</H2>
          <StarCount value={kid.stars} scale={starScale} />
        </View>

        <View style={st.surprise}>
          <Animated.View style={{ transform: [{ rotate }] }}>
            <Pod size={width < 400 ? 84 : 104} />
          </Animated.View>
          <View style={{ flex: 1, gap: 10 }}>
            <Text style={st.surpriseTitle}>{ready ? 'A surprise is ready!' : 'Next surprise'}</Text>
            <View style={st.pips} accessibilityLabel={`${Math.min(kid.stars, cost)} of ${cost} stars`}>
              {Array.from({ length: cost }, (_, i) => (
                <View key={i} style={[st.pip, i < kid.stars && st.pipOn]}>
                  <Text style={[st.pipStar, i < kid.stars && { color: '#fff' }]}>★</Text>
                </View>
              ))}
            </View>
            {ready ? (
              <Button title="Open it!" kind="primary" big onPress={onOpen} />
            ) : (
              <Body muted>Finish tasks to earn {cost - kid.stars} more star{cost - kid.stars > 1 ? 's' : ''}.</Body>
            )}
          </View>
        </View>

        <View style={st.tabs} accessibilityRole="tablist">
          {(['tasks', 'collection'] as const).map((t) => (
            <Pressable key={t} accessibilityRole="tab" accessibilityState={{ selected: tab === t }} onPress={() => setTab(t)} style={[st.tab, tab === t && st.tabOn]}>
              <Text style={[st.tabText, tab === t && { color: colors.bg }]}>
                {t === 'tasks' ? `Tasks${left.length ? ` (${left.length})` : ''}` : `Collection ${ownedCount(kid)}/${CHARACTERS.length}`}
              </Text>
            </Pressable>
          ))}
        </View>

        {tab === 'tasks' ? (
          <View style={{ gap: 10 }}>
            {tasks.map((t) => {
              const done = isDone(kid, t, today);
              return (
                <Squish key={t.id} silent label={`${t.name}, ${done ? 'done' : 'not done'}`} onPress={() => onTask(t.id)} style={[st.task, done && st.taskDone]}>
                  <Text style={st.taskIcon}>{t.icon}</Text>
                  <View style={{ flex: 1 }}>
                    <Text style={[st.taskName, done && st.taskNameDone]}>{t.name}</Text>
                    <Body muted style={{ fontSize: 14 }}>+{t.stars} ★ · {t.repeat === 'once' ? 'One time' : 'Every day'}</Body>
                  </View>
                  <View style={[st.chk, done && st.chkOn]}>{done ? <Text style={st.chkMark}>✓</Text> : null}</View>
                </Squish>
              );
            })}
            {tasks.length === 0 ? <Body muted style={st.allDone}>No tasks yet. Ask a grown-up to add some.</Body> : null}
            {tasks.length > 0 && left.length === 0 ? <Body style={st.allDone}>You finished everything today. Amazing work!</Body> : null}
          </View>
        ) : (
          <View style={{ gap: 18 }}>
            {([4, 3, 2, 1, 0] as Rarity[]).map((r) => {
              const list = CHARACTERS.filter((c) => c.rarity === r);
              const have = list.filter((c) => kid.collection[c.id]).length;
              return (
                <View key={r} style={{ gap: 10 }}>
                  <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
                    <RarityPill rarity={r} />
                    <Body muted style={{ fontSize: 14 }}>{have} of {list.length}</Body>
                  </View>
                  <View style={st.grid}>
                    {list.map((c) => {
                      const n = kid.collection[c.id] ?? 0;
                      return n ? (
                        <Squish key={c.id} label={c.name} onPress={() => setDetail(c.id)} style={[st.tile, { width: tileW, borderColor: RARITIES[r].color }]}>
                          {n > 1 ? <Text style={st.count}>×{n}</Text> : null}
                          <Character id={c.id} size={tileW - 16} />
                          <Text style={st.tileName} numberOfLines={1}>{c.name}</Text>
                        </Squish>
                      ) : (
                        <View key={c.id} style={[st.tile, { width: tileW }]} accessibilityLabel="Not found yet">
                          <Character id={c.id} size={tileW - 16} locked />
                          <Text style={[st.tileName, { color: colors.muted }]}>???</Text>
                        </View>
                      );
                    })}
                  </View>
                </View>
              );
            })}
          </View>
        )}
      </ScrollView>

      {note ? (
        <View pointerEvents="none" style={[st.toast, { bottom: insets.bottom + 20 }]}>
          <Text style={st.toastText}>{note}</Text>
        </View>
      ) : null}

      <Modal visible={!!detail} transparent animationType="fade" onRequestClose={() => setDetail(null)}>
        <Pressable style={st.scrim} onPress={() => setDetail(null)}>
          {detail ? (
            <Pressable style={st.sheet} onPress={() => {}}>
              <Character id={detail} size={200} />
              <RarityPill rarity={CHARACTER_BY_ID[detail].rarity} big center />
              <H2>{CHARACTER_BY_ID[detail].name}</H2>
              <Body muted style={{ textAlign: 'center' }}>
                {CHARACTER_BY_ID[detail].style} · {CHARACTER_BY_ID[detail].flavor}
              </Body>
              <View style={{ flexDirection: 'row', gap: 10 }}>
                {kid.buddy === detail ? (
                  <Body muted>This is your buddy!</Body>
                ) : (
                  <Button
                    title="Make my buddy"
                    kind="primary"
                    onPress={() => {
                      saveKid({ ...kid, buddy: detail });
                      setDetail(null);
                      setNote('New buddy!');
                    }}
                  />
                )}
                <Button title="Close" onPress={() => setDetail(null)} />
              </View>
            </Pressable>
          ) : null}
        </Pressable>
      </Modal>
    </View>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 16, maxWidth: 760, width: '100%', alignSelf: 'center' },
  head: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  back: { width: 48, height: 48, borderRadius: 24, backgroundColor: colors.surface, borderWidth: 2, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  backText: { fontFamily: fonts.display, fontSize: 30, color: colors.ink, marginTop: -4 },
  surprise: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 16,
    backgroundColor: colors.surface,
    borderRadius: 28,
    borderWidth: 2,
    borderColor: colors.line,
    padding: 16,
    ...shadow,
  },
  surpriseTitle: { fontFamily: fonts.displayBold, fontSize: 19, color: colors.ink },
  pips: { flexDirection: 'row', flexWrap: 'wrap', gap: 6 },
  pip: { width: 28, height: 28, borderRadius: 14, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.tile, alignItems: 'center', justifyContent: 'center' },
  pipOn: { backgroundColor: colors.star, borderColor: colors.star },
  pipStar: { color: colors.line, fontSize: 16 },
  tabs: { flexDirection: 'row', backgroundColor: colors.surface, borderRadius: 999, borderWidth: 2, borderColor: colors.line, padding: 4 },
  tab: { flex: 1, minHeight: 46, borderRadius: 999, alignItems: 'center', justifyContent: 'center' },
  tabOn: { backgroundColor: colors.ink },
  tabText: { fontFamily: fonts.bodyBold, fontSize: 16, color: colors.ink },
  task: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
    backgroundColor: colors.surface,
    borderRadius: 20,
    borderWidth: 2,
    borderColor: colors.line,
    paddingHorizontal: 14,
    paddingVertical: 12,
    minHeight: 74,
    ...shadow,
  },
  taskDone: { backgroundColor: colors.tile, shadowOpacity: 0, elevation: 0 },
  taskIcon: { fontSize: 30, width: 44, textAlign: 'center' },
  taskName: { fontFamily: fonts.bodyBold, fontSize: 18, color: colors.ink },
  taskNameDone: { textDecorationLine: 'line-through', color: colors.muted },
  chk: { width: 44, height: 44, borderRadius: 22, borderWidth: 3, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  chkOn: { backgroundColor: colors.good, borderColor: colors.good },
  chkMark: { color: '#fff', fontSize: 24, fontFamily: fonts.bodyBold },
  allDone: { textAlign: 'center', padding: 18, borderRadius: 20, borderWidth: 2, borderStyle: 'dashed', borderColor: colors.line },
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10 },
  tile: { backgroundColor: colors.tile, borderRadius: 18, borderWidth: 3, borderColor: colors.line, alignItems: 'center', paddingTop: 6, paddingBottom: 8, paddingHorizontal: 4 },
  tileName: { fontFamily: fonts.bodyBold, fontSize: 13, color: colors.ink, maxWidth: '100%' },
  count: { position: 'absolute', top: 4, right: 6, zIndex: 1, fontFamily: fonts.bodyBold, fontSize: 12, color: colors.bg, backgroundColor: colors.ink, borderRadius: 99, paddingHorizontal: 6, overflow: 'hidden' },
  toast: { position: 'absolute', alignSelf: 'center', backgroundColor: colors.ink, borderRadius: 99, paddingHorizontal: 20, paddingVertical: 12, maxWidth: '90%' },
  toastText: { color: colors.bg, fontFamily: fonts.bodyBold, fontSize: 16, textAlign: 'center' },
  scrim: { flex: 1, backgroundColor: 'rgba(23,19,42,0.6)', alignItems: 'center', justifyContent: 'center', padding: 20 },
  sheet: { backgroundColor: colors.surface, borderRadius: 28, padding: 22, alignItems: 'center', gap: 12, width: '100%', maxWidth: 420 },
});


import { Redirect, router } from 'expo-router';
import { useEffect, useRef, useState } from 'react';
import { Animated, Modal, Pressable, ScrollView, StyleSheet, Switch, Text, TextInput, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { PointsField, PrizeEditor, TaskEditor } from '../components/Editors.tsx';
import { Avatar, Body, Button, H2, Panel, Squish } from '../components/ui.tsx';
import { haptic } from '../feedback.ts';
import { makeKid, markGiven, MIN_SLIVERS, pendingWins, type Settings } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts } from '../theme.ts';

function PinGate({ pin, onUnlock }: { pin: string; onUnlock: () => void }) {
  const [entry, setEntry] = useState('');
  const shake = useRef(new Animated.Value(0)).current;
  const press = (k: string) => {
    haptic.tap();
    const next = k === 'del' ? entry.slice(0, -1) : (entry + k).slice(0, 4);
    if (next.length === 4) {
      if (next === pin) {
        onUnlock();
        return;
      }
      haptic.warn();
      Animated.sequence([1, -1, 0.6, 0].map((v) => Animated.timing(shake, { toValue: v * 12, duration: 60, useNativeDriver: true }))).start();
      setEntry('');
      return;
    }
    setEntry(next);
  };
  return (
    <Panel style={{ alignItems: 'center', gap: 18 }}>
      <Body muted>Enter the 4-digit grown-up code.</Body>
      <Animated.View style={[st.dots, { transform: [{ translateX: shake }] }]}>
        {[0, 1, 2, 3].map((i) => (
          <View key={i} style={[st.dot, i < entry.length && st.dotOn]} />
        ))}
      </Animated.View>
      <View style={st.keypad}>
        {['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '0', 'del'].map((k, i) =>
          k ? (
            <Pressable key={i} accessibilityLabel={k === 'del' ? 'Delete' : k} onPress={() => press(k)} style={st.key}>
              <Text style={st.keyText}>{k === 'del' ? '⌫' : k}</Text>
            </Pressable>
          ) : (
            <View key={i} style={{ width: 72, height: 72 }} />
          ),
        )}
      </View>
    </Panel>
  );
}

export default function Grownups() {
  const { state, saveSettings, saveKid, removeKid } = useFamily();
  const insets = useSafeAreaInsets();
  const [unlocked, setUnlocked] = useState(false);
  const [newKid, setNewKid] = useState('');
  const [newPin, setNewPin] = useState('');
  const [confirm, setConfirm] = useState<{ title: string; text: string; run: () => void } | null>(null);
  const [adjust, setAdjust] = useState(1);
  const [note, setNote] = useState<string | null>(null);

  useEffect(() => {
    if (!note) return;
    const t = setTimeout(() => setNote(null), 2200);
    return () => clearTimeout(t);
  }, [note]);

  const settings = state.settings;
  if (!settings) return <Redirect href="/setup" />;
  const kids = [...state.kids].sort((a, b) => a.createdAt - b.createdAt);

  const set = (patch: Partial<Settings>) => saveSettings({ ...settings, ...patch });
  const ask = (title: string, text: string, run: () => void) => setConfirm({ title, text, run });
  const toGive = kids.flatMap((k) => pendingWins(k).map((w) => ({ kid: k, win: w })));

  return (
    <View style={{ flex: 1 }}>
      <ScrollView keyboardShouldPersistTaps="handled" contentContainerStyle={[st.page, { paddingTop: insets.top + 10, paddingBottom: insets.bottom + 40 }]}>
        <View style={st.head}>
          <Squish label="Back" onPress={() => router.back()} style={st.back}>
            <Text style={st.backText}>‹</Text>
          </Squish>
          <H2 style={{ flex: 1 }}>Grown-ups</H2>
        </View>

        {settings.pin && !unlocked ? (
          <PinGate pin={settings.pin} onUnlock={() => setUnlocked(true)} />
        ) : (
          <>
            <Panel>
              <H2>Kids</H2>
              {kids.map((k) => (
                <View key={k.id} style={st.kidRow}>
                  <View style={st.kidTop}>
                    <Avatar color={k.color} name={k.name} size={52} />
                    <View style={{ flex: 1, gap: 4 }}>
                      <TextInput
                        defaultValue={k.name}
                        maxLength={24}
                        onEndEditing={(e) => {
                          const v = e.nativeEvent.text.trim();
                          if (v && v !== k.name) saveKid({ ...k, name: v });
                        }}
                        style={st.input}
                        accessibilityLabel={`Name for ${k.name}`}
                      />
                      <Body muted style={{ fontSize: 14 }}>
                        ★ {k.points} points · {k.wheel.length} slice{k.wheel.length === 1 ? '' : 's'} on the wheel · {k.wins.length} prize{k.wins.length === 1 ? '' : 's'} won
                      </Body>
                    </View>
                  </View>
                  <View style={st.btnRow}>
                    <Button title={`+${adjust} ★`} onPress={() => saveKid({ ...k, points: k.points + adjust })} />
                    <Button title={`−${adjust} ★`} onPress={() => saveKid({ ...k, points: Math.max(0, k.points - adjust) })} />
                    <Button
                      title="Remove"
                      kind="danger"
                      onPress={() =>
                        setConfirm({
                          title: `Remove ${k.name}?`,
                          text: `Their ${k.points} points, their wheel and their prize history will be deleted. This can't be undone.`,
                          run: () => removeKid(k.id),
                        })
                      }
                    />
                  </View>
                </View>
              ))}
              {kids.length ? (
                <View style={st.btnRow}>
                  <Body muted style={{ fontSize: 14 }}>Points the ± buttons add or take away:</Body>
                  <PointsField value={adjust} onChange={setAdjust} label="Points to add or take away" />
                </View>
              ) : null}
              <View style={st.btnRow}>
                <TextInput
                  value={newKid}
                  onChangeText={setNewKid}
                  placeholder="Add a kid"
                  placeholderTextColor={colors.muted}
                  maxLength={24}
                  style={[st.input, { flex: 1 }]}
                  accessibilityLabel="New kid's name"
                />
                <Button
                  title="Add"
                  kind="primary"
                  onPress={() => {
                    const v = newKid.trim();
                    if (!v) return;
                    saveKid(makeKid(v, kids.length));
                    setNewKid('');
                    setNote(`Added ${v}`);
                  }}
                />
              </View>
            </Panel>

            {toGive.length ? (
              <Panel style={{ borderColor: colors.star }}>
                <H2>Prizes to hand out</H2>
                <Body muted style={{ fontSize: 14 }}>The wheel landed on these. Tap Given once the kid has their prize.</Body>
                {toGive.map(({ kid: k, win: w }) => (
                  <View key={w.id} style={st.winRow}>
                    <Text style={{ fontSize: 26 }}>{w.icon}</Text>
                    <View style={{ flex: 1 }}>
                      <Text style={st.winName}>{w.name}</Text>
                      <Body muted style={{ fontSize: 14 }}>
                        {k.name} · {new Date(w.at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}
                      </Body>
                    </View>
                    <Button title="Given ✓" kind="primary" onPress={() => saveKid(markGiven(k, w.id))} />
                  </View>
                ))}
              </Panel>
            ) : null}

            <Panel>
              <H2>Tasks</H2>
              <Body muted style={{ fontSize: 14 }}>Set any number of points from 1 to 999. Every-day tasks reset each morning. One-time tasks stay done.</Body>
              <TaskEditor tasks={settings.tasks} onChange={(tasks) => set({ tasks })} confirm={ask} />
            </Panel>

            <Panel>
              <H2>Prizes</H2>
              <Body muted style={{ fontSize: 14 }}>
                Kids spend points to add a prize as a slice of their wheel, one slice per prize. Purchases are final. The wheel needs at least 4 slices to spin, and spinning is free. The kid wins the slice it lands on, which shows in Prizes to hand out, and the whole wheel clears.
              </Body>
              {settings.prizes.length < MIN_SLIVERS ? (
                <Body style={{ color: colors.danger, fontFamily: fonts.bodyBold }}>
                  Add at least {MIN_SLIVERS} prizes, or kids can't fill a wheel to spin.
                </Body>
              ) : null}
              <PrizeEditor prizes={settings.prizes} onChange={(prizes) => set({ prizes })} confirm={ask} />
              <View style={[st.btnRow, { justifyContent: 'space-between' }]}>
                <Body>Sounds</Body>
                <Switch value={settings.sound} onValueChange={(v) => set({ sound: v })} trackColor={{ true: colors.good }} />
              </View>
            </Panel>

            <Panel>
              <H2>Grown-up code</H2>
              <Body muted style={{ fontSize: 14 }}>
                {settings.pin ? 'A code is set. Kids need it to open this page.' : "No code yet. Add one so kids can't change tasks, prizes or points."} It keeps little hands out. It isn't a password.
              </Body>
              <View style={st.btnRow}>
                <TextInput
                  value={newPin}
                  onChangeText={(v) => setNewPin(v.replace(/\D/g, '').slice(0, 4))}
                  keyboardType="number-pad"
                  placeholder="4 digits"
                  placeholderTextColor={colors.muted}
                  style={[st.input, { width: 130 }]}
                  accessibilityLabel="New 4-digit code"
                />
                <Button
                  title={settings.pin ? 'Change code' : 'Set code'}
                  kind="primary"
                  onPress={() => {
                    if (!/^\d{4}$/.test(newPin)) {
                      setNote('Use exactly 4 digits.');
                      return;
                    }
                    set({ pin: newPin });
                    setNewPin('');
                    setNote('Code saved');
                  }}
                />
                {settings.pin ? <Button title="Remove code" onPress={() => set({ pin: '' })} /> : null}
              </View>
            </Panel>
            <Body muted style={st.foot}>Progress is saved on this device.</Body>
          </>
        )}
      </ScrollView>

      {note ? (
        <View pointerEvents="none" style={[st.toast, { bottom: insets.bottom + 20 }]}>
          <Text style={st.toastText}>{note}</Text>
        </View>
      ) : null}

      <Modal visible={!!confirm} transparent animationType="fade" onRequestClose={() => setConfirm(null)}>
        <View style={st.scrim}>
          <View style={st.sheet}>
            <H2 style={{ textAlign: 'center' }}>{confirm?.title}</H2>
            <Body muted style={{ textAlign: 'center' }}>{confirm?.text}</Body>
            <View style={st.btnRow}>
              <Button
                title="Remove"
                kind="danger"
                onPress={() => {
                  confirm?.run();
                  setConfirm(null);
                }}
              />
              <Button title="Cancel" onPress={() => setConfirm(null)} />
            </View>
          </View>
        </View>
      </Modal>

    </View>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 16, maxWidth: 760, width: '100%', alignSelf: 'center' },
  head: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  back: { width: 48, height: 48, borderRadius: 24, backgroundColor: colors.surface, borderWidth: 2, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  backText: { fontFamily: fonts.display, fontSize: 30, color: colors.ink, marginTop: -4 },
  input: { minHeight: 46, borderRadius: 12, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.tile, paddingHorizontal: 12, fontFamily: fonts.body, fontSize: 16, color: colors.ink },
  kidRow: { gap: 10, paddingVertical: 10, borderTopWidth: 2, borderTopColor: colors.tile },
  kidTop: { flexDirection: 'row', gap: 12, alignItems: 'center' },
  btnRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, alignItems: 'center' },
  dots: { flexDirection: 'row', gap: 14 },
  dot: { width: 18, height: 18, borderRadius: 9, borderWidth: 3, borderColor: colors.ink },
  dotOn: { backgroundColor: colors.ink },
  keypad: { flexDirection: 'row', flexWrap: 'wrap', width: 72 * 3 + 24, gap: 12 },
  key: { width: 72, height: 72, borderRadius: 36, backgroundColor: colors.tile, borderWidth: 2, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  keyText: { fontFamily: fonts.display, fontSize: 30, color: colors.ink },
  winRow: { flexDirection: 'row', alignItems: 'center', gap: 12, paddingVertical: 8, borderTopWidth: 2, borderTopColor: colors.tile },
  winName: { fontFamily: fonts.bodyBold, fontSize: 17, color: colors.ink },
  foot: { fontSize: 14, textAlign: 'center' },
  toast: { position: 'absolute', alignSelf: 'center', backgroundColor: colors.ink, borderRadius: 99, paddingHorizontal: 20, paddingVertical: 12, maxWidth: '90%' },
  toastText: { color: colors.bg, fontFamily: fonts.bodyBold, fontSize: 16, textAlign: 'center' },
  scrim: { flex: 1, backgroundColor: 'rgba(23,19,42,0.6)', alignItems: 'center', justifyContent: 'center', padding: 20 },
  sheet: { backgroundColor: colors.surface, borderRadius: 28, padding: 22, alignItems: 'center', gap: 12, width: '100%', maxWidth: 420 },
});

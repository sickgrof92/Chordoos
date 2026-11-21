import { router } from 'expo-router';
import { useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, TextInput, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Character } from '../characters/Character.tsx';
import { Body, Button, H1, H2, Panel } from '../components/ui.tsx';
import { CHARACTERS } from '../game/characters.ts';
import { makeKid, newId, SUGGESTED_TASKS } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts } from '../theme.ts';

const COSTS = [1, 2, 3, 4, 5, 6, 8, 10];
const SHOWCASE = ['bunbun', 'sprig', 'pip', 'geode', 'blazeking'];

export default function Setup() {
  const { saveSettings, saveKid, state } = useFamily();
  const insets = useSafeAreaInsets();
  const [names, setNames] = useState<string[]>([]);
  const [draft, setDraft] = useState('');
  const [picked, setPicked] = useState(SUGGESTED_TASKS.map((t) => t.on));
  const [cost, setCost] = useState(3);

  const addName = () => {
    const v = draft.trim();
    if (!v) return;
    setNames((n) => [...n, v.slice(0, 24)]);
    setDraft('');
  };

  const daily = SUGGESTED_TASKS.reduce((a, t, i) => a + (picked[i] ? t.stars : 0), 0);

  const start = () => {
    saveSettings({
      tasks: SUGGESTED_TASKS.filter((_, i) => picked[i]).map(({ on: _on, ...t }) => ({ ...t, id: newId() })),
      cost,
      pin: '',
      sound: true,
    });
    names.forEach((n, i) => saveKid(makeKid(n, i + state.kids.length)));
    router.replace('/');
  };

  return (
    <ScrollView
      keyboardShouldPersistTaps="handled"
      contentContainerStyle={[st.page, { paddingTop: insets.top + 16, paddingBottom: insets.bottom + 32 }]}
    >
      <Panel style={{ alignItems: 'center' }}>
        <View style={st.showcase}>
          {SHOWCASE.filter((id) => CHARACTERS.some((c) => c.id === id)).map((id) => (
            <Character key={id} id={id} size={64} />
          ))}
        </View>
        <H1 style={{ textAlign: 'center' }}>Finish tasks. Open surprises. Collect them all.</H1>
        <Body muted style={{ textAlign: 'center' }}>
          Kids tick off tasks like brushing teeth to earn stars. Stars open a surprise pod with a Chordoo inside, from Common to Legendary.
        </Body>
      </Panel>

      <Panel>
        <H2>1. Who's playing?</H2>
        <View style={st.row}>
          <TextInput
            value={draft}
            onChangeText={setDraft}
            onSubmitEditing={addName}
            placeholder="Kid's name"
            placeholderTextColor={colors.muted}
            maxLength={24}
            returnKeyType="done"
            style={[st.input, { flex: 1 }]}
            accessibilityLabel="Kid's name"
          />
          <Button title="Add" onPress={addName} />
        </View>
        <View style={st.chips}>
          {names.length === 0 ? <Body muted>Add at least one kid.</Body> : null}
          {names.map((n, i) => (
            <View key={`${n}-${i}`} style={st.chip}>
              <Text style={st.chipText}>{n}</Text>
              <Pressable accessibilityLabel={`Remove ${n}`} onPress={() => setNames((x) => x.filter((_, j) => j !== i))} style={st.chipX}>
                <Text style={st.chipText}>×</Text>
              </Pressable>
            </View>
          ))}
        </View>
      </Panel>

      <Panel>
        <H2>2. Pick the tasks</H2>
        <Body muted>You can change these any time in Grown-ups.</Body>
        {SUGGESTED_TASKS.map((t, i) => (
          <Pressable
            key={t.name}
            accessibilityRole="checkbox"
            accessibilityState={{ checked: picked[i] }}
            onPress={() => setPicked((p) => p.map((v, j) => (j === i ? !v : v)))}
            style={st.check}
          >
            <View style={[st.box, picked[i] && st.boxOn]}>{picked[i] ? <Text style={st.tick}>✓</Text> : null}</View>
            <Text style={{ fontSize: 22 }}>{t.icon}</Text>
            <Text style={st.checkText}>{t.name}</Text>
            <Body muted>+{t.stars}★</Body>
          </Pressable>
        ))}
      </Panel>

      <Panel>
        <H2>3. Stars per surprise</H2>
        <View style={st.chips}>
          {COSTS.map((n) => (
            <Pressable key={n} onPress={() => setCost(n)} style={[st.costChip, n === cost && st.costOn]} accessibilityRole="radio" accessibilityState={{ selected: n === cost }}>
              <Text style={[st.chipText, n === cost && { color: colors.accentInk }]}>{n}</Text>
            </Pressable>
          ))}
        </View>
        <Body muted>With these tasks, about {Math.max(1, Math.round((daily / cost) * 10) / 10)} surprises a day.</Body>
      </Panel>

      <Button title="Start collecting" kind="primary" big disabled={names.length === 0} onPress={start} />
    </ScrollView>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 16, maxWidth: 760, width: '100%', alignSelf: 'center' },
  showcase: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'center', gap: 4 },
  row: { flexDirection: 'row', gap: 10, alignItems: 'center' },
  input: {
    minHeight: 48,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: colors.line,
    backgroundColor: colors.tile,
    paddingHorizontal: 14,
    fontFamily: fonts.body,
    fontSize: 17,
    color: colors.ink,
  },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, alignItems: 'center' },
  chip: { flexDirection: 'row', alignItems: 'center', gap: 6, backgroundColor: colors.tile, borderRadius: 99, paddingLeft: 14, paddingRight: 6, paddingVertical: 6 },
  chipX: { width: 30, height: 30, borderRadius: 15, backgroundColor: colors.surface, alignItems: 'center', justifyContent: 'center' },
  chipText: { fontFamily: fonts.bodyBold, fontSize: 16, color: colors.ink },
  check: { flexDirection: 'row', alignItems: 'center', gap: 12, backgroundColor: colors.tile, borderRadius: 14, padding: 12, minHeight: 52 },
  box: { width: 26, height: 26, borderRadius: 8, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.surface, alignItems: 'center', justifyContent: 'center' },
  boxOn: { backgroundColor: colors.accent, borderColor: colors.accent },
  tick: { color: '#fff', fontFamily: fonts.bodyBold, fontSize: 16 },
  checkText: { flex: 1, fontFamily: fonts.bodyBold, fontSize: 16, color: colors.ink },
  costChip: { minWidth: 48, height: 48, borderRadius: 24, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.surface, alignItems: 'center', justifyContent: 'center' },
  costOn: { backgroundColor: colors.accent, borderColor: colors.accent },
});

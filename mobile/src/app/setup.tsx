import { router } from 'expo-router';
import { useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, TextInput, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { PrizeEditor, TaskEditor } from '../components/Editors.tsx';
import { Body, Button, H1, H2, Panel } from '../components/ui.tsx';
import { Wheel } from '../components/Wheel.tsx';
import { makeKid, MIN_SLIVERS, type Prize, type Sliver, type Task } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts } from '../theme.ts';

const DECOR: Sliver[] = ['🎁', '⭐', '🎉', '🎈', '🎁', '⭐'].map((icon, i) => ({ id: `d${i}`, prizeId: `d${i % 4}`, name: '', icon, cost: 0 }));

export default function Setup() {
  const { saveSettings, saveKid, state } = useFamily();
  const insets = useSafeAreaInsets();
  const [names, setNames] = useState<string[]>([]);
  const [draft, setDraft] = useState('');
  const [tasks, setTasks] = useState<Task[]>([]);
  const [prizes, setPrizes] = useState<Prize[]>([]);

  const addName = () => {
    const v = draft.trim();
    if (!v) return;
    setNames((n) => [...n, v.slice(0, 24)]);
    setDraft('');
  };

  const morePrizes = MIN_SLIVERS - prizes.length;
  const missing = [
    !names.length && 'a kid',
    !tasks.length && 'a task',
    morePrizes > 0 && `${morePrizes} more prize${morePrizes > 1 ? 's' : ''} (the wheel needs ${MIN_SLIVERS} to spin)`,
  ].filter(Boolean);

  const start = () => {
    saveSettings({ tasks, prizes, pin: '', sound: true });
    names.forEach((n, i) => saveKid(makeKid(n, i + state.kids.length)));
    router.replace('/');
  };

  return (
    <ScrollView keyboardShouldPersistTaps="handled" contentContainerStyle={[st.page, { paddingTop: insets.top + 16, paddingBottom: insets.bottom + 32 }]}>
      <Panel style={{ alignItems: 'center' }}>
        <Wheel wheel={DECOR} size={150} />
        <H1 style={{ textAlign: 'center' }}>Do tasks. Earn points. Spin for prizes.</H1>
        <Body muted style={{ textAlign: 'center' }}>
          You choose the tasks, how many points each one is worth, and the prizes. Kids spend points to put prizes on their wheel. Once it has {MIN_SLIVERS} slices they spin it for free, win one prize, and start a new wheel.
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
        <H2>2. Tasks and their points</H2>
        <Body muted>For example, brushing teeth for 1 point or making the bed for 2. Every-day tasks reset each morning.</Body>
        <TaskEditor tasks={tasks} onChange={setTasks} />
      </Panel>

      <Panel>
        <H2>3. Prizes and what they cost</H2>
        <Body muted>
          For example, a piece of chocolate for 5 points or an hour of video games for 20. Each prize a kid buys becomes one slice of their wheel. Add at least {MIN_SLIVERS} so the wheel can fill up.
        </Body>
        <PrizeEditor prizes={prizes} onChange={setPrizes} />
      </Panel>

      {missing.length ? <Body muted style={{ textAlign: 'center' }}>Add {missing.join(', ')} to start. You can change everything later in Grown-ups.</Body> : null}
      <Button title="Let's go" kind="primary" big disabled={missing.length > 0} onPress={start} />
    </ScrollView>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 16, maxWidth: 760, width: '100%', alignSelf: 'center' },
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
});

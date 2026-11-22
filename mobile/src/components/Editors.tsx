import { useEffect, useState } from 'react';
import { Modal, Pressable, StyleSheet, Text, TextInput, View } from 'react-native';
import { clampPoints, newId, PRIZE_ICONS, TASK_ICONS, type Prize, type Task } from '../game/rules.ts';
import { colors, fonts } from '../theme.ts';
import { Body, Button, H2 } from './ui.tsx';

type Confirm = (title: string, text: string, run: () => void) => void;

/** A whole-number field with − and + buttons. Typing any number from 1 to 999 works. */
export function PointsField({ value, onChange, label, unit = 'pts' }: { value: number; onChange: (n: number) => void; label: string; unit?: string }) {
  const [text, setText] = useState(String(value));
  useEffect(() => setText(String(value)), [value]);
  return (
    <View style={st.points}>
      <Button title="−" onPress={() => onChange(clampPoints(value - 1))} style={st.step} />
      <TextInput
        value={text}
        onChangeText={(v) => {
          const clean = v.replace(/\D/g, '').slice(0, 3);
          setText(clean);
          const n = parseInt(clean, 10);
          if (n > 0) onChange(clampPoints(n));
        }}
        onBlur={() => setText(String(value))}
        keyboardType="number-pad"
        selectTextOnFocus
        style={[st.input, st.num]}
        accessibilityLabel={label}
      />
      <Text style={st.unit}>{unit}</Text>
      <Button title="+" onPress={() => onChange(clampPoints(value + 1))} style={st.step} />
    </View>
  );
}

function IconPicker({ icons, open, onPick, onClose }: { icons: string[]; open: boolean; onPick: (i: string) => void; onClose: () => void }) {
  return (
    <Modal visible={open} transparent animationType="fade" onRequestClose={onClose}>
      <Pressable style={st.scrim} onPress={onClose}>
        <View style={st.sheet}>
          <H2>Pick an icon</H2>
          <View style={[st.row, { justifyContent: 'center' }]}>
            {icons.map((i) => (
              <Pressable key={i} accessibilityLabel={i} onPress={() => onPick(i)} style={st.iconBtn}>
                <Text style={{ fontSize: 26 }}>{i}</Text>
              </Pressable>
            ))}
          </View>
        </View>
      </Pressable>
    </Modal>
  );
}

/** Name + points form for adding a new task or prize. */
function AddRow({ placeholder, unit, onAdd, label }: { placeholder: string; unit: string; label: string; onAdd: (name: string, n: number) => void }) {
  const [name, setName] = useState('');
  const [n, setN] = useState(1);
  const add = () => {
    const v = name.trim();
    if (!v) return;
    onAdd(v.slice(0, 40), n);
    setName('');
    setN(1);
  };
  return (
    <View style={st.addBox}>
      <TextInput
        value={name}
        onChangeText={setName}
        onSubmitEditing={add}
        placeholder={placeholder}
        placeholderTextColor={colors.muted}
        maxLength={40}
        returnKeyType="done"
        style={st.input}
        accessibilityLabel={placeholder}
      />
      <View style={[st.row, { justifyContent: 'space-between' }]}>
        <PointsField value={n} onChange={setN} label={`${label} for the new item`} unit={unit} />
        <Button title="Add" kind="primary" disabled={!name.trim()} onPress={add} />
      </View>
    </View>
  );
}

export function TaskEditor({ tasks, onChange, confirm }: { tasks: Task[]; onChange: (t: Task[]) => void; confirm?: Confirm }) {
  const [iconFor, setIconFor] = useState<string | null>(null);
  const patch = (id: string, p: Partial<Task>) => onChange(tasks.map((t) => (t.id === id ? { ...t, ...p } : t)));
  const remove = (t: Task) => {
    const run = () => onChange(tasks.filter((x) => x.id !== t.id));
    if (confirm) confirm(`Remove "${t.name}"?`, 'Points already earned from it stay.', run);
    else run();
  };
  return (
    <View style={{ gap: 10 }}>
      {tasks.map((t) => (
        <View key={t.id} style={st.item}>
          <View style={st.row}>
            <Pressable accessibilityLabel={`Icon for ${t.name}`} onPress={() => setIconFor(t.id)} style={st.iconBtn}>
              <Text style={{ fontSize: 24 }}>{t.icon}</Text>
            </Pressable>
            <TextInput
              value={t.name}
              onChangeText={(v) => patch(t.id, { name: v.slice(0, 40) })}
              onBlur={() => {
                if (!t.name.trim()) patch(t.id, { name: 'Task' });
              }}
              maxLength={40}
              style={[st.input, { flex: 1 }]}
              accessibilityLabel="Task name"
            />
          </View>
          <View style={st.row}>
            <PointsField value={t.points} onChange={(n) => patch(t.id, { points: n })} label={`Points for ${t.name}`} />
            <Button title={t.repeat === 'once' ? 'One time' : 'Every day'} onPress={() => patch(t.id, { repeat: t.repeat === 'once' ? 'daily' : 'once' })} />
            <Button title="Remove" kind="danger" onPress={() => remove(t)} />
          </View>
        </View>
      ))}
      {tasks.length === 0 ? <Body muted>No tasks yet. Add the first one below.</Body> : null}
      <AddRow
        placeholder="New task, like Make your bed"
        unit="pts"
        label="Points"
        onAdd={(name, points) => onChange([...tasks, { id: newId(), name, icon: '⭐', points, repeat: 'daily' }])}
      />
      <IconPicker
        icons={TASK_ICONS}
        open={!!iconFor}
        onClose={() => setIconFor(null)}
        onPick={(i) => {
          if (iconFor) patch(iconFor, { icon: i });
          setIconFor(null);
        }}
      />
    </View>
  );
}

export function PrizeEditor({ prizes, onChange, confirm }: { prizes: Prize[]; onChange: (p: Prize[]) => void; confirm?: Confirm }) {
  const [iconFor, setIconFor] = useState<string | null>(null);
  const patch = (id: string, p: Partial<Prize>) => onChange(prizes.map((x) => (x.id === id ? { ...x, ...p } : x)));
  const remove = (p: Prize) => {
    const run = () => onChange(prizes.filter((x) => x.id !== p.id));
    if (confirm) confirm(`Remove "${p.name}"?`, 'Kids can no longer buy it. Slices already on a wheel stay.', run);
    else run();
  };
  return (
    <View style={{ gap: 10 }}>
      {prizes.map((p) => (
        <View key={p.id} style={st.item}>
          <View style={st.row}>
            <Pressable accessibilityLabel={`Icon for ${p.name}`} onPress={() => setIconFor(p.id)} style={st.iconBtn}>
              <Text style={{ fontSize: 24 }}>{p.icon}</Text>
            </Pressable>
            <TextInput
              value={p.name}
              onChangeText={(v) => patch(p.id, { name: v.slice(0, 40) })}
              onBlur={() => {
                if (!p.name.trim()) patch(p.id, { name: 'Prize' });
              }}
              maxLength={40}
              style={[st.input, { flex: 1 }]}
              accessibilityLabel="Prize name"
            />
          </View>
          <View style={st.row}>
            <Text style={st.costLabel}>Costs</Text>
            <PointsField value={p.cost} onChange={(n) => patch(p.id, { cost: n })} label={`Cost of ${p.name}`} />
            <Button title="Remove" kind="danger" onPress={() => remove(p)} />
          </View>
        </View>
      ))}
      {prizes.length === 0 ? <Body muted>No prizes yet. Add the first one below.</Body> : null}
      <AddRow
        placeholder="New prize, like A piece of chocolate"
        unit="pts"
        label="Cost"
        onAdd={(name, cost) => onChange([...prizes, { id: newId(), name, icon: '🎁', cost }])}
      />
      <IconPicker
        icons={PRIZE_ICONS}
        open={!!iconFor}
        onClose={() => setIconFor(null)}
        onPick={(i) => {
          if (iconFor) patch(iconFor, { icon: i });
          setIconFor(null);
        }}
      />
    </View>
  );
}

export const st = StyleSheet.create({
  row: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, alignItems: 'center' },
  item: { gap: 8, paddingVertical: 10, borderTopWidth: 2, borderTopColor: colors.tile },
  addBox: { gap: 8, padding: 12, borderRadius: 18, borderWidth: 2, borderStyle: 'dashed', borderColor: colors.line },
  input: { minHeight: 46, borderRadius: 12, borderWidth: 2, borderColor: colors.line, backgroundColor: colors.tile, paddingHorizontal: 12, fontFamily: fonts.body, fontSize: 16, color: colors.ink },
  num: { width: 60, textAlign: 'center', fontFamily: fonts.bodyBold, paddingHorizontal: 4 },
  points: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  step: { minWidth: 46, paddingHorizontal: 0 },
  unit: { fontFamily: fonts.bodyBold, fontSize: 14, color: colors.muted },
  costLabel: { fontFamily: fonts.bodyBold, fontSize: 15, color: colors.ink },
  iconBtn: { width: 52, height: 52, borderRadius: 14, backgroundColor: colors.tile, borderWidth: 2, borderColor: colors.line, alignItems: 'center', justifyContent: 'center' },
  scrim: { flex: 1, backgroundColor: 'rgba(23,19,42,0.6)', alignItems: 'center', justifyContent: 'center', padding: 20 },
  sheet: { backgroundColor: colors.surface, borderRadius: 28, padding: 22, alignItems: 'center', gap: 12, width: '100%', maxWidth: 420 },
});

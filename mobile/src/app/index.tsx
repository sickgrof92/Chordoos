import { Redirect, router } from 'expo-router';
import { ScrollView, StyleSheet, Text, useWindowDimensions, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Character } from '../characters/Character.tsx';
import { Avatar, Body, Button, H1, Panel, StarCount, Squish } from '../components/ui.tsx';
import { CHARACTERS } from '../game/characters.ts';
import { isDone, ownedCount } from '../game/rules.ts';
import { useFamily } from '../state/family.tsx';
import { colors, fonts, shadow } from '../theme.ts';

export default function Home() {
  const { state, today } = useFamily();
  const insets = useSafeAreaInsets();
  const { width } = useWindowDimensions();
  if (!state.settings) return <Redirect href="/setup" />;

  const tasks = state.settings.tasks;
  const kids = [...state.kids].sort((a, b) => a.createdAt - b.createdAt);
  const cols = width >= 700 ? 3 : 2;
  const cardW = (Math.min(width, 760) - 32 - 14 * (cols - 1)) / cols;

  return (
    <ScrollView contentContainerStyle={[st.page, { paddingTop: insets.top + 12, paddingBottom: insets.bottom + 32 }]}>
      <View style={st.top}>
        <Text style={st.brand}>Chordoos</Text>
        <Button title="🔒 Grown-ups" onPress={() => router.push('/grownups')} />
      </View>
      <H1>Who's doing tasks today?</H1>
      {kids.length === 0 ? (
        <Panel style={{ alignItems: 'center' }}>
          <Body muted>No kids yet. A grown-up can add kids in Grown-ups.</Body>
          <Button title="Open Grown-ups" kind="primary" onPress={() => router.push('/grownups')} />
        </Panel>
      ) : (
        <View style={st.grid}>
          {kids.map((k) => {
            const left = tasks.filter((t) => !isDone(k, t, today)).length;
            const owned = ownedCount(k);
            return (
              <Squish key={k.id} label={`${k.name}, ${k.stars} stars`} onPress={() => router.push(`/kid/${k.id}`)} style={[st.card, { width: cardW }]}>
                <Avatar color={k.color} name={k.name}>
                  {k.buddy && k.collection[k.buddy] ? <Character id={k.buddy} size={80} /> : undefined}
                </Avatar>
                <Text style={st.name} numberOfLines={1}>{k.name}</Text>
                <StarCount value={k.stars} />
                <Body muted style={st.small}>{left ? `${left} task${left > 1 ? 's' : ''} left` : 'All done today!'}</Body>
                <View style={st.meter}>
                  <View style={[st.meterFill, { width: `${(owned / CHARACTERS.length) * 100}%` }]} />
                </View>
                <Body muted style={st.small}>{owned} of {CHARACTERS.length} Chordoos</Body>
              </Squish>
            );
          })}
        </View>
      )}
    </ScrollView>
  );
}

const st = StyleSheet.create({
  page: { paddingHorizontal: 16, gap: 18, maxWidth: 760, width: '100%', alignSelf: 'center' },
  top: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  brand: { fontFamily: fonts.display, fontSize: 28, color: colors.ink },
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 14 },
  card: {
    backgroundColor: colors.surface,
    borderRadius: 24,
    borderWidth: 2,
    borderColor: colors.line,
    padding: 14,
    alignItems: 'center',
    gap: 8,
    ...shadow,
  },
  name: { fontFamily: fonts.display, fontSize: 22, color: colors.ink },
  small: { fontSize: 14 },
  meter: { height: 10, width: '100%', borderRadius: 99, backgroundColor: colors.tile, overflow: 'hidden' },
  meterFill: { height: '100%', backgroundColor: colors.good, borderRadius: 99 },
});

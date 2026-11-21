export type Rarity = 0 | 1 | 2 | 3 | 4;

export interface RarityInfo {
  key: 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary';
  label: string;
  /** Percent chance of this tier on each surprise. Tiers add up to 100. */
  odds: number;
  color: string;
}

export const RARITIES: readonly RarityInfo[] = [
  { key: 'common', label: 'Common', odds: 50, color: '#8A9BA8' },
  { key: 'uncommon', label: 'Uncommon', odds: 28, color: '#22B573' },
  { key: 'rare', label: 'Rare', odds: 14, color: '#3A86FF' },
  { key: 'epic', label: 'Epic', odds: 6, color: '#A24BFF' },
  { key: 'legendary', label: 'Legendary', odds: 2, color: '#F5A300' },
];

export interface CharacterInfo {
  id: string;
  name: string;
  rarity: Rarity;
  style: string;
  flavor: string;
}

const c = (id: string, name: string, rarity: Rarity, style: string, flavor: string): CharacterInfo => ({
  id,
  name,
  rarity,
  style,
  flavor,
});

/**
 * The roster. Every entry needs a matching art/<id>.svg (then run `npm run art`).
 * New batches are added here as they are drawn.
 */
export const CHARACTERS: readonly CharacterInfo[] = [
  c('puddle', 'Puddle', 0, 'Water', 'Smiles all day and blows bubbles when it is happy.'),
  c('bunbun', 'Bun Bun', 0, 'Cute', 'Hops three times before every nap, and never shares the carrot.'),
  c('sprig', 'Sprig', 0, 'Nature', 'A fox with a leaf for a tail. Grows a little every time it rains.'),
  c('pip', 'Pip', 0, 'Sky', 'Sings the wake-up song every morning, right on time.'),

  c('glimmer', 'Glimmer', 1, 'Fairy', 'A fairy drop who leaves a trail of glitter wherever it goes.'),
  c('volt', 'Volt', 1, 'Electric', 'A beetle that runs on 100% kid energy.'),

  c('shade', 'Shade', 2, 'Cool', 'Too cool for bedtime. Skates there anyway.'),

  c('geode', 'Geode', 3, 'Crystal', 'A gentle rock giant with a glowing crystal heart.'),

  c('blazeking', 'Blaze King', 4, 'Dragon', 'A mighty little dragon who only appears for the hardest workers.'),
];

export const CHARACTER_BY_ID: Readonly<Record<string, CharacterInfo>> = Object.fromEntries(
  CHARACTERS.map((ch) => [ch.id, ch]),
);

import { ROSTER } from './rosterData.ts';

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

/**
 * The roster lives in roster/roster.py. Running `npm run roster` regenerates
 * rosterData.ts with every Chordoo that has art/<id>.svg (then run `npm run art`).
 */
export const CHARACTERS: readonly CharacterInfo[] = ROSTER;

export const CHARACTER_BY_ID: Readonly<Record<string, CharacterInfo>> = Object.fromEntries(
  CHARACTERS.map((ch) => [ch.id, ch]),
);

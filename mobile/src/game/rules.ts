import { CHARACTERS, RARITIES, type CharacterInfo, type Rarity } from './characters.ts';

export type Repeat = 'daily' | 'once';

export interface Task {
  id: string;
  name: string;
  icon: string;
  stars: number;
  repeat: Repeat;
}

export interface Kid {
  id: string;
  name: string;
  color: string;
  stars: number;
  /** Character id -> how many of it this kid has. */
  collection: Record<string, number>;
  /** Task id -> local date (YYYY-MM-DD) it was last done. */
  done: Record<string, string>;
  pulls: number;
  /** Surprises opened since the last Rare-or-better. */
  sinceRare: number;
  buddy: string | null;
  createdAt: number;
}

export interface Settings {
  tasks: Task[];
  /** Stars needed for one surprise. */
  cost: number;
  pin: string;
  sound: boolean;
}

export interface FamilyState {
  version: 1;
  settings: Settings | null;
  kids: Kid[];
}

/** Every Nth surprise is guaranteed to be Rare or better. */
export const PITY_EVERY = 10;
/** Chance to swap a repeat for a character the kid doesn't have yet (same tier). */
export const NEW_BIAS = 0.6;

export const KID_COLORS = ['#FF6B4A', '#3A86FF', '#22B573', '#A24BFF', '#F5A300', '#FF4D8D', '#14B8A6'];

export function localDate(d: Date = new Date()): string {
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${d.getFullYear()}-${m}-${day}`;
}

export function newId(): string {
  return Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
}

export function makeKid(name: string, index: number, now = Date.now()): Kid {
  return {
    id: newId(),
    name: name.trim().slice(0, 24),
    color: KID_COLORS[index % KID_COLORS.length],
    stars: 0,
    collection: {},
    done: {},
    pulls: 0,
    sinceRare: 0,
    buddy: null,
    createdAt: now + index,
  };
}

export function isDone(kid: Kid, task: Task, today = localDate()): boolean {
  const v = kid.done[task.id];
  if (!v) return false;
  return task.repeat === 'once' ? true : v === today;
}

export function ownedCount(kid: Kid): number {
  return CHARACTERS.filter((ch) => (kid.collection[ch.id] ?? 0) > 0).length;
}

export type ToggleResult = { kid: Kid; change: 'done' | 'undone' } | { kid: Kid; change: 'blocked' };

/** Tick a task on or off. Unticking is blocked when the stars were already spent. */
export function toggleTask(kid: Kid, task: Task, today = localDate()): ToggleResult {
  if (isDone(kid, task, today)) {
    if (kid.stars < task.stars) return { kid, change: 'blocked' };
    const done = { ...kid.done };
    delete done[task.id];
    return { kid: { ...kid, done, stars: kid.stars - task.stars }, change: 'undone' };
  }
  return {
    kid: { ...kid, done: { ...kid.done, [task.id]: today }, stars: kid.stars + task.stars },
    change: 'done',
  };
}

export interface PullResult {
  kid: Kid;
  character: CharacterInfo;
  isNew: boolean;
  count: number;
}

export function rollRarity(rand: () => number): Rarity {
  const roll = rand() * 100;
  let acc = 0;
  for (let i = 0; i < RARITIES.length; i++) {
    acc += RARITIES[i].odds;
    if (roll < acc) return i as Rarity;
  }
  return 0;
}

/** Spend stars and open one surprise. Returns null when the kid can't afford it. */
export function openSurprise(kid: Kid, cost: number, rand: () => number = Math.random): PullResult | null {
  if (kid.stars < cost) return null;
  let rarity = rollRarity(rand);
  let sinceRare = kid.sinceRare + 1;
  if (sinceRare >= PITY_EVERY && rarity < 2) rarity = 2;
  if (rarity >= 2) sinceRare = 0;

  const pool = CHARACTERS.filter((ch) => ch.rarity === rarity);
  let pick = pool[Math.floor(rand() * pool.length)];
  if ((kid.collection[pick.id] ?? 0) > 0 && rand() < NEW_BIAS) {
    const fresh = pool.filter((ch) => !kid.collection[ch.id]);
    if (fresh.length) pick = fresh[Math.floor(rand() * fresh.length)];
  }
  const isNew = !kid.collection[pick.id];
  const count = (kid.collection[pick.id] ?? 0) + 1;
  const collection = { ...kid.collection, [pick.id]: count };
  const next: Kid = {
    ...kid,
    stars: kid.stars - cost,
    pulls: kid.pulls + 1,
    sinceRare,
    collection,
    buddy: kid.buddy ?? (isNew ? pick.id : null),
  };
  return { kid: next, character: pick, isNew, count };
}

export const SUGGESTED_TASKS: ReadonlyArray<Omit<Task, 'id'> & { on: boolean }> = [
  { name: 'Brush teeth (morning)', icon: '🦷', stars: 1, repeat: 'daily', on: true },
  { name: 'Brush teeth (bedtime)', icon: '🦷', stars: 1, repeat: 'daily', on: true },
  { name: 'Read a chapter of a book', icon: '📖', stars: 2, repeat: 'daily', on: true },
  { name: 'Make your bed', icon: '🛏️', stars: 1, repeat: 'daily', on: true },
  { name: 'Tidy up your toys', icon: '🧸', stars: 1, repeat: 'daily', on: true },
  { name: 'Get dressed by yourself', icon: '👕', stars: 1, repeat: 'daily', on: false },
  { name: 'Do your homework', icon: '✏️', stars: 2, repeat: 'daily', on: false },
  { name: 'Help set the table', icon: '🍽️', stars: 1, repeat: 'daily', on: false },
];

export const TASK_ICONS = ['🦷', '📖', '🛏️', '🧸', '👕', '✏️', '🍽️', '🛁', '🧹', '🥦', '🐶', '🌱', '🎹', '⚽', '🎒', '💧', '🙏', '⭐'];

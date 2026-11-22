export type Repeat = 'daily' | 'once';

export interface Task {
  id: string;
  name: string;
  icon: string;
  points: number;
  repeat: Repeat;
}

/** Something a grown-up offers. Kids buy it as a sliver on their wheel. */
export interface Prize {
  id: string;
  name: string;
  icon: string;
  cost: number;
}

/** One slice of a kid's wheel. Name and cost are copied so later edits don't change it. */
export interface Sliver {
  id: string;
  prizeId: string;
  name: string;
  icon: string;
  cost: number;
}

/** A prize the wheel landed on, waiting for a grown-up to hand it out. */
export interface Win {
  id: string;
  name: string;
  icon: string;
  at: number;
  given: boolean;
}

export interface Kid {
  id: string;
  name: string;
  color: string;
  points: number;
  /** Task id -> local date (YYYY-MM-DD) it was last done. */
  done: Record<string, string>;
  wheel: Sliver[];
  wins: Win[];
  createdAt: number;
}

export interface Settings {
  tasks: Task[];
  prizes: Prize[];
  pin: string;
  sound: boolean;
}

export interface FamilyState {
  version: 2;
  settings: Settings | null;
  kids: Kid[];
}

/** The wheel needs this many slivers before it can spin. */
export const MIN_SLIVERS = 4;
export const MAX_POINTS = 999;

export const KID_COLORS = ['#FF6B4A', '#3A86FF', '#22B573', '#A24BFF', '#F5A300', '#FF4D8D', '#14B8A6'];
export const SLIVER_COLORS = ['#FF6B4A', '#FFB703', '#22B573', '#3A86FF', '#A24BFF', '#FF4D8D', '#14B8A6', '#F77F00'];

export function localDate(d: Date = new Date()): string {
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${d.getFullYear()}-${m}-${day}`;
}

export function newId(): string {
  return Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
}

export function clampPoints(n: number): number {
  if (!Number.isFinite(n)) return 1;
  return Math.max(1, Math.min(MAX_POINTS, Math.round(n)));
}

export function makeKid(name: string, index: number, now = Date.now()): Kid {
  return {
    id: newId(),
    name: name.trim().slice(0, 24),
    color: KID_COLORS[index % KID_COLORS.length],
    points: 0,
    done: {},
    wheel: [],
    wins: [],
    createdAt: now + index,
  };
}

export function isDone(kid: Kid, task: Task, today = localDate()): boolean {
  const v = kid.done[task.id];
  if (!v) return false;
  return task.repeat === 'once' ? true : v === today;
}

export type ToggleResult = { kid: Kid; change: 'done' | 'undone' | 'blocked' };

/** Tick a task on or off. Unticking is blocked when the points were already spent. */
export function toggleTask(kid: Kid, task: Task, today = localDate()): ToggleResult {
  if (isDone(kid, task, today)) {
    if (kid.points < task.points) return { kid, change: 'blocked' };
    const done = { ...kid.done };
    delete done[task.id];
    return { kid: { ...kid, done, points: kid.points - task.points }, change: 'undone' };
  }
  return {
    kid: { ...kid, done: { ...kid.done, [task.id]: today }, points: kid.points + task.points },
    change: 'done',
  };
}

export type BuyResult = { ok: true; kid: Kid } | { ok: false; reason: 'points' | 'owned' };

export function onWheel(kid: Kid, prizeId: string): boolean {
  return kid.wheel.some((w) => w.prizeId === prizeId);
}

/** Spend points to put a prize on the wheel as one sliver. Each prize can be on the wheel once. Purchases are final. */
export function buySliver(kid: Kid, prize: Prize): BuyResult {
  if (onWheel(kid, prize.id)) return { ok: false, reason: 'owned' };
  if (kid.points < prize.cost) return { ok: false, reason: 'points' };
  const sliver: Sliver = { id: newId(), prizeId: prize.id, name: prize.name, icon: prize.icon, cost: prize.cost };
  return { ok: true, kid: { ...kid, points: kid.points - prize.cost, wheel: [...kid.wheel, sliver] } };
}

export function canSpin(kid: Kid): boolean {
  return kid.wheel.length >= MIN_SLIVERS;
}

export interface SpinResult {
  kid: Kid;
  /** Index of the winning sliver in the wheel as it was before the spin. */
  index: number;
  sliver: Sliver;
}

/**
 * Spin the wheel. Spinning is free and every sliver has the same chance. The winning sliver
 * becomes a prize to hand out, and the whole wheel clears so the kid starts a new one.
 */
export function spin(kid: Kid, rand: () => number = Math.random, now = Date.now()): SpinResult | null {
  if (!canSpin(kid)) return null;
  const index = Math.min(kid.wheel.length - 1, Math.floor(rand() * kid.wheel.length));
  const sliver = kid.wheel[index];
  const win: Win = { id: newId(), name: sliver.name, icon: sliver.icon, at: now, given: false };
  return {
    index,
    sliver,
    kid: { ...kid, wheel: [], wins: [win, ...kid.wins].slice(0, 100) },
  };
}

export function markGiven(kid: Kid, winId: string): Kid {
  return { ...kid, wins: kid.wins.map((w) => (w.id === winId ? { ...w, given: true } : w)) };
}

export function pendingWins(kid: Kid): Win[] {
  return kid.wins.filter((w) => !w.given);
}

/** Rotation (degrees, clockwise) that puts the middle of slice `index` under a pointer at the top. */
export function landingAngle(index: number, count: number, turns = 5, jitter = 0): number {
  const slice = 360 / count;
  const mid = index * slice + slice / 2 + jitter * slice * 0.35;
  return turns * 360 + (360 - mid);
}

export const TASK_ICONS = ['🦷', '📖', '🛏️', '🧸', '👕', '✏️', '🍽️', '🛁', '🧹', '🥦', '🐶', '🌱', '🎹', '⚽', '🎒', '💧', '🙏', '⭐'];
export const PRIZE_ICONS = ['🍫', '🍦', '🧸', '🎮', '📺', '🎨', '🍕', '🎟️', '📚', '🛝', '🏊', '🍿', '🎁', '⏰', '🚲', '💵', '🌙', '⭐'];

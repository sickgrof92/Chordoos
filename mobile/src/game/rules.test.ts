/// <reference types="node" />
import assert from 'node:assert/strict';
import { test } from 'node:test';
import {
  buySliver, canSpin, isDone, landingAngle, makeKid, markGiven, MIN_SLIVERS,
  pendingWins, spin, toggleTask, type Kid, type Prize, type Task,
} from './rules.ts';

const teeth: Task = { id: 't1', name: 'Brush teeth', icon: '🦷', points: 1, repeat: 'daily' };
const veg: Task = { id: 't2', name: 'Eat vegetables', icon: '🥦', points: 5, repeat: 'once' };
const choc: Prize = { id: 'p1', name: 'Chocolate', icon: '🍫', cost: 5 };
const toy: Prize = { id: 'p2', name: 'New toy', icon: '🧸', cost: 10 };
const games: Prize = { id: 'p3', name: 'Video games', icon: '🎮', cost: 20 };
const park: Prize = { id: 'p4', name: 'Trip to the park', icon: '🛝', cost: 8 };
const prizes = [choc, toy, games, park];

/** Buy a sliver that must succeed. */
function buy(kid: Kid, p: Prize): Kid {
  const r = buySliver(kid, p);
  if (!r.ok) throw new Error(`could not buy ${p.name}: ${r.reason}`);
  return r.kid;
}

test('ticking a task adds its points, unticking takes them back', () => {
  const kid = makeKid('Ava', 0);
  const a = toggleTask(kid, veg, '2026-11-22');
  assert.equal(a.change, 'done');
  assert.equal(a.kid.points, 5);
  const b = toggleTask(a.kid, veg, '2026-11-22');
  assert.equal(b.change, 'undone');
  assert.equal(b.kid.points, 0);
});

test('daily tasks reset the next day, one-time tasks stay done', () => {
  let kid = makeKid('Ava', 0);
  kid = toggleTask(kid, teeth, '2026-11-22').kid;
  kid = toggleTask(kid, veg, '2026-11-22').kid;
  assert.equal(isDone(kid, teeth, '2026-11-23'), false);
  assert.equal(isDone(kid, veg, '2026-11-23'), true);
});

test('unticking is blocked once the points are spent', () => {
  let kid = toggleTask(makeKid('Ava', 0), veg, '2026-11-22').kid;
  kid = buy(kid, choc);
  assert.equal(toggleTask(kid, veg, '2026-11-22').change, 'blocked');
});

test('buying a sliver costs its points and needs enough of them', () => {
  const kid = { ...makeKid('Ava', 0), points: 12 };
  const after = buy(kid, toy);
  assert.equal(after.points, 2);
  assert.equal(after.wheel.length, 1);
  assert.equal(after.wheel[0].name, 'New toy');
  const again = buySliver(after, games);
  assert.deepEqual(again, { ok: false, reason: 'points' });
});

test('each prize can be on the wheel only once', () => {
  const kid = buy({ ...makeKid('Ava', 0), points: 100 }, choc);
  assert.deepEqual(buySliver(kid, choc), { ok: false, reason: 'owned' });
  assert.equal(buy(kid, toy).wheel.length, 2);
});

test(`the wheel needs ${MIN_SLIVERS} slivers to spin`, () => {
  let kid = { ...makeKid('Ava', 0), points: 100 };
  for (const p of prizes.slice(0, MIN_SLIVERS - 1)) kid = buy(kid, p);
  assert.equal(canSpin(kid), false);
  assert.equal(spin(kid), null);
  assert.equal(canSpin(buy(kid, prizes[MIN_SLIVERS - 1])), true);
});

test('spinning is free, wins one prize and clears the whole wheel', () => {
  let kid = { ...makeKid('Ava', 0), points: 100 };
  for (const p of [choc, park, toy, games]) kid = buy(kid, p);
  const res = spin(kid, () => 0.6); // index 2 of 4
  if (!res) throw new Error('should spin');
  assert.equal(res.index, 2);
  assert.equal(res.sliver.name, 'New toy');
  assert.equal(res.kid.wheel.length, 0);
  assert.equal(canSpin(res.kid), false);
  assert.equal(res.kid.points, kid.points);
  assert.equal(pendingWins(res.kid).length, 1);
  const given = markGiven(res.kid, res.kid.wins[0].id);
  assert.equal(pendingWins(given).length, 0);
});

test('spin never picks past the end even when rand returns 1', () => {
  let kid = { ...makeKid('Ava', 0), points: 100 };
  for (const p of prizes) kid = buy(kid, p);
  assert.equal(spin(kid, () => 1)?.index, 3);
});

test('the landing angle puts the winning slice under the top pointer', () => {
  for (const count of [4, 5, 9, 12]) {
    for (let i = 0; i < count; i++) {
      const rot = landingAngle(i, count, 5, 0) % 360;
      // After rotating clockwise by rot, the point at angle a sits at a + rot. Top is 0.
      const mid = (i + 0.5) * (360 / count);
      assert.ok(Math.abs(((mid + rot) % 360)) < 1e-6 || Math.abs(((mid + rot) % 360) - 360) < 1e-6);
    }
  }
});

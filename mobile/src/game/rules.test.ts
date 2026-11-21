/// <reference types="node" />
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readdirSync } from 'node:fs';
import { CHARACTERS, RARITIES } from './characters.ts';
import { makeKid, openSurprise, toggleTask, isDone, rollRarity, PITY_EVERY, type Task } from './rules.ts';

const brush: Task = { id: 't1', name: 'Brush teeth', icon: '🦷', stars: 2, repeat: 'daily' };
const once: Task = { id: 't2', name: 'Clean room', icon: '🧹', stars: 1, repeat: 'once' };

test('odds add up to 100 and every tier has characters', () => {
  assert.equal(RARITIES.reduce((a, r) => a + r.odds, 0), 100);
  for (let r = 0; r < RARITIES.length; r++) assert.ok(CHARACTERS.some((c) => c.rarity === r));
  assert.equal(new Set(CHARACTERS.map((c) => c.id)).size, CHARACTERS.length);
});

test('ticking a task earns stars and unticking returns them', () => {
  const kid = makeKid('Ava', 0);
  const a = toggleTask(kid, brush, '2026-11-21');
  assert.equal(a.change, 'done');
  assert.equal(a.kid.stars, 2);
  assert.ok(isDone(a.kid, brush, '2026-11-21'));
  const b = toggleTask(a.kid, brush, '2026-11-21');
  assert.equal(b.change, 'undone');
  assert.equal(b.kid.stars, 0);
});

test('daily tasks reset the next day; one-time tasks stay done', () => {
  let kid = toggleTask(makeKid('Ava', 0), brush, '2026-11-21').kid;
  kid = toggleTask(kid, once, '2026-11-21').kid;
  assert.equal(isDone(kid, brush, '2026-11-22'), false);
  assert.equal(isDone(kid, once, '2026-11-22'), true);
});

test('unticking is blocked once the stars are spent', () => {
  const kid = { ...toggleTask(makeKid('Ava', 0), brush, '2026-11-21').kid };
  const spent = openSurprise(kid, 2)!.kid;
  assert.equal(toggleTask(spent, brush, '2026-11-21').change, 'blocked');
});

test('a surprise needs enough stars and spends them', () => {
  const kid = { ...makeKid('Ava', 0), stars: 2 };
  assert.equal(openSurprise(kid, 3), null);
  const r = openSurprise({ ...kid, stars: 5 }, 3)!;
  assert.equal(r.kid.stars, 2);
  assert.equal(r.kid.pulls, 1);
  assert.equal(r.isNew, true);
  assert.equal(r.kid.collection[r.character.id], 1);
  assert.equal(r.kid.buddy, r.character.id);
});

test('every 10th surprise without a Rare is upgraded to Rare', () => {
  const alwaysCommon = () => 0.01;
  let kid = { ...makeKid('Ava', 0), stars: 100 };
  for (let i = 1; i < PITY_EVERY; i++) {
    const r = openSurprise(kid, 1, alwaysCommon)!;
    assert.equal(r.character.rarity, 0);
    kid = r.kid;
  }
  const tenth = openSurprise(kid, 1, alwaysCommon)!;
  assert.equal(tenth.character.rarity, 2);
  assert.equal(tenth.kid.sinceRare, 0);
});

test('rarity roll matches the published odds', () => {
  const counts = [0, 0, 0, 0, 0];
  let seed = 42;
  // mulberry32: small seeded PRNG so the test is repeatable
  const rand = () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const n = 200000;
  for (let i = 0; i < n; i++) counts[rollRarity(rand)]++;
  RARITIES.forEach((r, i) => assert.ok(Math.abs((counts[i] / n) * 100 - r.odds) < 0.6, `${r.label}: ${(counts[i] / n) * 100}`));
});

test('every character has art', () => {
  const art = new Set(readdirSync(new URL('../../art', import.meta.url)).map((f) => f.replace(/\.svg$/, '')));
  for (const c of CHARACTERS) assert.ok(art.has(c.id), `missing art/${c.id}.svg`);
});

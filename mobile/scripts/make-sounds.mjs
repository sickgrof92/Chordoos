// Generates the small sound effects in assets/sounds as 16-bit mono WAV files.
// Run: node scripts/make-sounds.mjs
import { mkdirSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const RATE = 44100;
const out = join(dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'sounds');
mkdirSync(out, { recursive: true });

/** notes: [frequencyHz, startSec, durationSec, wave] */
function render(notes, total, volume = 0.35) {
  const n = Math.ceil(total * RATE);
  const buf = new Float32Array(n);
  for (const [f, start, dur, wave = 'tri'] of notes) {
    const s0 = Math.floor(start * RATE);
    const len = Math.floor(dur * RATE);
    for (let i = 0; i < len && s0 + i < n; i++) {
      const t = i / RATE;
      const ph = (t * f) % 1;
      let v = wave === 'sq' ? (ph < 0.5 ? 0.6 : -0.6) : wave === 'sine' ? Math.sin(2 * Math.PI * ph) : 1 - 4 * Math.abs(ph - 0.5);
      const attack = Math.min(1, i / (0.01 * RATE));
      const decay = Math.exp((-4 * i) / len);
      buf[s0 + i] += v * attack * decay * volume;
    }
  }
  const data = Buffer.alloc(n * 2);
  for (let i = 0; i < n; i++) data.writeInt16LE(Math.max(-1, Math.min(1, buf[i])) * 32767, i * 2);
  const h = Buffer.alloc(44);
  h.write('RIFF', 0); h.writeUInt32LE(36 + data.length, 4); h.write('WAVE', 8);
  h.write('fmt ', 12); h.writeUInt32LE(16, 16); h.writeUInt16LE(1, 20); h.writeUInt16LE(1, 22);
  h.writeUInt32LE(RATE, 24); h.writeUInt32LE(RATE * 2, 28); h.writeUInt16LE(2, 32); h.writeUInt16LE(16, 34);
  h.write('data', 36); h.writeUInt32LE(data.length, 40);
  return Buffer.concat([h, data]);
}

const files = {
  'ding.wav': render([[880, 0, 0.12], [1320, 0.08, 0.2]], 0.32),
  'tap.wav': render([[520, 0, 0.09, 'sq']], 0.12, 0.2),
  'reveal.wav': render([[523, 0, 0.25], [659, 0.1, 0.25], [784, 0.2, 0.25], [1047, 0.3, 0.5]], 0.85),
  'reveal-big.wav': render([[523, 0, 0.25], [659, 0.09, 0.25], [784, 0.18, 0.25], [1047, 0.27, 0.3], [1319, 0.36, 0.3], [1568, 0.45, 0.7]], 1.2),
};
for (const [name, buf] of Object.entries(files)) writeFileSync(join(out, name), buf);
console.log('Wrote', Object.keys(files).join(', '));

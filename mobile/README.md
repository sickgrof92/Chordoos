# Chordoos mobile app

The iOS and Android version of Chordoos, built with Expo (SDK 58) and React Native.

Kids tick off tasks to earn stars. Stars open a surprise pod with a Chordoo inside. Chordoos come in five rarity tiers (Common 50%, Uncommon 28%, Rare 14%, Epic 6%, Legendary 2%). Every 10th surprise is at least Rare, and new Chordoos are favored over repeats.

## Run it
```bash
npm install
npx expo start          # then open in a development build or simulator
```
The app uses native modules (audio, haptics, SVG), so use a development build: `npx eas-cli@latest build --profile development`, or `npx expo run:ios` / `npx expo run:android` on a machine with Xcode or Android Studio. No Mac is needed when building with EAS in the cloud.

## Checks
```bash
npm run typecheck       # TypeScript
npm test                # game rules: odds, pity, task ticking, every Chordoo has art
```

## Adding Chordoos
1. Draw `art/<id>.svg` (200×200 viewBox). Give glows and sparkles `class="fx"` so they are left out of the mystery silhouette.
2. Add the Chordoo to `CHARACTERS` in `src/game/characters.ts`.
3. Run `npm run art` to bundle the drawings, then `npm test`.

## Layout
- `src/app/` screens (Expo Router): home, setup, kid, reveal, grown-ups
- `src/game/` pure game rules and the roster, with tests
- `src/state/family.tsx` family data, saved on the device
- `src/characters/` the character renderer and bundled art
- `scripts/` art bundler and sound generator

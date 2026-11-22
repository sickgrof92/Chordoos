# Chordoos mobile app

The iOS and Android version of Chordoos, built with Expo (SDK 58) and React Native.

Grown-ups set everything: the tasks, how many points each one earns, and the prizes with their costs. Nothing is premade. Kids tick off tasks to earn points and spend them to put prizes on their wheel, one slice per prize. Purchases are final. Once the wheel has at least 4 slices the kid can spin it for free. They win the slice it lands on, which goes to the grown-ups' "Prizes to hand out" list, and the whole wheel clears.

## Run it
```bash
npm install
npx expo start          # then open in a development build or simulator
```
The app uses native modules (audio, haptics, SVG), so use a development build: `npx eas-cli@latest build --profile development`, or `npx expo run:ios` / `npx expo run:android` on a machine with Xcode or Android Studio. No Mac is needed when building with EAS in the cloud.

## Checks
```bash
npm run typecheck       # TypeScript
npm test                # game rules: points, buying slices, spinning and clearing, wheel angles
```

## Layout
- `src/app/` screens (Expo Router): home, setup, kid (tasks and prize shop), spin, grown-ups
- `src/game/` pure game rules, with tests
- `src/state/family.tsx` family data, saved on the device
- `src/components/Wheel.tsx` the prize wheel drawing
- `scripts/` sound generator

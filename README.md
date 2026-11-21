# Chordoos

A home-screen app for kids: finish tasks like brushing teeth or reading a chapter, earn stars, and open surprise pods to collect 30 original characters across five rarity tiers (Common, Uncommon, Rare, Epic, Legendary).

## Features
- Several kids per family, each with their own stars, collection and buddy avatar
- Daily tasks that reset each morning, plus one-time tasks
- Surprise pod reveal with rarity glow, confetti and sound
- Odds: Common 50%, Uncommon 28%, Rare 14%, Epic 6%, Legendary 2%; every 10th surprise is Rare or better; new characters are favored over repeats
- Grown-ups area behind an optional 4-digit code: edit tasks, stars per surprise, bonus stars, kids
- Works offline and installs to the home screen (PWA)

## Install on a phone or tablet
- iPhone/iPad (Safari): open the site, tap Share, then **Add to Home Screen**.
- Android (Chrome): open the site, tap the menu, then **Install app**.

Progress is saved on each device (browser storage). Each phone or tablet keeps its own family.

## Files
- `index.html`: the whole app (HTML, CSS, JS; characters are drawn as SVG in code)
- `manifest.webmanifest`, `sw.js`, `icons/`: install and offline support

## Hosting
Any static host works. On GitHub Pages: Settings → Pages → Deploy from branch → `main` / root.

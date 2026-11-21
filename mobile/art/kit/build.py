"""Writes art/<id>.svg for every Chordoo drawn with the toolkit.

Usage: python3 art/kit/build.py [theme ...]   (no args = all themes)
Then run `npm run art` to bundle the SVGs into the app.
"""
import importlib, re, sys
from pathlib import Path

KIT = Path(__file__).parent
sys.path.insert(0, str(KIT))
from artkit import REGISTRY, Art  # noqa: E402

THEMES = ["fire", "water", "plant", "sky", "electric", "ice", "crystal", "bug",
          "spooky", "cosmic", "snack", "music", "robot", "fairy", "desert", "street"]


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def main(themes):
    for t in themes:
        if (KIT / f"{t}.py").exists():
            importlib.import_module(t)
    out = KIT.parent
    for cid, fn in REGISTRY.items():
        a = Art(cid)
        fn(a)
        (out / f"{cid}.svg").write_text(a.render())
    print(f"wrote {len(REGISTRY)} drawings: {' '.join(REGISTRY)}")


if __name__ == "__main__":
    main(sys.argv[1:] or THEMES)

"""Writes the creature-style (v2) samples to art/v2/<id>.svg.

Usage: python3 art/kit/build_v2.py
"""
import sys
from pathlib import Path

KIT = Path(__file__).parent
sys.path.insert(0, str(KIT))
from artkit import REGISTRY, Art  # noqa: E402
import monsters  # noqa: E402,F401

out = KIT.parent / "v2"
out.mkdir(exist_ok=True)
for cid, fn in REGISTRY.items():
    a = Art(cid)
    fn(a)
    (out / f"{cid}.svg").write_text(a.render())
print(f"wrote {len(REGISTRY)} drawings: {' '.join(REGISTRY)}")

"""Creature style (v2): monster-collector look instead of cute mascots.

Differences from the v1 kit: flat cel shading with a hard shadow edge, almond
eyes with whites and slit or round pupils, heavier ink, real anatomy (claws,
fangs, muscle, armor) and poses with some attitude.
"""
from artkit import Art

INK2 = "#1A1424"


def cel(a: Art, d: str, base: str, shade: str, light: str | None = None,
        o: str = INK2, w: float = 4, shift=(9, 9)):
    """Fill a shape flat, shade its lower-right side with a hard edge, outline it."""
    cid = a._id("c")
    a.defs.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
    dx, dy = shift
    a.add(f'<path d="{d}" fill="{shade}"/>')
    a.add(f'<g clip-path="url(#{cid})"><path d="{d}" fill="{base}" transform="translate({-dx} {-dy})"/>'
          + (f'<path d="{d}" fill="none" stroke="{light}" stroke-width="5" opacity=".55" transform="translate({dx * 0.5} {dy * 0.5})"/>' if light else "")
          + '</g>')
    a.add(f'<path d="{d}" fill="none" stroke="{o}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')


def flat(a: Art, d: str, fill: str, o: str = INK2, w: float = 3.5, extra=""):
    a.add(f'<path d="{d}" fill="{fill}" stroke="{o}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"{extra}/>')


def ink(a: Art, d: str, w: float = 3, color: str = INK2, op=None):
    o = f' opacity="{op}"' if op else ""
    a.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{o}/>')


def feye(a: Art, cx, cy, w=10, h=8, iris="#FFB020", side=1, look=(0, 0), pupil="slit", tilt=12, glow=False):
    """Almond eye. side=1 is the viewer's left eye (inner corner on the right).

    tilt lifts the outer corner and drops the inner one for a determined look.
    """
    ox, ix = cx - side * w, cx + side * w            # outer and inner corners
    oy, iy = cy - tilt * 0.35, cy + tilt * 0.25
    d = (f"M{ox} {oy} Q{cx} {cy - h * 1.35} {ix} {iy} Q{cx} {cy + h * 1.05} {ox} {oy} Z")
    cid = a._id("ey")
    a.defs.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
    a.add(f'<path d="{d}" fill="#FFFFFF"/>')
    lx, ly = look
    ir = h * 0.95
    a.add(f'<g clip-path="url(#{cid})">'
          f'<circle cx="{cx + lx}" cy="{cy + ly}" r="{ir}" fill="{iris}"/>'
          f'<circle cx="{cx + lx}" cy="{cy + ly + ir * 0.35}" r="{ir * 0.8}" fill="#000" opacity=".18"/>'
          + (f'<ellipse cx="{cx + lx}" cy="{cy + ly}" rx="{ir * 0.28}" ry="{ir * 0.8}" fill="{INK2}"/>' if pupil == "slit"
             else f'<circle cx="{cx + lx}" cy="{cy + ly}" r="{ir * 0.5}" fill="{INK2}"/>')
          + f'<circle cx="{cx + lx - side * ir * 0.35}" cy="{cy + ly - ir * 0.4}" r="{ir * 0.28}" fill="#FFFFFF"/>'
          f'<path d="{d}" fill="none" stroke="#000" stroke-width="6" opacity=".12" transform="translate(0 -3)"/></g>')
    # heavy upper lid, thin lower
    a.add(f'<path d="M{ox - side * 2} {oy - 1} Q{cx} {cy - h * 1.45} {ix + side * 1} {iy}" fill="none" stroke="{INK2}" stroke-width="4" stroke-linecap="round"/>')
    a.add(f'<path d="M{ox} {oy} Q{cx} {cy + h * 1.05} {ix} {iy}" fill="none" stroke="{INK2}" stroke-width="2" stroke-linecap="round"/>')
    if glow:
        a.glow(cx, cy, w * 1.8, iris, 0.45)


def fang(a: Art, x, y, s=6, down=True):
    d = 1 if down else -1
    flat(a, f"M{x - s * 0.5} {y} L{x} {y + d * s * 1.3} L{x + s * 0.5} {y} Z", "#FFFFFF", INK2, 2)


def claws(a: Art, x, y, n=3, s=5, spread=6, down=True, color="#F4EEE0"):
    d = 1 if down else -1
    for i in range(n):
        cx = x + (i - (n - 1) / 2) * spread
        flat(a, f"M{cx - s * 0.45} {y} Q{cx} {y + d * s * 1.6} {cx + s * 0.5} {y + d * s * 0.2} Z", color, INK2, 1.8)


def shadow(a: Art, cx=100, cy=186, rx=60):
    a.ell(cx, cy, rx, 7, INK2, extra=' opacity=".18"')

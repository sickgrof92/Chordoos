"""Reusable props (bolts, stars, snowflakes, flowers, notes, gears) shared across themes."""
import math
from artkit import INK


def bolt(a, x, y, s=1.0, rot=0, fill="#FFE14D", o="#A87A00", w=2.5, cls=""):
    c = f' class="{cls}"' if cls else ""
    a.add(f'<path{c} transform="translate({x} {y}) rotate({rot}) scale({s})" '
          f'd="M4 -22 L-10 2 L-1 2 L-6 22 L10 -4 L1 -4 Z" fill="{fill}" stroke="{o}" stroke-width="{w / s:.2f}" stroke-linejoin="round"/>')


def star(a, x, y, r, fill="#FFE14D", o="#B8860B", w=2, rot=0, inner=0.5, cls=""):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + rot + i * 36)
        rr = r if i % 2 == 0 else r * inner
        pts.append(f"{x + rr * math.cos(ang):.1f} {y + rr * math.sin(ang):.1f}")
    c = f' class="{cls}"' if cls else ""
    st = f' stroke="{o}" stroke-width="{w}" stroke-linejoin="round"' if o else ""
    a.add(f'<path{c} d="M{" L".join(pts)} Z" fill="{fill}"{st}/>')


def snowflake(a, x, y, r, color="#FFFFFF", w=2, cls="fx"):
    d = ""
    for k in range(6):
        ang = math.radians(k * 60)
        ex, ey = x + r * math.cos(ang), y + r * math.sin(ang)
        d += f"M{x} {y} L{ex:.1f} {ey:.1f} "
        mx, my = x + r * 0.6 * math.cos(ang), y + r * 0.6 * math.sin(ang)
        for s in (-1, 1):
            b = ang + s * math.radians(40)
            d += f"M{mx:.1f} {my:.1f} L{mx + r * 0.3 * math.cos(b):.1f} {my + r * 0.3 * math.sin(b):.1f} "
    c = f' class="{cls}"' if cls else ""
    a.add(f'<path{c} d="{d}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" fill="none"/>')


def flower(a, x, y, r, petal="#FF8AC0", center="#FFD84D", o="#A04A7A", n=5, w=1.2, cls=""):
    c = f' class="{cls}"' if cls else ""
    a.add(f'<g{c}>' + "".join(
        f'<ellipse cx="{x}" cy="{y - r * 0.55}" rx="{r * 0.42}" ry="{r * 0.6}" fill="{petal}" stroke="{o}" '
        f'stroke-width="{w}" transform="rotate({k * 360 / n} {x} {y})"/>' for k in range(n))
        + f'<circle cx="{x}" cy="{y}" r="{r * 0.32}" fill="{center}"/></g>')


def note(a, x, y, s=1.0, color="#7A4AE0", double=False, cls="fx"):
    c = f' class="{cls}"' if cls else ""
    if double:
        d = (f"M{x} {y} V{y - 22 * s} L{x + 16 * s} {y - 26 * s} V{y - 4 * s}")
        a.add(f'<g{c}><path d="{d}" stroke="{color}" stroke-width="{2.6 * s}" fill="none" stroke-linejoin="round"/>'
              f'<ellipse cx="{x - 4 * s}" cy="{y}" rx="{5 * s}" ry="{4 * s}" fill="{color}" transform="rotate(-20 {x - 4 * s} {y})"/>'
              f'<ellipse cx="{x + 12 * s}" cy="{y - 4 * s}" rx="{5 * s}" ry="{4 * s}" fill="{color}" transform="rotate(-20 {x + 12 * s} {y - 4 * s})"/></g>')
    else:
        a.add(f'<g{c}><path d="M{x} {y} V{y - 22 * s} Q{x + 4 * s} {y - 14 * s} {x + 12 * s} {y - 12 * s}" stroke="{color}" stroke-width="{2.6 * s}" fill="none" stroke-linecap="round"/>'
              f'<ellipse cx="{x - 4 * s}" cy="{y}" rx="{5 * s}" ry="{4 * s}" fill="{color}" transform="rotate(-20 {x - 4 * s} {y})"/></g>')


def gear(a, x, y, r, fill="#C8CCD8", o="#4A5068", teeth=8, w=2.5):
    pts = []
    for i in range(teeth * 4):
        ang = math.radians(i * 360 / (teeth * 4))
        rr = r if (i % 4) in (0, 1) else r * 0.78
        pts.append(f"{x + rr * math.cos(ang):.1f} {y + rr * math.sin(ang):.1f}")
    a.add(f'<path d="M{" L".join(pts)} Z" fill="{fill}" stroke="{o}" stroke-width="{w}" stroke-linejoin="round"/>')
    a.circ(x, y, r * 0.32, "#FFFFFF", o, w * 0.8)


def zz(a, x, y, color="#8A78C8"):
    a.add(f'<text class="fx" x="{x}" y="{y}" font-size="20" font-weight="bold" font-family="sans-serif" fill="{color}">z</text>'
          f'<text class="fx" x="{x + 14}" y="{y - 14}" font-size="14" font-weight="bold" font-family="sans-serif" fill="{color}">z</text>')


def limb(a, d, fill, o=INK, w=9):
    """Tube-like arm or leg along a path: outline then fill."""
    a.line(d, o, w)
    a.line(d, fill, w - 4)

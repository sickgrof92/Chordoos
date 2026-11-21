"""Small drawing toolkit for Chordoos art.

Every Chordoo is still drawn by hand (its own body, limbs and props), but the
shared pieces (shading gradients, glossy eyes, cheeks, mouths, sparkles) come
from here so the whole collection keeps one consistent look.

All drawings use a 200x200 viewBox. Effects that should not appear in the
mystery silhouette (glows, sparkles) carry class="fx".
"""
from __future__ import annotations

REGISTRY: dict[str, callable] = {}
INK = "#2B2340"


def chordoo(cid: str):
    """Decorator: registers a drawing function under its Chordoo id."""
    def wrap(fn):
        REGISTRY[cid] = fn
        return fn
    return wrap


class Art:
    """Collects defs and shapes for one drawing. Ids are prefixed per Chordoo."""

    def __init__(self, cid: str):
        self.cid = cid
        self.defs: list[str] = []
        self.parts: list[str] = []
        self._n = 0

    # ---- ids & gradients -------------------------------------------------
    def _id(self, name: str) -> str:
        self._n += 1
        return f"{self.cid}-{name}{self._n}"

    def shade(self, light: str, mid: str, dark: str, cx=0.38, cy=0.3, r=0.85) -> str:
        """Soft 3-tone body shading, lit from the top left. Returns a fill value."""
        gid = self._id("s")
        self.defs.append(
            f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="{r}">'
            f'<stop offset="0" stop-color="{light}"/><stop offset="0.5" stop-color="{mid}"/>'
            f'<stop offset="1" stop-color="{dark}"/></radialGradient>')
        return f"url(#{gid})"

    def lin(self, *colors: str, x1=0, y1=0, x2=0, y2=1) -> str:
        gid = self._id("l")
        n = len(colors) - 1
        stops = "".join(f'<stop offset="{i / n:.2f}" stop-color="{c}"/>' for i, c in enumerate(colors))
        self.defs.append(f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{stops}</linearGradient>')
        return f"url(#{gid})"

    def fade(self, color: str, alpha=0.7) -> str:
        """Radial color that fades to transparent (cheeks, glows)."""
        gid = self._id("f")
        self.defs.append(
            f'<radialGradient id="{gid}"><stop offset="0" stop-color="{color}" stop-opacity="{alpha}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')
        return f"url(#{gid})"

    # ---- primitives ------------------------------------------------------
    def add(self, s: str):
        self.parts.append(s)
        return self

    def path(self, d: str, fill="none", stroke=INK, w=3.5, extra=""):
        sw = f' stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"' if stroke else ""
        return self.add(f'<path d="{d}" fill="{fill}"{sw}{extra}/>')

    def ell(self, cx, cy, rx, ry, fill, stroke=None, w=3.5, rot=0, extra=""):
        sw = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ""
        tr = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
        return self.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"{sw}{tr}{extra}/>')

    def circ(self, cx, cy, r, fill, stroke=None, w=3, extra=""):
        sw = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ""
        return self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{sw}{extra}/>')

    def line(self, d: str, color=INK, w=2.5, opacity=None):
        op = f' opacity="{opacity}"' if opacity is not None else ""
        return self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{op}/>')

    # ---- shared character pieces -----------------------------------------
    def ground(self, cx=100, cy=184, rx=54):
        return self.ell(cx, cy, rx, 6.5, INK, extra=' opacity=".13"')

    def gloss(self, cx, cy, rx=12, ry=6, rot=-35, op=0.55):
        return self.ell(cx, cy, rx, ry, "#FFFFFF", rot=rot, extra=f' opacity="{op}"')

    def glow(self, cx, cy, r, color, alpha=0.6):
        return self.circ(cx, cy, r, self.fade(color, alpha), extra=' class="fx"')

    def sparkle(self, x, y, r=6, color="#FFE14D"):
        return self.add(
            f'<path class="fx" d="M{x} {y - r} Q{x} {y} {x + r} {y} Q{x} {y} {x} {y + r} '
            f'Q{x} {y} {x - r} {y} Q{x} {y} {x} {y - r} Z" fill="{color}"/>')

    def cheeks(self, pts, color="#FF7F9B", rx=12, ry=8, dots=True):
        f = self.fade(color, 0.7)
        for (x, y) in pts:
            self.ell(x, y, rx, ry, f)
            if dots:
                self.circ(x - rx * 0.35, y - ry * 0.6, 1.5, "#FFFFFF", extra=' opacity=".9"')
        return self

    def eye(self, cx, cy, rx=11, ry=13, iris="#8A6BCB", pupil=("#4A3466", "#1A1226"),
            kind="glossy", look=(0, 0), lashes=0, side=1):
        """kind: glossy | star | sleepy | happy | dot | angry | wink | white | glow"""
        if kind == "sleepy":
            return self.line(f"M{cx - rx} {cy} Q{cx} {cy + ry * 0.6} {cx + rx} {cy}", INK, 3)
        if kind in ("happy", "wink"):
            return self.line(f"M{cx - rx} {cy + 3} Q{cx} {cy - ry * 0.7} {cx + rx} {cy + 3}", INK, 3)
        if kind == "dot":
            self.ell(cx, cy, rx * 0.5, ry * 0.55, pupil[1])
            return self.circ(cx + rx * 0.18, cy - ry * 0.22, rx * 0.17, "#FFFFFF")
        lx, ly = look
        if kind in ("white", "glow"):
            ring = "#FFFFFF" if kind == "white" else self.fade(iris, 0.95)
            self.ell(cx, cy, rx, ry, ring, INK if kind == "white" else None, 2.5)
            self.ell(cx + lx, cy + ly + 1, rx * 0.55, ry * 0.55, self._eyegrad(pupil))
            self.circ(cx + lx + rx * 0.25, cy + ly - ry * 0.2, rx * 0.22, "#FFFFFF")
        else:
            self.ell(cx, cy, rx, ry, self._eyegrad(pupil))
            self.path(f"M{cx - rx * 0.9} {cy + ry * 0.4} Q{cx} {cy + ry * 1.15} {cx + rx * 0.9} {cy + ry * 0.4} "
                      f"Q{cx + rx * 0.6} {cy + ry * 0.85} {cx} {cy + ry * 0.85} Q{cx - rx * 0.6} {cy + ry * 0.85} "
                      f"{cx - rx * 0.9} {cy + ry * 0.4} Z", iris, None, extra=' opacity=".85"')
            if kind == "star":
                hx, hy, s = cx + rx * 0.35 + lx, cy - ry * 0.35 + ly, rx * 0.5
                self.add(f'<path d="M{hx} {hy - s} Q{hx} {hy} {hx + s} {hy} Q{hx} {hy} {hx} {hy + s} '
                         f'Q{hx} {hy} {hx - s} {hy} Q{hx} {hy} {hx} {hy - s} Z" fill="#FFFFFF"/>')
            else:
                self.circ(cx + rx * 0.35 + lx, cy - ry * 0.4 + ly, rx * 0.4, "#FFFFFF")
            self.circ(cx - rx * 0.4 + lx, cy + ry * 0.4 + ly, rx * 0.18, "#FFFFFF")
            if kind == "angry":
                self.line(f"M{cx - rx * side} {cy - ry - 4} L{cx + rx * side} {cy - ry + 2}", INK, 3.2)
        for i in range(lashes):
            ox = cx - side * rx * 0.95
            oy = cy - ry * 0.55 + i * 6
            self.line(f"M{ox} {oy} L{ox - side * 6} {oy - 4 + i * 2}", pupil[1], 2.4)
        return self

    def _eyegrad(self, pupil):
        gid = self._id("e")
        self.defs.append(
            f'<radialGradient id="{gid}" cx="0.5" cy="0.35" r="0.75"><stop offset="0" stop-color="{pupil[0]}"/>'
            f'<stop offset="1" stop-color="{pupil[1]}"/></radialGradient>')
        return f"url(#{gid})"

    def eyes(self, y, xs=(78, 122), **kw):
        for i, x in enumerate(xs):
            self.eye(x, y, side=1 if i == 0 else -1, **kw)
        return self

    def mouth(self, x, y, kind="smile", w=8, color="#7A3E4E", tongue="#FF7F9B"):
        if kind == "smile":
            return self.line(f"M{x - w} {y} Q{x} {y + w * 0.8} {x + w} {y}", color, 2.8)
        if kind == "cat":
            return self.line(f"M{x - w} {y} Q{x - w / 2} {y + w * 0.6} {x} {y} Q{x + w / 2} {y + w * 0.6} {x + w} {y}", color, 2.6)
        if kind == "open":
            self.path(f"M{x - w} {y} Q{x} {y + w * 1.5} {x + w} {y} Z", color, color, 2.4)
            return self.path(f"M{x - w * 0.5} {y + w * 0.62} Q{x} {y + w * 0.3} {x + w * 0.5} {y + w * 0.62} "
                             f"Q{x} {y + w * 1.05} {x - w * 0.5} {y + w * 0.62} Z", tongue, None)
        if kind == "grin":
            return self.path(f"M{x - w * 1.3} {y} Q{x} {y + w * 1.5} {x + w * 1.3} {y} Z", "#FFFFFF", color, 2.6)
        if kind == "fang":
            self.line(f"M{x - w} {y} Q{x} {y + w * 0.8} {x + w} {y}", color, 2.8)
            return self.path(f"M{x - w * 0.55} {y + w * 0.3} L{x - w * 0.3} {y + w * 0.95} L{x - w * 0.05} {y + w * 0.5} Z", "#FFFFFF", color, 1.6)
        if kind == "o":
            return self.ell(x, y + 2, w * 0.45, w * 0.55, color)
        if kind == "smirk":
            return self.line(f"M{x - w} {y + 2} Q{x + w * 0.2} {y + w * 0.6} {x + w} {y - w * 0.4}", color, 2.8)
        if kind == "beak":
            self.path(f"M{x - w} {y} Q{x} {y - w * 0.5} {x + w} {y} L{x} {y + w * 1.3} Z", "#FFC83D", "#B8650F", 2.4)
            return self.line(f"M{x - w * 0.7} {y + w * 0.35} Q{x} {y + w * 0.65} {x + w * 0.7} {y + w * 0.35}", "#B8650F", 1.8)
        raise ValueError(kind)

    def render(self) -> str:
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
                f'<defs>{"".join(self.defs)}</defs>' + "\n".join(self.parts) + "</svg>\n")

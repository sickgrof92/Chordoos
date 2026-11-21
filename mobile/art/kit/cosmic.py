import math
from artkit import chordoo, INK
from shapes import limb, star

SP_O = "#241A50"


def planet(a, x, y, r, light, mid, dark, o=SP_O, w=3):
    a.circ(x, y, r, a.shade(light, mid, dark), o, w)


@chordoo("nova")
def nova(a):
    o = "#3A1A6A"
    a.glow(100, 110, 80, "#D8B8FF", 0.6)
    a.ground(rx=46)
    # puffy cloud-star body
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = 66 if i % 2 == 0 else 46
        pts.append((100 + r * math.cos(ang), 114 + r * math.sin(ang)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, 11):
        p = pts[i % 10]
        q = pts[i - 1]
        cx, cy = (p[0] + q[0]) / 2 + (p[0] + q[0] - 200) * 0.06, (p[1] + q[1]) / 2 + (p[1] + q[1] - 228) * 0.06
        d += f" Q{cx:.1f} {cy:.1f} {p[0]:.1f} {p[1]:.1f}"
    a.path(d + " Z", a.shade("#F4E8FF", "#B88AF0", "#6A3AB8"), o, 3.5)
    a.eyes(114, xs=(84, 116), rx=11, ry=13, kind="star", iris="#FFD84D", pupil=("#3A1A6A", "#12062A"))
    a.mouth(100, 136, "cat", w=7, color=o)
    a.cheeks([(70, 132), (130, 132)], "#FF9AD0", rx=8, ry=5)
    a.gloss(80, 84, 10, 5)
    # shooting star it came from
    a.line("M150 40 L184 20", "#FFE88A", 3, 0.7)
    star(a, 148, 42, 8, "#FFE88A", "#8A6A00", 1.5, cls="fx")
    for x, y in ((24, 60), (176, 150), (30, 160)):
        a.sparkle(x, y, 5)


@chordoo("moonbeam")
def moonbeam(a):
    o = "#5A4A1A"
    a.glow(100, 96, 80, "#FFF6C8", 0.55)
    a.ground(rx=40)
    moon = a.shade("#FFFFF0", "#FFE88A", "#D8B040")
    a.path("M120 24 C70 24 40 64 44 108 C48 150 84 178 126 172 C96 160 76 132 78 100 C80 64 100 36 120 24 Z", moon, o)
    for x, y, r in ((62, 80, 6), (70, 130, 5), (88, 156, 4)):
        a.circ(x, y, r, "#E8C860", extra=' opacity=".6"')
    a.eye(70, 104, kind="sleepy", rx=8)
    a.mouth(66, 124, "smile", w=6, color=o)
    a.cheeks([(56, 118)], "#FFA8A8", rx=6, ry=4)
    # nightcap with pompom
    a.path("M112 30 C120 18 138 20 150 34 C160 46 162 62 168 72 C154 64 142 50 132 44 Z", a.lin("#8AB8FF", "#3A6AD0"), "#1E3A7A", 2.5)
    a.circ(168, 74, 6, "#FFFFFF", "#1E3A7A", 2)
    a.add('<text class="fx" x="138" y="120" font-size="20" font-weight="bold" font-family="sans-serif" fill="#C8B060">z</text>')
    a.add('<text class="fx" x="154" y="104" font-size="14" font-weight="bold" font-family="sans-serif" fill="#C8B060">z</text>')
    for x, y in ((160, 160), (30, 40), (150, 140)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")


@chordoo("astro")
def astro(a):
    o = "#2A3456"
    a.ground(rx=40)
    suit = a.shade("#FFFFFF", "#EEF0F8", "#B0B8D0")
    # backpack
    a.path("M60 104 H140 V156 H60 Z", "#C8CCD8", o, 3)
    # legs and boots
    for x in (86, 114):
        a.path(f"M{x - 11} 150 V174 H{x + 11} V150", suit, o, 3)
        a.path(f"M{x - 13} 172 H{x + 13} V182 H{x - 13} Z", "#FF8A3A", "#7A3A0A", 2.5)
    # body
    a.path("M68 110 C68 98 132 98 132 110 V156 H68 Z", suit, o, 3.5)
    a.path("M86 118 H114 V138 H86 Z", "#3A4A6A", o, 2)
    for x, c in ((92, "#FF5A6A"), (100, "#FFD84D"), (108, "#5AE08A")):
        a.circ(x, 128, 2.5, c)
    # arm waving + arm with flag
    limb(a, "M70 116 C56 108 50 92 52 80", "#EEF0F8", o, 12)
    a.circ(52, 76, 7, "#FF8A3A", "#7A3A0A", 2)
    limb(a, "M130 118 C142 124 148 132 150 140", "#EEF0F8", o, 12)
    a.line("M152 150 V96", "#8A8AA8", 3)
    a.path("M152 96 H178 L172 104 L178 112 H152 Z", "#FF5A6A", "#7A1A1A", 2)
    star(a, 162, 104, 4, "#FFFFFF", None)
    # fishbowl helmet
    a.circ(100, 70, 40, a.fade("#BFE8FF", 0.35), o, 3)
    # head inside
    a.circ(100, 74, 26, a.shade("#FFE8D8", "#F0C8A8", "#C8987A"), "#6A4A30", 2.5)
    a.path("M76 66 C78 44 122 44 124 66 C116 58 104 56 96 60 C88 56 80 60 76 66 Z", "#6A3A1E", "#3A1E0A", 2)
    a.eyes(76, xs=(90, 110), rx=7, ry=9, iris="#6AA8FF", pupil=("#2A1A0A", "#0A0602"), kind="star")
    a.mouth(100, 88, "open", w=5, color="#7A3E2E")
    a.cheeks([(82, 86), (118, 86)], rx=5, ry=3, dots=False)
    a.path("M72 50 C80 38 92 34 104 34", "none", "#FFFFFF", 4, ' opacity=".8"')
    a.circ(100, 110, 6, "#C8CCD8", o, 2)
    for x, y in ((24, 30), (180, 40), (24, 150)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")
    planet(a, 176, 168, 10, "#FFD8F0", "#FF8AC0", "#C04A88", "#6A1A4A", 2)


@chordoo("starfry")
def starfry(a):
    o = "#6A3A0A"
    a.glow(100, 100, 80, "#FFE8A8", 0.5)
    a.ground(rx=40)
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = 74 if i % 2 == 0 else 34
        pts.append((100 + r * math.cos(ang), 104 + r * math.sin(ang)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, 11):
        p, q = pts[i % 10], pts[i - 1]
        d += f" Q{(p[0] + q[0]) / 2 + (100 - (p[0] + q[0]) / 2) * -0.12:.1f} {(p[1] + q[1]) / 2 + (104 - (p[1] + q[1]) / 2) * -0.12:.1f} {p[0]:.1f} {p[1]:.1f}"
    a.path(d + " Z", a.shade("#FFF6D0", "#FFB04A", "#E06A1A"), o, 3.5)
    # texture dots along arms
    for i in range(0, 10, 2):
        ang = math.radians(-90 + i * 36)
        for k in (40, 54):
            a.circ(round(100 + k * math.cos(ang), 1), round(104 + k * math.sin(ang), 1), 2.6, "#FFF6D0")
    a.eyes(102, xs=(88, 112), rx=8, ry=10, iris="#FFB04A", pupil=("#3A1A0A", "#120602"))
    a.mouth(100, 120, "smile", w=6, color=o)
    a.cheeks([(78, 116), (122, 116)], "#FF8AA8", rx=6, ry=4)
    # space bubbles / twinkles
    for x, y in ((30, 160), (172, 168), (176, 30), (24, 40)):
        a.sparkle(x, y, 6, "#FFFFFF")


@chordoo("cometail")
def cometail(a):
    fur = a.shade("#F4F0FF", "#C8C0F0", "#7A70B8")
    o = "#241A50"
    a.ground(rx=56)
    # comet tail streaming behind
    a.path("M140 122 C170 100 190 104 200 90 V140 C186 132 170 138 150 140 Z", a.lin("#FFF6A8", "#FF9A5A", "#FF5AA8", x2=1, y2=0), None, extra=' opacity=".9"')
    a.path("M146 126 C170 112 186 116 200 108", "none", "#FFFFFF", 3, ' opacity=".8"')
    star(a, 146, 128, 14, "#FFE88A", "#8A6A00", 2)
    # running legs
    for x, ang in ((54, -30), (76, 20), (116, -20), (136, 30)):
        a.add(f'<g transform="rotate({ang} {x} 140)">')
        limb(a, f"M{x} 140 L{x} 168", "#C8C0F0", o, 12)
        a.add('</g>')
    # body
    a.ell(96, 132, 46, 26, fur, o)
    a.ell(90, 140, 26, 12, "#FFFFFF", None, extra=' opacity=".6"')
    # head
    a.circ(60, 92, 32, fur, o)
    a.path("M34 76 C18 66 12 84 24 104 C30 96 34 88 40 84 Z", "#7A70B8", o, 3)
    a.path("M80 66 C92 50 108 58 102 80 C96 76 90 72 84 74 Z", "#7A70B8", o, 3)
    a.ell(46, 108, 14, 10, "#FFFFFF", o, 2)
    a.circ(38, 104, 4, o)
    a.mouth(48, 114, "open", w=5, color="#7A3E4E")
    a.eyes(90, xs=(54, 78), rx=8, ry=10, iris="#FFB04A", pupil=("#241A50", "#0A061A"), kind="star")
    a.cheeks([(64, 106)], rx=6, ry=4, dots=False)
    # space helmet bubble
    a.circ(62, 92, 42, a.fade("#BFE8FF", 0.25), "#8AB8E8", 2)
    a.path("M30 70 C40 56 54 52 66 52", "none", "#FFFFFF", 3, ' opacity=".8"')
    planet(a, 170, 40, 14, "#C8F0FF", "#5AB8F0", "#2A6AB8", "#1E3A7A", 2)


@chordoo("orbit")
def orbit(a):
    o = "#1E3A5A"
    a.ground(rx=36)
    # ring back half
    a.add(f'<path d="M24 104 A76 22 0 0 1 176 104" fill="none" stroke="{o}" stroke-width="14" transform="rotate(-14 100 104)"/>')
    a.add(f'<path d="M24 104 A76 22 0 0 1 176 104" fill="none" stroke="#FFC86A" stroke-width="9" transform="rotate(-14 100 104)"/>')
    planet(a, 100, 104, 50, "#E8FFF4", "#5AE0B0", "#1E8A7A", o, 3.5)
    # continents
    a.path("M70 80 C80 70 96 76 92 88 C88 98 72 96 70 80 Z", "#3AB87A", None, extra=' opacity=".8"')
    a.path("M118 126 C130 118 144 126 138 138 C130 146 116 140 118 126 Z", "#3AB87A", None, extra=' opacity=".8"')
    # ring front half
    a.add(f'<path d="M24 104 A76 22 0 0 0 176 104" fill="none" stroke="{o}" stroke-width="14" transform="rotate(-14 100 104)"/>')
    a.add(f'<path d="M24 104 A76 22 0 0 0 176 104" fill="none" stroke="#FFC86A" stroke-width="9" transform="rotate(-14 100 104)"/>')
    a.eyes(96, xs=(84, 116), kind="happy", rx=9)
    a.mouth(100, 106, "open", w=7, color="#5A1E3A")
    a.cheeks([(70, 104), (130, 104)], "#FF9AC0", rx=7, ry=4)
    a.gloss(78, 74, 12, 6)
    # dizzy swirl
    a.add('<path class="fx" d="M150 40 c6 -6 14 0 8 6 c-4 4 -10 -2 -6 -4" stroke="#8AB8E8" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    for x, y in ((40, 40), (170, 160), (26, 150)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")


@chordoo("ufolo")
def ufolo(a):
    o = "#24304A"
    # tractor beam
    a.path("M76 120 L50 190 H150 L124 120 Z", a.lin("#E8FFB0", "#E8FFB0"), None, extra=' class="fx" opacity=".45"')
    # beamed teddy
    a.circ(100, 170, 10, a.shade("#F0D0B0", "#C89870", "#8A5A3A"), "#4A2A10", 2)
    a.circ(93, 162, 4, "#C89870", "#4A2A10", 1.5)
    a.circ(107, 162, 4, "#C89870", "#4A2A10", 1.5)
    # dome with alien pilot
    a.path("M64 92 C64 50 136 50 136 92 Z", a.fade("#BFE8FF", 0.4), o, 3)
    alien = a.shade("#D8FFC8", "#8AE06A", "#3A9A3A")
    a.path("M78 92 C76 66 124 66 122 92 Z", alien, "#1E4A1E", 2.5)
    a.line("M90 70 L84 56 M110 70 L116 56", "#1E4A1E", 2.5)
    a.circ(84, 54, 4, "#FF8AC0", "#1E4A1E", 1.5)
    a.circ(116, 54, 4, "#FF8AC0", "#1E4A1E", 1.5)
    a.eye(100, 80, rx=10, ry=8, iris="#8AE06A", pupil=("#1E1E3A", "#06060E"))
    a.mouth(100, 89, "smile", w=5, color="#1E4A1E")
    a.path("M70 64 C76 56 86 52 94 52", "none", "#FFFFFF", 3, ' opacity=".8"')
    # saucer
    a.ell(100, 104, 76, 22, a.lin("#F0F4FF", "#A8B4D0", "#6A7898"), o, 3.5)
    a.ell(100, 98, 56, 10, "#C8D4F0", None)
    for i, x in enumerate((44, 72, 100, 128, 156)):
        a.circ(x, 110 if x in (72, 128) else (106 if x == 100 else 104), 5, ["#FF6A9A", "#FFD84D", "#6AE8D8", "#FFD84D", "#FF6A9A"][i], o, 1.5)
    a.ell(100, 120, 24, 6, "#8A98B8", o, 2.5)
    a.ground(rx=40, cy=190)
    for x, y in ((24, 30), (176, 40), (180, 150)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")


@chordoo("nebulynx")
def nebulynx(a):
    o = "#2A1450"
    a.glow(100, 100, 90, "#E0A8FF", 0.45)
    a.ground(rx=56)
    neb = a.lin("#FF8AD8", "#9A6AF0", "#4A6AE8", x1=0, y1=0, x2=1, y2=1)
    # tail swirling
    a.path("M146 140 C176 136 186 104 170 84 C160 72 146 78 152 90 C162 96 160 116 140 124 Z", neb, o, 3)
    # body sitting
    a.path("M56 150 C52 118 74 100 100 100 C128 100 150 118 146 150 C144 172 124 180 100 180 C76 180 58 172 56 150 Z", neb, o)
    for x in (80, 120):
        a.ell(x, 178, 14, 7, "#C8A8FF", o, 3)
    # cloudy swirl highlights
    a.path("M70 130 C80 120 96 124 98 136 C100 146 88 150 84 142", "none", "#FFFFFF", 3, ' opacity=".5"')
    a.path("M112 150 C120 140 134 144 132 156", "none", "#FFFFFF", 3, ' opacity=".5"')
    # head
    a.circ(100, 78, 36, neb, o)
    a.path("M70 58 L64 22 L92 46 Z", neb, o, 3)
    a.path("M130 58 L136 22 L108 46 Z", neb, o, 3)
    a.line("M64 22 L62 12 M136 22 L138 12", o, 3)
    a.eyes(78, xs=(86, 114), rx=10, ry=12, iris="#FFE88A", pupil=("#2A1450", "#0A061A"), kind="star")
    a.path("M96 92 L104 92 L100 96 Z", "#FFB0E0")
    a.mouth(100, 98, "cat", w=6, color=o)
    a.cheeks([(72, 94), (128, 94)], "#FFB0E0", rx=7, ry=4)
    # stars inside the fur
    for x, y in ((80, 60), (118, 58), (74, 140), (128, 132), (100, 160), (160, 100)):
        star(a, x, y, 3, "#FFFFFF", None)
    for x, y in ((30, 40), (176, 40), (24, 150)):
        a.sparkle(x, y, 6, "#FFFFFF")


@chordoo("saturnine")
def saturnine(a):
    o = "#3A2A1A"
    a.ground(rx=40)
    ring = a.lin("#FFE8C8", "#E8A86A")
    a.add(f'<path d="M14 110 A86 26 0 0 1 186 110" fill="none" stroke="{o}" stroke-width="20" transform="rotate(10 100 110)"/>')
    a.add(f'<path d="M14 110 A86 26 0 0 1 186 110" fill="none" stroke="{ring}" stroke-width="14" transform="rotate(10 100 110)"/>')
    planet(a, 100, 104, 52, "#FFF0D8", "#F0B870", "#B0703A", o, 3.5)
    for y, c in ((82, "#E09A5A"), (126, "#D08A4A")):
        a.path(f"M54 {y} Q100 {y + 10} 146 {y}", "none", c, 6, ' opacity=".7"')
    a.add(f'<path d="M14 110 A86 26 0 0 0 186 110" fill="none" stroke="{o}" stroke-width="20" transform="rotate(10 100 110)"/>')
    a.add(f'<path d="M14 110 A86 26 0 0 0 186 110" fill="none" stroke="{ring}" stroke-width="14" transform="rotate(10 100 110)"/>')
    a.eyes(98, xs=(84, 116), rx=9, ry=11, iris="#F0B870", pupil=("#3A2A1A", "#120A06"))
    a.mouth(100, 116, "grin", w=7, color=o)
    a.cheeks([(70, 112), (130, 112)], rx=7, ry=4)
    a.gloss(76, 74, 12, 6)
    # moon friends with faces
    for x, y, r, c in ((30, 40, 13, ("#F0F0FF", "#C8C8E0", "#8A8AA8")), (170, 34, 11, ("#FFE8F0", "#FFB0C8", "#C8708A")), (170, 168, 10, ("#E8FFF0", "#A8E8C8", "#5AA888"))):
        planet(a, x, y, r, *c, "#3A3A5A", 2)
        a.circ(x - 3, y - 1, 1.6, INK)
        a.circ(x + 3, y - 1, 1.6, INK)
        a.line(f"M{x - 3} {y + 3} Q{x} {y + 6} {x + 3} {y + 3}", INK, 1.4)


@chordoo("galactopus")
def galactopus(a):
    o = "#1A1450"
    a.ground(rx=60)
    sk = a.shade("#B8C8FF", "#5A6AE8", "#2A2A98")
    # tentacles
    for i in range(8):
        x0 = 56 + i * 12.5
        sx = -1 if i < 4 else 1
        d = f"M{x0:.1f} 126 C{x0 + sx * 6:.1f} 150 {x0 + sx * (14 + (i % 4) * 6):.1f} 160 {x0 + sx * (24 + (i % 4) * 10):.1f} {168 - (i % 2) * 20}"
        a.line(d, o, 13)
        a.line(d, "#5A6AE8", 9)
    # star suckers
    for x, y in ((40, 160), (60, 150), (140, 150), (162, 160), (30, 146), (172, 144)):
        star(a, x, y, 3.5, "#FFE88A", None)
    # juggled planets
    planet(a, 24, 80, 12, "#FFE0E8", "#FF8AA8", "#C84A6A", "#6A1A2A", 2)
    planet(a, 100, 16, 11, "#E8FFF0", "#8AE0B0", "#3A9A6A", "#1A4A2A", 2)
    planet(a, 176, 76, 13, "#FFF6D0", "#FFC86A", "#C8862A", "#6A4A0A", 2)
    a.add('<path class="fx" d="M30 66 C40 30 70 16 88 16 M112 16 C140 18 166 40 172 62" stroke="#A8B8F0" stroke-width="2" stroke-dasharray="4 6" fill="none"/>')
    # two arms reaching up
    limb(a, "M64 112 C50 102 36 94 30 90", "#5A6AE8", o, 12)
    limb(a, "M136 112 C152 102 164 92 168 86", "#5A6AE8", o, 12)
    # head
    a.path("M54 100 C50 56 76 36 100 36 C124 36 150 56 146 100 C144 122 126 132 100 132 C74 132 56 122 54 100 Z", sk, o)
    for x, y in ((76, 60), (120, 56), (132, 82), (66, 88)):
        star(a, x, y, 3, "#FFFFFF", None)
    a.eyes(94, xs=(84, 116), rx=10, ry=12, iris="#8AE0FF", pupil=("#1A1450", "#06041A"))
    a.mouth(100, 114, "open", w=7, color="#5A1A3A")
    a.cheeks([(70, 110), (130, 110)], "#FF9AD0", rx=7, ry=4)
    a.gloss(80, 54, 12, 6)


@chordoo("supernova")
def supernova(a):
    o = "#6A1A0A"
    a.glow(100, 100, 100, "#FFD08A", 0.7)
    # burst rays
    for i in range(12):
        ang = i * 30
        col = ["#FF5A6A", "#FFB03A", "#FFE84D", "#FF8AD8"][i % 4]
        a.add(f'<path class="fx" d="M100 100 L94 30 L100 8 L106 30 Z" fill="{col}" transform="rotate({ang} 100 100)" opacity=".85"/>')
    a.ground(rx=36)
    # star sprite body
    pts = []
    for i in range(16):
        ang = math.radians(-90 + i * 22.5)
        r = 58 if i % 2 == 0 else 42
        pts.append(f"{100 + r * math.cos(ang):.1f} {100 + r * math.sin(ang):.1f}")
    a.path("M" + " L".join(pts) + " Z", a.shade("#FFFFF0", "#FFD84D", "#FF7A2A"), o, 3.5)
    a.circ(100, 100, 38, a.shade("#FFFFFF", "#FFF6C8", "#FFD84D"))
    a.eyes(96, xs=(86, 114), rx=9, ry=11, kind="star", iris="#FF7A2A", pupil=("#6A1A0A", "#2A0602"))
    a.mouth(100, 116, "open", w=8, color="#8A2A1A")
    a.cheeks([(72, 112), (128, 112)], "#FF6A6A", rx=7, ry=4)
    # little fists up
    a.circ(48, 60, 9, a.shade("#FFFFF0", "#FFD84D", "#FF7A2A"), o, 2.5)
    a.circ(152, 60, 9, a.shade("#FFFFF0", "#FFD84D", "#FF7A2A"), o, 2.5)
    for x, y in ((24, 160), (176, 160), (20, 30), (180, 30)):
        a.sparkle(x, y, 7, "#FFFFFF")


@chordoo("cosmodrake")
def cosmodrake(a):
    o = "#0A0E30"
    sk = a.shade("#5A6AD8", "#262E8A", "#0E1240")
    a.glow(100, 100, 92, "#8A9AFF", 0.35)
    a.ground(rx=64)
    # wings: night-sky membranes
    for sx in (1, -1):
        a.path(f"M{100 + sx * 20} 98 C{100 + sx * 40} 50 {100 + sx * 70} 30 {100 + sx * 92} 36 C{100 + sx * 82} 50 {100 + sx * 86} 60 {100 + sx * 92} 70 "
               f"C{100 + sx * 78} 74 {100 + sx * 80} 86 {100 + sx * 86} 96 C{100 + sx * 66} 96 {100 + sx * 50} 104 {100 + sx * 36} 116 Z", a.lin("#3A4AB8", "#141A5A"), o, 3)
    # tail curling
    a.path("M130 164 C164 172 186 156 184 132 C182 116 166 112 162 124", "none", o, 16)
    a.path("M130 164 C164 172 186 156 184 132 C182 116 166 112 162 124", "none", "#262E8A", 11)
    # body
    a.path("M64 178 C54 146 64 108 100 106 C136 108 146 146 136 178 Z", sk, o)
    a.path("M84 178 C82 150 90 128 100 126 C110 128 118 150 116 178 Z", "#3A4AB8", None, extra=' opacity=".7"')
    for x in (78, 122):
        a.ell(x, 180, 14, 6, "#262E8A", o, 3)
    # head
    a.path("M60 72 C58 42 80 30 100 30 C120 30 142 42 140 72 C138 96 122 106 100 106 C78 106 62 96 60 72 Z", sk, o)
    a.path("M70 38 L62 12 L84 32 Z M130 38 L138 12 L116 32 Z", a.lin("#FFF6C8", "#C8B8FF"), "#3A2A8A", 2.5)
    a.ell(100, 92, 22, 11, "#3A4AB8", o, 2.5)
    a.circ(92, 90, 2, "#B8C8FF")
    a.circ(108, 90, 2, "#B8C8FF")
    a.eyes(68, xs=(84, 116), rx=10, ry=12, kind="star", iris="#8AB8FF", pupil=("#2A2A6A", "#06061A"))
    a.mouth(100, 100, "smile", w=6, color="#B8C8FF")
    a.cheeks([(70, 86), (130, 86)], "#FF9AD0", rx=6, ry=4, dots=False)
    # constellation drawn across its body and wings
    pts = [(-86, 48), (-74, 64), (-58, 58), (-50, 86)]
    for sx in (1, -1):
        p = [(100 + sx * dx, dy) for dx, dy in pts]
        a.line("M" + " L".join(f"{x} {y}" for x, y in p), "#C8D4FF", 1.8, 0.9)
        for x, y in p:
            star(a, x, y, 3.5, "#FFF6C8", None)
    body = [(88, 136), (100, 124), (114, 140), (104, 160), (92, 152)]
    a.line("M" + " L".join(f"{x} {y}" for x, y in body) + " Z", "#C8D4FF", 1.8, 0.9)
    for x, y in body + [(176, 140), (168, 158), (150, 166)]:
        star(a, x, y, 3.5, "#FFF6C8", None)
    for x, y in ((20, 150), (24, 110), (180, 20)):
        a.sparkle(x, y, 6, "#FFFFFF")


@chordoo("aurora")
def aurora(a):
    o = "#2A1A5A"
    # aurora ribbons
    for i, (c1, c2, y) in enumerate((("#6AFFC8", "#5AC8FF", 30), ("#B87AFF", "#FF8AD8", 56), ("#5AC8FF", "#6AFFC8", 82))):
        g = a.lin(c1, c2, x2=1, y2=0)
        a.add(f'<path class="fx" d="M0 {y + 20} C40 {y - 10} 70 {y + 30} 100 {y} C130 {y - 30} 160 {y + 20} 200 {y - 6} V{y + 10} C160 {y + 36} 130 {y - 14} 100 {y + 16} C70 {y + 46} 40 {y + 6} 0 {y + 36} Z" fill="{g}" opacity=".6"/>')
    a.ground(rx=40)
    # dress made of light
    dress = a.lin("#E8FFF6", "#8AF0D0", "#8AB8FF", "#C89AFF")
    a.path("M86 108 C72 140 56 170 44 184 C70 176 84 182 100 176 C116 182 130 176 156 184 C144 170 128 140 114 108 Z", dress, o, 3)
    # wings
    w = a.lin("#FFFFFF", "#C8F0FF", "#C8A8FF")
    a.path("M92 106 C70 80 30 76 22 100 C30 118 64 122 90 114 Z", w, o, 2.5, ' opacity=".95"')
    a.path("M108 106 C130 80 170 76 178 100 C170 118 136 122 110 114 Z", w, o, 2.5, ' opacity=".95"')
    a.path("M92 116 C76 130 54 144 52 158 C70 158 86 140 94 122 Z", w, o, 2.5)
    a.path("M108 116 C124 130 146 144 148 158 C130 158 114 140 106 122 Z", w, o, 2.5)
    # torso + head
    a.path("M88 96 H112 L114 112 H86 Z", "#F0FFF8", o, 2.5)
    skin = a.shade("#FFF4EC", "#F8D8C8", "#D8A898")
    a.circ(100, 72, 22, skin, "#6A3A3A", 2.5)
    # flowing hair in aurora colors
    a.path("M76 72 C70 40 130 40 124 72 C126 90 134 100 140 104 C124 106 120 92 118 80 C110 64 90 64 82 80 C80 92 76 106 60 104 C66 98 74 90 76 72 Z",
           a.lin("#6AFFC8", "#5AC8FF", "#B87AFF"), o, 2.5)
    a.eyes(74, xs=(92, 108), rx=6, ry=8, iris="#6AFFC8", pupil=("#2A1A5A", "#0A061A"), lashes=2)
    a.mouth(100, 86, "smile", w=5, color="#A04A5A")
    a.cheeks([(86, 84), (114, 84)], rx=5, ry=3, dots=False)
    # star tiara + wand
    star(a, 100, 48, 7, "#FFF6A8", "#8A6A00", 1.5)
    a.line("M126 112 L150 70", "#E8D8FF", 3)
    star(a, 152, 66, 9, "#FFFFFF", "#8A7AE8", 2)
    for x, y in ((30, 150), (172, 150), (20, 30), (182, 24)):
        a.sparkle(x, y, 6, "#FFFFFF")

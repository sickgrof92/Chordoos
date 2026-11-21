from artkit import chordoo, INK
from shapes import bolt, limb, star

YEL = ("#FFFBD0", "#FFE14D", "#E0A800")
EL_O = "#6A4A00"


@chordoo("zappy")
def zappy(a):
    a.ground(rx=44)
    fluff = a.shade(*YEL)
    # spiky static fluff: many little tufts around a circle
    import math
    pts = []
    for i in range(28):
        ang = math.radians(i * 360 / 28)
        r = 62 if i % 2 == 0 else 48
        pts.append(f"{100 + r * math.cos(ang):.1f} {112 + r * 0.92 * math.sin(ang):.1f}")
    a.path("M" + " L".join(pts) + " Z", fluff, EL_O, 3)
    a.circ(100, 112, 42, a.shade("#FFFFF0", "#FFF29A", "#F5CC2A"))
    a.eyes(106, xs=(84, 116), rx=10, ry=13, iris="#FFB020", pupil=("#3A2A00", "#140E00"))
    a.mouth(100, 128, "open", w=7, color="#7A3E1E")
    a.cheeks([(70, 124), (130, 124)], "#FF8A6A", rx=8, ry=5)
    # sock stuck on it
    a.path("M146 132 L170 140 C178 144 178 156 168 158 L148 152 Z", "#7AC8FF", "#1E5A8A", 2.5)
    a.path("M146 132 L152 134 L148 152 L142 150 Z", "#FFFFFF", "#1E5A8A", 2)
    for x, y, r in ((36, 50, -20), (166, 54, 30), (30, 150, 10)):
        bolt(a, x, y, 0.55, r, cls="fx")


@chordoo("glowbug")
def glowbug(a):
    o = "#2A3A1A"
    a.glow(100, 140, 60, "#E8FF6A", 0.7)
    a.ground(rx=36)
    # wings
    w = a.fade("#FFFFFF", 0.0)
    for sx in (1, -1):
        a.ell(100 + sx * 34, 76, 26, 14, "#E8F6FF", "#6A8AA8", 2.5, rot=sx * -30, extra=' opacity=".85"')
    # battery belly
    a.path("M74 106 H126 V168 C126 176 120 180 112 180 H88 C80 180 74 176 74 168 Z", a.lin("#F8FFB0", "#C8F040", "#8ACC20"), o, 3)
    a.path("M74 106 H126 V122 H74 Z", "#3A3A4A", o, 3)
    a.ell(100, 182, 8, 3, "#C8CCD8", o, 2)
    for y in (138, 152, 166):
        a.line(f"M82 {y} H118", "#FFFFFF", 4, 0.6)
    a.add('<text x="94" y="117" font-size="12" font-weight="bold" font-family="sans-serif" fill="#E8FF6A">+</text>')
    # head
    a.circ(100, 78, 30, a.shade("#8A9ACC", "#4A5A98", "#22285A"), "#141838", 3)
    a.line("M88 52 C82 36 76 30 70 30", "#141838", 2.5)
    a.line("M112 52 C118 36 124 30 130 30", "#141838", 2.5)
    a.circ(70, 30, 5, "#E8FF6A", "#141838", 2)
    a.circ(130, 30, 5, "#E8FF6A", "#141838", 2)
    a.eyes(80, xs=(88, 112), rx=9, ry=11, iris="#E8FF6A", pupil=("#2A2A1A", "#0A0A06"), kind="star")
    a.mouth(100, 96, "smile", w=6, color="#E8FF6A")
    a.cheeks([(76, 92), (124, 92)], "#FF8AC0", rx=6, ry=4, dots=False)
    for x, y in ((40, 120), (164, 110), (150, 40)):
        a.circ(x, y, 3, "#F0FF8A", extra=' class="fx"')


@chordoo("buzzby")
def buzzby(a):
    o = "#3A2A00"
    a.ground(rx=40)
    for sx in (1, -1):
        a.ell(100 + sx * 30, 70, 24, 16, "#E8F6FF", "#6A8AA8", 2.5, rot=sx * -40, extra=' opacity=".9"')
        a.line(f"M{100 + sx * 22} 76 L{100 + sx * 40} 62", "#A8C0D8", 1.6)
    body = a.shade(*YEL)
    a.ell(100, 124, 50, 46, body, o)
    # lightning stripes (zigzag bands)
    for y in (122, 146):
        a.path(f"M52 {y} L66 {y - 6} L78 {y + 4} L92 {y - 6} L106 {y + 4} L120 {y - 6} L134 {y + 4} L148 {y - 4} "
               f"L150 {y + 10} L134 {y + 16} L120 {y + 6} L106 {y + 16} L92 {y + 6} L78 {y + 16} L66 {y + 6} L54 {y + 14} Z", "#3A2A40", None)
    a.ell(100, 124, 50, 46, "none", o)
    a.path("M96 170 L100 182 L104 170 Z", "#3A2A40", o, 2)
    # face patch
    a.eyes(98, xs=(84, 116), rx=10, ry=12, iris="#FFB020", pupil=("#3A2A00", "#140E00"))
    a.mouth(100, 112, "smile", w=6, color=o)
    a.cheeks([(68, 110), (132, 110)], "#FF8A6A", rx=8, ry=5)
    a.line("M88 80 C84 62 78 56 72 56", o, 2.5)
    a.line("M112 80 C116 62 122 56 128 56", o, 2.5)
    bolt(a, 72, 52, 0.4, -10)
    bolt(a, 128, 52, 0.4, 10)
    a.gloss(70, 90, 8, 4)
    for x, y in ((30, 100), (172, 130)):
        a.line(f"M{x} {y} q6 -6 12 0 q6 6 12 0", "#C8A800", 2.4, 0.8)


@chordoo("ampere")
def ampere(a):
    o = "#0E2A4A"
    a.ground(rx=58)
    body = a.lin("#3A5AC8", "#1E2E7A")
    d = "M40 70 C40 40 80 36 92 60 C104 84 70 100 74 126 C78 150 120 160 140 140 C156 124 170 130 176 150"
    a.add(f'<path d="{d}" fill="none" stroke="{o}" stroke-width="38" stroke-linecap="round"/>')
    a.add(f'<path d="{d}" fill="none" stroke="{body}" stroke-width="32" stroke-linecap="round"/>')
    # neon stripes along the body
    a.add(f'<path d="{d}" fill="none" stroke="#5AFFE8" stroke-width="4" stroke-dasharray="10 12" stroke-linecap="round"/>')
    a.add(f'<path class="fx" d="{d}" fill="none" stroke="#5AFFE8" stroke-width="12" stroke-dasharray="10 12" opacity=".25" stroke-linecap="round"/>')
    # fin
    a.path("M170 140 L190 132 L186 160 Z", "#5AFFE8", o, 2.5)
    # head
    a.path("M26 66 C24 40 46 26 64 30 C84 34 90 56 82 74 C74 90 52 94 38 88 C30 84 26 76 26 66 Z", a.shade("#6A8AF0", "#3A5AC8", "#1E2E7A"), o)
    a.eye(50, 58, rx=8, ry=10, iris="#5AFFE8", pupil=("#0A1A3A", "#000814"))
    a.eye(72, 58, rx=8, ry=10, iris="#5AFFE8", pupil=("#0A1A3A", "#000814"))
    a.mouth(60, 76, "grin", w=7, color=o)
    a.cheeks([(38, 72), (80, 72)], "#FF8AC0", rx=5, ry=3, dots=False)
    for x, y in ((120, 50), (150, 80), (30, 140)):
        bolt(a, x, y, 0.5, 15, fill="#5AFFE8", o="#0E6A7A", cls="fx")
    for x, y in ((110, 100), (60, 170)):
        a.circ(x, y, 5, "none", "#8AD8FF", 2, extra=' class="fx"')


@chordoo("bulbo")
def bulbo(a):
    o = "#5A4A10"
    a.glow(100, 80, 70, "#FFF29A", 0.7)
    a.ground(rx=36)
    # legs
    limb(a, "M88 150 L84 178", "#9AA0B0", "#3A3A4A")
    limb(a, "M112 150 L116 178", "#9AA0B0", "#3A3A4A")
    a.ell(82, 180, 9, 5, "#FF6A5A", "#7A1A1A", 2.5)
    a.ell(118, 180, 9, 5, "#FF6A5A", "#7A1A1A", 2.5)
    # screw base
    a.path("M78 126 H122 V154 C122 160 114 162 100 162 C86 162 78 160 78 154 Z", a.lin("#E0E4EC", "#8A90A0"), "#3A3A4A", 3)
    for y in (134, 142, 150):
        a.line(f"M78 {y} Q100 {y + 4} 122 {y}", "#5A6070", 2)
    # glass bulb
    a.path("M78 128 C78 110 50 98 50 70 C50 40 74 22 100 22 C126 22 150 40 150 70 C150 98 122 110 122 128 Z",
           a.shade("#FFFFFF", "#FFF6C0", "#F5D84A"), o, 3.5)
    # filament smile
    a.line("M76 92 C84 106 116 106 124 92", "#FF9A20", 3.5)
    a.line("M88 98 L92 110 M112 98 L108 110", "#C8A060", 2)
    a.eyes(70, xs=(84, 116), rx=9, ry=11, iris="#FFC020", pupil=("#3A2A00", "#140E00"))
    a.cheeks([(68, 86), (132, 86)], "#FF8A6A", rx=7, ry=4)
    a.gloss(74, 46, 12, 6)
    # arms
    limb(a, "M78 136 C64 132 56 120 54 108", "#9AA0B0", "#3A3A4A", 7)
    limb(a, "M122 136 C138 134 148 126 152 114", "#9AA0B0", "#3A3A4A", 7)
    for x, y in ((30, 40), (170, 40), (24, 100), (176, 100)):
        a.line(f"M{x} {y} l{8 if x < 100 else -8} 4", "#FFC020", 3, 0.9)


@chordoo("joltlynx")
def joltlynx(a):
    fur = a.shade("#D8DCEC", "#8A90B8", "#4A507A")
    o = "#1E2248"
    a.ground(rx=56)
    # tail
    a.path("M146 150 C168 146 178 130 172 116 C168 108 160 110 162 118", "none", o, 12)
    a.path("M146 150 C168 146 178 130 172 116 C168 108 160 110 162 118", "none", "#8A90B8", 8)
    # body: storm cloud puffs
    for cx, cy, r in ((72, 140, 26), (100, 132, 30), (130, 140, 26), (104, 156, 26)):
        a.circ(cx, cy, r, fur, o, 3)
    for cx, cy, r in ((72, 140, 23), (100, 132, 27), (130, 140, 23), (104, 156, 23)):
        a.circ(cx, cy, r, fur)
    # paws
    for x in (70, 96, 122):
        a.ell(x, 176, 11, 8, "#E8ECF8", o, 3)
    # head
    a.path("M56 90 C52 60 76 48 100 48 C124 48 148 60 144 90 C140 116 122 124 100 124 C78 124 60 116 56 90 Z", fur, o)
    # tufted ears
    for sx in (1, -1):
        x = 100 + sx * 32
        a.path(f"M{x - sx * 12} 60 L{x + sx * 4} 26 L{x + sx * 14} 62 Z", fur, o, 3)
        a.line(f"M{x + sx * 4} 26 L{x + sx * 6} 14", o, 3)
        a.path(f"M{x - sx * 4} 58 L{x + sx * 3} 36 L{x + sx * 8} 58 Z", "#FFB0C8", None)
    # cheek ruff
    a.path("M56 96 L44 104 L58 108 L48 118 L66 116", fur, o, 2.5)
    a.path("M144 96 L156 104 L142 108 L152 118 L134 116", fur, o, 2.5)
    a.eyes(86, xs=(82, 118), rx=10, ry=12, iris="#FFE14D", pupil=("#1A1A3A", "#06060E"))
    a.path("M96 102 L104 102 L100 107 Z", "#FF8AA8", o, 1.5)
    a.mouth(100, 110, "cat", w=6, color=o)
    a.cheeks([(70, 104), (130, 104)], rx=7, ry=4, dots=False)
    # bolt markings on cloud body
    bolt(a, 100, 144, 0.55, 10)
    for x, y in ((28, 60), (176, 60)):
        bolt(a, x, y, 0.6, -15 if x < 100 else 15, cls="fx")


@chordoo("teslo")
def teslo(a):
    o = "#3A1A6A"
    a.glow(100, 96, 80, "#B89AFF", 0.55)
    a.ground(rx=30)
    # orbit rings
    a.ell(100, 96, 78, 22, "none", "#8A6AE0", 2.5, rot=-18)
    a.ell(100, 96, 78, 22, "none", "#5AC8FF", 2.5, rot=24)
    body = a.shade("#F6F0FF", "#B89AFF", "#6A4AC8")
    a.circ(100, 96, 44, body, o)
    # crackle surface lines
    a.line("M70 80 L80 88 L74 96 L84 104", "#FFFFFF", 2, 0.6)
    a.line("M128 112 L120 104 L128 98 L118 90", "#FFFFFF", 2, 0.6)
    a.eyes(92, xs=(84, 116), rx=10, ry=12, iris="#5AC8FF", pupil=("#2A1A4A", "#0A0614"))
    a.mouth(100, 114, "o", w=8, color="#5A2A6A")
    a.cheeks([(70, 108), (130, 108)], rx=7, ry=4)
    a.gloss(80, 70, 12, 6)
    # orbiting sparks
    for x, y, c in ((24, 110, "#FFE14D"), (176, 82, "#5AC8FF"), (150, 150, "#FF8AC0"), (52, 40, "#FFE14D")):
        star(a, x, y, 8, c, "#5A3A8A", 1.5)
    a.add('<text class="fx" x="142" y="40" font-size="22" fill="#8A6AE0">♪</text>')


@chordoo("neonix")
def neonix(a):
    o = "#0A3A2A"
    skin = a.shade("#C8FFE0", "#3AE8A0", "#0E8A5A")
    # upside down on ceiling: draw ceiling bar at top
    a.add('<rect x="0" y="0" width="200" height="16" fill="#3A3A5A"/>')
    a.add('<rect x="0" y="14" width="200" height="4" fill="#5A5A7A"/>')
    # tail curling down
    a.path("M120 70 C150 80 170 110 160 140 C152 160 132 158 134 144", "none", o, 14)
    a.path("M120 70 C150 80 170 110 160 140 C152 160 132 158 134 144", "none", "#3AE8A0", 9)
    # legs gripping ceiling with toe pads
    for x1, x2 in ((70, 56), (90, 98), (124, 120), (140, 156)):
        limb(a, f"M{x1} 56 L{x2} 24", "#3AE8A0", o, 10)
        for dx in (-6, 0, 6):
            a.circ(x2 + dx, 20, 4, "#C8FFE0", o, 1.8)
    # body
    a.ell(104, 62, 44, 22, skin, o)
    for x in (88, 104, 120):
        a.circ(x, 54, 4, "#FF6AD8", extra=' opacity=".9"')
    # head hanging down
    a.path("M40 80 C30 60 50 44 70 50 C92 56 94 84 84 100 C74 116 48 112 40 80 Z", skin, o)
    a.eye(54, 76, rx=10, ry=12, iris="#FF6AD8", pupil=("#1A0A2A", "#06020A"))
    a.eye(78, 80, rx=9, ry=11, iris="#FF6AD8", pupil=("#1A0A2A", "#06020A"))
    a.mouth(66, 100, "smile", w=8, color=o)
    a.cheeks([(44, 96), (88, 98)], "#FF8AC0", rx=6, ry=4, dots=False)
    a.glow(66, 80, 50, "#3AE8A0", 0.35)
    a.ground(cx=90, cy=184, rx=40)
    for x, y in ((30, 160), (176, 40), (100, 150)):
        a.sparkle(x, y, 5, "#5AFFC8")


@chordoo("thunderpaw")
def thunderpaw(a):
    fur = a.shade("#FFF6C8", "#FFC83A", "#C88A10")
    o = "#4A2E00"
    a.ground(rx=72)
    # tail with bolt tip
    a.line("M156 128 C176 120 180 96 170 82", o, 10)
    a.line("M156 128 C176 120 180 96 170 82", "#FFC83A", 6)
    bolt(a, 170, 70, 0.7, 20, fill="#3A2A60", o="#1A1030")
    # body, lunging pose
    a.path("M44 140 C40 114 70 100 108 102 C146 104 164 118 160 142 C156 164 130 168 102 168 C74 168 48 162 44 140 Z", fur, o)
    # stripes as bolts
    for x, r in ((96, 8), (122, -6), (144, 10)):
        bolt(a, x, 122, 0.75, r, fill="#3A2A60", o="#1A1030", w=1.5)
    # legs
    for x, ln in ((58, 20), (82, 18), (124, 18), (148, 20)):
        a.path(f"M{x - 10} 156 L{x - 10} {164 + ln} H{x + 10} L{x + 10} 156", fur, o, 3)
        a.ell(x, 164 + ln, 12, 6, "#FFF6E0", o, 2.5)
    # head
    a.path("M22 88 C20 58 46 44 70 46 C96 48 110 66 106 92 C102 118 80 126 60 126 C38 126 24 112 22 88 Z", fur, o)
    a.ell(36, 52, 9, 12, fur, o, 3, rot=-25)
    a.ell(90, 50, 9, 12, fur, o, 3, rot=25)
    a.ell(36, 53, 4, 6, "#FFB0A0", rot=-25)
    a.ell(90, 51, 4, 6, "#FFB0A0", rot=25)
    a.ell(60, 104, 24, 16, "#FFF6E0", None)
    a.path("M54 96 L66 96 L60 103 Z", "#FF8AA8", o, 1.6)
    a.mouth(60, 106, "fang", w=8, color=o)
    a.eyes(82, xs=(46, 76), kind="angry", rx=8, ry=10, iris="#5AC8FF", pupil=("#1A2A4A", "#06080E"))
    bolt(a, 60, 62, 0.45, 0, fill="#3A2A60", o="#1A1030", w=1.2)
    a.cheeks([(34, 104), (88, 104)], rx=6, ry=4, dots=False)
    for d in ("M180 150 l12 -2", "M176 164 l14 0", "M8 140 l10 2"):
        a.line(d, "#FFC83A", 3, 0.8)


@chordoo("gigawatt")
def gigawatt(a):
    o = "#2A2A4A"
    # light beam
    a.path("M100 40 L196 6 V76 Z", a.lin("#FFF6A8", "#FFF6A8", x2=1, y2=0), None, extra=' class="fx" opacity=".55"')
    a.path("M100 40 L4 10 V70 Z", "#FFF6A8", None, extra=' class="fx" opacity=".35"')
    a.ground(rx=48)
    # tower body with red/white stripes
    a.path("M70 180 L78 64 H122 L130 180 Z", "#FFFFFF", o, 3.5)
    a.path("M74 128 L76 100 H124 L126 128 Z", "#E8405A", None)
    a.path("M71 170 L72 150 H128 L129 170 Z", "#E8405A", None)
    a.path("M70 180 L78 64 H122 L130 180 Z", "none", o, 3.5)
    # face screen panel
    a.path("M82 104 H118 V136 H82 Z", "#2A3A5A", o, 2.5)
    a.eye(92, 118, rx=6, ry=7, kind="glow", iris="#5AFFE8", pupil=("#2A3A5A", "#0A1020"))
    a.eye(108, 118, rx=6, ry=7, kind="glow", iris="#5AFFE8", pupil=("#2A3A5A", "#0A1020"))
    a.mouth(100, 128, "smile", w=5, color="#5AFFE8")
    # lamp room
    a.path("M74 64 H126 V56 H74 Z", "#3A3A5A", o, 3)
    a.path("M80 56 V30 H120 V56 Z", a.shade("#FFFFFF", "#FFF6A8", "#FFD020"), o, 3)
    a.line("M90 30 V56 M110 30 V56", o, 2)
    a.path("M76 30 L100 12 L124 30 Z", "#E8405A", o, 3)
    a.circ(100, 10, 4, "#E8405A", o, 2)
    # arms
    limb(a, "M76 150 C60 148 54 138 52 126", "#9AA0B8", o, 9)
    limb(a, "M124 150 C140 148 146 138 148 126", "#9AA0B8", o, 9)
    a.circ(52, 122, 7, "#C8CCD8", o, 2.5)
    a.circ(148, 122, 7, "#C8CCD8", o, 2.5)
    # little boat
    a.path("M150 176 H186 L180 186 H156 Z", "#5AC8FF", "#1E5A8A", 2)
    a.line("M168 176 V160 L180 172", "#1E5A8A", 2)


@chordoo("voltaros")
def voltaros(a):
    sc = a.shade("#8A9AE8", "#3A4AB8", "#141E5A")
    o = "#0A0E30"
    a.glow(100, 70, 60, "#FFE84D", 0.4)
    a.ground(rx=70)
    # bat wings with bolt edges
    for sx in (1, -1):
        a.path(f"M{100 + sx * 24} 100 L{100 + sx * 60} 40 L{100 + sx * 92} 56 L{100 + sx * 80} 76 L{100 + sx * 96} 92 "
               f"L{100 + sx * 76} 104 L{100 + sx * 88} 124 L{100 + sx * 40} 124 Z", a.lin("#5A6AD8", "#2A3488"), o, 3)
        a.line(f"M{100 + sx * 30} 104 L{100 + sx * 60} 40 M{100 + sx * 40} 112 L{100 + sx * 80} 76", "#8A9AF0", 2, 0.6)
    # tail
    a.path("M128 170 C160 176 180 160 184 140", "none", o, 14)
    a.path("M128 170 C160 176 180 160 184 140", "none", "#3A4AB8", 9)
    bolt(a, 184, 128, 0.6, 20)
    # body
    a.path("M64 178 C56 146 66 110 100 108 C134 110 144 146 136 178 Z", sc, o)
    a.path("M82 178 C80 150 88 128 100 126 C112 128 120 150 118 178 Z", a.lin("#FFF6C8", "#FFD84D"), None)
    for y in (142, 156, 170):
        a.line(f"M84 {y} Q100 {y + 4} 116 {y}", "#C89A20", 1.8)
    # head
    a.path("M60 76 C58 44 80 32 100 32 C120 32 142 44 140 76 C138 100 122 110 100 110 C78 110 62 100 60 76 Z", sc, o)
    a.ell(100, 96, 24, 13, "#5A6AD8", o, 2.5)
    a.circ(90, 94, 2, o)
    a.circ(110, 94, 2, o)
    # crackling crown: three bolts
    bolt(a, 76, 24, 0.7, -25)
    bolt(a, 100, 12, 0.9, 0)
    bolt(a, 124, 24, 0.7, 25)
    a.eyes(70, xs=(82, 118), kind="angry", rx=10, ry=11, iris="#FFE84D", pupil=("#1A1A3A", "#06060E"))
    a.mouth(100, 106, "fang", w=8, color=o)
    for x, y in ((16, 140), (40, 20), (170, 20)):
        bolt(a, x, y, 0.5, 10, cls="fx")

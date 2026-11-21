import math
from artkit import chordoo, INK
from shapes import limb, star, flower, zz

FY_O = "#4A2A6A"


def fairy_wings(a, cx, cy, s=1.0, fill=None, o=FY_O):
    f = fill or a.lin("#FFFFFF", "#E8F4FF", "#D8C8FF")
    for sx in (1, -1):
        a.path(f"M{cx} {cy} C{cx + sx * 20 * s} {cy - 40 * s} {cx + sx * 56 * s} {cy - 44 * s} {cx + sx * 54 * s} {cy - 14 * s} C{cx + sx * 52 * s} {cy + 4 * s} {cx + sx * 26 * s} {cy + 6 * s} {cx} {cy} Z", f, o, 2.5, ' opacity=".92"')
        a.path(f"M{cx} {cy + 4} C{cx + sx * 30 * s} {cy + 6 * s} {cx + sx * 42 * s} {cy + 26 * s} {cx + sx * 30 * s} {cy + 36 * s} C{cx + sx * 18 * s} {cy + 42 * s} {cx + sx * 6 * s} {cy + 20 * s} {cx} {cy + 4} Z", f, o, 2.5, ' opacity=".92"')


@chordoo("snuggle")
def snuggle(a):
    o = "#5A4A8A"
    a.ground(rx=54)
    body = a.shade("#F6F0FF", "#D0C0F8", "#9A88D8")
    a.path("M30 130 C14 110 30 80 54 88 C56 58 92 46 110 66 C128 48 166 60 164 92 C186 96 188 132 166 142 C150 158 50 158 30 130 Z", body, o, 3.5)
    # scarf
    sc = a.lin("#FF8AA8", "#E8506A")
    a.path("M44 128 C70 140 130 140 156 128 L158 142 C130 154 70 154 42 142 Z", sc, "#8A1A3A", 3)
    a.path("M128 142 L136 176 L120 178 L116 146 Z", sc, "#8A1A3A", 3)
    for x in (52, 66, 80, 94, 108, 122, 136, 150):
        a.line(f"M{x} 134 v10", "#FFFFFF", 1.6, 0.6)
    a.line("M120 170 H136 M118 160 H134", "#FFFFFF", 2.5)
    a.eyes(104, xs=(82, 118), kind="happy", rx=9)
    a.mouth(100, 116, "smile", w=6, color=o)
    a.cheeks([(66, 114), (134, 114)], "#FFA8C8", rx=9, ry=5)
    a.gloss(66, 84, 12, 6)
    for x, y in ((24, 50), (176, 50)):
        a.add(f'<path class="fx" d="M{x} {y + 8} C{x - 8} {y} {x - 4} {y - 6} {x} {y - 2} C{x + 4} {y - 6} {x + 8} {y} {x} {y + 8} Z" fill="#FFA8C8"/>')


@chordoo("dewdrop")
def dewdrop(a):
    o = "#1E5A7A"
    a.glow(100, 100, 70, "#C8F4FF", 0.5)
    a.ground(rx=30)
    # dewdrop wings
    for sx in (1, -1):
        for dy, r in ((-14, 26), (18, 18)):
            a.path(f"M{100 + sx * 6} {96 + dy} C{100 + sx * (r + 10)} {96 + dy - r} {100 + sx * (r * 2 + 10)} {96 + dy} {100 + sx * (r + 6)} {96 + dy + r * 0.7} C{100 + sx * r * 0.7} {96 + dy + r} {100 + sx * 8} {96 + dy + 8} {100 + sx * 6} {96 + dy} Z",
                   a.shade("#FFFFFF", "#C8F4FF", "#6AC8F0"), o, 2.5, ' opacity=".9"')
    # leaf dress
    a.path("M88 110 C76 130 74 150 86 160 C92 150 96 146 100 160 C104 146 108 150 114 160 C126 150 124 130 112 110 Z", a.shade("#D6F5A8", "#7CC850", "#3E8A2E"), "#2A5A1E", 2.5)
    for x in (92, 108):
        limb(a, f"M{x} 158 L{x} 176", "#FFE0D0", "#8A4A3A", 6)
    # head
    a.circ(100, 86, 22, a.shade("#FFF4EC", "#F8D8C8", "#D8A898"), "#8A4A3A", 2.5)
    a.path("M78 86 C74 60 126 60 122 86 C116 74 104 70 100 76 C94 70 84 74 78 86 Z", a.lin("#8AE8D8", "#3AA8C8"), o, 2.5)
    a.eyes(88, xs=(92, 108), rx=5, ry=7, iris="#3AA8C8", pupil=("#1A2A3A", "#060A0E"))
    a.mouth(100, 98, "smile", w=4, color="#A04A5A")
    a.cheeks([(86, 96), (114, 96)], rx=4, ry=3, dots=False)
    # watering a flower with a dewdrop
    limb(a, "M112 120 L132 124", "#FFE0D0", "#8A4A3A", 6)
    a.path("M136 116 C142 126 142 132 136 134 C130 132 130 126 136 116 Z", a.shade("#FFFFFF", "#A8E8FF", "#4AA8E0"), o, 2)
    a.line("M150 184 V160", "#3E8A2E", 2.5)
    flower(a, 150, 154, 12, "#FFB0D0", "#FFD84D", "#A04A7A")
    for x, y in ((30, 50), (170, 60), (40, 150)):
        a.sparkle(x, y, 5, "#C8F4FF")


@chordoo("pillowpuff")
def pillowpuff(a):
    o = "#6A5A8A"
    a.ground(rx=66)
    body = a.shade("#FFFFFF", "#F4F0FF", "#C8C0E8")
    a.path("M34 64 C60 72 140 72 166 64 C158 90 158 130 166 158 C140 150 60 150 34 158 C42 130 42 90 34 64 Z", body, o, 3.5)
    # corner tassels
    for x, y in ((34, 64), (166, 64), (34, 158), (166, 158)):
        a.circ(x, y, 6, "#B89AF0", o, 2)
    # stitching
    a.path("M46 76 C70 82 130 82 154 76 M46 146 C70 140 130 140 154 146", "none", "#B8B0D8", 2, ' stroke-dasharray="4 5"')
    # button eyes (sleepy: one open button, one shut)
    for x in (80, 120):
        a.circ(x, 104, 11, a.shade("#D8C8FF", "#9A7AE0", "#5A3AA8"), "#3A1A7A", 2.5)
        for dx, dy in ((-3, -3), (3, -3), (-3, 3), (3, 3)):
            a.circ(x + dx, 104 + dy, 1.6, "#3A1A7A")
    a.mouth(100, 124, "o", w=8, color=o)
    a.cheeks([(62, 122), (138, 122)], "#FFB0D0", rx=9, ry=5)
    zz(a, 150, 44)


@chordoo("sugarplum")
def sugarplum(a):
    o = "#5A1A5A"
    a.ground(rx=34)
    # candy wings (striped lollipop-like)
    for sx in (1, -1):
        a.ell(100 + sx * 36, 76, 28, 22, a.lin("#FFFFFF", "#FFC8F0"), o, 2.5, rot=sx * -20)
        a.path(f"M{100 + sx * 14} 76 Q{100 + sx * 36} 56 {100 + sx * 60} 70 M{100 + sx * 14} 82 Q{100 + sx * 36} 96 {100 + sx * 58} 88", "none", "#FF6AB0", 3)
    # tutu
    a.path("M64 124 C80 112 120 112 136 124 C146 134 130 140 124 134 C120 144 108 142 106 134 C100 144 92 142 92 134 C88 142 76 142 76 134 C68 140 54 134 64 124 Z", a.shade("#FFF0FA", "#C89AFF", "#8A4AD8"), o, 2.5)
    # body + legs on tiptoe
    a.path("M88 96 H112 L114 124 H86 Z", a.lin("#FFB0E0", "#E86AB0"), o, 2.5)
    limb(a, "M94 140 L90 180", "#FFE0D8", "#8A4A3A", 7)
    limb(a, "M106 140 L116 168 L126 168", "#FFE0D8", "#8A4A3A", 7)
    a.ell(90, 182, 6, 3, "#FF6AB0")
    # arms up in a twirl
    limb(a, "M88 100 C74 90 70 74 78 62", "#FFE0D8", "#8A4A3A", 7)
    limb(a, "M112 100 C126 90 130 74 122 62", "#FFE0D8", "#8A4A3A", 7)
    # head
    a.circ(100, 70, 22, a.shade("#FFF4EC", "#F8D8C8", "#D8A898"), "#8A4A3A", 2.5)
    a.path("M78 70 C74 40 126 40 122 70 C118 58 104 54 98 60 C90 54 80 60 78 70 Z", a.lin("#C89AFF", "#7A4AD8"), o, 2.5)
    a.circ(100, 42, 10, a.shade("#E8D0FF", "#9A5AE8", "#5A2AA8"), o, 2.5)
    a.line("M100 32 C102 26 106 24 110 24", "#3E8A2E", 2)
    a.eyes(72, xs=(92, 108), kind="happy", rx=6)
    a.mouth(100, 82, "smile", w=4, color="#A04A5A")
    a.cheeks([(86, 80), (114, 80)], rx=4, ry=3, dots=False)
    for x, y, c in ((30, 140, "#FF6AB0"), (170, 140, "#C89AFF"), (40, 40, "#FFD84D"), (162, 36, "#6AC8FF")):
        a.sparkle(x, y, 6, c)


@chordoo("dreamsheep")
def dreamsheep(a):
    o = "#5A5A8A"
    a.ground(rx=60)
    cloudf = a.shade("#FFFFFF", "#F0F4FF", "#B8C4E8")
    # legs
    for x in (66, 88, 118, 140):
        a.path(f"M{x - 5} 140 V176 H{x + 5} V140", "#5A5A7A", o, 2)
    # cloud fleece
    for cx, cy, r in ((62, 120, 24), (86, 104, 26), (116, 102, 26), (142, 118, 24), (102, 132, 28), (70, 140, 18), (134, 142, 18)):
        a.circ(cx, cy, r, cloudf, o, 3)
    for cx, cy, r in ((62, 120, 21), (86, 104, 23), (116, 102, 23), (142, 118, 21), (102, 132, 25), (70, 140, 15), (134, 142, 15)):
        a.circ(cx, cy, r, cloudf)
    # head
    a.path("M26 92 C24 72 38 62 54 64 C70 66 76 82 72 96 C68 112 52 116 40 112 C30 108 26 102 26 92 Z", a.shade("#8A8AA8", "#5A5A7A", "#3A3A54"), o, 3)
    a.ell(28, 82, 12, 6, "#5A5A7A", o, 2.5, rot=-30)
    a.ell(70, 78, 12, 6, "#5A5A7A", o, 2.5, rot=30)
    for x, y in ((40, 66), (52, 60), (62, 68)):
        a.circ(x, y, 8, cloudf, o, 2)
    a.eye(42, 88, kind="sleepy", rx=6)
    a.eye(60, 88, kind="sleepy", rx=6)
    a.mouth(50, 102, "smile", w=4, color="#FFFFFF")
    a.cheeks([(36, 98), (64, 98)], "#FFB0D0", rx=4, ry=3, dots=False)
    # moon + counting numbers
    a.path("M168 22 C150 26 146 50 162 58 C150 56 140 44 146 30 C150 22 160 20 168 22 Z", "#FFE88A", "#C8A030", 2, ' class="fx"')
    for x, y, t in ((140, 60, "1"), (160, 80, "2"), (176, 104, "3")):
        a.add(f'<text class="fx" x="{x}" y="{y}" font-size="14" font-weight="bold" font-family="sans-serif" fill="#8A8AC8">{t}</text>')


@chordoo("twinkle")
def twinkle(a):
    o = "#6A4A00"
    a.glow(100, 96, 80, "#FFF6A8", 0.6)
    a.ground(rx=30)
    # sparkle trail
    a.path("M40 170 C60 150 50 120 76 112", "none", "#FFE88A", 4, ' class="fx" stroke-dasharray="2 8"')
    for x, y, r in ((34, 176, 6), (52, 146, 5), (60, 124, 4)):
        a.sparkle(x, y, r)
    fairy_wings(a, 100, 100, 0.9)
    # star body
    star(a, 100, 104, 46, a.shade("#FFFFF0", "#FFE84D", "#E0A800"), o, 3.5, inner=0.55)
    a.eyes(102, xs=(90, 110), rx=7, ry=9, kind="star", iris="#FFB020", pupil=("#3A2A00", "#140E00"))
    a.mouth(100, 118, "smile", w=5, color=o)
    a.cheeks([(80, 114), (120, 114)], "#FF9AA8", rx=5, ry=3)
    # tiny wand
    a.line("M136 120 L156 92", "#E8D8FF", 3)
    star(a, 158, 88, 7, "#FFFFFF", "#B89AF0", 1.5)


@chordoo("unibun")
def unibun(a):
    fur = a.shade("#FFFFFF", "#FFF0F8", "#E0C0D8")
    o = "#7A4A7A"
    a.ground(rx=56)
    # rainbow it's hopping over
    for i, c in enumerate(("#FF8AA8", "#FFC86A", "#FFF08A", "#9AE89A", "#8AC8FF", "#C8A8FF")):
        a.add(f'<path class="fx" d="M14 184 A86 86 0 0 1 186 184" fill="none" stroke="{c}" stroke-width="6" transform="translate(0 {i * 6}) scale(1 {1 - i * 0.04})" opacity=".55"/>')
    # body mid-hop
    a.path("M52 140 C48 112 72 96 100 98 C130 100 150 118 146 140 C142 162 120 166 98 166 C74 166 56 160 52 140 Z", fur, o)
    a.circ(150, 128, 12, a.shade("#FFFFFF", "#FFE8F8", "#E8B8D8"), o, 2.5)
    a.ell(64, 166, 14, 7, fur, o, 2.5, rot=-20)
    a.ell(132, 168, 16, 7, fur, o, 2.5, rot=20)
    # head
    a.circ(78, 84, 32, fur, o)
    # ears
    a.path("M60 60 C50 30 56 10 66 12 C76 14 76 40 72 58 Z", fur, o, 3)
    a.path("M92 58 C98 28 112 14 120 20 C126 28 112 48 100 62 Z", fur, o, 3)
    a.path("M62 54 C58 34 62 22 66 22 C70 24 70 40 68 52 Z", "#FFB0D0", None)
    a.path("M96 56 C102 36 110 26 114 28 C116 34 106 46 100 58 Z", "#FFB0D0", None)
    # horn
    a.path("M76 54 L82 22 L88 54 Z", a.lin("#FFF6A8", "#FFB0E0", "#C89AFF"), "#8A5AA8", 2.5)
    a.line("M78 46 L86 42 M80 36 L85 33", "#8A5AA8", 1.5)
    # mane tuft
    a.path("M60 66 C54 56 64 48 72 54 C70 46 82 44 84 54", a.lin("#FF8AC8", "#8AC8FF"), o, 2.5)
    a.eyes(88, xs=(66, 92), rx=8, ry=10, iris="#C8A8FF", pupil=("#2A1A4A", "#0A0614"), lashes=1)
    a.path("M76 100 L82 100 L79 104 Z", "#FF8AB0")
    a.mouth(79, 106, "cat", w=5, color=o)
    a.cheeks([(56, 102), (104, 100)], "#FFB0D0", rx=6, ry=4)


@chordoo("wishkit")
def wishkit(a):
    fur = a.shade("#FFF8E8", "#FFD8A0", "#D89A50")
    o = "#6A3A14"
    a.ground(rx=50)
    # wishing-star tail
    a.path("M140 150 C164 146 172 124 164 104", "none", o, 10)
    a.path("M140 150 C164 146 172 124 164 104", "none", "#FFD8A0", 6)
    star(a, 164, 94, 16, a.shade("#FFFFF0", "#FFE84D", "#E0A800"), "#8A6A00", 2.5)
    a.add('<path class="fx" d="M176 80 L190 66 M180 92 L196 88 M166 76 L170 60" stroke="#FFE88A" stroke-width="2.5" stroke-linecap="round"/>')
    # body sitting
    a.path("M56 150 C52 122 72 106 100 106 C128 106 148 122 144 150 C142 172 124 180 100 180 C76 180 58 172 56 150 Z", fur, o)
    a.path("M80 140 C80 124 120 124 120 140 C120 162 110 172 100 172 C90 172 80 162 80 140 Z", "#FFFBF2")
    a.ell(80, 178, 12, 6, "#FFFBF2", o, 2.5)
    a.ell(120, 178, 12, 6, "#FFFBF2", o, 2.5)
    # head
    a.circ(100, 76, 34, fur, o)
    a.path("M72 58 L66 26 L92 46 Z", fur, o, 3)
    a.path("M128 58 L134 26 L108 46 Z", fur, o, 3)
    a.path("M74 52 L71 34 L84 45 Z", "#FFB0C0", None)
    a.path("M126 52 L129 34 L116 45 Z", "#FFB0C0", None)
    # orange tabby stripes
    a.path("M92 44 L96 54 M100 42 V54 M108 44 L104 54", "none", "#D89A50", 3)
    a.eyes(78, xs=(86, 114), rx=9, ry=11, iris="#FFC83A", pupil=("#3A2010", "#120804"), kind="star")
    a.path("M96 90 L104 90 L100 94 Z", "#FF8AA8")
    a.mouth(100, 96, "cat", w=5, color=o)
    a.cheeks([(74, 94), (126, 94)], "#FFA8B8", rx=7, ry=4)
    for x, y in ((24, 60), (30, 140), (150, 30)):
        a.sparkle(x, y, 5)


@chordoo("pegapony")
def pegapony(a):
    coat = a.shade("#FFFFFF", "#FFF4E8", "#F0D0B0")
    o = "#7A4A3A"
    a.ground(rx=60)
    # butterfly wings
    for k, (cx, cy, rx, ry, rot, c) in enumerate(((112, 74, 34, 24, -30, ("#FFF0FA", "#FFA8D8", "#E060A8")), (146, 68, 30, 22, 20, ("#F0FAFF", "#8AD0FF", "#3A88D0")),
                                                    (110, 104, 22, 14, -10, ("#FFFBE0", "#FFD86A", "#E09A2A")), (138, 102, 20, 12, 30, ("#F0FFF0", "#9AE8A8", "#3AA85A")))):
        a.ell(cx, cy, rx, ry, a.shade(*c), "#4A2A5A", 2.5, rot=rot)
        a.circ(cx, cy, 4, "#FFFFFF", extra=' opacity=".8"')
    # legs
    for x in (62, 80, 120, 138):
        a.path(f"M{x - 6} 140 L{x - 6} 176 H{x + 6} L{x + 6} 140", coat, o, 3)
        a.path(f"M{x - 7} 172 H{x + 7} V180 H{x - 7} Z", "#FFB0D0", o, 2)
    a.ell(100, 128, 48, 26, coat, o)
    # tail: pastel
    a.path("M146 120 C170 112 180 132 170 150 C166 136 160 132 150 134 Z", a.lin("#FFA8D8", "#8AD0FF"), o, 2.5)
    # neck + head
    a.path("M58 120 C50 100 50 86 54 74 L78 76 C76 90 78 104 84 114 Z", coat, o, 3)
    a.path("M26 70 C24 48 42 38 58 40 C76 42 82 56 78 70 C74 86 58 90 44 90 C32 88 26 80 26 70 Z", coat, o)
    a.ell(34, 80, 9, 7, "#FFE0EC", None)
    a.circ(30, 78, 1.6, o)
    a.circ(36, 82, 1.6, o)
    a.path("M50 38 C62 28 82 36 80 52 C86 64 80 76 78 88 C72 78 72 68 68 60 C62 52 52 48 50 38 Z", a.lin("#FFA8D8", "#C8A8FF", "#8AD0FF"), o, 2.5)
    a.ell(62, 38, 5, 10, coat, o, 2.5, rot=20)
    a.eye(56, 62, rx=7, ry=9, iris="#8AD0FF", pupil=("#2A2A5A", "#0A0A1A"), lashes=2, side=-1)
    a.mouth(40, 86, "smile", w=4, color=o)
    a.cheeks([(64, 76)], "#FFB0D0", rx=5, ry=3, dots=False)
    for x, y in ((20, 130), (176, 30), (100, 30)):
        a.sparkle(x, y, 5, "#FFA8D8")


@chordoo("fairyqueen")
def fairyqueen(a):
    o = "#5A2A5A"
    a.glow(100, 90, 90, "#FFE0F4", 0.5)
    a.ground(rx=40)
    fairy_wings(a, 100, 100, 1.3, a.lin("#FFFFFF", "#FFE8F8", "#C8F0D8"))
    # petal gown
    for k, c in enumerate(("#FFB0D0", "#FF8AC0", "#E860A0")):
        y = 120 + k * 18
        w = 22 + k * 12
        a.path(f"M{100 - w} {y + 24} C{100 - w * 0.8} {y} {100 - w * 0.3} {y - 6} 100 {y - 8} C{100 + w * 0.3} {y - 6} {100 + w * 0.8} {y} {100 + w} {y + 24} "
               f"C{100 + w * 0.5} {y + 16} {100 + w * 0.2} {y + 30} 100 {y + 20} C{100 - w * 0.2} {y + 30} {100 - w * 0.5} {y + 16} {100 - w} {y + 24} Z", c, o, 2.5)
    a.path("M88 98 H112 L114 116 H86 Z", a.lin("#D6F5A8", "#7CC850"), "#2A5A1E", 2.5)
    # arms holding a flower scepter
    limb(a, "M88 104 C76 110 70 120 70 130", "#FFE8DC", "#8A4A3A", 6)
    limb(a, "M112 104 C124 108 130 104 136 96", "#FFE8DC", "#8A4A3A", 6)
    a.line("M138 160 L140 60", "#3E8A2E", 3)
    flower(a, 140, 54, 14, "#FFFFFF", "#FFD84D", "#A04A7A")
    # head
    a.circ(100, 76, 22, a.shade("#FFF4EC", "#F8D8C8", "#D8A898"), "#8A4A3A", 2.5)
    a.path("M78 78 C70 46 130 46 122 78 C130 92 132 106 124 116 C122 100 118 88 114 80 C108 66 92 66 86 80 C82 88 78 100 76 116 C68 106 70 92 78 78 Z",
           a.lin("#FFE8A0", "#E8B860"), "#8A6A20", 2.5)
    # flower crown
    for x, y, c in ((82, 58, "#FFB0D0"), (92, 52, "#FFFFFF"), (100, 50, "#C8A8FF"), (108, 52, "#FFD84D"), (118, 58, "#FFB0D0")):
        flower(a, x, y, 8, c, "#FFC83A", "#A04A7A", w=1)
    a.eyes(80, xs=(92, 108), rx=6, ry=7, iris="#7CC850", pupil=("#2A3A1A", "#0A0E06"), lashes=2)
    a.mouth(100, 92, "smile", w=5, color="#A04A5A")
    a.cheeks([(86, 88), (114, 88)], rx=4, ry=3, dots=False)
    for x, y in ((24, 140), (176, 140), (30, 40), (172, 30)):
        a.sparkle(x, y, 6, "#FFB0D0")


@chordoo("sandmane")
def sandmane(a):
    fur = a.shade("#F4ECFF", "#B8A8E8", "#6A58A8")
    o = "#2A1E5A"
    a.glow(100, 80, 80, "#FFE8C0", 0.45)
    a.ground(rx=66)
    # sand mane: big fluffy dune ring with sparkles
    import math as m
    pts = []
    for i in range(24):
        ang = m.radians(i * 15)
        r = 58 if i % 2 == 0 else 48
        pts.append(f"{100 + r * m.cos(ang):.1f} {78 + r * m.sin(ang):.1f}")
    mane = a.shade("#FFF6DC", "#F0D498", "#C8A050")
    a.path("M" + " L".join(pts) + " Z", mane, "#8A6A2A", 3)
    for i in range(12):
        ang = m.radians(i * 30 + 10)
        a.circ(round(100 + 44 * m.cos(ang), 1), round(78 + 44 * m.sin(ang), 1), 2, "#FFFFFF", extra=' opacity=".9"')
    # body lying down
    a.path("M40 160 C36 132 60 120 100 120 C140 120 166 132 162 160 C160 178 140 182 100 182 C60 182 42 178 40 160 Z", fur, o)
    a.ell(64, 176, 18, 8, fur, o, 2.5)
    a.ell(136, 176, 18, 8, fur, o, 2.5)
    # tail tuft of sand
    a.path("M160 150 C178 146 186 132 180 120", "none", o, 8)
    a.path("M160 150 C178 146 186 132 180 120", "none", "#B8A8E8", 4)
    a.circ(180, 116, 8, mane, "#8A6A2A", 2)
    # face
    a.circ(100, 80, 32, fur, o)
    a.circ(74, 56, 9, fur, o, 2.5)
    a.circ(126, 56, 9, fur, o, 2.5)
    a.eyes(78, xs=(88, 112), kind="sleepy", rx=8)
    a.ell(100, 94, 12, 8, "#F4ECFF", o, 2)
    a.path("M96 89 L104 89 L100 93 Z", "#FF9AC0")
    a.mouth(100, 98, "cat", w=5, color=o)
    a.cheeks([(76, 92), (124, 92)], "#FFB0D0", rx=6, ry=4, dots=False)
    # sprinkling sleepy sand
    for x, y in ((24, 30), (40, 20), (30, 50), (176, 40), (164, 24)):
        a.circ(x, y, 2.5, "#F0D498", extra=' class="fx"')
    for x, y in ((36, 110), (170, 90)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")


@chordoo("lullabelle")
def lullabelle(a):
    o = "#2A2A6A"
    a.glow(100, 96, 96, "#C8D0FF", 0.5)
    a.ground(rx=56)
    # starry wings
    w = a.lin("#3A3AA8", "#1E1E6A")
    a.path("M96 112 C80 70 40 40 12 48 C26 60 22 70 34 76 C20 84 26 96 40 96 C34 106 46 116 62 114 C70 122 84 120 96 118 Z", w, o, 3)
    a.path("M110 108 C130 60 168 30 192 36 C180 50 186 58 174 66 C188 72 182 86 168 86 C176 96 164 106 148 104 C140 114 124 114 112 116 Z", w, o, 3)
    for x, y in ((40, 64), (60, 90), (30, 86), (76, 100), (160, 52), (176, 76), (146, 86), (130, 98)):
        star(a, x, y, 4, "#FFF6C8", None)
    # swan body
    body = a.shade("#FFFFFF", "#EEF0FF", "#B0B8E8")
    a.path("M46 150 C46 124 70 114 102 118 C132 122 160 132 160 152 C160 172 130 180 100 178 C70 176 46 170 46 150 Z", body, o)
    # long neck + head
    a.path("M62 138 C44 110 42 74 62 58 C74 48 92 52 94 64", "none", o, 15)
    a.path("M62 138 C44 110 42 74 62 58 C74 48 92 52 94 64", "none", "#F6F8FF", 10)
    a.circ(80, 60, 18, body, o, 3)
    a.path("M96 60 L112 66 L96 70 Z", "#FFC83A", "#8A5A00", 2)
    a.eye(80, 58, kind="sleepy", rx=6)
    a.cheeks([(86, 68)], "#FFB0D0", rx=5, ry=3, dots=False)
    # moon crown
    a.path("M74 42 C68 34 72 24 80 22 C76 28 78 36 86 38 C82 42 78 42 74 42 Z", "#FFE88A", "#8A6A00", 1.6)
    # lullaby notes
    for x, y in ((130, 30), (150, 140), (30, 150)):
        a.add(f'<text class="fx" x="{x}" y="{y}" font-size="20" fill="#8A9AF0">♪</text>')
    a.ell(100, 182, 70, 6, "#C8D0FF", extra=' class="fx" opacity=".6"')

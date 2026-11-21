import math
from artkit import chordoo, INK
from shapes import limb, star

BUG_O = "#2A1A2A"


def heart(a, x, y, s, fill, o=None, w=1.5, cls=""):
    c = f' class="{cls}"' if cls else ""
    st = f' stroke="{o}" stroke-width="{w}"' if o else ""
    a.add(f'<path{c} d="M{x} {y + s * 0.9} C{x - s * 1.4} {y} {x - s} {y - s} {x} {y - s * 0.35} '
          f'C{x + s} {y - s} {x + s * 1.4} {y} {x} {y + s * 0.9} Z" fill="{fill}"{st}/>')


@chordoo("ladybop")
def ladybop(a):
    o = BUG_O
    a.ground(rx=58)
    for x in (60, 84, 116, 140):
        a.line(f"M{x} 160 L{x + (x - 100) * 0.2} 180", o, 4)
    shell = a.shade("#FFB0B0", "#F03A4A", "#A0101E")
    a.path("M36 150 C34 100 64 72 104 72 C144 72 170 100 168 150 C140 164 64 164 36 150 Z", shell, o)
    a.line("M104 74 V156", o, 3)
    for x, y, s in ((64, 108, 9), (80, 138, 7), (140, 104, 9), (128, 136, 7), (104, 92, 6)):
        heart(a, x, y, s, "#2A1A2A")
    a.gloss(66, 90, 14, 6)
    # head on front-top
    a.path("M70 76 C70 44 134 44 134 76 C134 92 120 96 100 96 C80 96 70 92 70 76 Z", a.shade("#5A4A5A", "#2A1A2A", "#0A060A"), o)
    a.line("M86 50 C80 36 72 30 64 30", o, 2.5)
    a.line("M114 50 C120 36 128 30 136 30", o, 2.5)
    heart(a, 64, 30, 6, "#F03A4A", o, 1.5)
    heart(a, 136, 30, 6, "#F03A4A", o, 1.5)
    a.eyes(72, xs=(88, 112), kind="white", rx=9, ry=10, pupil=("#3A2A3A", "#0A060A"))
    a.mouth(100, 86, "smile", w=6, color="#FFFFFF")
    a.cheeks([(78, 86), (122, 86)], "#FF8AA8", rx=5, ry=3, dots=False)
    # counting fingers: numbers floating
    a.add('<text class="fx" x="156" y="60" font-size="18" font-weight="bold" font-family="sans-serif" fill="#F03A4A">5!</text>')


@chordoo("wiggly")
def wiggly(a):
    sk = a.shade("#E8FFC8", "#9AE05A", "#4E9A2A")
    o = "#2A4A12"
    a.ground(rx=66)
    # inching arch body: segments along an arch
    for i in range(9):
        t = i / 8
        x = 30 + t * 120
        y = 170 - math.sin(t * math.pi) * 70
        a.circ(round(x, 1), round(y, 1), 16 if i < 8 else 0, sk, o, 3)
    # feet dots under ends
    for x in (26, 40, 140, 152):
        a.ell(x, 184, 5, 3, "#4E9A2A")
    # head
    a.circ(160, 140, 26, sk, o)
    a.line("M150 116 C146 100 140 96 134 96 M168 116 C172 100 178 96 184 98", o, 2.5)
    a.circ(134, 96, 4, "#FFD84D", o, 1.5)
    a.circ(184, 98, 4, "#FFD84D", o, 1.5)
    # glasses
    a.eye(150, 138, rx=6, ry=7, iris="#9AE05A", pupil=("#2A1A0A", "#0A0602"))
    a.eye(172, 138, rx=6, ry=7, iris="#9AE05A", pupil=("#2A1A0A", "#0A0602"))
    a.circ(150, 138, 10, "none", "#3A2A1A", 2.5)
    a.circ(172, 138, 10, "none", "#3A2A1A", 2.5)
    a.line("M160 136 H162", "#3A2A1A", 2.5)
    a.mouth(162, 154, "smile", w=6, color=o)
    a.cheeks([(144, 152), (180, 152)], rx=5, ry=3, dots=False)
    # tape measure
    a.path("M10 150 H70 V160 H10 Z", "#FFD84D", "#8A6A00", 2)
    for x in range(14, 70, 6):
        a.line(f"M{x} 150 v{4 if x % 12 else 6}", "#8A6A00", 1.4)


@chordoo("antsy")
def antsy(a):
    sk = a.shade("#D88A6A", "#A0402A", "#5A1A0E")
    o = "#2A0A04"
    a.ground(rx=66)
    # giant crumb held overhead
    a.path("M40 54 C34 28 66 14 100 16 C140 18 170 30 164 56 C160 76 120 82 98 80 C66 78 44 74 40 54 Z", a.shade("#FFE8B8", "#E8B060", "#A8702A"), "#6A3A0A", 3)
    for x, y in ((70, 40), (100, 30), (130, 46), (90, 60), (146, 38)):
        a.circ(x, y, 3, "#A8702A")
    # legs running
    for x, d in ((60, -1), (80, 1), (100, -1), (120, 1), (140, -1), (160, 1)):
        a.line(f"M{x} 148 L{x + d * 10} 166 L{x + d * 4} 182", o, 3.5)
    # abdomen, thorax
    a.ell(144, 138, 30, 24, sk, o)
    a.ell(104, 138, 16, 14, sk, o)
    # head
    a.circ(64, 128, 26, sk, o)
    a.line("M54 106 C46 92 40 90 32 92 M70 104 C72 90 78 84 86 84", o, 2.5)
    # arms up holding crumb
    limb(a, "M100 128 L96 78", "#A0402A", o, 7)
    limb(a, "M112 128 L122 78", "#A0402A", o, 7)
    a.eye(56, 124, rx=6, ry=8, iris="#FF8A5A", pupil=("#2A0A04", "#0A0302"))
    a.eye(74, 124, rx=6, ry=8, iris="#FF8A5A", pupil=("#2A0A04", "#0A0302"))
    a.mouth(66, 140, "open", w=6, color="#5A1A0E")
    a.cheeks([(48, 138)], rx=5, ry=3, dots=False)
    for y in (110, 130, 150):
        a.line(f"M{180} {y} H196", "#C8A890", 2.5, 0.8)
    a.add('<path class="fx" d="M30 70 q-2 -8 2 -12 M24 80 q-4 -6 -2 -10" stroke="#8AC8F0" stroke-width="2.5" fill="none" stroke-linecap="round"/>')


@chordoo("snailbert")
def snailbert(a):
    sk = a.shade("#FFF0E0", "#F0C8A8", "#B88A6A")
    o = "#4A2A1A"
    a.ground(rx=66)
    a.path("M26 178 C26 160 46 154 74 154 H140 C160 154 168 128 160 108 C168 94 182 98 182 120 C182 156 166 182 132 182 H36 Z", sk, o)
    # cupcake shell: wrapper + frosting swirl
    a.path("M56 160 L64 112 H136 L144 160 Z", a.lin("#8AD8FF", "#4AA8E8"), "#1E5A8A", 3)
    for x in range(70, 140, 10):
        a.line(f"M{x} 114 L{x - 2 + (x - 100) * 0.1} 158", "#1E5A8A", 1.6, 0.5)
    a.path("M54 116 C44 100 60 84 74 90 C72 66 104 56 114 74 C130 62 154 78 146 98 C160 104 154 122 140 118 Z",
           a.shade("#FFFFFF", "#FFD0E4", "#F090B8"), "#A0406A", 3)
    a.line("M76 100 C86 90 100 92 104 100 C110 108 124 106 128 98", "#F090B8", 2.5)
    for x, y, c in ((80, 86, "#FFD84D"), (100, 76, "#6AC8FF"), (120, 86, "#8AE06A"), (110, 104, "#FF6A8A"), (68, 106, "#B89AF0"), (132, 106, "#FFD84D")):
        a.line(f"M{x - 3} {y} l6 -3", c, 3)
    a.circ(100, 56, 9, a.shade("#FFB0B0", "#E8203A", "#8A0A1A"), "#5A0A14", 2.5)
    a.line("M100 48 C102 40 108 36 112 36", "#3E6A1E", 2.2)
    # eyes on stalks
    a.line("M166 108 L162 80 M178 108 L182 82", o, 3)
    a.eye(162, 76, rx=6, ry=8, iris="#F090B8", pupil=("#2A1A0A", "#0A0602"))
    a.eye(182, 78, rx=6, ry=8, iris="#F090B8", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(172, 132, "smile", w=6, color=o)
    a.cheeks([(162, 124)], rx=5, ry=3, dots=False)


@chordoo("mantee")
def mantee(a):
    sk = a.shade("#E0FFC8", "#7AD050", "#3A8A22")
    o = "#1E4A12"
    a.ground(rx=50)
    # back legs
    a.line("M90 140 L70 160 L60 182", o, 4)
    a.line("M110 140 L134 160 L146 182", o, 4)
    # abdomen
    a.path("M86 120 C76 150 84 178 104 180 C124 178 128 150 116 120 Z", sk, o)
    # karate gi top
    a.path("M78 84 C76 104 80 124 84 132 H118 C124 124 126 104 122 84 C112 78 88 78 78 84 Z", "#FFFFFF", "#5A5A6A", 3)
    a.path("M100 84 L90 112 M100 84 L110 112", "none", "#5A5A6A", 2.5)
    a.path("M80 116 H120 V124 H80 Z", "#2A2A2A", INK, 2)
    a.path("M108 124 L114 140 L106 138 Z M112 124 L122 138 L114 140 Z", "#2A2A2A", INK, 1.5)
    # raptorial arms in a karate pose
    limb(a, "M80 94 L52 84 L46 60", "#7AD050", o, 9)
    a.path("M46 60 L40 44 L52 54 Z", "#7AD050", o, 2.5)
    limb(a, "M120 94 L150 98 L170 80", "#7AD050", o, 9)
    a.path("M170 80 L182 68 L176 84 Z", "#7AD050", o, 2.5)
    # triangle head
    a.path("M70 50 C70 30 130 30 130 50 C130 66 112 82 100 82 C88 82 70 66 70 50 Z", sk, o)
    a.line("M88 34 C84 20 76 14 68 14 M112 34 C116 20 124 14 132 14", o, 2.5)
    # headband
    a.path("M70 44 H130 V52 H70 Z", "#E8303A", "#6A0A14", 2)
    a.path("M130 46 L146 40 L144 50 L132 50 Z", "#E8303A", "#6A0A14", 2)
    a.eye(84, 58, rx=8, ry=9, kind="angry", iris="#7AD050", pupil=("#1E3A12", "#060E04"))
    a.eye(116, 58, rx=8, ry=9, kind="angry", iris="#7AD050", pupil=("#1E3A12", "#060E04"), side=-1)
    a.mouth(100, 72, "smile", w=5, color=o)
    for d in ("M24 70 l10 4", "M26 90 l10 0", "M180 100 l10 2"):
        a.line(d, "#A8D890", 3, 0.8)


@chordoo("dragonfli")
def dragonfli(a):
    o = "#1A2A4A"
    a.ground(rx=36)
    # stained-glass wings: leaded panels
    cols = ["#FF6A8A", "#FFD84D", "#6AC8FF", "#8AE06A", "#B89AF0", "#FF9A3A"]
    for i, (sx, y0, ln, ang) in enumerate(((1, 70, 84, -14), (1, 86, 74, 14), (-1, 70, 84, 14), (-1, 86, 74, -14))):
        g = f'<g transform="translate({100 + sx * 8} {y0}) rotate({ang if sx > 0 else 180 + ang})">'
        g += f'<path d="M0 0 C{ln * 0.3} -20 {ln} -18 {ln} 0 C{ln} 16 {ln * 0.3} 18 0 0 Z" fill="#FFFFFF" stroke="{o}" stroke-width="3"/>'
        for k in range(3):
            x0, x1 = ln * (0.12 + k * 0.28), ln * (0.12 + (k + 1) * 0.28)
            g += f'<path d="M{x0:.1f} -12 L{x1:.1f} -13 L{x1:.1f} 0 L{x0:.1f} 0 Z" fill="{cols[(i + k) % 6]}" stroke="{o}" stroke-width="1.6" opacity=".9"/>'
            g += f'<path d="M{x0:.1f} 0 L{x1:.1f} 0 L{x1:.1f} 11 L{x0:.1f} 10 Z" fill="{cols[(i + k + 3) % 6]}" stroke="{o}" stroke-width="1.6" opacity=".9"/>'
        g += '</g>'
        a.add(g)
    # long body
    body = a.lin("#6AE8D8", "#2A88C8")
    a.path("M94 92 C92 130 94 160 100 178 C106 160 108 130 106 92 Z", body, o, 3)
    for y in (108, 124, 140, 156):
        a.line(f"M95 {y} H105", o, 1.6, 0.6)
    a.ell(100, 82, 12, 14, a.shade("#B8FFF8", "#6AE8D8", "#2A88C8"), o, 3)
    # head with huge eyes
    a.circ(100, 56, 18, a.shade("#B8FFF8", "#6AE8D8", "#2A88C8"), o, 3)
    a.circ(86, 50, 12, "#FFFFFF", o, 2.5)
    a.circ(114, 50, 12, "#FFFFFF", o, 2.5)
    a.eye(86, 51, rx=8, ry=9, iris="#6AE8D8", pupil=("#1A2A4A", "#060A14"))
    a.eye(114, 51, rx=8, ry=9, iris="#6AE8D8", pupil=("#1A2A4A", "#060A14"))
    a.mouth(100, 66, "smile", w=5, color=o)
    for x, y in ((24, 140), (176, 150)):
        a.ell(x, y, 14, 4, "#8AD8F0", extra=' class="fx" opacity=".6"')


@chordoo("beetlejoy")
def beetlejoy(a):
    o = "#1A2A1A"
    a.ground(rx=72)
    # giant gumball
    a.circ(64, 120, 52, a.shade("#FFFFFF", "#FF7AC0", "#C02A80"), "#6A0A40", 3.5)
    for x, y, c in ((44, 100, "#FFD84D"), (80, 92, "#6AC8FF"), (60, 140, "#8AE06A"), (90, 130, "#FFFFFF"), (36, 130, "#B89AF0")):
        a.circ(x, y, 6, c, extra=' opacity=".85"')
    a.gloss(46, 88, 14, 7)
    # beetle pushing (standing on front legs, back legs on ball)
    sh = a.shade("#B8F0A8", "#3AAA6A", "#145A2A")
    for x1, y1, x2, y2 in ((130, 160, 120, 182), (148, 160, 152, 182), (166, 156, 182, 176), (134, 130, 112, 110), (142, 124, 116, 90)):
        a.line(f"M{x1} {y1} L{x2} {y2}", o, 4)
    a.ell(154, 138, 32, 26, sh, o, rot=-25)
    a.line("M136 120 L172 156", o, 2.5)
    a.gloss(142, 124, 10, 4, rot=-60)
    # head pointing toward ball
    a.circ(126, 152, 16, a.shade("#5A6A5A", "#2A3A2A", "#0A140A"), o, 3)
    a.eye(122, 150, rx=5, ry=6, kind="white", pupil=("#2A3A2A", "#0A140A"))
    a.eye(134, 150, rx=5, ry=6, kind="white", pupil=("#2A3A2A", "#0A140A"))
    a.mouth(128, 162, "smile", w=4, color="#FFFFFF")
    a.line("M120 140 C114 130 110 128 104 130 M134 138 C136 128 142 124 148 126", o, 2)
    # collection: little shiny things
    for x, y, c in ((176, 60, "#FFD84D"), (150, 40, "#6AC8FF"), (182, 100, "#FF7AC0")):
        star(a, x, y, 8, c, "#6A4A00", 1.5, cls="fx")


@chordoo("webster")
def webster(a):
    sk = a.shade("#D8C8F0", "#8A6AB8", "#4A2A78")
    o = "#24103A"
    # web behind
    for ang in range(0, 360, 45):
        a.add(f'<path class="fx" d="M100 70 L100 0" stroke="#C8C0E0" stroke-width="1.5" transform="rotate({ang} 100 70)"/>')
    for r in (24, 44, 64):
        a.circ(100, 70, r, "none", "#C8C0E0", 1.5, extra=' class="fx"')
    a.ground(rx=56)
    # 8 legs
    for sx in (1, -1):
        for k, (dx, dy) in enumerate(((44, -20), (52, 0), (50, 22), (40, 44))):
            a.line(f"M{100 + sx * 26} {130 + k * 6} Q{100 + sx * (26 + dx * 0.6)} {110 + k * 8 + dy * 0.2} {100 + sx * (26 + dx)} {138 + dy + k * 6}", o, 4)
    # knitting: needles + scarf
    a.line("M60 120 L140 108", "#C8A060", 3)
    a.line("M60 108 L140 122", "#C8A060", 3)
    # body
    a.ell(100, 134, 38, 34, sk, o)
    # yarn scarf dangling
    a.path("M74 146 C80 160 120 160 126 146 L124 160 C112 172 88 172 76 160 Z", a.lin("#FFD84D", "#FF9A3A"), "#8A4A00", 2.5)
    for x in (84, 96, 108, 120):
        a.path(f"M{x - 4} 156 l4 4 l4 -4", "none", "#FFFFFF", 1.6)
    a.eyes(124, xs=(86, 114), rx=9, ry=11, iris="#B89AF0", pupil=("#24103A", "#0A0414"))
    a.circ(100, 108, 4, "#FFFFFF", o, 1.5)
    a.circ(92, 108, 3, "#FFFFFF", o, 1.5)
    a.circ(108, 108, 3, "#FFFFFF", o, 1.5)
    a.mouth(100, 140, "smile", w=6, color=o)
    a.cheeks([(76, 136), (124, 136)], rx=6, ry=4)
    # yarn ball
    a.circ(160, 176, 10, "#FF6A9A", "#8A1A4A", 2)
    a.line("M152 172 C158 178 164 170 168 178 M154 182 C160 174 164 184 168 172", "#8A1A4A", 1.4)


@chordoo("monarcha")
def monarcha(a):
    o = "#2A1408"
    a.ground(rx=36)
    org = a.shade("#FFE0A8", "#FF9A20", "#C85A00")
    for sx in (1, -1):
        a.path(f"M100 90 C{100 + sx * 30} 40 {100 + sx * 92} 26 {100 + sx * 90} 76 C{100 + sx * 88} 100 {100 + sx * 50} 108 100 100 Z", org, o, 3.5)
        a.path(f"M100 104 C{100 + sx * 50} 108 {100 + sx * 76} 128 {100 + sx * 62} 156 C{100 + sx * 48} 170 {100 + sx * 18} 150 100 116 Z", org, o, 3.5)
        # vein pattern
        a.line(f"M100 94 C{100 + sx * 30} 74 {100 + sx * 60} 56 {100 + sx * 84} 52 M100 98 C{100 + sx * 40} 92 {100 + sx * 70} 84 {100 + sx * 88} 80 "
               f"M100 108 C{100 + sx * 30} 118 {100 + sx * 50} 132 {100 + sx * 58} 150", o, 3)
        for k in range(5):
            a.circ(100 + sx * (60 + k * 6), 36 + k * 9, 3, "#FFFFFF")
        for k in range(3):
            a.circ(100 + sx * (40 + k * 8), 154 - k * 4, 2.5, "#FFFFFF")
    a.ell(100, 128, 9, 30, a.shade("#5A4A3A", "#2A1A0E", "#0A0604"), o, 2.5)
    a.circ(100, 92, 16, a.shade("#5A4A3A", "#2A1A0E", "#0A0604"), o, 2.5)
    # tiny crown
    a.path("M90 78 L92 66 L97 72 L100 62 L103 72 L108 66 L110 78 Z", a.lin("#FFF6A8", "#FFC020"), "#8A5A00", 2)
    a.eyes(92, xs=(93, 107), rx=5, ry=6, kind="white", pupil=("#2A1A0E", "#0A0604"))
    a.mouth(100, 102, "smile", w=4, color="#FFFFFF")
    a.line("M94 64 C88 50 82 46 76 48 M106 64 C112 50 118 46 124 48", o, 2)
    # tiny suitcase for travels
    a.path("M146 160 H170 V178 H146 Z", "#8A5A2A", "#3A2010", 2)
    a.path("M152 160 V154 H164 V160", "none", "#3A2010", 2)
    a.circ(158, 169, 3, "#FFD84D")


@chordoo("scorpio")
def scorpio(a):
    sk = a.shade("#FFE8C0", "#E8B060", "#A8702A")
    o = "#4A2A0A"
    a.ground(rx=66)
    # tail arching over with heart tip
    a.path("M140 140 C170 130 178 96 160 68 C150 52 128 50 118 62", "none", o, 18)
    a.path("M140 140 C170 130 178 96 160 68 C150 52 128 50 118 62", "none", "#E8B060", 13)
    for t in ((166, 112), (168, 86), (150, 60)):
        a.circ(t[0], t[1], 2, o)
    heart(a, 112, 62, 13, a.shade("#FFB0C8", "#FF4A7A", "#B0103A"), "#6A0A1E", 2.5)
    # legs
    for x, d in ((70, -1), (84, -1), (116, 1), (130, 1)):
        a.line(f"M{x} 150 L{x + d * 14} 166 L{x + d * 20} 182", o, 4)
    # pincers
    for sx in (1, -1):
        cx = 100 + sx * 66
        limb(a, f"M{100 + sx * 36} 140 C{100 + sx * 50} 140 {cx} 136 {cx} 128", "#E8B060", o, 9)
        a.path(f"M{cx} 132 C{cx - 14} 122 {cx - 10} 102 {cx + 2} 100 C{cx} 110 {cx + 2} 116 {cx + 6} 118 C{cx + 12} 112 {cx + 14} 104 {cx + 12} 100 "
               f"C{cx + 22} 108 {cx + 16} 132 {cx} 132 Z", "#E8B060", o, 3)
    # body
    a.ell(100, 144, 42, 26, sk, o)
    for x in (88, 100, 112):
        a.line(f"M{x} 122 Q{x + 4} 144 {x} 166", o, 1.6, 0.4)
    a.eyes(140, xs=(86, 114), rx=9, ry=11, iris="#FF8AA8", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(100, 156, "smile", w=6, color=o)
    a.cheeks([(72, 154), (128, 154)], "#FF8AA8", rx=6, ry=4)
    # brows look tough
    a.line("M76 124 L94 128 M124 124 L106 128", o, 3)


@chordoo("hivequeen")
def hivequeen(a):
    o = "#3A2400"
    a.glow(100, 70, 60, "#FFE88A", 0.5)
    a.ground(rx=46)
    for sx in (1, -1):
        a.ell(100 + sx * 46, 84, 34, 18, "#F0F8FF", "#7A9AB8", 2.5, rot=sx * -30, extra=' opacity=".9"')
        a.ell(100 + sx * 40, 108, 24, 12, "#F0F8FF", "#7A9AB8", 2.5, rot=sx * 10, extra=' opacity=".9"')
    # long royal abdomen
    body = a.shade("#FFF6C0", "#FFC83A", "#C88A00")
    a.path("M70 118 C66 150 80 182 100 184 C120 182 134 150 130 118 Z", body, o)
    for y in (134, 152, 168):
        a.path(f"M{70 + (y - 118) * 0.1} {y} Q100 {y + 8} {130 - (y - 118) * 0.1} {y}", "none", "#3A2400", 7)
    # thorax with fluffy collar
    a.circ(100, 108, 22, a.shade("#FFFFFF", "#FFF0C8", "#E0C88A"), o, 3)
    # head
    a.circ(100, 72, 28, body, o)
    # honeycomb crown
    for x, y in ((84, 40), (100, 34), (116, 40), (92, 26), (108, 26)):
        pts = " ".join(f"{x + 8 * math.cos(math.radians(60 * k + 30)):.1f},{y + 8 * math.sin(math.radians(60 * k + 30)):.1f}" for k in range(6))
        a.add(f'<polygon points="{pts}" fill="{a.lin("#FFE88A", "#FFB020")}" stroke="#8A5A00" stroke-width="2"/>')
    a.circ(100, 30, 2.5, "#FF6A8A")
    a.eyes(74, xs=(88, 112), rx=8, ry=10, iris="#FFB020", pupil=("#2A1A00", "#0A0600"), lashes=2)
    a.mouth(100, 88, "smile", w=6, color=o)
    a.cheeks([(78, 86), (122, 86)], rx=6, ry=4)
    # scepter
    a.line("M134 120 L160 60", "#8A5A00", 4)
    a.circ(160, 56, 8, a.shade("#FFF6C0", "#FFC83A", "#C88A00"), "#8A5A00", 2)
    limb(a, "M120 110 L138 116", "#FFC83A", o, 8)
    for x, y in ((30, 150), (170, 150), (24, 50)):
        a.add(f'<g class="fx"><ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="#FFC83A" stroke="{o}" stroke-width="1.5"/>'
              f'<path d="M{x - 2} {y - 5} V{y + 5} M{x + 2} {y - 5} V{y + 5}" stroke="{o}" stroke-width="2"/></g>')


@chordoo("lunamoth")
def lunamoth(a):
    o = "#1E3A3A"
    a.glow(100, 92, 100, "#C8FFE8", 0.5)
    a.ground(rx=40)
    wing = a.shade("#F4FFF0", "#B8F0C8", "#5AB88A")
    for sx in (1, -1):
        a.path(f"M100 86 C{100 + sx * 24} 30 {100 + sx * 92} 18 {100 + sx * 92} 70 C{100 + sx * 92} 98 {100 + sx * 54} 106 100 100 Z", wing, o, 3)
        # long trailing hindwing tails
        a.path(f"M100 104 C{100 + sx * 46} 108 {100 + sx * 60} 128 {100 + sx * 54} 148 C{100 + sx * 50} 164 {100 + sx * 58} 180 {100 + sx * 66} 192 "
               f"C{100 + sx * 40} 180 {100 + sx * 30} 160 {100 + sx * 26} 146 C{100 + sx * 20} 130 {100 + sx * 8} 118 100 112 Z", wing, o, 3)
        # glowing wing-eyes
        ex = 100 + sx * 56
        a.glow(ex, 66, 18, "#FFF6A8", 0.9)
        a.circ(ex, 66, 11, "#FFF6C8", "#8A7A2A", 2)
        a.circ(ex, 66, 6, "#6A4A9A")
        a.circ(ex + 2, 64, 2, "#FFFFFF")
        a.line(f"M{100 + sx * 8} 60 C{100 + sx * 40} 44 {100 + sx * 70} 40 {100 + sx * 86} 50", "#E8C8FF", 3, 0.8)
    body = a.shade("#FFFFFF", "#F0F0F0", "#B8C0C8")
    a.ell(100, 120, 13, 30, body, o, 3)
    a.circ(100, 82, 20, body, o, 3)
    for sx in (1, -1):
        a.path(f"M{100 + sx * 8} 66 C{100 + sx * 14} 46 {100 + sx * 24} 38 {100 + sx * 34} 36 C{100 + sx * 28} 46 {100 + sx * 20} 56 {100 + sx * 12} 66 Z", "#F0E0B8", "#8A7A4A", 2)
    a.eyes(82, xs=(92, 108), rx=6, ry=7, iris="#5AB88A", pupil=("#1E3A3A", "#0A1414"), kind="star")
    a.mouth(100, 94, "smile", w=4, color=o)
    a.cheeks([(86, 92), (114, 92)], "#FFA8C8", rx=4, ry=3, dots=False)
    # full moon
    a.circ(100, 20, 12, a.shade("#FFFFF0", "#FFF6C8", "#E8D890"), extra=' class="fx"')

from artkit import chordoo, INK
from shapes import limb, star, zz

GHOST = ("#FFFFFF", "#F0EEFF", "#B8B0E0")
SP_O = "#2E2450"


def ghost_body(a, top, bottom, left, right, fill, o=SP_O, waves=4):
    """Classic sheet-ghost silhouette with a wavy hem."""
    w = (right - left) / waves
    hem = ""
    for i in range(waves):
        x0 = right - i * w
        hem += f" Q{x0 - w * 0.25} {bottom + 10} {x0 - w * 0.5} {bottom} Q{x0 - w * 0.75} {bottom - 10} {x0 - w} {bottom}"
    mid = (left + right) / 2
    a.path(f"M{left} {bottom} V{top + 40} C{left} {top} {right} {top} {right} {top + 40} V{bottom}{hem} Z", fill, o)


@chordoo("drizzle")
def drizzle(a):
    a.ground(rx=36)
    a.glow(100, 100, 70, "#D8D0FF", 0.4)
    # cloud puffs behind its head
    for x, y, r in ((64, 72, 16), (84, 52, 18), (112, 48, 18), (136, 68, 16)):
        a.circ(x, y, r, a.shade(*GHOST), SP_O, 3)
    ghost_body(a, 50, 160, 56, 144, a.shade(*GHOST))
    a.eyes(104, xs=(84, 116), kind="sleepy", rx=9)
    a.mouth(100, 122, "o", w=7, color="#6A5A9A")
    a.cheeks([(72, 118), (128, 118)], "#C8A8FF", rx=8, ry=5, dots=False)
    # little arms
    a.path("M56 120 C44 120 40 112 44 106", "none", SP_O, 3)
    a.path("M144 120 C156 120 160 112 156 106", "none", SP_O, 3)
    zz(a, 150, 40)
    for x in (80, 100, 120):
        a.path(f"M{x} 172 C{x + 3} 177 {x + 3} 180 {x} 181 C{x - 3} 180 {x - 3} 177 {x} 172 Z", "#B8C8F0", extra=' class="fx"')


@chordoo("peekaberry")
def peekaberry(a):
    o = "#3A1A5A"
    a.ground(rx=36)
    ghost_body(a, 44, 164, 50, 150, a.shade("#E8D8FF", "#A06AE0", "#5A2AA0"), o)
    # berry dimples
    for x, y in ((74, 140), (120, 146), (100, 70), (132, 96), (66, 94)):
        a.circ(x, y, 2.5, "#E8D8FF", extra=' opacity=".7"')
    # leaf + stem on top
    a.line("M100 46 C100 36 104 30 110 26", "#3E8A2E", 3)
    a.ell(118, 30, 14, 6, a.shade("#D6F5A8", "#7CC850", "#3E8A2E"), "#2A5A1E", 2.5, rot=-20)
    a.eyes(104, xs=(82, 118), rx=10, ry=12, iris="#C8A8FF", pupil=("#2A1A4A", "#0A0614"))
    a.mouth(100, 126, "open", w=8, color="#5A1A3A")
    a.cheeks([(68, 120), (132, 120)], "#FF8AC0", rx=9, ry=6)
    # hands up "boo" then sorry sweat drop
    a.path("M50 110 C36 104 32 90 40 84 C46 82 50 90 52 96", a.shade("#E8D8FF", "#A06AE0", "#5A2AA0"), o, 3)
    a.path("M150 110 C164 104 168 90 160 84 C154 82 150 90 148 96", a.shade("#E8D8FF", "#A06AE0", "#5A2AA0"), o, 3)
    a.path("M146 64 C150 72 150 76 146 78 C142 76 142 72 146 64 Z", "#8AD0FF", "#3A8AD0", 1.5)
    a.add('<text class="fx" x="14" y="50" font-size="20" font-weight="bold" font-family="sans-serif" fill="#A06AE0">boo!</text>')


@chordoo("batty")
def batty(a):
    fur = a.shade("#B8A8D8", "#6A5A98", "#2E2458")
    o = "#140E2A"
    a.ground(rx=40)
    # wings
    for sx in (1, -1):
        a.path(f"M{100 + sx * 36} 110 C{100 + sx * 58} 90 {100 + sx * 80} 86 {100 + sx * 92} 96 C{100 + sx * 84} 104 {100 + sx * 86} 112 {100 + sx * 90} 122 "
               f"C{100 + sx * 78} 120 {100 + sx * 70} 126 {100 + sx * 72} 136 C{100 + sx * 60} 130 {100 + sx * 50} 132 {100 + sx * 40} 138 Z",
               a.lin("#8A78C8", "#3A2E6A"), o, 3)
    # round body
    a.circ(100, 122, 44, fur, o)
    # huge ears
    for sx in (1, -1):
        a.path(f"M{100 + sx * 18} 86 C{100 + sx * 20} 50 {100 + sx * 36} 20 {100 + sx * 56} 18 C{100 + sx * 58} 46 {100 + sx * 50} 76 {100 + sx * 38} 92 Z", fur, o, 3)
        a.path(f"M{100 + sx * 26} 82 C{100 + sx * 28} 58 {100 + sx * 38} 36 {100 + sx * 50} 30 C{100 + sx * 50} 50 {100 + sx * 44} 70 {100 + sx * 36} 84 Z", "#FFB0D0", None)
    a.path("M80 132 C80 118 120 118 120 132 C120 150 110 160 100 160 C90 160 80 150 80 132 Z", "#E8E0FF", None, extra=' opacity=".5"')
    a.eyes(116, xs=(84, 116), rx=10, ry=12, iris="#FF8AC0", pupil=("#2A1A4A", "#0A0614"))
    a.mouth(100, 136, "fang", w=7, color=o)
    a.cheeks([(70, 132), (130, 132)], "#FF8AC0", rx=7, ry=4)
    a.path("M88 166 l-2 10 M112 166 l2 10", "none", o, 3)
    a.gloss(76, 100, 8, 4)


@chordoo("skelly")
def skelly(a):
    bone = a.shade("#FFFFFF", "#F4F0E6", "#C8C0AA")
    o = "#3A3428"
    a.ground(rx=40)
    # legs
    for x in (88, 112):
        a.line(f"M{x} 140 V176", o, 8)
        a.line(f"M{x} 140 V176", "#F4F0E6", 4)
        a.ell(x + (x - 100) * 0.3, 178, 9, 5, "#F4F0E6", o, 2.5)
    # spine & ribs
    a.line("M100 104 V142", o, 8)
    a.line("M100 104 V142", "#F4F0E6", 4)
    for y, w in ((112, 20), (122, 18), (132, 14)):
        a.path(f"M{100 - w} {y + 4} Q100 {y - 6} {100 + w} {y + 4}", "none", o, 7)
        a.path(f"M{100 - w} {y + 4} Q100 {y - 6} {100 + w} {y + 4}", "none", "#F4F0E6", 3)
    a.ell(100, 144, 18, 7, bone, o, 3)
    # arms waving
    limb(a, "M84 112 L64 100 L56 80", "#F4F0E6", o, 8)
    limb(a, "M116 112 L136 120 L150 108", "#F4F0E6", o, 8)
    a.circ(56, 76, 6, bone, o, 2.5)
    a.circ(152, 104, 6, bone, o, 2.5)
    # skull
    a.path("M64 64 C64 34 136 34 136 64 C136 80 128 88 122 92 V100 H78 V92 C72 88 64 80 64 64 Z", bone, o)
    a.ell(84, 64, 11, 12, "#3A3050")
    a.ell(116, 64, 11, 12, "#3A3050")
    a.circ(88, 60, 4, "#FFFFFF")
    a.circ(120, 60, 4, "#FFFFFF")
    a.path("M96 78 L100 72 L104 78 Z", "#3A3050")
    a.path("M84 90 Q100 98 116 90", "none", o, 2.5)
    for x in (92, 100, 108):
        a.line(f"M{x} 90 V96", o, 1.8)
    a.cheeks([(72, 80), (128, 80)], "#FFA8C0", rx=6, ry=4, dots=False)
    # party hat
    a.path("M86 40 L104 4 L118 38 Z", a.lin("#6AC8FF", "#3A7AE8"), "#1E3A8A", 2.5)
    for x, y, c in ((98, 26, "#FFD84D"), (108, 18, "#FF6A9A"), (104, 32, "#8AE06A")):
        a.circ(x, y, 2.5, c)
    a.circ(104, 4, 4, "#FFD84D", "#8A6A00", 1.5)
    for x, y, c in ((30, 40, "#FF6A9A"), (170, 50, "#FFD84D"), (164, 150, "#6AC8FF"), (34, 140, "#8AE06A")):
        a.add(f'<rect class="fx" x="{x}" y="{y}" width="6" height="10" fill="{c}" transform="rotate(30 {x} {y})"/>')


@chordoo("pumpkinhead")
def pumpkinhead(a):
    o = "#4A2A0A"
    a.ground(rx=44)
    # crow on the fence post
    a.line("M168 190 V120", "#8A5A2A", 6)
    a.ell(168, 112, 10, 8, "#3A3A4A", "#14141E", 2)
    a.circ(174, 104, 6, "#3A3A4A", "#14141E", 2)
    a.path("M179 104 L186 106 L179 108 Z", "#FFC83D")
    a.circ(176, 102, 1.5, "#FFFFFF")
    # stick legs + patched pants
    a.line("M90 150 V182 M110 150 V182", "#8A5A2A", 6)
    a.path("M76 128 H124 L120 158 H80 Z", a.lin("#6A8AD8", "#3A5AA8"), "#1E2E6A", 3)
    a.path("M108 140 H118 V150 H108 Z", "#FFD84D", "#8A6A00", 1.5)
    # flannel shirt + straw arms
    a.path("M70 96 H130 L126 132 H74 Z", "#E8503A", "#6A1A0E", 3)
    a.line("M86 96 V132 M100 96 V132 M114 96 V132", "#A02A1A", 2, 0.6)
    a.line("M72 110 H128 M72 122 H128", "#A02A1A", 2, 0.6)
    a.line("M70 102 L30 96", "#C89A4A", 6)
    a.line("M130 102 L170 96", "#C89A4A", 6)
    for x, sx in ((30, -1), (170, 1)):
        for k in (-6, 0, 6):
            a.line(f"M{x} 96 l{sx * 10} {k}", "#E8C87A", 3)
    # jack-o-lantern head
    pk = a.shade("#FFD8A0", "#FF9A3A", "#C85A14")
    for cx, rx in ((82, 22), (118, 22), (100, 28)):
        a.ell(cx, 70, rx, 30, pk, o, 3)
    a.path("M96 42 C94 32 98 26 104 24 L108 30 C104 32 104 36 106 42 Z", "#6E8A2A", "#3A4A12", 2.5)
    # straw hat
    a.path("M54 48 C70 38 130 38 146 48 C130 52 70 52 54 48 Z", "#E8C87A", "#8A6A2A", 2.5)
    a.path("M76 46 C76 24 124 24 124 46 Z", "#E8C87A", "#8A6A2A", 2.5)
    a.path("M76 40 H124 V46 H76 Z", "#E8503A", None)
    # carved friendly face
    a.path("M78 66 L86 56 L94 66 Z M106 66 L114 56 L122 66 Z", "#FFE84D", "#6A2A0A", 2)
    a.path("M78 80 Q100 98 122 80 L116 84 L110 80 L104 86 L96 80 L90 86 L84 80 Z", "#FFE84D", "#6A2A0A", 2)


@chordoo("cobweb")
def cobweb(a):
    fur = a.shade("#5A4A6A", "#2E2440", "#140E20")
    o = "#08040E"
    # web
    a.path("M10 30 Q100 50 190 30 M10 30 L100 100 L190 30 M100 0 V100", "none", "#C8C0E0", 1.5, ' class="fx"')
    a.ground(rx=66)
    # 8 legs in boots, tap-dancing
    boots = ["#FF6A9A", "#FFD84D", "#6AC8FF", "#8AE06A"]
    for sx in (1, -1):
        for k in range(4):
            fx = 100 + sx * (34 + k * 16)
            fy = 176 - (8 if (k + (sx > 0)) % 2 else 0)
            a.line(f"M{100 + sx * 20} {130 + k * 4} Q{100 + sx * (36 + k * 10)} {112 + k * 4} {fx} {fy - 8}", o, 5)
            a.path(f"M{fx - 5} {fy - 10} H{fx + 5} V{fy} H{fx + sx * 10} V{fy + 4} H{fx - 5} Z", boots[k], o, 1.8)
    # fuzzy body
    import math
    pts = " ".join(f"{100 + (40 if i % 2 else 34) * math.cos(math.radians(i * 12)):.1f},{124 + (38 if i % 2 else 32) * math.sin(math.radians(i * 12)):.1f}" for i in range(30))
    a.add(f'<polygon points="{pts}" fill="{fur}" stroke="{o}" stroke-width="3" stroke-linejoin="round"/>')
    a.eyes(118, xs=(86, 114), kind="white", rx=11, ry=12, pupil=("#3A2A4A", "#0A060E"))
    a.circ(100, 98, 4, "#FFFFFF")
    a.circ(90, 100, 3, "#FFFFFF")
    a.circ(110, 100, 3, "#FFFFFF")
    a.mouth(100, 138, "open", w=7, color="#FF8AB0", tongue="#FF5A8A")
    a.cheeks([(74, 134), (126, 134)], "#FF6A9A", rx=6, ry=4, dots=False)
    # top hat
    a.path("M80 92 H120 V86 H80 Z", "#1A1A2A", o, 2)
    a.path("M86 86 V66 H114 V86 Z", "#1A1A2A", o, 2)
    a.path("M86 80 H114 V84 H86 Z", "#FF6A9A", None)
    a.add('<text class="fx" x="150" y="80" font-size="16" font-weight="bold" font-family="sans-serif" fill="#8A78C8">tap!</text>')


@chordoo("wispurr")
def wispurr(a):
    o = "#3A3470"
    a.glow(100, 100, 74, "#D8E0FF", 0.5)
    body = a.shade("#FFFFFF", "#E8ECFF", "#A8B4E8")
    # wispy tail trailing off
    a.path("M128 136 C160 140 176 120 170 96 C166 80 152 78 150 90 C158 92 160 104 154 112 C146 122 132 122 124 120 Z", body, o, 3, ' opacity=".9"')
    # body fading at bottom
    a.path("M56 120 C52 92 72 80 100 80 C128 80 148 92 144 120 C142 140 134 156 120 162 C114 152 108 168 100 160 C92 168 86 152 80 162 C66 156 58 140 56 120 Z", body, o)
    # head
    a.circ(100, 76, 34, body, o)
    a.path("M70 58 L66 26 L90 48 Z", body, o, 3)
    a.path("M130 58 L134 26 L110 48 Z", body, o, 3)
    a.path("M72 52 L70 34 L84 46 Z", "#FFC8E0", None)
    a.path("M128 52 L130 34 L116 46 Z", "#FFC8E0", None)
    a.eyes(76, xs=(86, 114), kind="happy", rx=8)
    a.path("M96 86 L104 86 L100 90 Z", "#FF9AC0")
    a.mouth(100, 92, "cat", w=6, color=o)
    a.cheeks([(76, 90), (124, 90)], "#FFB0D0", rx=6, ry=4)
    for sx in (1, -1):
        for k in (-4, 4):
            a.line(f"M{100 + sx * 18} {88 + k * 0.5} L{100 + sx * 40} {84 + k * 1.5}", o, 1.6, 0.6)
    zz(a, 140, 40, "#A8B4E8")
    a.add('<text class="fx" x="22" y="150" font-size="14" font-weight="bold" font-family="sans-serif" fill="#A8B4E8">purr</text>')


@chordoo("gloomsy")
def gloomsy(a):
    o = "#1E2A4A"
    a.glow(140, 76, 40, "#FFE88A", 0.7)
    a.ground(rx=40)
    ghost_body(a, 36, 168, 50, 150, a.shade("#E8F0FF", "#9AAAD8", "#4A5A98"), o, 5)
    # lantern eye on the right, regular eye left
    a.eye(76, 96, rx=10, ry=12, iris="#9AAAD8", pupil=("#1E2A4A", "#060A14"))
    a.circ(124, 96, 18, "#3A3A5A", o, 3)
    a.circ(124, 96, 13, a.shade("#FFFFF0", "#FFE88A", "#FFB020"), "#8A6A00", 2)
    a.ell(124, 98, 4, 7, "#FF9A20")
    a.ell(124, 99, 2, 4, "#FFFFFF")
    a.line("M124 78 V70 M110 84 L104 78 M138 84 L144 78", "#3A3A5A", 2.5)
    a.mouth(98, 126, "smile", w=8, color=o)
    a.cheeks([(66, 118), (132, 122)], "#C8A8FF", rx=7, ry=4, dots=False)
    # arms holding a teddy (guards your dreams)
    a.circ(100, 150, 12, a.shade("#F0D0B0", "#C89870", "#8A5A3A"), "#4A2A10", 2.5)
    a.circ(91, 140, 5, "#C89870", "#4A2A10", 2)
    a.circ(109, 140, 5, "#C89870", "#4A2A10", 2)
    a.circ(96, 150, 1.5, "#4A2A10")
    a.circ(104, 150, 1.5, "#4A2A10")
    a.path("M70 140 C80 154 90 156 96 154 M130 140 C120 154 110 156 104 154", "none", o, 3)
    for x, y in ((30, 40), (176, 160), (24, 140)):
        star(a, x, y, 6, "#FFE88A", "#8A6A00", 1.2, cls="fx")


@chordoo("hexie")
def hexie(a):
    sk = a.shade("#D8FFB8", "#7AD050", "#3A8A22")
    o = "#1E4A12"
    a.ground(rx=56)
    # cauldron with hot chocolate
    a.path("M120 140 C116 176 176 176 172 140 Z", "#2A2A3A", "#0A0A14", 3)
    a.ell(146, 140, 28, 7, "#8A4A2A", "#0A0A14", 3)
    a.circ(140, 138, 4, "#FFFFFF", "#C8C0B0", 1)
    a.circ(152, 140, 3, "#FFFFFF", "#C8C0B0", 1)
    a.add('<path class="fx" d="M138 128 q-4 -10 2 -16 q6 -6 0 -14 M154 126 q4 -8 -2 -14" stroke="#C8B0A0" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    # frog body sitting
    a.path("M30 150 C26 122 50 106 74 106 C98 106 120 122 116 150 C114 170 96 178 72 178 C48 178 32 170 30 150 Z", sk, o)
    a.ell(72, 154, 24, 18, "#F0FFE0")
    a.ell(42, 176, 14, 6, sk, o, 3)
    a.ell(102, 176, 14, 6, sk, o, 3)
    # stirring arm with spoon
    a.line("M104 132 L136 118", "#C8A070", 4)
    limb(a, "M100 136 C110 132 116 128 120 124", "#7AD050", o, 8)
    # head with big top eyes
    a.path("M30 102 C28 80 46 70 72 70 C98 70 116 80 114 102 C112 120 94 126 72 126 C50 126 32 120 30 102 Z", sk, o)
    a.circ(52, 80, 14, sk, o, 3)
    a.circ(92, 80, 14, sk, o, 3)
    a.eye(52, 82, rx=9, ry=10, iris="#B87AF0", pupil=("#1E1A3A", "#06040E"))
    a.eye(92, 82, rx=9, ry=10, iris="#B87AF0", pupil=("#1E1A3A", "#06040E"))
    a.mouth(72, 108, "smile", w=14, color=o)
    a.cheeks([(42, 106), (102, 106)], rx=7, ry=4)
    # pointy witch hat
    a.path("M36 70 C50 64 94 64 108 70 C94 74 50 74 36 70 Z", "#5A2A8A", "#2A0E4A", 2.5)
    a.path("M52 68 C58 44 64 26 86 10 C80 30 84 50 92 68 Z", a.lin("#8A5AC8", "#4A1E7A"), "#2A0E4A", 2.5)
    a.path("M54 62 H90 V68 H54 Z", "#FFD84D", None)
    star(a, 72, 46, 5, "#FFD84D", "#8A6A00", 1)
    for x, y in ((160, 40), (180, 80)):
        a.sparkle(x, y, 6, "#B87AF0")


@chordoo("vampurr")
def vampurr(a):
    fur = a.shade("#6A5A8A", "#3A2E5A", "#1A1430")
    o = "#0A0618"
    a.ground(rx=56)
    # cape
    a.path("M40 176 C40 130 60 96 100 96 C140 96 160 130 160 176 C140 166 120 176 100 168 C80 176 60 166 40 176 Z", a.lin("#C8203A", "#6A0A1E"), "#3A0410", 3)
    a.path("M62 100 L40 76 L74 92 Z M138 100 L160 76 L126 92 Z", "#2A1430", "#0A0618", 2.5)
    # bat wings peeking
    for sx in (1, -1):
        a.path(f"M{100 + sx * 54} 120 L{100 + sx * 92} 102 L{100 + sx * 84} 120 L{100 + sx * 94} 136 L{100 + sx * 60} 140 Z", "#5A4A7A", o, 2.5)
    # body + glass of tomato juice
    a.path("M74 176 C70 140 80 118 100 118 C120 118 130 140 126 176 Z", fur, o)
    a.path("M112 136 H128 L126 162 H114 Z", "#FFFFFF", "#8A8AA8", 2, ' opacity=".9"')
    a.path("M113 142 H127 L126 162 H114 Z", "#E8303A")
    a.line("M124 132 L130 120", "#5AC8FF", 2.5)
    limb(a, "M84 140 C96 150 106 150 114 148", "#3A2E5A", o, 8)
    # cat head
    a.circ(100, 76, 34, fur, o)
    a.path("M72 56 L66 24 L92 46 Z", fur, o, 3)
    a.path("M128 56 L134 24 L108 46 Z", fur, o, 3)
    a.path("M74 50 L71 34 L84 44 Z", "#FF8AC0", None)
    a.path("M126 50 L129 34 L116 44 Z", "#FF8AC0", None)
    # widow's peak tuft
    a.path("M90 44 L100 58 L110 44", "#1A1430", None)
    a.eyes(76, xs=(86, 114), rx=9, ry=11, iris="#FF5A7A", pupil=("#2A0A1A", "#0A0206"))
    a.path("M96 88 L104 88 L100 92 Z", "#FF8AC0")
    a.mouth(100, 94, "fang", w=7, color="#FFFFFF")
    a.cheeks([(74, 92), (126, 92)], "#FF6A9A", rx=6, ry=4, dots=False)


@chordoo("mummo")
def mummo(a):
    o = "#4A3A2A"
    a.ground(rx=50)
    wrap = a.shade("#FFFFFF", "#F4ECDC", "#C8B8A0")
    rain = ["#FF8AA8", "#FFC86A", "#FFF08A", "#9AE89A", "#8AC8FF", "#C8A8FF"]
    # legs
    for x in (82, 118):
        a.path(f"M{x - 12} 140 L{x - 12} 180 H{x + 12} L{x + 12} 140", wrap, o, 3)
    # body
    a.path("M56 90 C52 70 70 58 100 58 C130 58 148 70 144 90 L144 146 C144 156 130 160 100 160 C70 160 56 156 56 146 Z", wrap, o, 3.5)
    # rainbow bandage stripes
    for i, y in enumerate(range(76, 160, 13)):
        a.path(f"M57 {y} Q100 {y + 8 - (i % 2) * 6} 143 {y - 4}", "none", rain[i % 6], 7)
    for i, y in enumerate((150, 164, 176)):
        a.line(f"M71 {y} L93 {y - 3} M107 {y - 3} L129 {y}", rain[(i + 2) % 6], 6)
    a.path("M56 90 C52 70 70 58 100 58 C130 58 148 70 144 90 L144 146 C144 156 130 160 100 160 C70 160 56 156 56 146 Z", "none", o, 3.5)
    # arms wide for a bear hug
    a.path("M58 96 C36 92 22 76 24 60 C34 58 40 70 56 80", wrap, o, 3)
    a.path("M142 96 C164 92 178 76 176 60 C166 58 160 70 144 80", wrap, o, 3)
    a.line("M30 64 L48 80", rain[0], 5)
    a.line("M170 64 L152 80", rain[4], 5)
    # loose ribbon end
    a.path("M144 130 C160 134 168 148 162 160", "none", rain[3], 6)
    # face gap
    a.path("M70 92 C80 86 120 86 130 92 V110 C120 116 80 116 70 110 Z", "#3A2E40", o, 2.5)
    a.eye(86, 100, rx=7, ry=8, kind="glow", iris="#FFE88A", pupil=("#3A2E40", "#0A0610"))
    a.eye(114, 100, rx=7, ry=8, kind="glow", iris="#FFE88A", pupil=("#3A2E40", "#0A0610"))
    a.mouth(100, 126, "open", w=8, color="#7A3E4E")
    a.cheeks([(72, 124), (128, 124)], rx=7, ry=4)


@chordoo("phantasma")
def phantasma(a):
    o = "#3A1E5A"
    a.glow(100, 96, 96, "#E8C8FF", 0.5)
    a.ground(rx=44)
    # flowing veil
    veil = a.lin("#FFFFFF", "#E8D8FF", "#B898F0")
    a.path("M100 30 C40 40 20 110 30 180 C50 166 60 178 72 168 C70 130 76 80 100 60 C124 80 130 130 128 168 C140 178 150 166 170 180 C180 110 160 40 100 30 Z", veil, o, 3, ' opacity=".9"')
    # ghost body
    ghost_body(a, 52, 172, 64, 136, a.shade("#FFFFFF", "#F4EEFF", "#C0B0E8"), o, 4)
    # crown
    a.path("M76 62 L80 40 L90 54 L100 34 L110 54 L120 40 L124 62 Z", a.lin("#FFF6A8", "#FFC020"), "#8A5A00", 2.5)
    for x, c in ((80, "#C87AFF"), (100, "#FF6AA8"), (120, "#6AC8FF")):
        a.circ(x, 42 if x != 100 else 36, 3, c)
    a.eyes(96, xs=(86, 114), rx=8, ry=10, iris="#B87AF0", pupil=("#2A1A4A", "#0A0614"), lashes=2)
    a.mouth(100, 116, "smile", w=6, color=o)
    a.cheeks([(76, 112), (124, 112)], "#FFA8D8", rx=6, ry=4)
    # party: disco ball + streamers
    a.line("M170 0 V22", "#8A8AA8", 1.5)
    a.circ(170, 32, 11, a.shade("#FFFFFF", "#C8C8E0", "#7A7A9A"), "#4A4A6A", 2)
    a.path("M160 30 H180 M170 21 V43 M162 24 L178 40 M178 24 L162 40", "none", "#FFFFFF", 1, ' opacity=".6"')
    for x, y, c in ((20, 40, "#FF6AA8"), (30, 100, "#FFD84D"), (176, 120, "#6AC8FF")):
        star(a, x, y, 6, c, None, cls="fx")


@chordoo("duskhorn")
def duskhorn(a):
    coat = a.shade("#5A5A8A", "#2A2A54", "#10102A")
    o = "#06061A"
    a.glow(70, 60, 60, "#B8A8FF", 0.4)
    a.ground(rx=70)
    # legs
    for x in (66, 84, 128, 146):
        a.path(f"M{x - 6} 140 L{x - 6} 176 H{x + 6} L{x + 6} 140", coat, o, 3)
        a.path(f"M{x - 7} 172 H{x + 7} V180 H{x - 7} Z", "#B8A8FF", o, 2)
    # body
    a.ell(106, 130, 50, 28, coat, o)
    # starlit tail
    tail = a.lin("#3A2A8A", "#7A5AE8", "#B8A8FF")
    a.path("M152 120 C176 110 192 130 184 160 C178 140 170 136 160 140 C170 150 168 166 156 172 C158 152 150 140 146 132 Z", tail, o, 2.5)
    # neck + head
    a.path("M64 122 C56 100 56 84 60 70 L84 72 C82 88 84 104 90 116 Z", coat, o, 3)
    a.path("M30 70 C28 48 46 36 64 38 C84 40 92 56 88 70 C84 88 66 92 52 92 C38 92 30 82 30 70 Z", coat, o)
    a.ell(40, 80, 10, 8, "#3A3A6A", None)
    a.circ(36, 78, 1.8, "#B8A8FF")
    # glowing horn
    a.path("M58 40 L62 4 L70 40 Z", a.lin("#FFFFFF", "#D8C8FF", "#8A7AE8"), "#3A2A8A", 2.5)
    a.line("M60 32 L68 28 M61 22 L67 18", "#8A7AE8", 1.5)
    a.glow(64, 16, 14, "#FFFFFF", 0.8)
    # starlit mane
    mane = a.lin("#7A5AE8", "#3A2A8A")
    a.path("M70 36 C86 30 100 44 96 60 C104 72 98 86 94 100 C88 88 88 78 84 70 C78 58 68 48 70 36 Z", mane, o, 2.5)
    a.ell(78, 40, 5, 10, coat, o, 2.5, rot=20)
    a.eye(64, 62, rx=7, ry=9, iris="#B8A8FF", pupil=("#1A1A3A", "#06060E"), lashes=2, side=-1, kind="star")
    a.mouth(44, 88, "smile", w=4, color="#B8A8FF")
    # stars sprinkled on mane, tail and body
    for x, y in ((86, 52), (90, 76), (170, 130), (178, 150), (120, 120), (140, 136), (96, 132)):
        star(a, x, y, 3.5, "#FFFFFF", None)
    for x, y in ((150, 40), (180, 70), (20, 130), (120, 20)):
        a.sparkle(x, y, 6, "#D8C8FF")

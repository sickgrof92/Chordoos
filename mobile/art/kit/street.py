import math
from artkit import chordoo, INK
from shapes import limb, star, note, bolt

ST_O = "#1E1A2E"


def skateboard(a, cx, y, w=60, deck="#FF5A8A", o=ST_O):
    a.path(f"M{cx - w} {y} H{cx + w} C{cx + w + 8} {y} {cx + w + 10} {y - 8} {cx + w + 6} {y - 10} L{cx + w} {y - 4} H{cx - w} L{cx - w - 6} {y - 10} C{cx - w - 10} {y - 8} {cx - w - 8} {y} {cx - w} {y} Z", deck, o, 2.5)
    for x in (cx - w * 0.65, cx + w * 0.65):
        a.circ(round(x, 1), y + 7, 6, "#FFD84D", o, 2)


@chordoo("ziggy")
def ziggy(a):
    o = "#5A4200"
    a.ground(rx=56, cy=190)
    skateboard(a, 100, 176, 56, "#3AC8E8")
    body = a.shade("#FFFBD0", "#FFE14D", "#E0A800")
    # zigzag body
    a.path("M54 168 L60 110 L52 96 L66 80 L60 64 C70 50 130 50 140 64 L134 80 L148 96 L140 110 L146 168 Z", body, o, 3.5)
    a.path("M60 120 L80 110 L100 122 L120 110 L140 122", "none", "#E0A800", 4)
    a.path("M60 146 L80 136 L100 148 L120 136 L142 148", "none", "#E0A800", 4)
    # mohawk
    a.path("M76 58 L80 30 L88 50 L94 22 L100 48 L108 20 L112 48 L122 28 L124 58 Z", a.lin("#FF6AB0", "#C82A88"), "#6A0A40", 2.5)
    a.eyes(88, xs=(84, 116), rx=9, ry=11, iris="#FF6AB0", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(100, 104, "grin", w=8, color=o)
    a.cheeks([(70, 100), (130, 100)], "#FF8A6A", rx=6, ry=4)
    # arms out for balance
    limb(a, "M60 110 L34 98", "#FFE14D", o, 9)
    limb(a, "M140 110 L166 120", "#FFE14D", o, 9)
    for d in ("M10 150 H32", "M14 160 H30", "M168 150 H188"):
        a.line(d, "#C8C0D8", 3, 0.8)


@chordoo("graffito")
def graffito(a):
    fur = a.shade("#D8D8E0", "#8A8A9A", "#4A4A5A")
    o = ST_O
    # wall behind with mural
    a.path("M0 30 H200 V150 H0 Z", "#E8E0D8", None, extra=' class="fx"')
    a.add('<path class="fx" d="M20 120 C30 60 70 50 90 80 C110 40 150 50 160 100" stroke="#FF6AB0" stroke-width="10" fill="none" stroke-linecap="round"/>')
    a.add('<path class="fx" d="M130 60 l10 20 l14 -24" stroke="#3AC8E8" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    a.ground(rx=56)
    # striped tail
    for i in range(5):
        a.ell(150 + i * 6, 156 - i * 10, 10, 8, "#4A4A5A" if i % 2 else "#C8C8D0", o, 2.5, rot=-50)
    # body
    a.path("M56 154 C52 124 74 110 100 110 C126 110 148 124 144 154 C142 174 124 182 100 182 C76 182 58 174 56 154 Z", fur, o)
    a.path("M82 148 C82 132 118 132 118 148 C118 166 110 174 100 174 C90 174 82 166 82 148 Z", "#E8E8EE")
    # head with bandit mask
    a.path("M52 80 C52 58 72 46 100 46 C128 46 148 58 148 80 C148 104 128 116 100 116 C72 116 52 104 52 80 Z", fur, o)
    a.path("M60 46 L58 20 L82 40 Z M140 46 L142 20 L118 40 Z", fur, o, 3)
    a.path("M56 78 C64 66 92 66 100 76 C108 66 136 66 144 78 C138 92 112 94 100 86 C88 94 62 92 56 78 Z", "#2A2A3A")
    a.eyes(80, xs=(80, 120), rx=8, ry=10, kind="white", pupil=("#3A3A5A", "#0A0A14"))
    a.path("M82 96 C86 90 114 90 118 96 C114 108 86 108 82 96 Z", "#F4F4F8")
    a.circ(100, 96, 4, o)
    a.mouth(100, 102, "smile", w=6, color=o)
    # paint splatters on fur
    for x, y, c in ((70, 140, "#FF6AB0"), (126, 132, "#3AC8E8"), (88, 60, "#FFD84D"), (116, 164, "#8AE06A")):
        a.circ(x, y, 5, c)
        a.circ(x + 6, y - 4, 2, c)
    # spray can
    limb(a, "M140 130 L156 116", "#8A8A9A", o, 9)
    a.path("M154 88 H170 V116 H154 Z", a.lin("#FF6AB0", "#C82A88", x2=1, y2=0), o, 2.5)
    a.path("M158 82 H166 V88 H158 Z", "#C8CCD8", o, 2)


@chordoo("beatbox")
def beatbox(a):
    o = ST_O
    a.ground(rx=56)
    # legs dancing
    limb(a, "M76 150 L66 178", "#3A3A4A", o, 9)
    limb(a, "M124 150 L140 170 L150 168", "#3A3A4A", o, 9)
    a.path("M54 176 H74 V184 H54 Z", "#FF5A6A", o, 2)
    a.path("M146 162 H164 V170 H146 Z", "#FF5A6A", o, 2)
    # boombox body
    a.path("M30 70 H170 V152 H30 Z", a.lin("#7A5AE8", "#4A2AA8"), o, 3.5)
    a.path("M60 50 H140 V70", "none", "#C8CCD8", 5)
    # speakers = eyes
    for x in (64, 136):
        a.circ(x, 112, 28, "#2A2A3A", o, 3)
        a.circ(x, 112, 22, a.shade("#5A5A7A", "#2A2A3A", "#0A0A14"))
        a.circ(x, 112, 10, "#FFFFFF")
        a.circ(x + 2, 112, 6, "#141420")
        a.circ(x + 4, 108, 3, "#FFFFFF")
    # tape deck smile
    a.path("M84 96 H116 V128 H84 Z", "#C8C8E8", o, 2.5)
    a.path("M88 116 Q100 126 112 116", "none", o, 2.5)
    a.circ(92, 106, 4, "none", o, 2)
    a.circ(108, 106, 4, "none", o, 2)
    for x, c in ((44, "#FF5A6A"), (54, "#FFD84D"), (146, "#6AE8A0"), (156, "#3AC8E8")):
        a.circ(x, 80, 3.5, c)
    a.cheeks([(36, 140), (164, 140)], "#FF8AC0", rx=6, ry=4, dots=False)
    note(a, 20, 50, 1, "#7A5AE8", double=True)
    note(a, 176, 40, 1, "#FF5AB0")
    for d in ("M10 108 l-6 0", "M190 108 l6 0"):
        a.line(d, "#7A5AE8", 3)


@chordoo("hoopster")
def hoopster(a):
    o = "#5A2400"
    a.ground(rx=46)
    # legs + sneakers
    for x in (86, 114):
        limb(a, f"M{x} 146 L{x} 172", "#FFD8B8", "#8A4A2A", 9)
        a.path(f"M{x - 12} 172 H{x + 12} C{x + 16} 172 {x + 16} 182 {x + 12} 182 H{x - 12} Z", "#FFFFFF", o, 2)
        a.line(f"M{x - 8} 176 H{x + 6}", "#E8303A", 2)
    # jersey shorts
    a.path("M74 132 H126 L130 156 H70 Z", "#3A5AE8", "#1E2A7A", 2.5)
    # basketball body
    ball = a.shade("#FFD8A8", "#FF8A2A", "#C8500A")
    a.circ(100, 94, 52, ball, o, 3.5)
    a.path("M48 94 H152 M100 42 V146", "none", o, 2.5)
    a.path("M64 54 C80 74 80 114 64 134 M136 54 C120 74 120 114 136 134", "none", o, 2.5)
    a.path("M70 106 C76 92 124 92 130 106 V114 C124 104 76 104 70 114 Z", "#FFFFFF", None, extra=' opacity="0"')
    # headband
    a.path("M54 62 C80 50 120 50 146 62 L148 72 C120 60 80 60 52 72 Z", "#FFFFFF", "#3A5AE8", 2)
    a.eyes(88, xs=(84, 116), rx=9, ry=11, iris="#FF8A2A", pupil=("#2A1A0A", "#0A0602"), kind="star")
    a.mouth(100, 112, "grin", w=8, color=o)
    a.cheeks([(70, 108), (130, 108)], "#FF6A5A", rx=6, ry=4)
    # arm shooting a tiny ball into a hoop
    limb(a, "M146 86 L166 62", "#FFD8B8", "#8A4A2A", 8)
    a.circ(170, 54, 7, ball, o, 2)
    a.path("M150 22 H190 V26 H150 Z", "#E8303A", "#6A0A14", 1.5)
    a.path("M154 26 L160 40 H180 L186 26", "none", "#FFFFFF", 1.6)
    a.add('<path class="fx" d="M170 46 C168 36 166 32 168 28" stroke="#FF8A2A" stroke-width="2" fill="none" stroke-dasharray="3 4"/>')


@chordoo("skaterpillar")
def skaterpillar(a):
    o = "#1E4A12"
    a.ground(rx=76, cy=190)
    skateboard(a, 100, 172, 72, "#FF8A2A")
    sk = a.shade("#E8FFC8", "#8AE05A", "#3E9A2A")
    # segments riding
    segs = [(40, 152, 16), (62, 150, 17), (86, 148, 18), (110, 146, 18)]
    for i, (x, y, r) in enumerate(segs):
        a.circ(x, y, r, sk, o, 3)
        a.circ(x, y - r + 4, 3, "#FFD84D")
        a.line(f"M{x - 6} {y + r - 4} l-2 8 M{x + 6} {y + r - 4} l2 8", o, 3)
    # head popped up
    a.circ(140, 120, 30, sk, o)
    a.line("M128 92 C122 74 114 70 108 72 M152 92 C158 74 166 70 172 72", o, 2.5)
    a.circ(108, 72, 4, "#FF8A2A", o, 1.5)
    a.circ(172, 72, 4, "#FF8A2A", o, 1.5)
    # backwards cap
    a.path("M112 108 C112 86 168 86 168 108 Z", a.lin("#3AC8E8", "#1E78C0"), "#0E3A6A", 2.5)
    a.path("M108 106 L96 112 L112 112 Z", "#1E78C0", "#0E3A6A", 2)
    a.eyes(122, xs=(130, 152), rx=7, ry=9, iris="#8AE05A", pupil=("#1A2A1A", "#060A06"))
    a.mouth(142, 138, "open", w=7, color="#5A1A2A")
    a.cheeks([(120, 136), (162, 134)], rx=5, ry=3, dots=False)
    # ollie twig + motion lines
    a.line("M20 184 L44 180", "#8A5A2A", 4)
    for d in ("M4 140 H22", "M6 156 H20"):
        a.line(d, "#C8C0D8", 3, 0.8)


@chordoo("djdoodle")
def djdoodle(a):
    fur = a.shade("#FFFFFF", "#FFE8F4", "#E8B0D0")
    o = "#5A1A4A"
    a.ground(rx=66)
    # turntable deck in front
    a.path("M14 150 H186 V186 H14 Z", a.lin("#3A3A4A", "#1A1A24"), ST_O, 3)
    for x in (60, 140):
        a.ell(x, 150, 34, 10, "#1A1A24", ST_O, 2.5)
        a.ell(x, 150, 10, 3, "#FF6AB0")
    a.line("M88 166 H112", "#6AE8A0", 4)
    a.circ(100, 176, 4, "#FFD84D")
    # poodle body behind deck (fluffy puffs)
    for cx, cy, r in ((70, 136, 20), (100, 128, 24), (130, 136, 20)):
        a.circ(cx, cy, r, fur, o, 3)
    # paws scratching records
    a.circ(60, 144, 10, fur, o, 2.5)
    a.circ(140, 144, 10, fur, o, 2.5)
    # head
    a.circ(100, 86, 30, fur, o)
    a.circ(100, 54, 16, fur, o, 3)
    for x, y in ((90, 46), (110, 46), (100, 40)):
        a.circ(x, y, 8, fur)
    # ears as puffs (under headphones)
    a.circ(66, 96, 16, fur, o, 3)
    a.circ(134, 96, 16, fur, o, 3)
    # headphones
    a.path("M70 80 C70 46 130 46 130 80", "none", ST_O, 6)
    for x in (68, 132):
        a.ell(x, 86, 9, 13, a.lin("#FF6AB0", "#C82A88"), ST_O, 2.5)
    a.eyes(84, xs=(88, 112), kind="happy", rx=7)
    a.ell(100, 100, 6, 4, o)
    a.mouth(100, 104, "open", w=6, color="#7A2A4A")
    a.cheeks([(82, 98), (118, 98)], "#FF8AC0", rx=5, ry=3, dots=False)
    note(a, 20, 60, 1, "#FF6AB0")
    note(a, 172, 50, 1, "#3AC8E8", double=True)


@chordoo("spinz")
def spinz(a):
    fur = a.shade("#FFF0DC", "#E8C49A", "#A87A50")
    o = "#3A2410"
    a.ground(rx=46)
    # spin swirl around it
    a.ell(100, 120, 84, 22, "none", "#C8C0D8", 3, rot=-8, extra=' class="fx" stroke-dasharray="14 10"')
    # quills: spiky crown fanned behind, tipped in neon
    q = a.lin("#8A6A4A", "#4A3420")
    for i in range(11):
        ang = -170 + i * 16
        a.add(f'<g transform="translate(100 104) rotate({ang})"><path d="M0 -10 L60 0 L0 10 Z" fill="{q}" stroke="{o}" stroke-width="2.2" stroke-linejoin="round"/>'
              f'<path d="M44 -3 L60 0 L44 3 Z" fill="#3AC8E8"/></g>')
    # body
    a.circ(100, 112, 40, fur, o)
    a.ell(100, 124, 26, 22, "#FFF8EC", None)
    # one leg planted (spinning on a toe), one kicked out
    limb(a, "M92 148 L90 176", "#E8C49A", o, 10)
    a.ell(92, 180, 12, 6, "#FFFFFF", o, 2.5)
    a.line("M86 180 H98", "#3AC8E8", 2.5)
    limb(a, "M114 144 L150 156", "#E8C49A", o, 10)
    a.ell(156, 158, 12, 7, "#FFFFFF", o, 2.5, rot=20)
    a.line("M150 156 l10 4", "#FF5AB0", 2.5)
    # arms out wide for the spin
    limb(a, "M62 108 L30 96", "#E8C49A", o, 9)
    limb(a, "M138 108 L170 92", "#E8C49A", o, 9)
    # face
    a.eyes(106, xs=(86, 114), kind="happy", rx=8)
    a.ell(100, 120, 5, 4, "#3A2010")
    a.mouth(100, 126, "open", w=6, color="#7A3E2E")
    a.cheeks([(76, 120), (124, 120)], rx=6, ry=4)
    # backwards cap
    a.path("M72 84 C74 64 126 64 128 84 Z", "#E8303A", "#6A0A14", 2.5)
    a.path("M126 82 L144 78 L140 86 L126 86 Z", "#E8303A", "#6A0A14", 2)
    for d in ("M20 140 q-6 -10 0 -20", "M184 136 q6 -10 0 -20"):
        a.add(f'<path class="fx" d="{d}" stroke="#C8C0D8" stroke-width="3" fill="none" stroke-linecap="round"/>')


@chordoo("rexykicks")
def rexykicks(a):
    sk = a.shade("#C8F0E0", "#5ACCA0", "#1E8A6A")
    o = "#0E3A2A"
    a.ground(rx=60)
    # tail
    a.path("M130 136 C160 140 182 128 194 110 C176 114 158 116 140 116 Z", sk, o, 3)
    # big legs with high-tops
    for x in (80, 118):
        a.path(f"M{x - 13} 128 L{x - 13} 158 H{x + 13} L{x + 13} 128", sk, o, 3)
        a.path(f"M{x - 15} 152 H{x + 13} L{x + 14} 172 C{x + 22} 172 {x + 24} 182 {x + 18} 184 H{x - 15} Z", "#FFFFFF", ST_O, 2.5)
        a.path(f"M{x - 15} 152 H{x + 13} V160 H{x - 15} Z", "#E8303A", ST_O, 2)
        a.line(f"M{x - 15} 180 H{x + 20}", "#3A3A4A", 3)
        for k in range(3):
            a.line(f"M{x - 6} {164 + k * 4} H{x + 6}", "#3A3A4A", 1.4)
    # body
    a.path("M60 130 C56 100 70 80 100 80 C130 80 144 100 140 130 C138 146 122 150 100 150 C78 150 62 146 60 130 Z", sk, o)
    a.path("M80 132 C78 108 88 96 100 96 C112 96 122 108 120 132 Z", "#E8FFF4", None)
    # tiny arms
    limb(a, "M70 104 L58 112", "#5ACCA0", o, 8)
    limb(a, "M130 104 L142 112", "#5ACCA0", o, 8)
    # head
    a.path("M54 60 C52 32 78 20 104 22 C134 24 152 40 150 62 C148 84 126 92 100 92 C74 92 56 84 54 60 Z", sk, o)
    for x in (76, 94, 112):
        a.path(f"M{x} 26 L{x + 6} 14 L{x + 12} 26 Z", "#FFD84D", o, 2)
    a.eyes(54, xs=(84, 116), rx=9, ry=11, iris="#5ACCA0", pupil=("#0E2A1E", "#020A06"))
    a.mouth(100, 74, "grin", w=10, color=o)
    a.cheeks([(68, 70), (132, 70)], "#FF9AA8", rx=6, ry=4)
    for d in ("M20 160 l-8 -4", "M24 172 l-10 0", "M172 168 l10 -4"):
        a.line(d, "#C8C0D8", 3, 0.8)


@chordoo("neonninja")
def neonninja(a):
    sk = a.shade("#C8F0B8", "#5AB84A", "#2A7A2A")
    o = "#0A1A0A"
    a.ground(rx=46)
    # crouched frog ninja, dark suit
    suit = a.shade("#5A5A7A", "#2A2A40", "#10101C")
    a.ell(66, 170, 22, 10, sk, o, 3)
    a.ell(134, 170, 22, 10, sk, o, 3)
    a.path("M52 150 C48 116 70 100 100 100 C130 100 152 116 148 150 C146 170 126 176 100 176 C74 176 54 170 52 150 Z", suit, o)
    a.path("M72 128 H128 V136 H72 Z", "#2A2A40", None)
    # sneaking arms: one with cookie
    limb(a, "M58 126 C42 120 36 110 36 100", "#5AB84A", o, 9)
    a.circ(34, 92, 12, a.lin("#E8B070", "#A86A2A"), "#5A3410", 2.5)
    for x, y in ((30, 88), (38, 94), (32, 98)):
        a.circ(x, y, 2, "#4A2A10")
    limb(a, "M142 126 C156 132 160 140 158 150", "#5AB84A", o, 9)
    # head: frog with eye bumps
    a.path("M48 90 C46 64 70 52 100 52 C130 52 154 64 152 90 C150 108 130 118 100 118 C70 118 50 108 48 90 Z", sk, o)
    a.circ(74, 60, 16, sk, o, 3)
    a.circ(126, 60, 16, sk, o, 3)
    # mask band (dark) across the face
    a.path("M48 80 C70 72 130 72 152 80 V96 C130 90 70 90 48 96 Z", suit, o, 2)
    # glow headband with tails
    gb = a.lin("#6AFFE8", "#FF6AD8", x2=1, y2=0)
    a.path("M52 70 C74 62 126 62 148 70 L148 78 C126 70 74 70 52 78 Z", gb, o, 2)
    a.path("M150 72 C166 64 178 70 186 60 M150 76 C168 76 178 84 190 80", "none", "#6AFFE8", 4)
    a.glow(100, 70, 40, "#6AFFE8", 0.4)
    a.eye(74, 60, rx=8, ry=9, iris="#6AFFE8", pupil=("#0A1A1A", "#020606"))
    a.eye(126, 60, rx=8, ry=9, iris="#6AFFE8", pupil=("#0A1A1A", "#020606"))
    a.mouth(100, 104, "smirk", w=12, color=o)
    a.cheeks([(64, 104), (136, 104)], "#FF8AC0", rx=6, ry=3, dots=False)
    a.add('<text class="fx" x="16" y="56" font-size="14" font-weight="bold" font-family="sans-serif" fill="#8AA0C8">shh</text>')


@chordoo("majormuffin")
def majormuffin(a):
    o = "#4A2408"
    a.ground(rx=50)
    # cape flowing
    a.path("M64 96 C40 120 26 160 20 182 C50 172 70 182 100 176 C130 182 150 172 180 182 C174 160 160 120 136 96 Z", a.lin("#E8303A", "#8A0A1E"), "#4A0410", 3)
    # wrapper body
    a.path("M58 108 H142 L132 172 H68 Z", a.lin("#3A8AE8", "#1E4AA8"), "#0E2A6A", 3)
    for x in range(66, 140, 10):
        a.line(f"M{x} 110 L{x + (100 - x) * 0.12:.0f} 170", "#0E2A6A", 1.4, 0.5)
    # emblem
    a.path("M86 124 H114 L118 132 L100 156 L82 132 Z", "#FFD84D", "#8A5A00", 2.5)
    a.add('<text x="93" y="144" font-size="16" font-weight="bold" font-family="sans-serif" fill="#E8303A">M</text>')
    # legs + boots
    for x in (84, 116):
        limb(a, f"M{x} 170 L{x} 178", "#E8B070", o, 8)
        a.path(f"M{x - 10} 176 H{x + 10} V184 H{x - 10} Z", "#E8303A", "#4A0410", 2)
    # muffin top head
    top = a.shade("#F8D8A8", "#D8A060", "#9A6020")
    a.path("M44 104 C30 98 36 70 54 66 C56 40 82 30 100 36 C118 30 144 40 146 66 C164 70 170 98 156 104 C130 114 70 114 44 104 Z", top, o, 3.5)
    for x, y in ((66, 60), (90, 48), (118, 52), (136, 70), (78, 78), (124, 80)):
        a.ell(x, y, 4, 5, "#5A2A8A")
    # mask
    a.path("M62 82 C74 74 126 74 138 82 C136 96 116 98 100 92 C84 98 64 96 62 82 Z", "#E8303A", "#4A0410", 2)
    a.eyes(86, xs=(84, 116), kind="white", rx=8, ry=8, pupil=("#3A2A1A", "#0A0806"))
    a.mouth(100, 100, "grin", w=7, color=o)
    # arm raised in fist
    limb(a, "M140 116 C156 104 164 86 162 66", "#E8B070", o, 10)
    a.circ(162, 60, 9, "#E8303A", "#4A0410", 2.5)
    limb(a, "M60 116 C50 126 48 138 52 148", "#E8B070", o, 10)
    a.circ(52, 152, 8, "#E8303A", "#4A0410", 2.5)
    for x, y in ((178, 40), (150, 24), (24, 60)):
        a.sparkle(x, y, 6)


@chordoo("rockstarling")
def rockstarling(a):
    feat = a.shade("#5A5A7A", "#2A2A44", "#10101C")
    o = "#06060E"
    a.glow(100, 100, 92, "#FF8AD8", 0.35)
    a.ground(rx=56)
    # stage lights
    a.path("M30 0 L70 200 H90 Z", "#FFF6A8", None, extra=' class="fx" opacity=".25"')
    a.path("M170 0 L130 200 H110 Z", "#A8E8FF", None, extra=' class="fx" opacity=".25"')
    # legs + boots
    for x, d in ((86, -1), (114, 1)):
        a.line(f"M{x} 150 L{x + d * 8} 176", "#FFB030", 4)
        a.path(f"M{x + d * 8 - 9} 174 H{x + d * 8 + 9} V184 H{x + d * 8 - 9} Z", "#1A1A2A", o, 2)
    # body + leather vest
    a.ell(100, 124, 36, 34, feat, o)
    a.path("M76 104 C84 98 116 98 124 104 L120 150 H80 Z", "#1A1A2A", o, 2)
    a.path("M92 104 L100 140 L108 104", "#FFF0F8", None)
    for x, y in ((82, 116), (118, 116), (84, 132), (116, 132)):
        a.circ(x, y, 2, "#C8CCD8")
    # electric guitar (star-shaped body) across
    a.path("M60 150 L150 84", "#3A2A1A", 7)
    a.path("M146 86 L170 68 L176 76 L152 92 Z", "#1A1A2A", o, 2)
    for k in range(3):
        a.line(f"M{156 + k * 6} {74 + k * -4} l3 -4", "#C8CCD8", 2)
    star(a, 70, 144, 28, a.lin("#FF6AD8", "#8A2AE8"), o, 3, rot=15, inner=0.55)
    a.circ(70, 144, 5, "#FFFFFF", o, 1.5)
    a.line("M64 150 L150 86", "#E8E8F0", 1, 0.8)
    # wing strumming
    a.path("M130 114 C150 118 160 134 150 146 C140 140 130 130 126 122 Z", feat, o, 3)
    # head with spiky crest
    a.circ(100, 76, 30, feat, o)
    a.path("M78 56 L70 26 L88 46 L92 14 L102 44 L114 18 L114 48 L130 30 L124 58 Z", a.lin("#FF6AD8", "#8A2AE8"), "#3A0A4A", 2.5)
    # star sunglasses
    star(a, 88, 78, 12, a.lin("#FFE84D", "#FF9A20"), o, 2)
    star(a, 112, 78, 12, a.lin("#FFE84D", "#FF9A20"), o, 2)
    a.line("M98 78 H102", o, 2.5)
    a.mouth(100, 96, "beak", w=7)
    a.cheeks([(76, 92), (124, 92)], "#FF6AD8", rx=5, ry=3, dots=False)
    bolt(a, 176, 120, 0.6, 20, cls="fx")
    bolt(a, 24, 100, 0.6, -20, cls="fx")
    note(a, 160, 160, 1, "#FF6AD8", double=True)

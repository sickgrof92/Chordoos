from artkit import chordoo, INK
from shapes import limb, star

ROCK = ("#E0DCD4", "#A49C90", "#6A6258")
ROCK_O = "#3A342C"


def gem(a, x, y, s, light, mid, dark, o="#3A1A5A", rot=0, w=2.2):
    """Faceted gem (hexagonal crystal point) centred at x,y."""
    a.add(f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
          f'<path d="M0 -14 L8 -6 L8 8 L0 14 L-8 8 L-8 -6 Z" fill="{mid}" stroke="{o}" stroke-width="{w / s:.2f}" stroke-linejoin="round"/>'
          f'<path d="M0 -14 L8 -6 L0 -2 L-8 -6 Z" fill="{light}"/>'
          f'<path d="M0 -2 L8 -6 L8 8 L0 14 Z" fill="{dark}" opacity=".7"/>'
          f'<path d="M0 -14 L8 -6 L8 8 L0 14 L-8 8 L-8 -6 Z" fill="none" stroke="{o}" stroke-width="{w / s:.2f}" stroke-linejoin="round"/></g>')


def spire(a, x, y, w, h, light, mid, dark, o, rot=0, sw=2.5):
    """Tall crystal point growing up from (x, y)."""
    a.add(f'<g transform="rotate({rot} {x} {y})">'
          f'<path d="M{x - w / 2} {y} L{x - w / 2} {y - h * 0.7} L{x} {y - h} L{x + w / 2} {y - h * 0.7} L{x + w / 2} {y} Z" fill="{mid}" stroke="{o}" stroke-width="{sw}" stroke-linejoin="round"/>'
          f'<path d="M{x} {y - h} L{x + w / 2} {y - h * 0.7} L{x + w / 2} {y} L{x} {y} Z" fill="{dark}" opacity=".55"/>'
          f'<path d="M{x - w / 2 + 3} {y - h * 0.65} L{x - w / 2 + 3} {y - 6}" stroke="{light}" stroke-width="2.5" stroke-linecap="round"/>'
          f'<path d="M{x - w / 2} {y} L{x - w / 2} {y - h * 0.7} L{x} {y - h} L{x + w / 2} {y - h * 0.7} L{x + w / 2} {y} Z" fill="none" stroke="{o}" stroke-width="{sw}" stroke-linejoin="round"/></g>')


@chordoo("pebble")
def pebble(a):
    a.ground(rx=56)
    a.path("M36 140 C30 104 62 84 100 84 C140 84 172 104 164 142 C160 168 132 180 100 180 C66 180 40 166 36 140 Z", a.shade("#F0ECE4", "#B8B0A2", "#7A7266"), ROCK_O)
    for x, y, r in ((60, 150, 4), (142, 132, 3), (120, 166, 5), (76, 112, 3)):
        a.circ(x, y, r, "#8A8276", extra=' opacity=".5"')
    # moss hat with tiny sprout
    a.path("M58 96 C62 72 82 62 100 62 C120 62 138 72 142 96 C134 92 128 100 120 96 C112 92 104 102 96 96 C88 92 80 102 72 96 C66 92 62 100 58 96 Z",
           a.lin("#B8E87A", "#5EA83A"), "#2A5A1E", 3)
    a.line("M100 62 V48", "#3E8A2E", 3)
    a.ell(93, 46, 7, 4, "#7CC850", "#2A5A1E", 1.8, rot=-30)
    a.ell(107, 46, 7, 4, "#7CC850", "#2A5A1E", 1.8, rot=30)
    a.eyes(128, xs=(80, 120), rx=6, ry=7, kind="dot", pupil=("#2A241C", "#2A241C"))
    a.mouth(100, 146, "smile", w=6, color=ROCK_O)
    a.cheeks([(64, 140), (136, 140)], "#FFA8A8", rx=10, ry=6)
    a.gloss(64, 112, 10, 5)


@chordoo("gemmy")
def gemmy(a):
    fur = a.shade("#FFF4EC", "#F0CDB4", "#B88A6A")
    o = "#4A2E1E"
    a.ground(rx=60)
    # tail wag
    a.path("M148 132 C162 122 166 108 160 98", "none", o, 9)
    a.path("M148 132 C162 122 166 108 160 98", "none", "#F0CDB4", 5)
    gem(a, 160, 94, 0.6, "#FFE8F8", "#FF6AC8", "#B02A88")
    # body
    a.path("M54 146 C50 122 72 110 104 110 C136 110 156 120 154 146 C152 166 132 170 104 170 C76 170 56 166 54 146 Z", fur, o)
    for x, y, c in ((96, 128, ("#E8FFFF", "#4AD8E8", "#1A8A9A")), (124, 136, ("#F4E8FF", "#A86AF0", "#5A2AA8")), (138, 122, ("#FFF4D0", "#FFC83A", "#B87A00"))):
        gem(a, x, y, 0.55, *c)
    # paws dirty from digging
    for x in (68, 92, 122, 142):
        a.ell(x, 172, 11, 8, "#B88A6A", o, 3)
    # head
    a.circ(64, 96, 38, fur, o)
    a.path("M30 78 C16 82 14 112 26 122 C34 112 36 96 36 84 Z", "#B88A6A", o, 3)
    a.path("M96 72 C112 70 118 100 108 112 C102 100 96 88 92 80 Z", "#B88A6A", o, 3)
    gem(a, 64, 64, 0.5, "#E8FFFF", "#4AD8E8", "#1A8A9A")
    a.ell(64, 112, 16, 11, "#FFFFFF", o, 2)
    a.ell(64, 106, 6, 4, "#3A2010")
    a.mouth(64, 114, "open", w=6, color="#7A3E2E")
    a.eyes(92, xs=(50, 78), rx=8, ry=10, iris="#A86AF0", pupil=("#2A1808", "#0A0602"))
    a.cheeks([(38, 106), (90, 106)], rx=6, ry=4, dots=False)
    a.sparkle(30, 40, 6)
    a.sparkle(110, 46, 4)


@chordoo("quartzy")
def quartzy(a):
    shell = a.shade("#FFF0F8", "#FFB0D8", "#D06AA8")
    o = "#6A1A4A"
    a.ground(rx=66)
    # legs (sideways walker)
    for x, d in ((50, -1), (62, -1), (138, 1), (150, 1)):
        a.line(f"M{x} 150 L{x + d * 16} 164 L{x + d * 20} 182", o, 4)
    # claws raised
    for sx in (1, -1):
        cx = 100 + sx * 72
        limb(a, f"M{100 + sx * 40} 130 C{100 + sx * 56} 120 {cx} 110 {cx} 96", "#FF8AC0", o, 9)
        a.path(f"M{cx} 100 C{cx - 16} 90 {cx - 14} 66 {cx} 62 C{cx - 2} 74 {cx + 4} 80 {cx + 6} 84 "
               f"C{cx + 12} 76 {cx + 14} 66 {cx + 12} 62 C{cx + 22} 70 {cx + 18} 96 {cx} 100 Z", "#FF8AC0", o, 3)
    # body
    a.ell(100, 140, 52, 28, shell, o)
    # crystal shell cluster on top
    for x, w, h, r in ((72, 16, 40, -20), (88, 18, 56, -8), (106, 20, 64, 4), (124, 16, 46, 16), (138, 12, 30, 28)):
        spire(a, x, 126, w, h, "#FFFFFF", "#F4E6FF", "#B8A0E8", "#5A3A8A", r, 2.5)
    # eyes on stalks
    for x in (84, 116):
        a.line(f"M{x} 128 V112", o, 3)
        a.circ(x, 106, 10, "#FFFFFF", o, 2.5)
        a.eye(x, 107, rx=6, ry=7, iris="#FF8AC0", pupil=("#3A0A2A", "#12030E"))
    a.mouth(100, 148, "smile", w=8, color=o)
    a.cheeks([(72, 146), (128, 146)], "#FF6AA8", rx=7, ry=4, dots=False)


@chordoo("rubbles")
def rubbles(a):
    rock = a.shade(*ROCK)
    o = ROCK_O
    a.ground(rx=46)
    # legs
    for x in (82, 118):
        a.path(f"M{x - 11} 150 L{x - 12} 178 H{x + 12} L{x + 11} 150 Z", rock, o, 3)
    # body: chunky angular rock
    a.path("M56 88 L78 62 L124 58 L148 82 L150 132 L130 156 L74 158 L52 134 Z", rock, o, 3.5)
    a.path("M78 62 L124 58 L112 74 L86 76 Z", "#F0ECE4", None, extra=' opacity=".6"')
    a.line("M130 156 L124 120 L150 104", "#6A6258", 2, 0.6)
    a.line("M60 120 L74 112", "#6A6258", 2, 0.6)
    # hard hat
    a.path("M66 64 C66 34 134 34 134 64 Z", a.lin("#FFE84D", "#FFB020"), "#8A5A00", 3)
    a.path("M58 64 H142 V72 H58 Z", "#FFB020", "#8A5A00", 3)
    a.line("M100 38 V64", "#8A5A00", 2.5)
    a.eyes(98, xs=(84, 116), rx=9, ry=11, iris="#FFB020", pupil=("#2A241C", "#0A0806"))
    a.mouth(100, 120, "grin", w=8, color=o)
    a.cheeks([(70, 116), (130, 116)], rx=7, ry=4)
    # arm holding pickaxe
    limb(a, "M148 112 C160 114 166 104 166 94", "#A49C90", o, 11)
    a.line("M150 150 L176 60", "#8A5A2A", 6)
    a.path("M150 60 C164 50 186 50 198 62 C186 58 176 60 168 66 Z", "#C8CCD8", "#3A3A4A", 3)
    limb(a, "M54 112 C42 118 38 132 44 142", "#A49C90", o, 11)


@chordoo("opalynn")
def opalynn(a):
    o = "#3A2A5A"
    a.ground(rx=66)
    # rainbow trail
    for i, c in enumerate(("#FF8AA8", "#FFD84D", "#8AE08A", "#6AC8FF", "#B89AF0")):
        a.line(f"M14 {170 + i * 3} H60", c, 3, 0.8)
    # body foot
    skin = a.shade("#E8F8F0", "#A8E0C8", "#5AA890")
    a.path("M40 176 C40 160 60 154 90 154 H150 C170 154 178 130 170 110 C178 96 190 100 190 120 C190 156 172 180 140 180 H50 Z", skin, o)
    # opal shell
    shell = a.shade("#FFFFFF", "#E8F0FF", "#B8C8F0")
    a.circ(98, 112, 46, shell, o, 3.5)
    # opal color flecks
    for x, y, c in ((80, 96, "#FF8AC8"), (112, 90, "#6AE8D8"), (120, 120, "#FFD84D"), (84, 128, "#8AB8FF"), (100, 108, "#C89AFF")):
        a.ell(x, y, 10, 6, c, rot=(x * 7) % 60 - 30, extra=' opacity=".75"')
    a.line("M98 112 C98 98 112 94 118 104 C124 116 110 130 96 128 C78 124 74 102 86 90 C100 76 128 80 136 100", o, 2.5, 0.7)
    a.gloss(74, 82, 12, 6)
    # head + stalk eyes
    for x, ln in ((172, 14), (186, 10)):
        a.line(f"M{x} 104 L{x + 2} {104 - ln - 10}", o, 3)
    a.eye(174, 76, rx=6, ry=8, iris="#6AE8D8", pupil=("#1A1A3A", "#06060E"))
    a.eye(188, 82, rx=5, ry=7, iris="#6AE8D8", pupil=("#1A1A3A", "#06060E"))
    a.mouth(178, 130, "smile", w=6, color=o)
    a.cheeks([(170, 122)], "#FF9AC8", rx=5, ry=3, dots=False)
    a.sparkle(40, 60, 6, "#FFFFFF")
    a.sparkle(150, 40, 5, "#C89AFF")


@chordoo("boulderdash")
def boulderdash(a):
    shell = a.shade("#E8DCC8", "#B09A78", "#6E5A3E")
    o = "#3A2A18"
    a.ground(cx=110, rx=50)
    # motion lines + slope
    a.line("M0 190 L200 170", "#C8B89A", 3, 0.6)
    for y in (100, 120, 140):
        a.line(f"M8 {y} H40", "#C8B89A", 3, 0.8)
    # rolled-up ball
    a.circ(110, 120, 60, shell, o)
    for r in (46, 30):
        a.add(f'<path d="M{110 - r} 120 A{r} {r} 0 0 1 {110 + r} 120" fill="none" stroke="{o}" stroke-width="3" opacity=".6"/>')
    for ang in range(-80, 90, 32):
        a.add(f'<path d="M110 120 L110 60" stroke="{o}" stroke-width="2.5" opacity=".35" transform="rotate({ang} 110 120)"/>')
    # face peeking out of the roll
    a.path("M78 130 C78 112 110 104 128 116 C140 126 136 150 116 156 C96 160 78 148 78 130 Z", "#F4E6D0", o, 3)
    a.ell(84, 140, 8, 6, "#F4E6D0", o, 2.5)
    a.circ(78, 140, 2.5, o)
    a.eye(102, 128, rx=7, ry=9, iris="#B09A78", pupil=("#2A1A0A", "#0A0602"))
    a.eye(122, 130, rx=6, ry=8, iris="#B09A78", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(104, 148, "open", w=6, color="#7A3E2E")
    a.ell(110, 78, 8, 12, "#F4E6D0", o, 2.5, rot=20)
    a.ell(126, 82, 7, 11, "#F4E6D0", o, 2.5, rot=40)
    a.gloss(80, 84, 12, 6)


@chordoo("amethyx")
def amethyx(a):
    fur = a.shade("#E8E4F0", "#9A92B0", "#5A5270")
    o = "#2A2240"
    a.ground(rx=70)
    # amethyst crystals on back
    for x, w, h, r in ((86, 14, 34, -18), (102, 18, 48, -6), (120, 18, 52, 6), (138, 14, 36, 18)):
        spire(a, x, 112, w, h, "#F4E0FF", "#B87AF0", "#6A2AB8", "#3A1A6A", r)
    # tail
    a.path("M156 130 C176 124 186 104 178 90 C190 104 188 130 166 144 Z", fur, o, 3)
    # body
    a.path("M54 142 C50 118 76 106 110 106 C142 106 162 118 160 142 C158 162 136 168 108 168 C80 168 58 164 54 142 Z", fur, o)
    for x in (66, 88, 128, 148):
        a.path(f"M{x - 9} 156 L{x - 9} 180 H{x + 9} L{x + 9} 156", fur, o, 3)
        a.ell(x, 180, 11, 5, "#E8E4F0", o, 2.5)
    # head
    a.path("M20 94 C18 66 42 54 64 56 C88 58 100 76 96 98 C92 120 72 126 54 126 C34 126 22 114 20 94 Z", fur, o)
    a.path("M30 66 L26 32 L50 56 Z", fur, o, 3)
    a.path("M72 58 L86 26 L88 66 Z", fur, o, 3)
    a.path("M32 62 L30 42 L44 56 Z", "#B87AF0", None)
    a.path("M78 58 L85 38 L86 62 Z", "#B87AF0", None)
    a.ell(40, 108, 18, 12, "#E8E4F0", o, 2)
    a.ell(28, 104, 6, 4.5, o)
    a.mouth(40, 114, "smile", w=6, color=o)
    a.eyes(88, xs=(52, 78), rx=8, ry=10, iris="#B87AF0", pupil=("#2A1A4A", "#0A0614"))
    gem(a, 64, 70, 0.4, "#F4E0FF", "#B87AF0", "#6A2AB8")
    for x, y in ((140, 40), (176, 70), (110, 30)):
        a.sparkle(x, y, 5, "#E0C8FF")


@chordoo("obsidino")
def obsidino(a):
    sk = a.shade("#6A6A80", "#2A2A3A", "#0A0A14")
    o = "#000006"
    a.ground(rx=56)
    # tail
    a.path("M130 150 C160 156 180 146 190 128 C170 134 152 134 138 128 Z", sk, o, 3)
    # legs
    for x in (78, 118):
        a.path(f"M{x - 12} 150 L{x - 12} 180 H{x + 12} L{x + 12} 150", sk, o, 3)
        a.line(f"M{x - 8} 180 v-4 M{x} 180 v-4 M{x + 8} 180 v-4", "#9A9AB0", 2)
    # body
    a.path("M56 150 C50 116 70 92 100 92 C132 92 148 116 144 150 C140 170 120 174 100 174 C80 174 60 170 56 150 Z", sk, o)
    a.path("M78 150 C76 128 86 114 100 114 C114 114 124 128 122 150 C118 164 82 164 78 150 Z", "#3A3A50")
    # back plates
    for x, y in ((140, 104), (150, 122), (128, 90)):
        a.path(f"M{x - 8} {y + 6} L{x} {y - 10} L{x + 8} {y + 6} Z", "#4A4A60", o, 2.5)
    # tiny arms
    limb(a, "M62 128 L48 132", "#2A2A3A", o, 9)
    limb(a, "M138 128 L150 136", "#2A2A3A", o, 9)
    # head
    a.path("M54 70 C52 42 80 30 104 32 C130 34 146 50 144 72 C142 96 120 104 98 104 C74 104 56 94 54 70 Z", sk, o)
    a.eyes(66, xs=(84, 116), rx=10, ry=12, iris="#FFC83A", pupil=("#2A1A0A", "#0A0602"), kind="star")
    a.mouth(100, 88, "smirk", w=10, color="#C8C8E0")
    a.cheeks([(68, 84), (132, 84)], "#FF6AA8", rx=7, ry=4, dots=False)
    # super shiny highlights
    a.gloss(74, 48, 14, 6, op=0.7)
    a.gloss(72, 120, 6, 12, rot=-10, op=0.5)
    a.line("M120 46 L132 56", "#FFFFFF", 3, 0.6)
    for x, y in ((30, 40), (170, 36), (176, 90)):
        a.sparkle(x, y, 7, "#FFFFFF")


@chordoo("prismara")
def prismara(a):
    o = "#2A2A5A"
    a.ground(rx=36)
    # rainbow beam out the right side
    for i, c in enumerate(("#FF5A6A", "#FF9A3A", "#FFD84D", "#6ACC5A", "#4AA8FF", "#9A6AE8")):
        a.path(f"M128 {98 + i * 3} L200 {66 + i * 12} L200 {72 + i * 12} L128 {101 + i * 3} Z", c, None, extra=' class="fx" opacity=".85"')
    # incoming white light
    a.path("M0 78 L72 104 L72 108 L0 84 Z", "#FFFFFF", "#D8D8F0", 1, ' class="fx"')
    # floating prism body
    a.path("M100 30 L150 130 H50 Z", a.lin("#FFFFFF", "#E8F0FF", "#B8C8F0"), o, 3.5)
    a.path("M100 30 L150 130 H122 Z", "#C8D4F8", None, extra=' opacity=".7"')
    a.path("M100 30 L150 130 H50 Z", "none", o, 3.5)
    a.line("M100 30 L122 130", o, 2, 0.4)
    a.eyes(98, xs=(86, 110), rx=7, ry=9, iris="#9A6AE8", pupil=("#2A1A4A", "#0A0614"))
    a.mouth(98, 114, "smile", w=6, color=o)
    a.cheeks([(76, 112), (120, 112)], "#FF8AC8", rx=5, ry=3, dots=False)
    a.gloss(84, 70, 4, 12, rot=25)
    # little floating crystals underneath
    for x, y in ((76, 150), (124, 152), (100, 162)):
        a.path(f"M{x} {y - 7} L{x + 5} {y} L{x} {y + 7} L{x - 5} {y} Z", "#E8F0FF", o, 2)
    for x, y in ((30, 140), (40, 30), (170, 150)):
        a.sparkle(x, y, 6, "#B89AF0")


@chordoo("diamondo")
def diamondo(a):
    o = "#1E3A5A"
    a.ground(rx=74)
    sk = a.shade("#D8E0EC", "#8A98B0", "#4A5670")
    # legs
    for x in (48, 74, 128, 154):
        a.path(f"M{x - 11} 150 L{x - 12} 180 H{x + 12} L{x + 11} 150", sk, "#1E2A40", 3)
        a.line(f"M{x - 8} 180 v-5 M{x} 180 v-5 M{x + 8} 180 v-5", "#1E2A40", 2)
    # tail
    a.path("M170 140 L194 150 L172 156 Z", "#C8F0FF", o, 2.5)
    # diamond plate shell
    a.path("M30 150 C30 98 64 70 104 70 C144 70 176 98 176 150 Z", a.lin("#FFFFFF", "#C8F0FF", "#6AB8E8"), o, 3.5)
    rows = [(150, 128, 8), (128, 106, 7), (106, 86, 5)]
    for (y1, y2, n) in rows:
        span = {150: (34, 172), 128: (44, 164), 106: (60, 148)}[y1]
        step = (span[1] - span[0]) / n
        for i in range(n):
            x0 = span[0] + i * step
            a.path(f"M{x0:.1f} {y1} L{x0 + step / 2:.1f} {y2} L{x0 + step:.1f} {y1}", "#FFFFFF" if i % 2 else "#A8E0FF", o, 2)
    a.path("M30 150 C30 98 64 70 104 70 C144 70 176 98 176 150 Z", "none", o, 3.5)
    # head with helmet plate
    a.path("M4 128 C2 104 22 92 42 94 C60 96 70 112 64 130 C58 148 36 152 22 148 C10 144 4 138 4 128 Z", sk, "#1E2A40")
    a.path("M14 104 C22 88 48 86 60 100 L50 108 C42 100 28 100 20 110 Z", "#C8F0FF", o, 2.5)
    a.eye(24, 122, rx=6, ry=8, kind="angry", iris="#5AC8FF", pupil=("#1A2A4A", "#060A14"), side=-1)
    a.eye(46, 122, rx=6, ry=8, kind="angry", iris="#5AC8FF", pupil=("#1A2A4A", "#060A14"))
    a.mouth(32, 138, "smirk", w=7, color="#1E2A40")
    for x, y in ((80, 50), (150, 56), (184, 110)):
        a.sparkle(x, y, 7, "#FFFFFF")


@chordoo("mountaine")
def mountaine(a):
    o = "#2A2A3A"
    rock = a.shade("#C8C4D8", "#7A7890", "#4A4860")
    a.ground(rx=82)
    # body as a mountain with snowy peaks
    a.path("M14 184 L48 92 L72 112 L100 34 L130 104 L152 86 L188 184 Z", rock, o, 3.5)
    a.path("M100 34 L116 70 L106 64 L98 76 L90 62 L84 72 Z", "#FFFFFF", o, 2.5)
    a.path("M48 92 L58 108 L52 106 L46 112 L42 106 Z", "#FFFFFF", o, 2)
    a.path("M152 86 L162 104 L156 102 L150 108 L146 100 Z", "#FFFFFF", o, 2)
    # pine trees on shoulders
    for x, y in ((40, 140), (164, 138), (150, 156)):
        a.path(f"M{x} {y - 14} L{x + 8} {y} H{x - 8} Z", "#3E8A4A", "#1E4A2A", 1.8)
    # face
    a.path("M74 92 Q86 84 96 92 M104 92 Q114 84 126 92", "none", "#FFFFFF", 6)
    a.eyes(104, xs=(86, 114), kind="happy", rx=8)
    a.cheeks([(72, 116), (128, 116)], "#FF9AA8", rx=7, ry=4, dots=False)
    a.mouth(100, 118, "smile", w=7, color=o)
    # waterfall beard
    a.path("M80 124 C84 132 86 150 82 182 H118 C114 150 116 132 120 124 C110 130 90 130 80 124 Z",
           a.lin("#E8FAFF", "#8AD8FF", "#3A98E0"), "#1E5A8A", 2.5)
    for x in (90, 100, 110):
        a.line(f"M{x} 132 C{x - 2} 150 {x + 2} 166 {x} 180", "#FFFFFF", 2.5, 0.8)
    a.ell(100, 184, 30, 5, "#8AD8FF", "#1E5A8A", 2)
    # cloud at summit
    a.ell(132, 42, 18, 8, "#FFFFFF", "#A8B8D8", 2, extra=' class="fx"')
    a.ell(60, 60, 14, 6, "#FFFFFF", "#A8B8D8", 2, extra=' class="fx"')
    # bird
    a.line("M164 44 q5 -5 10 0 q5 -5 10 0", o, 2.2)

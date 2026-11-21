from artkit import chordoo, INK
from shapes import snowflake, limb, star

SNOW = ("#FFFFFF", "#EAF4FF", "#A8C8E8")
ICE = ("#F0FCFF", "#A8E8FF", "#4AA8D8")
ICE_O = "#1E4A7A"


def icicle(a, x, y, w, h, fill="#D8F4FF", o=ICE_O, sw=2):
    a.path(f"M{x - w / 2} {y} L{x} {y + h} L{x + w / 2} {y} Z", fill, o, sw)


@chordoo("frostbite")
def frostbite(a):
    a.ground(rx=48)
    body = a.shade(*SNOW)
    a.circ(100, 116, 60, body, "#5A7AA8", 3.5)
    # snow lumps
    for x, y in ((60, 86), (138, 92), (70, 160), (140, 150)):
        a.circ(x, y, 6, "none", "#C8DCF0", 2)
    a.eyes(104, xs=(80, 120), rx=10, ry=12, iris="#7ACCFF", pupil=("#1E3A6E", "#0A1630"))
    # mouth with icicle teeth
    a.path("M78 130 Q100 150 122 130 Q100 140 78 130 Z", "#3A4A7A", "#1E2A5A", 2.5)
    for x in (88, 100, 112):
        icicle(a, x, 134 if x != 100 else 137, 7, 9, "#FFFFFF", "#5A7AA8", 1.4)
    a.cheeks([(64, 126), (136, 126)], "#FF9AB8", rx=9, ry=6)
    a.gloss(74, 80, 14, 7)
    # sneeze snowflakes
    for x, y, r in ((36, 50, 9), (164, 44, 7), (176, 110, 6), (24, 120, 6)):
        snowflake(a, x, y, r, "#8AC8F0", 2)


@chordoo("pengwyn")
def pengwyn(a):
    o = "#141E3A"
    a.ground(rx=44)
    body = a.shade("#5A6A9A", "#2A3460", "#0E1430")
    a.path("M100 40 C140 40 152 80 150 120 C148 160 128 180 100 180 C72 180 52 160 50 120 C48 80 60 40 100 40 Z", body, o)
    a.path("M100 84 C126 84 134 110 132 136 C130 162 118 174 100 174 C82 174 70 162 68 136 C66 110 74 84 100 84 Z", "#FFFFFF")
    a.path("M70 64 C80 54 120 54 130 64 C136 76 128 92 100 92 C72 92 64 76 70 64 Z", "#FFFFFF")
    # flippers
    a.path("M52 110 C38 122 34 142 40 150 C50 140 54 128 56 120 Z", body, o, 3)
    a.path("M148 110 C162 122 166 142 160 150 C150 140 146 128 144 120 Z", body, o, 3)
    a.ell(84, 182, 12, 5, "#FFA020", "#8A4A00", 2.5)
    a.ell(116, 182, 12, 5, "#FFA020", "#8A4A00", 2.5)
    a.eyes(72, xs=(86, 114), rx=8, ry=10, iris="#6A8AD8", pupil=("#141E3A", "#060A18"))
    a.path("M92 84 L108 84 L100 94 Z", "#FFA020", "#8A4A00", 2)
    a.cheeks([(76, 86), (124, 86)], rx=6, ry=4, dots=False)
    # knitted scarf
    sc = a.lin("#FF6A7A", "#D6304A")
    a.path("M62 98 C80 108 120 108 138 98 L140 112 C120 122 80 122 60 112 Z", sc, "#6A0E1E", 3)
    a.path("M120 112 L128 150 L114 152 L108 114 Z", sc, "#6A0E1E", 3)
    for y in (124, 134, 144):
        a.line(f"M{112 + (y - 112) * 0.15} {y} L{126 + (y - 112) * 0.05} {y - 1}", "#FFFFFF", 2.5)
    for x in (72, 86, 100, 114, 128):
        a.line(f"M{x} 104 v10", "#FFFFFF", 1.6, 0.5)
    a.gloss(78, 54, 10, 5)


@chordoo("sleetle")
def sleetle(a):
    o = "#1E2A5A"
    a.ground(rx=56)
    # ice patch
    a.ell(100, 180, 80, 12, a.lin("#E8F8FF", "#A8D8F0"), "#6AA8D0", 2.5)
    a.line("M40 178 l20 -2 M130 182 l24 -2", "#FFFFFF", 2.5, 0.9)
    # legs with skate blades
    for x in (74, 100, 126):
        a.line(f"M{x} 150 L{x - 4} 168", o, 3.5)
        a.path(f"M{x - 14} 170 H{x + 6} Q{x + 10} 170 {x + 8} 166", "none", "#8A9AB8", 3)
    # shell: icy blue with snowflake spots
    shell = a.shade("#E8F8FF", "#6AC0F0", "#2A6AB0")
    a.path("M40 140 C40 96 70 76 104 76 C138 76 166 96 166 140 C140 156 66 156 40 140 Z", shell, o)
    a.line("M104 78 V150", o, 3)
    for x, y, r in ((70, 108, 9), (82, 134, 7), (134, 104, 9), (126, 134, 7)):
        snowflake(a, x, y, r, "#FFFFFF", 2.4, cls="")
    a.gloss(72, 90, 14, 6)
    # head
    a.path("M150 120 C150 98 186 96 188 122 C190 144 152 146 150 120 Z", a.shade("#5A6A9A", "#2A3460", "#0E1430"), o, 3)
    a.eye(162, 116, rx=6, ry=8, iris="#6AC0F0", pupil=("#0E1430", "#060A18"))
    a.eye(178, 116, rx=6, ry=8, iris="#6AC0F0", pupil=("#0E1430", "#060A18"))
    a.mouth(170, 130, "smile", w=5, color="#FFFFFF")
    a.line("M162 100 C160 88 154 84 148 84 M178 100 C182 88 188 86 192 88", o, 2.2)
    # earmuff
    a.circ(150, 112, 7, "#FF8AC0", "#7A1A4A", 2)


@chordoo("mittsy")
def mittsy(a):
    o = "#5A1A3A"
    a.ground(rx=40)
    knit = a.shade("#FFD8E8", "#FF7AAA", "#C83A6A")
    # mitten: thumb on left
    a.path("M64 170 V100 C64 70 76 46 104 46 C132 46 144 70 144 100 V170 Z", knit, o, 3.5)
    a.path("M66 116 C46 112 38 92 46 80 C54 70 66 76 68 88", knit, o, 3.5)
    # knit pattern rows
    for y in (70, 90):
        for x in range(76, 134, 12):
            a.path(f"M{x} {y} l6 6 l6 -6", "none", "#FFFFFF", 2)
    # cuff
    a.path("M58 150 H150 V180 H58 Z", "#FFFFFF", o, 3)
    for x in range(64, 150, 8):
        a.line(f"M{x} 154 V176", "#E0C8D8", 2)
    # pompom
    a.circ(150, 150, 14, a.shade("#FFFFFF", "#FFF0F6", "#E0B8CC"), o, 3)
    for x, y in ((144, 144), (154, 152), (148, 158)):
        a.circ(x, y, 2, "#E0B8CC")
    a.eyes(112, xs=(88, 120), rx=9, ry=11, iris="#FF7AAA", pupil=("#3A0A1E", "#12030A"))
    a.mouth(104, 132, "cat", w=7, color=o)
    a.cheeks([(76, 128), (132, 128)], "#FFFFFF", rx=7, ry=4, dots=False)
    a.gloss(84, 62, 10, 5)
    for x, y in ((30, 140), (36, 40), (170, 70)):
        a.add(f'<path class="fx" d="M{x} {y} q4 -8 0 -14 q-4 -6 0 -12" stroke="#FFB080" stroke-width="2.5" fill="none" stroke-linecap="round"/>')


@chordoo("polarbit")
def polarbit(a):
    fur = a.shade("#FFFFFF", "#F2F6FF", "#C0CCE0")
    o = "#3A4A6A"
    a.ground(rx=60)
    # body sitting
    a.path("M46 150 C40 112 66 96 100 96 C134 96 160 112 154 150 C150 176 126 182 100 182 C74 182 50 176 46 150 Z", fur, o)
    a.ell(72, 172, 18, 12, fur, o, 3)
    a.ell(128, 172, 18, 12, fur, o, 3)
    for x in (66, 72, 78, 122, 128, 134):
        a.circ(x, 168, 2.2, "#C0CCE0")
    # arms open for a hug
    a.path("M50 120 C30 112 24 96 30 88 C38 82 50 92 58 108", fur, o, 3)
    a.path("M150 120 C170 112 176 96 170 88 C162 82 150 92 142 108", fur, o, 3)
    # head
    a.circ(100, 76, 44, fur, o)
    # frosty ears
    for sx in (1, -1):
        a.circ(100 + sx * 34, 40, 13, fur, o, 3)
        a.circ(100 + sx * 34, 40, 7, a.shade("#E8F8FF", "#9AD8FF", "#4AA8D8"))
        snowflake(a, 100 + sx * 34, 40, 5, "#FFFFFF", 1.4, cls="")
    a.ell(100, 92, 18, 13, "#FFFFFF", o, 2.5)
    a.path("M93 86 L107 86 L100 93 Z", "#3A4A6A")
    a.mouth(100, 96, "cat", w=5, color=o)
    a.eyes(72, xs=(80, 120), rx=8, ry=10, iris="#9AD8FF", pupil=("#1E2A4A", "#0A0E1A"))
    a.cheeks([(66, 90), (134, 90)], rx=8, ry=5)
    a.add('<path class="fx" d="M100 128 C96 120 86 122 88 130 C90 136 100 142 100 142 C100 142 110 136 112 130 C114 122 104 120 100 128 Z" fill="#FF8AA8"/>')
    for x, y in ((24, 40), (176, 140)):
        snowflake(a, x, y, 7, "#9AC8F0", 2)


@chordoo("glacio")
def glacio(a):
    o = ICE_O
    a.ground(rx=56)
    cube = a.lin("#F0FCFF", "#A8E8FF", "#5AB8E8")
    # legs
    for x in (78, 122):
        a.path(f"M{x - 12} 150 H{x + 12} V178 H{x - 12} Z", a.lin("#D8F6FF", "#7ACCF0"), o, 3)
    # arms: smaller cubes
    a.path("M30 102 H54 V130 H30 Z", cube, o, 3)
    a.path("M146 102 H170 V130 H146 Z", cube, o, 3)
    # big cube body in pseudo-3D
    a.path("M52 70 L72 52 H160 L140 70 Z", "#E8FAFF", o, 3)
    a.path("M140 70 L160 52 V138 L140 156 Z", "#6AC0E8", o, 3)
    a.path("M52 70 H140 V156 H52 Z", cube, o, 3.5)
    a.gloss(68, 84, 10, 5, rot=0)
    a.line("M60 140 L70 130 M120 80 L130 74", "#FFFFFF", 2.5, 0.8)
    a.eyes(106, xs=(80, 112), rx=9, ry=11, iris="#4AA8D8", pupil=("#0E2A4A", "#04101C"))
    a.mouth(96, 126, "smile", w=8, color=o)
    a.cheeks([(66, 122), (126, 122)], "#FF9AB8", rx=7, ry=5)
    # melting drips
    for x, h in ((70, 12), (118, 18)):
        a.path(f"M{x - 4} 156 C{x - 4} {156 + h} {x + 4} {156 + h} {x + 4} 156 Z", "#A8E8FF", o, 2)
    a.ell(148, 182, 14, 3, "#A8E8FF", extra=' opacity=".8"')


@chordoo("snowl")
def snowl(a):
    feat = a.shade("#FFFFFF", "#F2F6FF", "#C0CCE0")
    o = "#3A4A6A"
    a.ground(rx=44)
    a.ell(100, 124, 52, 56, feat, o)
    for x, y in ((82, 140), (104, 150), (120, 132), (90, 160), (114, 168)):
        a.path(f"M{x - 4} {y} l4 4 l4 -4", "none", "#8A9AB8", 2)
    a.path("M50 110 C40 130 44 160 60 170 C62 148 62 128 56 112 Z", feat, o, 3)
    a.path("M150 110 C160 130 156 160 140 170 C138 148 138 128 144 112 Z", feat, o, 3)
    a.path("M86 180 l-4 6 M92 180 v7 M108 180 v7 M114 180 l4 6", "none", "#8A9AB8", 3)
    # face discs
    a.ell(80, 104, 20, 19, "#FFFFFF", "#C0CCE0", 2)
    a.ell(120, 104, 20, 19, "#FFFFFF", "#C0CCE0", 2)
    a.eyes(104, xs=(80, 120), rx=11, ry=13, iris="#FFD020", pupil=("#2A2A3A", "#0A0A12"))
    a.mouth(100, 116, "beak", w=6)
    # ear tufts
    a.path("M58 74 L54 54 L72 68 Z", feat, o, 3)
    a.path("M142 74 L146 54 L128 68 Z", feat, o, 3)
    # frost crown of ice spikes
    for x, h in ((80, 18), (90, 26), (100, 32), (110, 26), (120, 18)):
        icicle(a, x, 70, 10, -h, a.lin("#FFFFFF", "#9AD8FF"), ICE_O, 2)
    a.line("M76 70 H124", ICE_O, 2.5)
    for x, y in ((26, 40), (172, 50), (30, 150), (176, 160)):
        snowflake(a, x, y, 7, "#9AC8F0", 2)


@chordoo("yetti")
def yetti(a):
    fur = a.shade("#FFFFFF", "#EEF2FA", "#B8C4DA")
    o = "#3A4A6A"
    a.ground(rx=62)
    # snow fort blocks behind
    for x, y in ((14, 150), (40, 150), (160, 150), (186, 150), (26, 128), (174, 128)):
        a.path(f"M{x - 13} {y} H{x + 13} V{y + 22} H{x - 13} Z", "#F6FAFF", "#A8C0DA", 2)
    # body shaggy
    a.path("M54 120 C50 90 70 68 100 68 C130 68 150 90 146 120 L150 160 L138 156 L132 170 L120 162 L110 174 L100 164 L90 174 L80 162 L68 170 L62 156 L50 160 Z", fur, o)
    # face patch
    a.path("M72 96 C72 80 128 80 128 96 C128 118 116 128 100 128 C84 128 72 118 72 96 Z", a.shade("#E8F4FF", "#A8D0F0", "#6AA0D0"), o, 2.5)
    # blue horns
    for sx in (1, -1):
        a.path(f"M{100 + sx * 30} 76 C{100 + sx * 44} 64 {100 + sx * 46} 46 {100 + sx * 38} 34 C{100 + sx * 34} 48 {100 + sx * 28} 58 {100 + sx * 20} 66 Z",
               a.lin("#9AD8FF", "#3A7AD0"), "#1E3A7A", 2.5)
    # arms holding a snowball
    a.path("M56 116 C40 120 34 136 40 146 C48 142 54 134 60 128", fur, o, 3)
    a.path("M144 116 C160 120 166 136 160 146 C152 142 146 134 140 128", fur, o, 3)
    a.circ(100, 148, 16, a.shade(*SNOW), "#8AA0C0", 2.5)
    # feet
    a.ell(80, 178, 14, 6, "#B8C4DA", o, 2.5)
    a.ell(120, 178, 14, 6, "#B8C4DA", o, 2.5)
    a.eyes(100, xs=(88, 112), rx=7, ry=9, iris="#3A7AD0", pupil=("#0E1A3A", "#04080E"))
    a.mouth(100, 116, "grin", w=7, color="#1E3A7A")
    a.cheeks([(78, 112), (122, 112)], rx=5, ry=3, dots=False)


@chordoo("auroracub")
def auroracub(a):
    fur = a.shade("#FFFFFF", "#F2F6FF", "#C8D2E8")
    o = "#2A3A6A"
    a.ground(rx=60)
    # aurora tail sweeping up
    tail = a.lin("#6AFFC8", "#5AC8FF", "#B87AFF", "#FF8AD8", x1=0, y1=1, x2=1, y2=0)
    a.path("M140 150 C170 150 190 120 184 84 C182 66 168 50 156 52 C170 70 168 96 156 110 C150 120 140 128 132 132 Z", tail, o, 3)
    a.add('<path class="fx" d="M178 58 C196 40 190 20 176 10" stroke="#6AFFC8" stroke-width="6" fill="none" opacity=".5" stroke-linecap="round"/>')
    a.add('<path class="fx" d="M186 80 C198 64 200 46 194 32" stroke="#B87AFF" stroke-width="5" fill="none" opacity=".45" stroke-linecap="round"/>')
    # body
    a.path("M50 150 C46 124 70 110 100 110 C130 110 150 122 148 150 C146 172 126 180 100 180 C74 180 52 172 50 150 Z", fur, o)
    for x in (70, 92, 116):
        a.ell(x, 178, 10, 6, "#FFFFFF", o, 2.5)
    # head
    a.path("M40 84 C38 60 64 48 86 52 C110 56 120 76 116 96 C112 118 92 124 74 124 C54 124 42 108 40 84 Z", fur, o)
    a.path("M46 58 L40 24 L68 48 Z", fur, o, 3)
    a.path("M100 52 L118 22 L118 62 Z", fur, o, 3)
    a.path("M48 52 L45 34 L60 48 Z", "#B87AFF", None)
    a.path("M106 52 L115 34 L114 56 Z", "#5AC8FF", None)
    a.ell(54, 104, 16, 10, "#FFFFFF", o, 2)
    a.circ(42, 102, 4, o)
    a.eyes(84, xs=(64, 96), rx=8, ry=10, iris="#5AC8FF", pupil=("#1A2A5A", "#060A1A"), lashes=1)
    a.mouth(54, 110, "smile", w=5, color=o)
    a.cheeks([(76, 104), (108, 102)], "#FF8AD8", rx=6, ry=4, dots=False)
    for x, y in ((24, 140), (140, 30), (80, 20)):
        a.sparkle(x, y, 5, "#B8FFE8")


@chordoo("crystalisk")
def crystalisk(a):
    sk = a.shade("#E8FAFF", "#8AD8F0", "#3A8AC0")
    o = "#123A5A"
    a.ground(rx=70)
    # frosty footprints
    for x in (20, 40):
        snowflake(a, x, 184, 5, "#8AC8F0", 1.6)
    # tail
    a.path("M140 150 C170 154 184 140 188 124 C176 134 160 136 146 132 Z", sk, o, 3)
    # body
    a.path("M40 136 C40 112 70 104 104 106 C134 108 152 120 148 142 C146 160 124 164 100 164 C70 164 40 158 40 136 Z", sk, o)
    # crystal spines along back
    for x, h, r in ((62, 26, -15), (82, 34, -5), (104, 38, 5), (126, 30, 15), (144, 22, 25)):
        a.add(f'<g transform="rotate({r} {x} 110)"><path d="M{x - 8} 112 L{x} {112 - h} L{x + 8} 112 Z" fill="{a.lin("#FFFFFF", "#9AE8FF", "#4AA8E8")}" stroke="{o}" stroke-width="2.5" stroke-linejoin="round"/>'
              f'<path d="M{x} {112 - h} L{x + 2} 112" stroke="#FFFFFF" stroke-width="1.5" opacity=".7"/></g>')
    # legs
    for x in (54, 80, 116, 138):
        a.path(f"M{x - 8} 154 L{x - 10} 176 L{x + 10} 176 L{x + 8} 154", sk, o, 3)
        a.line(f"M{x - 8} 176 v4 M{x} 176 v4 M{x + 8} 176 v4", o, 2)
    # head
    a.path("M10 116 C10 96 30 86 50 90 C66 94 70 112 62 124 C52 138 20 140 10 116 Z", sk, o)
    a.eye(34, 106, rx=8, ry=10, iris="#5AC8FF", pupil=("#0E2A4A", "#04101C"))
    a.eye(52, 108, rx=6, ry=8, iris="#5AC8FF", pupil=("#0E2A4A", "#04101C"))
    a.mouth(26, 124, "smile", w=8, color=o)
    a.cheeks([(42, 124)], rx=5, ry=3, dots=False)
    for x in (36, 48):
        icicle(a, x, 88, 6, -12, "#FFFFFF", o, 2)


@chordoo("blizzaron")
def blizzaron(a):
    o = "#2A4A7A"
    a.glow(100, 100, 90, "#D8F0FF", 0.6)
    a.ground(rx=58)
    snow = a.shade(*SNOW)
    # swirling coils: overlapping snow puffs along a spiral
    import math
    pts = []
    for i in range(22):
        t = i / 21
        ang = math.radians(200 + t * 520)
        r = 70 - t * 50
        pts.append((100 + r * math.cos(ang), 120 + r * 0.6 * math.sin(ang), 18 - t * 4))
    for (x, y, r) in pts:
        a.circ(round(x, 1), round(y, 1), round(r, 1), snow, "#8AA8D0", 2.5)
    for (x, y, r) in pts[::3]:
        snowflake(a, round(x, 1), round(y, 1), r * 0.5, "#9AC8F0", 1.6, cls="")
    # head rising at top of swirl
    head = a.shade("#FFFFFF", "#E0F0FF", "#8AB8E8")
    a.path("M70 66 C66 38 92 26 112 30 C136 34 146 56 138 76 C130 94 108 98 92 94 C78 90 72 80 70 66 Z", head, o)
    # icy horns + fins
    a.path("M84 36 L74 10 L96 30 Z", a.lin("#FFFFFF", "#9AE8FF"), o, 2.5)
    a.path("M122 32 L134 8 L132 40 Z", a.lin("#FFFFFF", "#9AE8FF"), o, 2.5)
    a.path("M138 60 L160 50 L148 72 Z", a.lin("#FFFFFF", "#9AE8FF"), o, 2.5)
    a.eyes(62, xs=(94, 120), rx=8, ry=10, iris="#5AC8FF", pupil=("#1A2A5A", "#060A1A"), kind="star")
    a.mouth(106, 80, "open", w=7, color="#3A4A8A", tongue="#9AD8FF")
    a.cheeks([(84, 76), (132, 72)], "#FF9AC8", rx=5, ry=3, dots=False)
    for x, y in ((24, 30), (176, 100), (20, 100), (170, 170)):
        snowflake(a, x, y, 8, "#8AC0F0", 2)


@chordoo("frostfang")
def frostfang(a):
    fur = a.shade("#FFFFFF", "#D8E2F4", "#8A9CC8")
    o = "#2A3456"
    a.ground(rx=66)
    # tail
    a.path("M146 136 C170 128 184 108 176 88 C186 110 180 136 158 150 Z", fur, o, 3)
    # body sitting, howling
    a.path("M70 180 C58 150 64 118 96 110 C130 104 156 124 156 156 C156 172 146 180 130 180 Z", fur, o)
    a.ell(82, 178, 14, 7, fur, o, 3)
    a.ell(140, 178, 14, 7, fur, o, 3)
    a.path("M74 176 L80 120 L96 120 L94 176 Z", fur, o, 3)
    # icicle mane hanging around the neck
    for x, h in ((58, 22), (70, 30), (84, 34), (98, 30), (112, 24)):
        a.path(f"M{x - 8} 104 L{x} {104 + h} L{x + 8} 104 Z", a.lin("#FFFFFF", "#9AE8FF", "#3A98E0"), "#1E4A7A", 2.4)
    # head tilted up
    a.add('<g transform="rotate(-24 80 70)">')
    a.path("M50 80 C46 54 68 40 90 42 C108 44 116 56 136 60 C142 64 140 76 132 80 C118 84 108 86 100 96 C88 108 56 106 50 80 Z", fur, o)
    a.path("M58 50 L56 22 L78 44 Z", fur, o, 3)
    a.path("M82 44 L92 18 L98 46 Z", fur, o, 3)
    a.path("M62 46 L61 30 L72 42 Z", "#9AD8FF", None)
    a.circ(138, 66, 5, o)
    a.eye(84, 64, kind="sleepy", rx=8)
    a.path("M108 82 Q120 92 132 82 Q122 98 108 82 Z", "#3A2A5A", o, 2)
    a.add('</g>')
    a.cheeks([(78, 92)], rx=6, ry=4, dots=False)
    # moon + howl notes
    a.circ(164, 34, 16, a.shade("#FFFFF0", "#FFF6C8", "#E8D890"), extra=' class="fx"')
    for x, y in ((140, 18), (186, 70)):
        snowflake(a, x, y, 7, "#9AC8F0", 2)
    a.line("M150 60 q6 -4 12 0 M154 70 q8 -4 16 0", "#9AC8F0", 2.5)


@chordoo("glaciera")
def glaciera(a):
    o = "#123A6A"
    a.glow(100, 90, 96, "#C8F0FF", 0.55)
    # mountain peak she sleeps on
    a.path("M0 200 L60 120 L84 140 L110 108 L200 200 Z", a.lin("#FFFFFF", "#C8DCF0", "#8AA8D0"), "#5A7AA8", 3)
    a.path("M60 120 L72 136 L66 140 L84 140 Z M110 108 L124 128 L114 126 L106 134 L100 120 Z", "#FFFFFF", None)
    # crystal wings
    w = a.lin("#FFFFFF", "#B8F0FF", "#5AB8E8")
    a.path("M100 110 L60 40 L74 74 L40 60 L66 96 L30 96 L86 120 Z", w, o, 3)
    a.path("M120 108 L170 30 L156 70 L190 54 L160 92 L196 92 L134 120 Z", w, o, 3)
    for d in ("M96 108 L60 40", "M90 114 L40 60", "M124 106 L170 30", "M130 112 L190 54"):
        a.line(d, "#FFFFFF", 1.8, 0.7)
    # tail curled around
    a.path("M70 150 C40 160 34 184 60 188 C90 192 130 180 150 166", "none", o, 16)
    a.path("M70 150 C40 160 34 184 60 188 C90 192 130 180 150 166", "none", "#8ADAF8", 11)
    # body curled
    body = a.shade("#F0FCFF", "#8ADAF8", "#3A8AC8")
    a.path("M70 160 C62 124 84 104 112 106 C144 108 156 136 146 160 C136 178 82 180 70 160 Z", body, o)
    a.path("M88 162 C86 140 96 126 112 126 C128 126 136 142 132 162 Z", "#E8FAFF", None)
    # head resting
    a.path("M100 112 C96 84 118 70 138 74 C160 78 170 98 162 116 C154 132 128 138 112 130 C104 126 100 120 100 112 Z", body, o)
    a.path("M120 78 L114 52 L132 72 Z M146 76 L156 50 L156 82 Z", a.lin("#FFFFFF", "#9AE8FF"), o, 2.5)
    a.eyes(102, xs=(124, 148), kind="sleepy", rx=8)
    a.mouth(138, 120, "smile", w=6, color=o)
    a.cheeks([(116, 116), (158, 112)], "#FF9AC8", rx=5, ry=3, dots=False)
    a.add('<text class="fx" x="164" y="70" font-size="18" font-weight="bold" font-family="sans-serif" fill="#5A8AC8">z</text>')
    a.add('<text class="fx" x="178" y="54" font-size="13" font-weight="bold" font-family="sans-serif" fill="#5A8AC8">z</text>')
    for x, y in ((20, 30), (100, 20), (30, 130)):
        snowflake(a, x, y, 7, "#FFFFFF", 2)

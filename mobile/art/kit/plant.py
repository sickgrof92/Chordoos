from artkit import chordoo, INK

LEAF = ("#D6F5A8", "#7CC850", "#3E8A2E")
LEAF_O = "#2A5A1E"


def leaf(a, x, y, length, angle, fill, o=LEAF_O, w=3, vein=True):
    """Pointed leaf from (x,y) pointing at `angle` degrees."""
    L = length
    a.add(f'<g transform="translate({x} {y}) rotate({angle})">'
          f'<path d="M0 0 C{L * 0.3} {-L * 0.32} {L * 0.75} {-L * 0.3} {L} 0 C{L * 0.75} {L * 0.3} {L * 0.3} {L * 0.32} 0 0 Z" '
          f'fill="{fill}" stroke="{o}" stroke-width="{w}" stroke-linejoin="round"/>'
          + (f'<path d="M{L * 0.1} 0 L{L * 0.85} 0" stroke="{o}" stroke-width="1.8" stroke-linecap="round" opacity=".6"/>' if vein else "")
          + '</g>')


@chordoo("mossy")
def mossy(a):
    rock = a.shade("#D8D4CC", "#9C968A", "#635D52")
    o = "#3A352C"
    a.ground(rx=56)
    a.path("M40 150 C36 112 66 94 100 94 C136 94 164 112 160 150 C158 172 134 180 100 180 C66 180 42 172 40 150 Z", rock, o)
    # moss blanket
    a.path("M42 136 C50 118 70 106 100 106 C130 106 152 118 158 136 C150 132 146 140 138 136 C132 130 124 140 116 134 "
           "C108 130 100 140 92 134 C84 130 76 140 68 134 C60 130 52 140 42 136 Z", a.lin("#A8E070", "#5EA83A"), LEAF_O, 3)
    # mushroom cap hat
    a.line("M112 98 V80", "#E8DCC0", 7)
    a.line("M112 98 V80", o, 1.5, 0.3)
    a.path("M84 82 C84 56 140 56 140 82 C130 86 94 86 84 82 Z", a.shade("#FF9A8A", "#E8503E", "#A82A22"), "#6E1A14", 3)
    for x, y, r in ((100, 70, 4), (120, 66, 5), (130, 78, 3), (94, 80, 2.5)):
        a.circ(x, y, r, "#FFF4E6")
    a.eyes(146, xs=(82, 118), kind="sleepy", rx=9)
    a.mouth(100, 160, "smile", w=6, color=o)
    a.cheeks([(68, 158), (132, 158)], "#FF9AA8", rx=9, ry=5)
    for x in (54, 150, 64):
        a.circ(x, 178 if x != 64 else 172, 3, "#7CC850")


@chordoo("sprout")
def sprout(a):
    skin = a.shade("#FFF4D6", "#F2D49A", "#C49A5A")
    o = "#5A3E1E"
    a.ground(rx=40)
    # stem and leaves
    a.line("M100 72 C100 56 98 48 100 36", "#4E9E3A", 5)
    leaf(a, 100, 40, 54, -160, a.shade(*LEAF))
    leaf(a, 100, 36, 54, -20, a.shade(*LEAF))
    # legs
    a.path("M84 158 L82 178 H94 L94 160", skin, o, 3)
    a.path("M106 160 L106 178 H118 L116 158", skin, o, 3)
    # body (seed-shaped)
    a.path("M100 64 C134 64 144 96 142 124 C140 152 124 166 100 166 C76 166 60 152 58 124 C56 96 66 64 100 64 Z", skin, o)
    a.path("M70 132 C80 150 120 150 130 132 C128 154 116 164 100 164 C84 164 72 154 70 132 Z", "#7CC850", None, extra=' opacity=".45"')
    # stretching arms
    a.path("M62 112 C48 100 44 88 46 78", "none", o, 9)
    a.path("M62 112 C48 100 44 88 46 78", "none", "#F2D49A", 5)
    a.path("M138 112 C152 100 156 88 154 78", "none", o, 9)
    a.path("M138 112 C152 100 156 88 154 78", "none", "#F2D49A", 5)
    a.eyes(110, xs=(84, 116), rx=9, ry=11, iris="#7CC850", pupil=("#3A2A1A", "#140C06"))
    a.mouth(100, 130, "open", w=7, color="#7A3E2E")
    a.cheeks([(72, 126), (128, 126)], rx=8, ry=5)
    a.gloss(76, 82, 8, 4)


@chordoo("acornelius")
def acornelius(a):
    nut = a.shade("#F5C890", "#D08A44", "#8A5220")
    o = "#4A2A10"
    a.ground(rx=42)
    a.ell(84, 176, 10, 6, "#8A5220", o, 3)
    a.ell(116, 176, 10, 6, "#8A5220", o, 3)
    a.path("M56 96 C56 140 72 172 100 172 C128 172 144 140 144 96 Z", nut, o)
    # cap
    cap = a.lin("#C89A5A", "#8A6234")
    a.path("M50 98 C50 70 72 58 100 58 C128 58 150 70 150 98 C130 104 70 104 50 98 Z", cap, o)
    for y in (70, 82, 92):
        a.line(f"M{62 if y > 70 else 76} {y} Q100 {y + 6} {138 if y > 70 else 124} {y}", "#6E4A22", 2, 0.6)
    # beret on top
    a.ell(96, 52, 30, 10, a.shade("#FF7A7A", "#D63A4A", "#8A1A2A"), "#5A0E1A", 3, rot=-10)
    a.circ(98, 42, 4, "#5A0E1A")
    a.eyes(120, xs=(84, 116), rx=9, ry=11, iris="#E0A060", pupil=("#3A2010", "#120804"))
    a.mouth(100, 142, "cat", w=7, color=o)
    a.cheeks([(72, 136), (128, 136)], rx=8, ry=5)
    # button it is holding
    a.circ(146, 140, 11, "#5AB0E8", "#1E5A8A", 3)
    for dx, dy in ((-3, -3), (3, -3), (-3, 3), (3, 3)):
        a.circ(146 + dx, 140 + dy, 1.6, "#1E5A8A")
    a.gloss(74, 112, 7, 12, rot=-10, op=0.4)


@chordoo("petalfly")
def petalfly(a):
    o = "#7A2A5A"
    pet1 = a.shade("#FFF0F6", "#FFA8D0", "#E0609A")
    pet2 = a.shade("#FFFBE0", "#FFD86A", "#E09A2A")
    a.ground(rx=34)
    # wings: petals
    for ang, fill, ln in ((-130, pet1, 70), (-160, pet2, 56), (-50, pet1, 70), (-20, pet2, 56)):
        a.add(f'<g transform="translate(100 110) rotate({ang})"><path d="M0 0 C{ln * 0.2} -30 {ln} -26 {ln} 0 '
              f'C{ln} 26 {ln * 0.2} 30 0 0 Z" fill="{fill}" stroke="{o}" stroke-width="3" stroke-linejoin="round"/>'
              f'<path d="M8 0 L{ln * 0.8} 0" stroke="{o}" stroke-width="1.6" opacity=".4"/></g>')
    # body
    body = a.shade("#C8F0A0", "#6EC04A", "#3A7A2A")
    a.ell(100, 134, 10, 30, body, LEAF_O, 3)
    for y in (124, 136, 148):
        a.line(f"M92 {y} Q100 {y + 3} 108 {y}", LEAF_O, 1.6, 0.6)
    # head
    a.circ(100, 94, 20, body, LEAF_O, 3)
    a.line("M92 76 C88 62 80 56 74 56", LEAF_O, 2.5)
    a.line("M108 76 C112 62 120 56 126 56", LEAF_O, 2.5)
    a.circ(74, 56, 5, "#FFD86A", o, 2)
    a.circ(126, 56, 5, "#FF8AC0", o, 2)
    a.eyes(94, xs=(92, 108), rx=6, ry=7, iris="#6EC04A", pupil=("#1E3A1E", "#0A140A"))
    a.mouth(100, 104, "smile", w=4, color=LEAF_O)
    a.cheeks([(86, 102), (114, 102)], rx=4, ry=3, dots=False)
    a.sparkle(40, 50, 5)
    a.sparkle(162, 160, 4, "#FFA8D0")


@chordoo("thornby")
def thornby(a):
    fur = a.shade("#FFE6C8", "#E8B888", "#A87450")
    o = "#4A2A1A"
    a.ground(rx=64)
    # quills: rose-stem spikes in a fan
    q = a.lin("#7CC850", "#2E7A2A")
    for i in range(11):
        ang = -170 + i * 15
        a.add(f'<g transform="translate(110 130) rotate({ang})"><path d="M0 -12 L66 0 L0 12 Z" fill="{q}" stroke="{LEAF_O}" stroke-width="2.5" stroke-linejoin="round"/></g>')
    # roses on the back
    for x, y in ((84, 82), (132, 78), (156, 108)):
        a.circ(x, y, 10, a.shade("#FFB0C0", "#E8405A", "#A01A34"), "#6E0E22", 2.5)
        a.line(f"M{x - 4} {y} Q{x} {y - 5} {x + 4} {y} Q{x} {y + 4} {x - 2} {y - 1}", "#6E0E22", 1.8)
    # body
    a.path("M52 150 C48 116 76 96 112 98 C146 100 166 122 162 150 C158 174 130 180 104 180 C78 180 56 172 52 150 Z", fur, o)
    # face/snout pointing left
    a.path("M32 146 C34 128 52 118 70 122 C84 126 88 146 80 158 C70 170 40 168 32 146 Z", "#FFF0DE", o, 3)
    a.circ(30, 146, 6, "#3A2010")
    a.eye(62, 136, rx=7, ry=9, iris="#7CC850", pupil=("#3A2010", "#120804"))
    a.mouth(52, 158, "smile", w=6, color=o)
    a.cheeks([(72, 152)], rx=6, ry=4)
    for x in (80, 124):
        a.ell(x, 178, 10, 6, "#A87450", o, 3)
    # tiny bow tie for politeness
    a.path("M88 132 L78 126 L78 140 Z M88 132 L98 126 L98 140 Z", "#E8405A", "#6E0E22", 2)
    a.circ(88, 133, 3, "#A01A34")


@chordoo("pumpkid")
def pumpkid(a):
    pk = a.shade("#FFD8A0", "#FF9A3A", "#C85A14")
    o = "#6A2A0A"
    a.ground(rx=62)
    # vine arms
    a.line("M48 128 C30 120 22 104 30 94 C36 86 46 92 42 100", "#3E8A2E", 5)
    a.line("M152 128 C170 120 178 104 170 94 C164 86 154 92 158 100", "#3E8A2E", 5)
    leaf(a, 30, 112, 20, 120, a.shade(*LEAF), w=2, vein=False)
    leaf(a, 170, 112, 20, 60, a.shade(*LEAF), w=2, vein=False)
    # pumpkin lobes
    for cx, rx in ((66, 32), (134, 32), (84, 34), (116, 34), (100, 36)):
        a.ell(cx, 134, rx, 46, pk, o, 3)
    # stem + curl
    a.path("M94 92 C92 80 96 70 104 66 L110 72 C104 76 104 84 106 92 Z", "#6E8A2A", "#3A4A12", 3)
    a.line("M108 70 C120 60 132 66 126 76 C122 82 114 78 118 72", "#3E8A2E", 3)
    leaf(a, 110, 80, 26, -20, a.shade(*LEAF), w=2.5)
    # face
    a.eyes(126, xs=(84, 116), rx=10, ry=12, iris="#FFB04A", pupil=("#4A2A0A", "#140A02"))
    a.mouth(100, 148, "grin", w=11, color=o)
    a.cheeks([(68, 146), (132, 146)], "#FF6A5A", rx=9, ry=6)
    a.gloss(70, 108, 8, 12, rot=-15, op=0.45)


@chordoo("bloomoth")
def bloomoth(a):
    o = "#3A2A6A"
    a.glow(100, 100, 90, "#C8A8FF", 0.45)
    a.ground(rx=36)
    wing = a.shade("#F0E6FF", "#B89AF0", "#6A4AB8")
    for sx in (1, -1):
        a.path(f"M100 96 C{100 + sx * 30} 50 {100 + sx * 86} 40 {100 + sx * 84} 82 C{100 + sx * 82} 110 {100 + sx * 50} 112 100 104 Z", wing, o)
        a.path(f"M100 110 C{100 + sx * 40} 112 {100 + sx * 70} 130 {100 + sx * 60} 154 C{100 + sx * 48} 170 {100 + sx * 20} 150 100 118 Z", wing, o)
        # blooming flowers on the wings
        for (fx, fy, r) in ((136, 76, 11), (126, 138, 9)):
            x = 100 + sx * (fx - 100)
            for k in range(5):
                a.add(f'<ellipse cx="{x}" cy="{fy - r * 0.6}" rx="{r * 0.45}" ry="{r * 0.7}" fill="#FFE6F4" stroke="#C060A0" stroke-width="1.4" transform="rotate({k * 72} {x} {fy})"/>')
            a.circ(x, fy, r * 0.35, "#FFD84D")
    # fuzzy body
    body = a.shade("#FFFFFF", "#E8E0F8", "#A898D0")
    a.ell(100, 122, 14, 32, body, o, 3)
    a.circ(100, 88, 20, body, o, 3)
    # feathery antennae
    for sx in (1, -1):
        a.line(f"M{100 + sx * 8} 72 C{100 + sx * 16} 52 {100 + sx * 26} 44 {100 + sx * 36} 42", o, 2.5)
        for t in range(3):
            x0 = 100 + sx * (16 + t * 7)
            a.line(f"M{x0} {54 - t * 4} l{sx * 4} -7", o, 1.6)
    a.eyes(88, xs=(92, 108), rx=6, ry=7, iris="#B89AF0", pupil=("#2A1A4A", "#0A0614"), lashes=2)
    a.mouth(100, 98, "smile", w=4, color=o)
    a.cheeks([(86, 96), (114, 96)], rx=4, ry=3, dots=False)
    for x, y in ((30, 40), (172, 160), (162, 30)):
        a.sparkle(x, y, 5, "#E8D8FF")


@chordoo("mushroomba")
def mushroomba(a):
    o = "#5A1A2A"
    stem = a.shade("#FFFBF2", "#F5E6CC", "#C8B08A")
    a.ground(rx=46)
    # legs in a dance step
    a.path("M86 150 C80 162 70 168 62 176 L74 182 C84 172 94 164 98 156", stem, "#5A4A2A", 3)
    a.path("M110 154 L114 180 H128 L124 152", stem, "#5A4A2A", 3)
    a.ell(66, 180, 10, 5, "#8A3A2A", o, 2.5)
    a.ell(124, 182, 10, 5, "#8A3A2A", o, 2.5)
    # stem body
    a.path("M76 100 C72 130 78 160 100 162 C122 160 128 130 124 100 Z", stem, "#5A4A2A")
    # arms up
    a.line("M78 118 C64 108 56 96 52 82", "#5A4A2A", 8)
    a.line("M78 118 C64 108 56 96 52 82", "#F5E6CC", 4.5)
    a.line("M122 118 C140 120 150 112 158 102", "#5A4A2A", 8)
    a.line("M122 118 C140 120 150 112 158 102", "#F5E6CC", 4.5)
    # cap tilted
    a.add('<g transform="rotate(-10 100 80)">')
    a.path("M36 96 C36 40 164 40 164 96 C140 106 60 106 36 96 Z", a.shade("#C8A8FF", "#8A5AE0", "#4E2A9A"), "#2A1460", 3.5)
    for x, y, r in ((70, 66, 9), (106, 54, 10), (140, 74, 8), (90, 86, 6), (124, 90, 5), (52, 86, 5)):
        a.circ(x, y, r, "#FFF6D6")
    a.add('</g>')
    a.eyes(124, xs=(88, 112), kind="happy", rx=8)
    a.mouth(100, 138, "open", w=7, color="#7A3E2E")
    a.cheeks([(80, 134), (120, 134)], rx=7, ry=5)
    a.add('<text class="fx" x="160" y="70" font-size="22" fill="#8A5AE0">♪</text>')
    a.add('<text class="fx" x="24" y="140" font-size="18" fill="#8A5AE0">♫</text>')


@chordoo("barkley")
def barkley(a):
    bark = a.shade("#D8B48A", "#9A6A3E", "#5A3A1A")
    o = "#3A2410"
    a.ground(rx=66)
    # tail: leafy twig wagging
    a.line("M150 130 C166 118 172 100 168 86", o, 7)
    a.line("M150 130 C166 118 172 100 168 86", "#9A6A3E", 4)
    leaf(a, 168, 88, 22, -60, a.shade(*LEAF), w=2.5, vein=False)
    leaf(a, 166, 96, 20, -10, a.shade(*LEAF), w=2.5, vein=False)
    # body
    a.path("M54 146 C50 120 74 110 104 110 C136 110 156 120 154 146 C152 166 132 170 104 170 C76 170 56 166 54 146 Z", bark, o)
    for d in ("M80 120 C84 136 80 152 84 164", "M110 116 C106 134 112 150 108 166", "M134 122 C138 138 134 150 138 162"):
        a.line(d, "#5A3A1A", 2, 0.55)
    # legs
    for x in (66, 90, 122, 144):
        a.path(f"M{x - 9} 160 L{x - 9} 180 H{x + 9} L{x + 9} 160", bark, o, 3)
    # head
    a.path("M30 92 C30 62 56 50 78 52 C102 54 116 72 112 96 C108 122 86 130 64 128 C42 126 30 112 30 92 Z", bark, o)
    # ears = big leaves
    leaf(a, 42, 64, 38, 120, a.shade(*LEAF))
    leaf(a, 96, 60, 38, 70, a.shade(*LEAF))
    # muzzle
    a.ell(62, 108, 22, 14, "#E8C8A0", o, 3)
    a.ell(62, 100, 7, 5, "#2A1808")
    a.mouth(62, 110, "cat", w=6, color=o)
    a.eye(50, 86, rx=7, ry=9, iris="#7CC850", pupil=("#2A1808", "#0A0602"))
    a.eye(80, 86, rx=7, ry=9, iris="#7CC850", pupil=("#2A1808", "#0A0602"))
    a.cheeks([(38, 104), (88, 104)], rx=6, ry=4)
    # pinecone in mouth
    a.ell(48, 128, 9, 14, a.lin("#B87A3E", "#6E4220"), o, 2.5, rot=60)
    a.line("M38 124 L56 134 M42 120 L58 128 M40 130 L52 138", o, 1.4, 0.6)


@chordoo("willowisp")
def willowisp(a):
    o = "#1E4A4A"
    a.glow(100, 92, 76, "#A8FFE0", 0.55)
    # willow fronds hanging (hair)
    for i, x in enumerate(range(54, 150, 12)):
        ln = 70 + (i % 3) * 18
        a.line(f"M{x + 6} 70 C{x} {70 + ln * 0.5} {x + 10} {70 + ln * 0.8} {x + 2} {70 + ln}", "#4EA86A", 4)
        for k in range(1, 4):
            yy = 70 + ln * k / 4
            leaf(a, x + 4, yy, 12, 100 if k % 2 else 70, "#9AE08A", "#2E7A3A", 1.4, vein=False)
    # glowing body: wisp shape
    body = a.shade("#FFFFFF", "#C8FFF0", "#5ED8C0")
    a.path("M60 84 C60 50 140 50 140 84 C140 114 122 128 112 140 C106 150 112 160 102 170 C102 156 92 150 88 140 C78 128 60 114 60 84 Z", body, o)
    # canopy crown
    a.path("M54 76 C56 40 144 40 146 76 C134 66 120 70 112 62 C104 70 96 70 88 62 C80 70 66 66 54 76 Z", a.lin("#9AE08A", "#3E8A3E"), "#1E5A2A", 3)
    a.eyes(90, xs=(86, 114), kind="sleepy", rx=8)
    a.mouth(100, 104, "smile", w=6, color=o)
    a.cheeks([(76, 102), (124, 102)], "#7AE8C8", rx=7, ry=4, dots=False)
    for x, y in ((30, 60), (170, 90), (40, 150), (160, 150), (100, 26)):
        a.circ(x, y, 4, "#E8FFB0", extra=' class="fx"')
        a.glow(x, y, 10, "#E8FFB0", 0.7)


@chordoo("elderoak")
def elderoak(a):
    bark = a.shade("#C8A07A", "#8A6040", "#4A2E16")
    o = "#2A1808"
    a.ground(rx=78)
    # canopy
    can = a.shade("#C8F0A0", "#5EAA3E", "#2A6A22")
    for cx, cy, r in ((56, 60, 32), (144, 60, 32), (78, 38, 32), (122, 38, 32), (100, 52, 40)):
        a.circ(cx, cy, r, can, "#1E4A16", 3)
    # nest with a little bird
    a.ell(132, 34, 20, 9, a.lin("#C89A5A", "#7A522A"), "#4A2E10", 2.5)
    a.line("M114 32 L150 36 M118 38 L146 30", "#4A2E10", 1.5, 0.6)
    a.circ(132, 22, 9, a.shade("#BFE8FF", "#6AB8F0", "#2E78C0"), "#1E4A7A", 2.5)
    a.circ(134, 20, 1.8, INK)
    a.path("M140 22 L147 24 L140 26 Z", "#FFC83D", "#B8650F", 1.2)
    # trunk body
    a.path("M56 182 C60 150 58 112 66 88 C80 78 120 78 134 88 C142 112 140 150 144 182 Z", bark, o)
    # roots/feet
    for d in ("M56 182 C46 182 38 176 36 170", "M144 182 C154 182 162 176 164 170", "M90 182 C86 186 80 186 76 184"):
        a.line(d, o, 4)
    # bark grain
    for d in ("M74 100 C70 130 76 160 72 178", "M128 100 C132 130 126 160 130 178", "M100 150 C98 160 102 170 100 180"):
        a.line(d, "#4A2E16", 2.2, 0.6)
    # branch arms
    a.path("M64 116 C46 112 32 98 28 86 L36 82 C42 94 52 102 66 104", bark, o, 3)
    a.path("M136 116 C154 112 168 98 172 86 L164 82 C158 94 148 102 134 104", bark, o, 3)
    leaf(a, 30, 84, 18, -110, can, "#1E4A16", 2, False)
    leaf(a, 170, 84, 18, -70, can, "#1E4A16", 2, False)
    # wise face: bushy moss brows and beard
    a.path("M72 108 Q86 98 96 108 M104 108 Q114 98 128 108", "none", "#3E8A2E", 6)
    a.eyes(120, xs=(84, 116), kind="happy", rx=8)
    a.path("M78 136 C82 158 92 168 100 172 C108 168 118 158 122 136 C112 142 88 142 78 136 Z", a.lin("#A8E070", "#4E9A3A"), "#1E4A16", 2.5)
    a.mouth(100, 134, "smile", w=8, color=o)
    a.cheeks([(72, 128), (128, 128)], "#FF9A8A", rx=7, ry=4, dots=False)


@chordoo("gaiaflora")
def gaiaflora(a):
    fur = a.shade("#FFF2DE", "#E8C090", "#A87A48")
    o = "#4A2E14"
    a.glow(100, 100, 92, "#FFE8A8", 0.5)
    a.ground(rx=66)
    # flowers sprouting at feet
    for x, c in ((40, "#FF8AC0"), (162, "#FFD84D"), (128, "#B89AF0")):
        a.line(f"M{x} 184 V172", "#3E8A2E", 2.5)
        for k in range(5):
            a.add(f'<ellipse class="fx" cx="{x}" cy="{168}" rx="3" ry="5" fill="{c}" transform="rotate({k * 72} {x} 172)"/>')
        a.circ(x, 172, 2.5, "#FFF6D6", extra=' class="fx"')
    # legs (slender)
    for x in (70, 86, 124, 140):
        a.path(f"M{x - 5} 140 L{x - 4} 178 H{x + 4} L{x + 5} 140", fur, o, 3)
        a.ell(x, 179, 6, 3.5, "#5A3A1A")
    # body
    a.path("M56 132 C56 112 80 104 108 106 C136 108 152 118 150 138 C148 156 126 160 100 158 C76 156 56 150 56 132 Z", fur, o)
    for x, y in ((90, 122), (110, 118), (126, 128), (100, 138)):
        a.circ(x, y, 3.5, "#FFFBF2")
    a.path("M148 122 C158 116 162 124 156 130", "#FFFBF2", o, 2.5)
    # neck & head
    a.path("M62 124 C58 104 60 90 64 80 L84 84 C82 98 84 110 88 120 Z", fur, o, 3)
    a.path("M44 78 C44 60 60 52 74 54 C90 56 96 68 92 82 C88 96 74 100 62 100 C50 100 44 92 44 78 Z", fur, o)
    a.ell(48, 88, 8, 6, "#FFF2DE", o, 2)
    a.circ(42, 86, 3, "#3A2010")
    # ears
    a.ell(56, 54, 6, 12, fur, o, 2.5, rot=-40)
    a.ell(88, 56, 6, 12, fur, o, 2.5, rot=40)
    # antlers as flowering branches
    for sx, base in ((-1, 62), (1, 82)):
        bx = base
        a.line(f"M{bx} 54 C{bx + sx * 8} 40 {bx + sx * 6} 28 {bx + sx * 16} 16", "#7A5A2A", 4)
        a.line(f"M{bx + sx * 6} 38 C{bx + sx * 16} 34 {bx + sx * 22} 28 {bx + sx * 28} 30", "#7A5A2A", 3.5)
    for x, y, c in ((46, 16, "#FF8AC0"), (34, 30, "#FFD84D"), (98, 16, "#FFFFFF"), (110, 30, "#FF8AC0"), (60, 28, "#B89AF0"), (90, 30, "#FFD84D")):
        for k in range(5):
            a.add(f'<ellipse cx="{x}" cy="{y - 4}" rx="3.2" ry="5" fill="{c}" stroke="#A04A7A" stroke-width=".8" transform="rotate({k * 72} {x} {y})"/>')
        a.circ(x, y, 2.6, "#FFB03A")
    leaf(a, 80, 24, 14, -40, a.shade(*LEAF), w=1.6, vein=False)
    leaf(a, 64, 22, 14, -140, a.shade(*LEAF), w=1.6, vein=False)
    a.eye(72, 76, rx=7, ry=9, iris="#7CC850", pupil=("#2A1A0A", "#0A0602"), lashes=2, side=-1)
    a.cheeks([(78, 90)], rx=5, ry=3, dots=False)
    a.mouth(56, 94, "smile", w=4, color=o)
    # tail
    a.ell(152, 118, 6, 9, "#FFFBF2", o, 2.5, rot=30)
    for x, y in ((24, 60), (176, 70), (164, 40)):
        a.sparkle(x, y, 5)

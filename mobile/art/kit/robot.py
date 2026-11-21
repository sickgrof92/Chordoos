import math
from artkit import chordoo, INK
from shapes import limb, star, gear, flower

RB_O = "#2A3044"
METAL = ("#F4F6FC", "#BCC4D8", "#7A84A0")


def bolt_dot(a, x, y, r=2.5):
    a.circ(x, y, r, "#E8ECF8", RB_O, 1.4)


@chordoo("pixel")
def pixel(a):
    a.ground(rx=46)
    body = a.shade("#C8F0FF", "#6AC0F0", "#2A78C0")
    for x in (82, 118):
        limb(a, f"M{x} 150 V176", "#9AA4BC", RB_O, 9)
        a.path(f"M{x - 11} 174 H{x + 11} V182 H{x - 11} Z", "#3A4058", RB_O, 2)
    # boxy body
    a.path("M54 58 H146 V156 H54 Z", body, RB_O, 3.5)
    for x, y in ((60, 64), (140, 64), (60, 150), (140, 150)):
        bolt_dot(a, x, y)
    # screen face
    a.path("M66 70 H134 V122 H66 Z", "#1E2A3A", RB_O, 3)
    # pixel eyes and smile (squares)
    for x in (84, 108):
        a.path(f"M{x} 84 H{x + 8} V96 H{x} Z", "#6AFFB0")
    for x, y in ((80, 106), (88, 112), (96, 112), (104, 112), (112, 106)):
        a.path(f"M{x} {y} H{x + 8} V{y + 6} H{x} Z", "#6AFFB0")
    a.path("M72 74 H82 V78 H72 Z", "#FFFFFF", None, extra=' opacity=".4"')
    # buttons + antenna
    for x, c in ((80, "#FF6A7A"), (100, "#FFD84D"), (120, "#6AFFB0")):
        a.circ(x, 138, 5, c, RB_O, 2)
    a.line("M100 58 V40", RB_O, 3)
    a.circ(100, 36, 6, "#FF6A7A", RB_O, 2)
    limb(a, "M54 104 C40 104 34 94 34 84", "#9AA4BC", RB_O, 9)
    limb(a, "M146 104 C160 104 166 94 166 84", "#9AA4BC", RB_O, 9)
    a.circ(34, 80, 6, "#9AA4BC", RB_O, 2)
    a.circ(166, 80, 6, "#9AA4BC", RB_O, 2)
    a.add('<text class="fx" x="138" y="40" font-size="14" font-weight="bold" font-family="monospace" fill="#2A78C0">beep!</text>')


@chordoo("boltie")
def boltie(a):
    o = "#5A2A0A"
    a.ground(rx=40)
    tin = a.shade("#FFE0C0", "#FF9A4A", "#C85A14")
    # wind-up key on the back
    a.line("M146 110 H168", "#8A6A2A", 5)
    a.path("M168 92 C186 86 192 104 176 110 C192 116 186 134 168 128 Z", a.lin("#FFE88A", "#D8A020"), "#6A4A00", 2.5)
    # legs
    for x in (84, 116):
        a.path(f"M{x - 8} 150 H{x + 8} V176 H{x - 8} Z", "#C8CCD8", RB_O, 2.5)
        a.path(f"M{x - 12} 174 H{x + 12} V182 H{x - 12} Z", "#3A4058", RB_O, 2)
    # round tin body
    a.path("M56 100 C56 84 144 84 144 100 V148 C144 160 56 160 56 148 Z", tin, o, 3.5)
    a.line("M56 110 H144 M56 140 H144", "#C85A14", 2, 0.6)
    for x in range(64, 144, 12):
        bolt_dot(a, x, 125, 2)
    # dome head
    a.path("M66 92 C66 50 134 50 134 92 Z", a.shade("#F0F6FF", "#B8C8E8", "#7A88B0"), RB_O, 3.5)
    a.eyes(76, xs=(86, 114), kind="sleepy", rx=8)
    a.mouth(100, 84, "smile", w=5, color=RB_O)
    a.cheeks([(76, 84), (124, 84)], rx=5, ry=3, dots=False)
    a.line("M100 54 V42", RB_O, 3)
    a.circ(100, 38, 5, "#FFD84D", RB_O, 2)
    # arms with pincers
    limb(a, "M58 112 L40 128", "#C8CCD8", RB_O, 8)
    limb(a, "M142 112 L156 134", "#C8CCD8", RB_O, 8)
    a.add('<text class="fx" x="22" y="56" font-size="18" font-weight="bold" font-family="sans-serif" fill="#8A78C8">z</text>')
    a.add('<text class="fx" x="34" y="42" font-size="13" font-weight="bold" font-family="sans-serif" fill="#8A78C8">z</text>')


@chordoo("gizmo")
def gizmo(a):
    o = "#3A1A0A"
    a.ground(rx=56)
    for x in (62, 86, 114, 138):
        a.line(f"M{x} 150 L{x + (x - 100) * 0.2} 168 L{x + (x - 100) * 0.3} 180", "#6A5030", 4)
    # brass shell halves slightly open showing gears
    a.path("M40 150 C40 104 70 80 100 80 C130 80 160 104 160 150 Z", "#3A2A1A", o, 3)
    gear(a, 80, 124, 18, "#D8A848", "#6A4A10")
    gear(a, 116, 118, 14, "#E8C060", "#6A4A10", 7)
    gear(a, 106, 142, 10, "#C89030", "#6A4A10", 6)
    br = a.shade("#FFD8C0", "#E8604A", "#A02A1A")
    a.path("M40 150 C38 112 56 84 96 80 C84 100 76 124 74 152 Z", br, o, 3)
    a.path("M160 150 C162 112 144 84 104 80 C116 100 124 124 126 152 Z", br, o, 3)
    for x, y in ((56, 112), (62, 136), (144, 112), (138, 136)):
        a.circ(x, y, 6, "#2A1A1A")
    a.gloss(58, 100, 8, 4)
    # head
    a.path("M70 82 C70 54 130 54 130 82 Z", a.shade("#E8D8B8", "#B89A60", "#7A5A20"), o, 3)
    a.eyes(72, xs=(88, 112), kind="white", rx=8, ry=9, pupil=("#3A2A1A", "#0A0806"))
    a.circ(88, 72, 11, "none", "#B89A60", 2.5)
    a.circ(112, 72, 11, "none", "#B89A60", 2.5)
    a.line("M88 58 C84 44 78 40 72 40 M112 58 C116 44 122 40 128 40", o, 2.5)
    a.circ(72, 40, 4, "#E8604A", o, 1.5)
    a.circ(128, 40, 4, "#E8604A", o, 1.5)
    # wind key on top
    a.line("M100 54 V40", "#8A6A2A", 4)
    a.path("M90 30 C88 20 112 20 110 30 C112 40 88 40 90 30 Z", "#FFD84D", "#6A4A00", 2)
    a.add('<text class="fx" x="134" y="58" font-size="12" font-weight="bold" font-family="sans-serif" fill="#B89A60">tick tock</text>')


@chordoo("sprocket")
def sprocket(a):
    o = RB_O
    met = a.shade(*METAL)
    a.ground(rx=60)
    # tail antenna wagging
    a.line("M148 120 L170 92", o, 3)
    a.circ(172, 88, 5, "#6AFFB0", o, 2)
    # legs (pistons)
    for x in (66, 90, 118, 142):
        a.path(f"M{x - 6} 140 H{x + 6} V174 H{x - 6} Z", "#9AA4BC", o, 2.5)
        a.ell(x, 178, 11, 5, "#3A4058", o, 2)
    # body
    a.path("M54 112 C54 102 62 98 72 98 H140 C150 98 156 104 156 114 V136 C156 146 150 150 140 150 H70 C60 150 54 146 54 136 Z", met, o, 3.5)
    a.path("M76 112 H132 V128 H76 Z", "#3A4058", o, 2)
    a.path("M80 120 H96 L100 114 L104 126 L108 120 H128", "none", "#6AFFB0", 2)
    # head
    a.path("M20 74 C20 56 34 48 52 48 C74 48 86 58 86 76 C86 96 72 106 52 106 C34 106 20 94 20 74 Z", met, o, 3.5)
    # gear ears
    gear(a, 26, 50, 14, "#FFC83A", "#6A4A00", 8)
    gear(a, 80, 48, 14, "#FFC83A", "#6A4A00", 8)
    a.eye(42, 74, kind="glow", rx=9, ry=10, iris="#6AE8FF", pupil=("#1A3A5A", "#06121C"))
    a.eye(66, 74, kind="glow", rx=9, ry=10, iris="#6AE8FF", pupil=("#1A3A5A", "#06121C"))
    a.ell(52, 94, 10, 6, "#3A4058", o, 2)
    a.mouth(52, 98, "smile", w=5, color="#FFFFFF")
    a.cheeks([(28, 90), (80, 90)], rx=5, ry=3, dots=False)
    # screw in mouth (fetching)
    a.line("M60 102 L76 110", "#C8CCD8", 4)
    a.path("M74 106 L82 112 L78 116 Z", "#C8CCD8", o, 1.5)


@chordoo("rustle")
def rustle(a):
    o = "#4A2410"
    rust = a.shade("#F0C8A0", "#C8784A", "#8A4A22")
    a.ground(rx=48)
    # flower pot it tends
    a.path("M136 150 H176 L170 182 H142 Z", "#D86A3A", "#6A2A0A", 2.5)
    a.line("M156 150 V120", "#3E8A2E", 3)
    flower(a, 156, 112, 14, "#FFB0D0", "#FFD84D", "#A04A7A")
    # legs
    for x in (74, 102):
        a.path(f"M{x - 8} 150 H{x + 8} V176 H{x - 8} Z", rust, o, 2.5)
        a.ell(x, 180, 12, 5, "#5A3A2A")
    # body + rust patches
    a.path("M50 96 H126 V156 H50 Z", rust, o, 3.5)
    for x, y, r in ((62, 140, 7), (112, 108, 6), (98, 146, 5)):
        a.circ(x, y, r, "#8A4A22", extra=' opacity=".5"')
    a.path("M70 112 H106 V136 H70 Z", "#E8D8B8", o, 2)
    a.circ(80, 124, 4, "#3E8A2E")
    a.circ(96, 124, 4, "#FF8AB0")
    # watering-can arm
    limb(a, "M124 116 L138 102", "#C8784A", o, 8)
    a.path("M132 84 H152 V100 H132 Z", "#6AC8FF", "#1E5A8A", 2)
    a.line("M152 88 L164 80", "#1E5A8A", 3)
    a.add('<path class="fx" d="M166 82 l2 6 M170 80 l4 6 M164 86 l0 6" stroke="#6AC8FF" stroke-width="2" stroke-linecap="round"/>')
    limb(a, "M52 116 L38 132", "#C8784A", o, 8)
    # head
    a.path("M54 56 H122 V96 H54 Z", rust, o, 3.5)
    a.eyes(76, xs=(74, 102), rx=8, ry=9, kind="white", pupil=("#3A2A1A", "#0A0806"))
    a.mouth(88, 88, "smile", w=6, color=o)
    a.cheeks([(62, 88), (114, 88)], rx=5, ry=3, dots=False)
    # little flower on head
    a.line("M88 56 V40", "#3E8A2E", 3)
    flower(a, 88, 36, 10, "#FFD84D", "#FF8A3A", "#8A5A00")
    for x, y in ((58, 60), (118, 60), (58, 92), (118, 92)):
        bolt_dot(a, x, y, 2)


@chordoo("clank")
def clank(a):
    o = RB_O
    a.ground(rx=54)
    can = a.lin("#9AA4BC", "#E8ECF8", "#8A94AC", x2=1, y2=0)
    # treads
    a.path("M40 162 H160 C170 162 170 182 160 182 H40 C30 182 30 162 40 162 Z", "#3A4058", o, 3)
    for x in (48, 74, 100, 126, 152):
        a.circ(x, 172, 6, "#9AA4BC", o, 2)
    # can body
    a.path("M54 70 H146 L140 164 H60 Z", can, o, 3.5)
    for x in (74, 100, 126):
        a.line(f"M{x} 76 L{x + (x - 100) * 0.06:.0f} 158", "#7A84A0", 2.5, 0.6)
    # recycle sign
    a.add('<path d="M100 118 l8 14 h-16 z" fill="none" stroke="#3AB86A" stroke-width="3" stroke-linejoin="round"/>')
    a.circ(100, 127, 16, "none", "#3AB86A", 2.5)
    # lid hat, flipped open
    a.path("M48 62 L148 50 L150 58 L50 70 Z", "#BCC4D8", o, 3)
    a.path("M92 54 C92 44 108 42 110 52", "none", o, 3)
    # eyes peeking under lid
    a.eyes(88, xs=(84, 116), kind="glow", rx=9, ry=10, iris="#FFD84D", pupil=("#2A3044", "#0A0E18"))
    a.mouth(100, 104, "smile", w=6, color=o)
    # arms grabbing recyclables
    limb(a, "M56 100 C40 96 30 84 28 72", "#9AA4BC", o, 9)
    a.path("M16 54 H34 V74 H16 Z", "#6AC8FF", "#1E5A8A", 2, ' opacity=".9"')
    a.path("M20 50 H30 V54 H20 Z", "#1E5A8A")
    limb(a, "M144 100 C160 96 168 86 170 76", "#9AA4BC", o, 9)
    a.path("M160 56 C164 50 180 50 182 58 L178 76 H164 Z", "#E8303A", "#6A0A14", 2)


@chordoo("drono")
def drono(a):
    o = RB_O
    a.ground(rx=34, cy=190)
    # rotors
    for x in (40, 160):
        a.line(f"M{x} 66 V82", o, 3)
        a.ell(x, 62, 30, 5, "#C8D4F0", o, 2, extra=' opacity=".8"')
        a.circ(x, 62, 4, "#3A4058")
    a.line("M40 84 H160", o, 6)
    a.line("M40 84 H160", "#BCC4D8", 3)
    # puppy-ish body
    body = a.shade("#FFFFFF", "#FFE0A8", "#E8A040")
    a.path("M56 90 C56 70 144 70 144 90 V126 C144 146 56 146 56 126 Z", body, "#6A4200", 3.5)
    # floppy ear flaps
    a.path("M56 92 C40 96 38 120 48 128 C54 118 56 106 60 100 Z", "#C8883A", "#6A4200", 3)
    a.path("M144 92 C160 96 162 120 152 128 C146 118 144 106 140 100 Z", "#C8883A", "#6A4200", 3)
    a.eyes(106, xs=(82, 118), rx=11, ry=13, iris="#8A5A2A", pupil=("#2A1A0A", "#0A0602"))
    a.ell(100, 122, 6, 4, "#3A2010")
    a.mouth(100, 126, "open", w=6, color="#7A3E2E")
    a.cheeks([(70, 124), (130, 124)], rx=6, ry=4)
    # package (hug) hanging
    a.line("M90 144 V156 M110 144 V156", "#8A6A3A", 2)
    a.path("M80 156 H120 V184 H80 Z", a.lin("#E8C890", "#C89A5A"), "#6A4A1A", 2.5)
    a.add('<path d="M100 178 C88 170 90 162 100 167 C110 162 112 170 100 178 Z" fill="#FF6A8A"/>')


@chordoo("mechanix")
def mechanix(a):
    o = RB_O
    a.ground(rx=46)
    met = a.shade("#E8F0FF", "#8AA8E0", "#3A5AA8")
    # shelf with a cookie jar at the top
    a.path("M140 30 H196 V36 H140 Z", "#A8784A", "#5A3A1A", 2)
    a.path("M150 12 H170 V30 H150 Z", "#C8E8FF", "#2A5A8A", 2)
    a.circ(160, 21, 4, "#C89A5A")
    # legs
    for x in (82, 118):
        a.path(f"M{x - 9} 150 H{x + 9} V176 H{x - 9} Z", "#9AA4BC", o, 2.5)
        a.path(f"M{x - 13} 174 H{x + 13} V182 H{x - 13} Z", "#3A4058", o, 2)
    # body
    a.path("M58 92 H142 V154 H58 Z", met, o, 3.5)
    gear(a, 100, 124, 14, "#FFC83A", "#6A4A00", 8)
    # telescoping arm reaching up
    for i, (x1, y1, x2, y2, w) in enumerate(((140, 104, 152, 80, 14), (152, 80, 160, 58, 11), (160, 58, 164, 40, 8))):
        a.line(f"M{x1} {y1} L{x2} {y2}", o, w + 4)
        a.line(f"M{x1} {y1} L{x2} {y2}", ["#9AA4BC", "#BCC4D8", "#E0E4EE"][i], w)
    a.path("M158 40 L164 30 L172 38", "none", o, 3)
    limb(a, "M60 110 L42 134", "#9AA4BC", o, 12)
    # head
    a.path("M64 50 H136 V92 H64 Z", met, o, 3.5)
    a.path("M72 58 H128 V82 H72 Z", "#1E2A3A", o, 2)
    a.eye(88, 70, kind="glow", rx=7, ry=8, iris="#6AE8FF", pupil=("#1A3A5A", "#06121C"))
    a.eye(112, 70, kind="glow", rx=7, ry=8, iris="#6AE8FF", pupil=("#1A3A5A", "#06121C"))
    a.mouth(100, 84, "smile", w=6, color="#6AE8FF")
    a.line("M76 50 V40 M124 50 V40", o, 3)
    a.circ(76, 38, 4, "#FF6A7A", o, 1.5)
    a.circ(124, 38, 4, "#FFD84D", o, 1.5)


@chordoo("cyberpaw")
def cyberpaw(a):
    o = "#141A2A"
    met = a.shade("#E8ECFF", "#A0A8D0", "#50587A")
    a.ground(rx=56)
    # tail: segmented cable
    for i in range(6):
        t = i / 5
        x = 140 + 30 * math.sin(t * 2.2)
        y = 150 - t * 60
        a.circ(round(x, 1), round(y, 1), 7 - t * 2, "#A0A8D0", o, 2)
    a.circ(164, 86, 5, "#FF6AD8", o, 2)
    # body sitting
    a.path("M58 150 C54 120 74 104 100 104 C126 104 146 120 142 150 C140 170 124 180 100 180 C76 180 60 170 58 150 Z", met, o)
    a.path("M84 128 H116 V150 H84 Z", "#1E2A3A", o, 2)
    a.add('<text x="87" y="144" font-size="10" font-family="monospace" fill="#6AFFB0">0101</text>')
    for x in (80, 120):
        a.ell(x, 178, 13, 6, "#50587A", o, 2.5)
    # head
    a.path("M56 80 C56 54 76 44 100 44 C124 44 144 54 144 80 C144 104 126 114 100 114 C74 114 56 104 56 80 Z", met, o)
    a.path("M64 58 L60 24 L88 48 Z", met, o, 3)
    a.path("M136 58 L140 24 L112 48 Z", met, o, 3)
    a.path("M66 52 L64 34 L80 46 Z", "#FF6AD8", None)
    a.path("M134 52 L136 34 L120 46 Z", "#FF6AD8", None)
    # visor eyes
    a.path("M68 66 H132 C134 84 126 90 100 90 C74 90 66 84 68 66 Z", "#1E2A3A", o, 2.5)
    a.path("M78 78 Q86 70 94 78 M106 78 Q114 70 122 78", "none", "#6AFFE8", 3.5)
    a.path("M96 96 L104 96 L100 100 Z", "#FF6AD8")
    a.mouth(100, 102, "cat", w=5, color=o)
    # LED whiskers
    for sx in (1, -1):
        for k, c in ((-4, "#6AFFE8"), (4, "#FF6AD8")):
            a.line(f"M{100 + sx * 22} {98 + k * 0.5} L{100 + sx * 50} {94 + k * 2}", c, 2.5)
            a.circ(100 + sx * 50, 94 + k * 2, 2.5, c, extra=' class="fx"')


@chordoo("rocketto")
def rocketto(a):
    o = "#3A1A2A"
    a.ground(rx=40, cy=190)
    # exhaust flame
    a.path("M84 152 C80 170 92 186 100 196 C108 186 120 170 116 152 Z", a.lin("#FFF6A8", "#FF9A3A", "#FF4A3A"), None, extra=' class="fx"')
    # fins
    a.path("M64 120 C44 128 38 150 42 164 L70 150 Z", "#E8303A", "#6A0A14", 3)
    a.path("M136 120 C156 128 162 150 158 164 L130 150 Z", "#E8303A", "#6A0A14", 3)
    # body
    a.path("M100 12 C130 30 142 80 136 152 H64 C58 80 70 30 100 12 Z", a.lin("#FFFFFF", "#E8ECF8", "#B8C0D8", x2=1, y2=0), "#3A4058", 3.5)
    a.path("M100 12 C114 20 124 34 130 50 H70 C76 34 86 20 100 12 Z", "#E8303A", "#6A0A14", 3)
    a.path("M66 140 H134 V152 H66 Z", "#3A4058", None)
    # window face
    a.circ(100, 92, 26, "#3A4058", "#3A4058", 3)
    a.circ(100, 92, 21, a.shade("#E8FAFF", "#8AD8F0", "#3A98C8"))
    a.eyes(88, xs=(91, 109), rx=6, ry=8, iris="#3A98C8", pupil=("#1A2A4A", "#060A14"))
    a.mouth(100, 102, "open", w=5, color="#7A3E4E")
    a.cheeks([(82, 100), (118, 100)], rx=4, ry=3, dots=False)
    a.gloss(88, 80, 6, 3)
    # countdown
    a.add('<text class="fx" x="150" y="50" font-size="22" font-weight="bold" font-family="sans-serif" fill="#E8303A">3</text>')
    a.add('<text class="fx" x="164" y="80" font-size="18" font-weight="bold" font-family="sans-serif" fill="#FF9A3A">2</text>')
    a.add('<text class="fx" x="172" y="104" font-size="14" font-weight="bold" font-family="sans-serif" fill="#FFC83A">1</text>')
    for x, y in ((30, 40), (34, 100)):
        star(a, x, y, 5, "#FFE88A", None, cls="fx")


@chordoo("megabyte")
def megabyte(a):
    o = "#141E3A"
    a.ground(rx=80)
    arm = a.shade("#FFF0C8", "#FFC83A", "#C88A00")
    body = a.shade("#E8F0FF", "#5A8AE8", "#1E3A98")
    # legs
    for x in (66, 134):
        a.path(f"M{x - 16} 140 H{x + 16} L{x + 18} 174 H{x - 18} Z", body, o, 3)
        a.path(f"M{x - 22} 172 H{x + 22} V184 H{x - 22} Z", "#3A4058", o, 2.5)
    # big shoulders + arms
    for sx in (1, -1):
        a.circ(100 + sx * 66, 74, 20, arm, o, 3)
        a.path(f"M{100 + sx * 58} 90 H{100 + sx * 82} V140 H{100 + sx * 58} Z", body, o, 3)
        a.circ(100 + sx * 70, 148, 14, "#9AA4BC", o, 3)
    # torso with cockpit
    a.path("M42 56 H158 L150 146 H50 Z", body, o, 3.5)
    a.path("M60 46 C60 20 140 20 140 46 V104 H60 Z", a.fade("#BFE8FF", 0.45), o, 3)
    # pilot kid inside cockpit
    a.circ(100, 76, 18, a.shade("#FFE8D8", "#F0C8A8", "#C8987A"), "#6A4A30", 2)
    a.path("M82 72 C82 52 118 52 118 72 C110 64 90 64 82 72 Z", "#E8303A", "#6A0A14", 2)
    a.eyes(76, xs=(93, 107), rx=4, ry=5, iris="#5A8AE8", pupil=("#2A1A0A", "#0A0602"), kind="star")
    a.mouth(100, 86, "smile", w=4, color="#7A3E2E")
    a.path("M68 34 C76 26 88 24 98 24", "none", "#FFFFFF", 3, ' opacity=".8"')
    # robot face below cockpit
    a.path("M72 112 H128 V136 H72 Z", "#1E2A3A", o, 2)
    a.eye(88, 124, kind="glow", rx=6, ry=6, iris="#FFD84D", pupil=("#1E2A3A", "#0A0E18"))
    a.eye(112, 124, kind="glow", rx=6, ry=6, iris="#FFD84D", pupil=("#1E2A3A", "#0A0E18"))
    a.add('<path d="M100 150 C90 142 92 136 100 140 C108 136 110 142 100 150 Z" fill="#FF6A8A"/>')


@chordoo("steamdrake")
def steamdrake(a):
    o = "#3A2008"
    brass = a.shade("#FFE8B0", "#D8A048", "#8A5A14")
    cop = a.shade("#FFD0B0", "#C87A4A", "#7A3A14")
    a.ground(rx=66)
    # steam rings
    for x, y, r in ((40, 40, 10), (24, 22, 7), (60, 26, 6)):
        a.circ(x, y, r, "none", "#C8C0C0", 4, extra=' class="fx"')
    # wings: riveted brass frames with canvas
    for sx in (1, -1):
        a.path(f"M{100 + sx * 20} 100 L{100 + sx * 60} 46 L{100 + sx * 90} 70 L{100 + sx * 70} 110 Z", a.lin("#F6ECD8", "#D8C8A8"), o, 3)
        a.line(f"M{100 + sx * 20} 100 L{100 + sx * 60} 46 L{100 + sx * 90} 70", "#8A5A14", 5)
        a.line(f"M{100 + sx * 40} 100 L{100 + sx * 75} 58", "#8A5A14", 3)
    # tail with gear tip
    a.path("M130 160 C160 170 180 156 180 136", "none", o, 14)
    a.path("M130 160 C160 170 180 156 180 136", "none", "#C87A4A", 9)
    gear(a, 180, 130, 12, "#D8A048", "#6A4A00", 7)
    # body boiler
    a.path("M62 178 C54 146 64 110 100 108 C136 110 146 146 138 178 Z", cop, o)
    for y in (130, 150, 168):
        a.line(f"M{66 + (178 - y) * 0.06:.0f} {y} H{134 - (178 - y) * 0.06:.0f}", "#8A5A14", 4)
    gear(a, 100, 142, 14, "#FFE8B0", "#6A4A00", 8)
    for x in (80, 120):
        a.ell(x, 180, 14, 6, "#8A5A14", o, 2.5)
    # head with goggles + chimney horns
    a.path("M60 76 C58 46 80 34 100 34 C120 34 142 46 140 76 C138 98 122 108 100 108 C78 108 62 98 60 76 Z", brass, o)
    a.path("M72 40 V20 H84 V40 Z M116 40 V20 H128 V40 Z", "#5A4A3A", o, 2.5)
    a.line("M70 20 H86 M114 20 H130", o, 4)
    a.line("M62 70 H138", "#5A3A1A", 5)
    for x in (84, 116):
        a.circ(x, 70, 14, "#8A5A14", o, 3)
        a.circ(x, 70, 10, a.shade("#E8FFF8", "#8AE0C8", "#3A9A88"))
        a.eye(x, 71, rx=5, ry=6, iris="#3A9A88", pupil=("#1A2A2A", "#060A0A"))
    a.ell(100, 94, 20, 10, "#C87A4A", o, 2.5)
    a.circ(92, 92, 2, o)
    a.circ(108, 92, 2, o)
    a.mouth(100, 100, "smile", w=6, color=o)


@chordoo("chronotron")
def chronotron(a):
    o = "#2A1A0A"
    a.glow(100, 90, 92, "#FFE8A8", 0.45)
    a.ground(rx=56)
    gold = a.shade("#FFF6C8", "#E8B840", "#A87A10")
    # clock-hand wings
    for sx in (1, -1):
        for k, (ln, ang) in enumerate(((84, -30), (64, 0), (50, 28))):
            g = f'<g transform="translate({100 + sx * 30} 96) scale({sx} 1) rotate({ang})">'
            g += f'<path d="M0 -5 L{ln * 0.7} -5 L{ln * 0.72} -12 L{ln} 0 L{ln * 0.72} 12 L{ln * 0.7} 5 L0 5 Z" fill="{["#3A2A4A", "#5A4A6A", "#7A6A8A"][k]}" stroke="{o}" stroke-width="2.5" stroke-linejoin="round"/></g>'
            a.add(g)
    # legs
    for x in (84, 116):
        a.path(f"M{x - 8} 150 H{x + 8} V176 H{x - 8} Z", gold, o, 2.5)
        a.path(f"M{x - 12} 174 H{x + 12} V182 H{x - 12} Z", "#3A2A4A", o, 2)
    # body: pendulum case
    a.path("M70 120 H130 V160 H70 Z", a.lin("#7A4A2A", "#4A2A10"), o, 3)
    a.line("M100 120 V146", "#E8B840", 2.5)
    a.circ(100, 150, 7, gold, o, 2)
    # clock face head
    a.circ(100, 76, 48, gold, o, 3.5)
    a.circ(100, 76, 38, "#FFFBF0", o, 2.5)
    for k in range(12):
        ang = math.radians(k * 30)
        x1, y1 = 100 + 33 * math.sin(ang), 76 - 33 * math.cos(ang)
        x2, y2 = 100 + 37 * math.sin(ang), 76 - 37 * math.cos(ang)
        a.line(f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}", o, 2.5 if k % 3 == 0 else 1.4)
    # hands pointing at bedtime (8 o'clock) as nose
    a.line("M100 76 L100 52", o, 3)
    a.line("M100 76 L80 88", o, 4)
    a.eyes(70, xs=(84, 116), rx=7, ry=8, iris="#A87A10", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(100, 96, "smile", w=8, color=o)
    a.cheeks([(76, 88), (124, 88)], "#FF9AA8", rx=6, ry=4, dots=False)
    a.circ(100, 76, 3, o)
    # bells on top
    for x in (68, 132):
        a.path(f"M{x - 12} 34 C{x - 12} 16 {x + 12} 16 {x + 12} 34 Z", gold, o, 2.5)
    for x, y in ((20, 30), (180, 30), (24, 160)):
        a.sparkle(x, y, 6)

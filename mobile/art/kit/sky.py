from artkit import chordoo, INK

SKY_O = "#2A4A7A"


def cloud(a, cx, cy, s, fill, o=SKY_O, w=3, cls=""):
    """Puffy cloud centred on (cx, cy), roughly 2s wide."""
    c = f' class="{cls}"' if cls else ""
    a.add(f'<path{c} d="M{cx - s} {cy + s * 0.3} C{cx - s * 1.2} {cy - s * 0.1} {cx - s * 0.8} {cy - s * 0.5} {cx - s * 0.5} {cy - s * 0.3} '
          f'C{cx - s * 0.4} {cy - s * 0.8} {cx + s * 0.2} {cy - s * 0.9} {cx + s * 0.3} {cy - s * 0.4} '
          f'C{cx + s * 0.7} {cy - s * 0.6} {cx + s * 1.2} {cy - s * 0.2} {cx + s} {cy + s * 0.3} '
          f'C{cx + s * 0.6} {cy + s * 0.55} {cx - s * 0.6} {cy + s * 0.55} {cx - s} {cy + s * 0.3} Z" '
          f'fill="{fill}" stroke="{o}" stroke-width="{w}" stroke-linejoin="round"/>')


@chordoo("nimbo")
def nimbo(a):
    body = a.shade("#FFFFFF", "#EAF2FF", "#A8C0E8")
    a.ground(rx=46)
    # little rain under it
    for x in (76, 98, 120):
        a.path(f"M{x} 150 C{x + 4} 158 {x + 4} 162 {x} 164 C{x - 4} 162 {x - 4} 158 {x} 150 Z", "#8AD0FF", "#3A8AD0", 1.6)
    a.path("M30 120 C18 96 40 70 62 80 C66 52 104 42 120 66 C140 50 172 66 166 92 C186 98 184 132 160 136 "
           "C140 146 60 146 40 136 C30 132 28 126 30 120 Z", body, "#6A88C0", 3.5)
    a.eyes(104, xs=(82, 118), rx=10, ry=12, iris="#8AB8FF", pupil=("#2A3A6A", "#0A1430"))
    a.mouth(100, 122, "o", w=8, color="#5A3E6E")
    a.cheeks([(64, 118), (136, 118)], "#FF8FB0", rx=12, ry=7)
    a.gloss(66, 82, 12, 6)
    a.sparkle(170, 40, 6, "#FFE14D")


@chordoo("kitezy")
def kitezy(a):
    o = "#6A1A4A"
    a.ground(cx=110, rx=26)
    # ribbon tail with bows
    a.line("M100 160 C80 170 120 180 96 192", o, 3)
    for x, y, c in ((92, 168, "#FFD84D"), (108, 178, "#5AC8FF")):
        a.path(f"M{x} {y} L{x - 8} {y - 5} L{x - 8} {y + 5} Z M{x} {y} L{x + 8} {y - 5} L{x + 8} {y + 5} Z", c, o, 2)
    # diamond kite body in four colored panels
    top, left, right, bot = (100, 18), (40, 86), (160, 86), (100, 162)
    for (p1, p2, c) in ((top, left, "#FF6A9A"), (top, right, "#FFD84D"), (left, bot, "#5AC8FF"), (right, bot, "#8AE06A")):
        a.path(f"M100 86 L{p1[0]} {p1[1]} L{p2[0]} {p2[1]} Z", c, None)
    a.path("M100 18 L160 86 L100 162 L40 86 Z", "none", o, 3.5)
    a.line("M100 18 V162 M40 86 H160", o, 2, 0.6)
    a.gloss(80, 56, 10, 5)
    a.eyes(80, xs=(84, 116), rx=10, ry=12, iris="#FF6A9A", pupil=("#3A1A2A", "#120610"))
    a.mouth(100, 100, "open", w=8, color="#7A2A3E")
    a.cheeks([(70, 98), (130, 98)], rx=8, ry=5)
    # wind swoosh
    a.line("M150 30 Q170 24 180 34 M156 44 Q172 40 184 48", "#8AB8E8", 3, 0.8)


@chordoo("breezle")
def breezle(a):
    fur = a.shade("#F5E0C8", "#C8986A", "#8A5E3A")
    o = "#4A2E16"
    a.ground(rx=36, cy=188)
    # leaf glider held above
    a.path("M20 70 C40 30 160 30 180 70 C150 62 120 72 100 64 C80 72 50 62 20 70 Z", a.shade("#FFE8A8", "#FFAA3A", "#C85A14"), "#7A3A0A", 3)
    a.line("M24 68 C70 48 130 48 176 68", "#7A3A0A", 2, 0.5)
    for x in (60, 100, 140):
        a.line(f"M{x} 56 L{x + (100 - x) * 0.2} 70", "#7A3A0A", 1.6, 0.4)
    # gliding membrane body (stretched)
    a.path("M46 104 C60 94 80 90 100 92 C120 90 140 94 154 104 C150 124 136 150 100 156 C64 150 50 124 46 104 Z", fur, o)
    a.path("M80 112 C80 104 120 104 120 112 C122 134 110 148 100 148 C90 148 78 134 80 112 Z", "#FFF2E0")
    # arms holding leaf
    a.line("M54 102 L38 70", o, 8)
    a.line("M54 102 L38 70", "#C8986A", 4.5)
    a.line("M146 102 L162 70", o, 8)
    a.line("M146 102 L162 70", "#C8986A", 4.5)
    # bushy tail
    a.path("M100 154 C96 170 110 182 124 178 C112 176 110 168 116 160 Z", fur, o, 3)
    # head
    a.circ(100, 96, 24, fur, o, 3.5)
    a.ell(82, 74, 7, 10, fur, o, 3, rot=-20)
    a.ell(118, 74, 7, 10, fur, o, 3, rot=20)
    a.ell(82, 75, 3, 5, "#FFB0A0", rot=-20)
    a.ell(118, 75, 3, 5, "#FFB0A0", rot=20)
    a.eyes(94, xs=(90, 110), rx=7, ry=9, iris="#C8986A", pupil=("#2A1808", "#0A0602"))
    a.circ(100, 104, 2.5, "#3A2010")
    a.mouth(100, 108, "cat", w=5, color=o)
    a.cheeks([(82, 106), (118, 106)], rx=5, ry=3, dots=False)
    a.line("M30 130 Q44 124 52 132 M150 140 Q162 134 172 140", "#A8C8F0", 3, 0.8)


@chordoo("hootsie")
def hootsie(a):
    feat = a.shade("#E8DEFF", "#A890D8", "#6A54A8")
    o = "#2E2060"
    a.ground(rx=42)
    a.ell(100, 128, 48, 52, feat, o)
    a.path("M70 130 C70 112 130 112 130 130 C132 160 116 174 100 174 C84 174 68 160 70 130 Z", "#F5F0FF")
    for y in (134, 146, 158):
        for x in (88, 100, 112):
            a.path(f"M{x - 4} {y} Q{x} {y + 4} {x + 4} {y}", "none", "#B8A8E0", 1.6)
    # wings
    a.path("M54 112 C40 124 40 148 56 160 C58 140 60 124 54 112 Z", feat, o, 3)
    a.path("M146 112 C160 124 160 148 144 160 C142 140 140 124 146 112 Z", feat, o, 3)
    # feet
    a.path("M86 176 l-4 6 M90 176 v7 M94 176 l4 6 M106 176 l-4 6 M110 176 v7 M114 176 l4 6", "none", "#E09A2A", 3)
    # face disc
    a.ell(84, 106, 18, 17, "#FFFFFF", None)
    a.ell(116, 106, 18, 17, "#FFFFFF", None)
    a.eyes(106, xs=(84, 116), kind="sleepy", rx=10)
    a.mouth(100, 116, "beak", w=6)
    # nightcap
    a.path("M56 86 C60 52 100 36 128 50 C150 60 162 80 170 100 C150 92 140 84 136 80 C120 74 80 76 56 86 Z", a.lin("#5AA8FF", "#2A5AC8"), "#1A2A6A", 3)
    for x, y in ((90, 60), (118, 58), (140, 76), (74, 74)):
        a.sparkle(x, y, 4, "#FFE14D")
    a.circ(170, 104, 8, "#FFFFFF", "#1A2A6A", 2.5)
    a.path("M52 84 C80 74 120 74 142 84 L140 92 C118 84 82 84 54 92 Z", "#FFFFFF", "#1A2A6A", 2.5)
    a.add('<text class="fx" x="150" y="40" font-size="20" font-weight="bold" fill="#8A78C8">z</text>')
    a.add('<text class="fx" x="166" y="24" font-size="14" font-weight="bold" fill="#8A78C8">z</text>')


@chordoo("zephyrin")
def zephyrin(a):
    o = "#1E6A7A"
    a.glow(100, 100, 80, "#B8F4FF", 0.5)
    body = a.shade("#FFFFFF", "#C8F4FF", "#6AC8E0")
    # swirling tail spiral
    a.path("M100 120 C140 130 150 160 120 172 C96 182 76 166 86 150 C94 138 112 144 108 156", "none", o, 9)
    a.path("M100 120 C140 130 150 160 120 172 C96 182 76 166 86 150 C94 138 112 144 108 156", "none", "#C8F4FF", 5)
    # body
    a.path("M62 90 C62 56 138 56 138 90 C138 116 122 128 100 128 C78 128 62 116 62 90 Z", body, o)
    # hair swirl curls
    a.path("M70 70 C64 50 80 34 98 38 C88 44 90 54 100 56 C104 40 124 34 136 46 C122 46 118 58 130 70", body, o, 3)
    a.line("M100 56 C104 50 112 50 112 56", o, 2)
    # wispy arms
    a.line("M64 98 C48 96 40 86 44 76 C48 70 56 74 52 80", o, 3)
    a.line("M136 98 C152 96 160 86 156 76 C152 70 144 74 148 80", o, 3)
    a.eyes(90, xs=(86, 114), rx=8, ry=10, iris="#6AC8E0", pupil=("#1A3A4A", "#061218"))
    a.mouth(100, 108, "smile", w=6, color=o)
    a.cheeks([(76, 104), (124, 104)], "#FFA8C8", rx=6, ry=4)
    # book pages fluttering
    for x, y, r in ((30, 130, -20), (164, 120, 15), (40, 44, 10)):
        a.add(f'<g class="fx" transform="rotate({r} {x} {y})"><path d="M{x - 10} {y - 6} H{x + 10} V{y + 8} H{x - 10} Z" fill="#FFFFFF" stroke="#8AB0C0" stroke-width="1.5"/>'
              f'<path d="M{x - 6} {y - 1} H{x + 6} M{x - 6} {y + 3} H{x + 4}" stroke="#8AB0C0" stroke-width="1.2"/></g>')
    for d in ("M20 90 Q40 80 56 88", "M150 150 Q166 142 184 150"):
        a.line(d, "#8AD8F0", 3, 0.8)


@chordoo("balloonbo")
def balloonbo(a):
    o = "#6A2A1A"
    a.ground(rx=28, cy=190)
    # balloon envelope with stripes
    a.path("M100 12 C150 12 170 50 164 82 C158 108 130 126 116 136 H84 C70 126 42 108 36 82 C30 50 50 12 100 12 Z", a.shade("#FFF0F0", "#FF7A6A", "#C83A3A"), o)
    for d, c in (("M100 12 C80 40 76 100 88 136 H112 C124 100 120 40 100 12 Z", "#FFD84D"),):
        a.path(d, c, o, 2.5)
    a.path("M40 60 C70 70 130 70 160 60 C162 66 164 72 164 80 C130 92 70 92 36 80 C36 72 38 66 40 60 Z", "#5AC8FF", o, 2.5, ' opacity=".9"')
    a.gloss(66, 34, 14, 7)
    # ropes
    a.line("M86 136 L80 152 M114 136 L120 152", "#6E4A2A", 2.2)
    # basket face
    a.path("M70 150 H130 L124 184 H76 Z", a.lin("#E8B070", "#A86A2A"), "#5A3410", 3)
    a.line("M72 160 H128 M74 172 H126", "#5A3410", 1.6, 0.5)
    a.eyes(162, xs=(88, 112), kind="happy", rx=6)
    a.mouth(100, 170, "smile", w=6, color="#5A3410")
    a.cheeks([(80, 170), (120, 170)], rx=5, ry=3, dots=False)
    for x, y in ((24, 120), (176, 40)):
        cloud(a, x, y, 14, "#FFFFFF", "#A8C0E8", 2, "fx")


@chordoo("rainbeaux")
def rainbeaux(a):
    o = "#3A2A6A"
    a.ground(rx=60)
    cols = ["#FF5A6A", "#FF9A3A", "#FFD84D", "#6ACC5A", "#4AA8FF", "#9A6AE8"]
    # body: coiled S-curve built from striped segments
    path = "M30 160 C30 120 80 120 90 140 C100 160 150 170 160 130 C168 100 140 76 116 80"
    for i, c in enumerate(cols):
        a.add(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="{34 - i * 5}" stroke-linecap="round"/>')
    a.add(f'<path d="{path}" fill="none" stroke="{o}" stroke-width="37" stroke-linecap="round" opacity=".0"/>')
    # tail cloud puff
    cloud(a, 30, 164, 18, "#FFFFFF", "#8AA0D0", 2.5)
    # head
    head = a.shade("#FFFFFF", "#E8E0FF", "#A898E0")
    a.path("M84 66 C84 40 118 32 136 46 C152 58 150 86 130 94 C110 100 84 92 84 66 Z", head, o)
    # little cloud horns
    cloud(a, 100, 40, 10, "#FFFFFF", "#8AA0D0", 2)
    cloud(a, 132, 36, 10, "#FFFFFF", "#8AA0D0", 2)
    a.eyes(66, xs=(104, 128), rx=7, ry=9, iris="#9A6AE8", pupil=("#2A1A4A", "#0A0614"))
    a.line("M136 82 Q144 88 140 94 L144 98", "#E8405A", 2)
    a.mouth(118, 82, "smile", w=6, color=o)
    a.cheeks([(96, 80), (140, 76)], rx=5, ry=3, dots=False)
    for x, y in ((40, 40), (176, 60), (64, 92)):
        a.sparkle(x, y, 5)


@chordoo("gustav")
def gustav(a):
    feat = a.shade("#F0DCC0", "#B8885A", "#6E4A28")
    o = "#3A2410"
    a.ground(rx=44)
    # wings spread
    for sx in (1, -1):
        a.path(f"M{100 + sx * 30} 110 C{100 + sx * 60} 90 {100 + sx * 84} 96 {100 + sx * 88} 110 "
               f"C{100 + sx * 76} 112 {100 + sx * 80} 122 {100 + sx * 70} 124 C{100 + sx * 60} 126 {100 + sx * 62} 134 {100 + sx * 40} 136 Z", feat, o, 3)
    # body
    a.ell(100, 134, 36, 42, feat, o)
    a.ell(100, 146, 22, 26, "#FFF2DE")
    a.path("M84 174 l-4 8 M90 176 v8 M110 176 v8 M116 174 l4 8", "none", "#E0A030", 3.5)
    # white fluffy head
    head = a.shade("#FFFFFF", "#F2F0EA", "#C8C2B0")
    a.circ(100, 82, 32, head, o)
    for x, y in ((74, 60), (100, 50), (126, 60)):
        a.ell(x, y, 8, 6, head, o, 2.5)
    # goggles on forehead area over eyes
    a.add(f'<path d="M66 76 H134" stroke="#5A3410" stroke-width="6" stroke-linecap="round"/>')
    for x in (86, 114):
        a.circ(x, 80, 14, "#C8C8D0", "#3A3A4A", 3)
        a.circ(x, 80, 10, a.shade("#E8FAFF", "#9AD8F0", "#4A98C0"))
        a.eye(x, 81, rx=6, ry=7, iris="#4A98C0", pupil=("#2A1808", "#0A0602"))
    a.mouth(100, 98, "beak", w=9)
    a.cheeks([(72, 98), (128, 98)], rx=6, ry=4, dots=False)
    a.line("M30 50 Q46 42 58 50 M150 40 Q164 32 178 40", "#A8C8F0", 3, 0.8)


@chordoo("skyfoal")
def skyfoal(a):
    coat = a.shade("#FFFFFF", "#F0F0FF", "#B8B8E0")
    o = "#3A3A7A"
    a.ground(rx=60)
    # wings
    w = a.shade("#FFFFFF", "#DDE8FF", "#9AB0E8")
    a.path("M92 108 C80 70 50 50 30 58 C40 66 36 74 46 78 C38 84 42 92 54 92 C50 100 60 108 72 106", w, o, 3)
    a.path("M112 104 C118 66 140 42 162 44 C154 54 160 60 150 66 C160 70 156 80 144 82 C150 90 140 98 128 98", w, o, 3)
    # legs with cloud hooves
    for x, y in ((70, 150), (88, 154), (122, 154), (140, 150)):
        a.path(f"M{x - 5} {y - 20} L{x - 4} {y + 14} H{x + 4} L{x + 5} {y - 20}", coat, o, 3)
        cloud(a, x, y + 20, 10, "#FFFFFF", "#8AA0D0", 2)
    # body
    a.ell(104, 128, 46, 28, coat, o)
    # tail: pastel wavy
    a.path("M148 120 C168 112 176 130 168 144 C164 132 158 128 150 130 Z", a.lin("#FFB0D0", "#B8A0FF"), o, 2.5)
    # neck + head
    a.path("M70 120 C62 100 60 86 62 74 L86 76 C84 92 86 106 90 116 Z", coat, o, 3)
    a.path("M40 70 C38 50 56 40 72 42 C90 44 96 58 92 72 C88 88 72 92 58 92 C46 90 40 82 40 70 Z", coat, o)
    a.ell(48, 82, 9, 7, "#FFE0EC", None)
    a.circ(44, 80, 1.6, o)
    a.circ(50, 84, 1.6, o)
    # mane
    a.path("M64 40 C76 30 96 38 94 54 C100 66 94 78 92 90 C86 80 86 70 82 62 C76 54 66 50 64 40 Z", a.lin("#FFB0D0", "#B8A0FF", "#8AD8FF"), o, 2.5)
    a.ell(78, 40, 5, 10, coat, o, 2.5, rot=20)
    a.eye(68, 64, rx=7, ry=9, iris="#B8A0FF", pupil=("#2A2A5A", "#0A0A1A"), lashes=2, side=-1)
    a.mouth(54, 88, "smile", w=4, color=o)
    a.cheeks([(76, 78)], rx=5, ry=3, dots=False)
    a.sparkle(172, 80, 5)
    a.sparkle(24, 120, 4, "#B8A0FF")


@chordoo("aerodon")
def aerodon(a):
    o = "#2A3A7A"
    a.ground(rx=56)
    body = a.shade("#FFFFFF", "#E2ECFF", "#9AB0E0")
    # feathered wings behind
    for sx in (1, -1):
        for k in range(4):
            ln = 70 - k * 10
            ang = (-150 + k * 18) if sx < 0 else (-30 - k * 18)
            a.add(f'<g transform="translate({100 + sx * 18} 96) rotate({ang})"><path d="M0 -8 C{ln * 0.5} -16 {ln} -10 {ln} 0 C{ln} 10 {ln * 0.5} 12 0 8 Z" '
                  f'fill="{["#FFFFFF", "#E6F0FF", "#C8DCFF", "#A8C4FF"][k]}" stroke="{o}" stroke-width="2.5" stroke-linejoin="round"/></g>')
    # cloud-puff tail curling
    a.path("M120 150 C150 160 176 150 178 128 C180 112 164 106 156 114", "none", o, 16)
    a.path("M120 150 C150 160 176 150 178 128 C180 112 164 106 156 114", "none", "#E2ECFF", 11)
    cloud(a, 160, 112, 14, "#FFFFFF", "#8AA0D0", 2.5)
    # body
    a.path("M70 170 C60 140 70 106 100 104 C130 106 140 140 130 170 C120 180 80 180 70 170 Z", body, o)
    a.path("M86 170 C82 146 88 122 100 120 C112 122 118 146 114 170 Z", "#FFF6E0", None)
    for y in (132, 146, 160):
        a.line(f"M88 {y} Q100 {y + 4} 112 {y}", "#E0C89A", 1.6)
    # head
    a.path("M64 74 C64 44 136 44 136 74 C136 98 120 110 100 110 C80 110 64 98 64 74 Z", body, o)
    a.ell(100, 96, 20, 12, "#F2F6FF", o, 2)
    a.circ(92, 94, 1.8, o)
    a.circ(108, 94, 1.8, o)
    # horns + feather crest
    a.path("M74 54 C68 38 70 28 76 22 C80 34 84 42 86 50 Z", "#FFE6A8", "#A8782A", 2.5)
    a.path("M126 54 C132 38 130 28 124 22 C120 34 116 42 114 50 Z", "#FFE6A8", "#A8782A", 2.5)
    for x, r in ((94, -10), (100, 0), (106, 10)):
        a.ell(x, 42, 4, 12, "#8AD8FF", o, 2, rot=r)
    a.eyes(74, xs=(84, 116), rx=8, ry=10, iris="#6AA8FF", pupil=("#1A2A5A", "#060A1A"))
    a.mouth(100, 102, "smile", w=6, color=o)
    a.cheeks([(72, 90), (128, 90)], rx=6, ry=4, dots=False)
    for d in ("M16 60 Q34 52 46 62", "M160 40 Q176 32 190 42"):
        a.line(d, "#A8C8F0", 3, 0.8)


@chordoo("stormcrest")
def stormcrest(a):
    feat = a.shade("#C8D4F0", "#6A7AB8", "#2E3A78")
    o = "#141E4A"
    a.ground(rx=50)
    # rain cloud behind
    cloud(a, 100, 40, 50, a.lin("#9AA8C8", "#6A7898"), "#3A4868", 3)
    for x in (62, 84, 118, 140):
        a.line(f"M{x} 66 l-4 10", "#8AD0FF", 3, 0.9)
    # wings folded
    a.path("M60 110 C40 128 38 160 56 176 C64 156 70 132 72 116 Z", feat, o, 3)
    a.path("M140 110 C160 128 162 160 144 176 C136 156 130 132 128 116 Z", feat, o, 3)
    # body
    a.path("M100 84 C138 84 146 120 140 150 C134 172 118 180 100 180 C82 180 66 172 60 150 C54 120 62 84 100 84 Z", feat, o)
    a.path("M100 120 C120 120 126 140 122 158 C118 172 108 176 100 176 C92 176 82 172 78 158 C74 140 80 120 100 120 Z", "#E6ECFF")
    # lightning crest
    a.path("M100 88 L90 56 L102 62 L96 30 L118 64 L106 60 L114 86 Z", a.lin("#FFF6A8", "#FFD020"), "#A87A00", 3)
    a.glow(104, 58, 26, "#FFE84D", 0.5)
    a.eyes(110, xs=(86, 114), kind="angry", rx=8, ry=9, iris="#FFD020", pupil=("#1A2A5A", "#060A1A"))
    a.mouth(100, 124, "beak", w=8)
    a.path("M88 180 l-4 6 M96 180 v7 M104 180 v7 M112 180 l4 6", "none", "#E0A030", 3)
    # sprout getting rained on (kindness)
    a.line("M168 184 V172", "#3E8A2E", 2.5)
    a.ell(164, 170, 5, 3, "#7CC850", rot=-30)
    a.ell(172, 170, 5, 3, "#7CC850", rot=30)


@chordoo("zenithia")
def zenithia(a):
    o = "#5A2A7A"
    a.glow(100, 96, 96, "#FFE6A8", 0.55)
    a.ground(rx=46)
    # comet tail sweeping behind
    a.path("M104 140 C140 150 176 130 190 96 C176 116 156 122 136 118 C160 112 176 96 182 76 C166 96 140 104 116 104 Z",
           a.lin("#FFFFFF", "#FFD8F0", "#B8A0FF", x2=1, y2=0), o, 2.5)
    for x, y in ((150, 120), (170, 100), (160, 86)):
        a.sparkle(x, y, 4, "#FFFFFF")
    # long tail feathers down
    for i, c in enumerate(("#FFB0D8", "#FFD84D", "#B8A0FF")):
        a.path(f"M{92 + i * 8} 150 C{80 + i * 10} 168 {74 + i * 16} 180 {70 + i * 20} 192", "none", c, 6)
    # wings raised
    w = a.shade("#FFFFFF", "#FFF0FA", "#D8B8F0")
    a.path("M78 110 C50 96 30 66 34 34 C46 46 52 44 58 58 C62 48 70 50 72 62 C78 56 86 64 84 80", w, o, 3)
    a.path("M122 110 C150 96 170 66 166 34 C154 46 148 44 142 58 C138 48 130 50 128 62 C122 56 114 64 116 80", w, o, 3)
    # body
    body = a.shade("#FFFFFF", "#FFE8F4", "#E0A8D0")
    a.path("M100 84 C126 84 134 110 128 132 C122 152 112 158 100 158 C88 158 78 152 72 132 C66 110 74 84 100 84 Z", body, o)
    # head
    a.circ(100, 78, 22, body, o)
    # golden crown with gems
    a.path("M80 60 L84 40 L92 52 L100 34 L108 52 L116 40 L120 60 Z", a.lin("#FFF6A8", "#FFC020"), "#A87A00", 2.5)
    for x, c in ((84, "#FF5A8A"), (100, "#5AC8FF"), (116, "#8AE06A")):
        a.circ(x, 41 if x != 100 else 35, 3, c)
    a.eyes(80, xs=(92, 108), rx=6, ry=8, iris="#B8A0FF", pupil=("#2A1A4A", "#0A0614"), kind="star", lashes=2)
    a.mouth(100, 92, "beak", w=5)
    a.cheeks([(84, 90), (116, 90)], rx=5, ry=3, dots=False)
    # chest gem
    a.path("M100 110 L108 120 L100 132 L92 120 Z", a.lin("#E8FFFF", "#5AC8FF"), "#1E5A8A", 2)
    for x, y in ((24, 120), (40, 160), (176, 40), (150, 20)):
        a.sparkle(x, y, 5)

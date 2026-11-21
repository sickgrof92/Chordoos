import math
from artkit import chordoo, INK
from shapes import limb, star

SN_O = "#4A2A14"


def sprinkles(a, pts, cls=""):
    cols = ["#FF6A9A", "#FFD84D", "#6AC8FF", "#8AE06A", "#B89AF0", "#FFFFFF"]
    c = f' class="{cls}"' if cls else ""
    for i, (x, y) in enumerate(pts):
        a.add(f'<rect{c} x="{x - 4}" y="{y - 1.5}" width="8" height="3" rx="1.5" fill="{cols[i % 6]}" transform="rotate({(i * 47) % 180} {x} {y})"/>')


@chordoo("toasty")
def toasty(a):
    o = "#5A3410"
    a.ground(rx=46)
    # legs
    for x in (84, 116):
        limb(a, f"M{x} 164 L{x} 180", "#E8B060", o, 8)
        a.ell(x, 182, 8, 4, "#5A3410")
    # crust then bread
    a.path("M48 168 V84 C34 80 32 50 52 40 C70 30 88 36 100 44 C112 36 130 30 148 40 C168 50 166 80 152 84 V168 Z", a.lin("#E8A050", "#A8601E"), o, 3.5)
    a.path("M58 160 V90 C46 84 44 58 60 50 C74 44 88 48 100 56 C112 48 126 44 140 50 C156 58 154 84 142 90 V160 Z", a.shade("#FFF6DC", "#FFE4A8", "#F0C070"))
    # toast marks
    a.line("M70 70 L84 62 M112 62 L126 70", "#E0A050", 3, 0.5)
    a.eyes(104, xs=(84, 116), rx=9, ry=11, iris="#E8A050", pupil=("#3A2010", "#120804"))
    a.mouth(100, 128, "open", w=7, color="#7A3E2E")
    # jam cheeks
    for x in (68, 132):
        a.path(f"M{x - 10} 122 C{x - 12} 112 {x + 12} 112 {x + 10} 122 C{x + 10} 132 {x + 4} 136 {x + 2} 130 C{x} 136 {x - 8} 134 {x - 10} 122 Z", "#E8304A", "#8A0A1E", 1.5)
        a.circ(x - 3, 118, 2, "#FFFFFF", extra=' opacity=".8"')
    # arms up (pop!)
    limb(a, "M50 120 C38 110 34 96 36 84", "#E8B060", o, 8)
    limb(a, "M150 120 C162 110 166 96 164 84", "#E8B060", o, 8)
    for x, y in ((24, 60), (176, 60)):
        a.line(f"M{x} {y} l{6 if x < 100 else -6} -8 M{x + (8 if x < 100 else -8)} {y + 6} l{8 if x < 100 else -8} -2", "#E8B060", 3, 0.9)


@chordoo("marsh")
def marsh(a):
    o = "#8A7A9A"
    a.ground(rx=50)
    body = a.shade("#FFFFFF", "#FAF6FF", "#D8D0E8")
    a.path("M46 64 C46 46 154 46 154 64 V156 C154 176 46 176 46 156 Z", body, o, 3.5)
    a.ell(100, 62, 54, 14, "#FFFFFF", o, 3)
    a.ell(100, 62, 50, 10, a.shade("#FFFFFF", "#F4E8FF", "#E0D0F0"))
    # toasty bottom
    a.path("M47 150 C60 164 140 164 153 150 V156 C153 176 47 176 47 156 Z", "#F0D8B8", None, extra=' opacity=".7"')
    a.eyes(110, xs=(80, 120), kind="sleepy", rx=10)
    a.mouth(100, 128, "smile", w=7, color="#8A5A7A")
    a.cheeks([(64, 124), (136, 124)], "#FFB0D0", rx=10, ry=6)
    # arms wrapped in a hug
    a.ell(60, 144, 12, 8, a.shade("#FFFFFF", "#FAF6FF", "#D8D0E8"), o, 2.5, rot=-30)
    a.ell(140, 144, 12, 8, a.shade("#FFFFFF", "#FAF6FF", "#D8D0E8"), o, 2.5, rot=30)
    a.add('<path class="fx" d="M100 30 C96 22 86 24 88 32 C90 38 100 44 100 44 C100 44 110 38 112 32 C114 24 104 22 100 30 Z" fill="#FF9AC0"/>')


@chordoo("nibbles")
def nibbles(a):
    fur = a.shade("#FFF4E0", "#F0C890", "#C08A4A")
    o = "#5A3410"
    a.ground(rx=50)
    a.path("M46 140 C42 104 66 76 100 76 C134 76 158 104 154 140 C152 170 128 182 100 182 C72 182 48 170 46 140 Z", fur, o)
    a.path("M70 148 C70 126 130 126 130 148 C130 170 116 178 100 178 C84 178 70 170 70 148 Z", "#FFFBF2")
    # ears
    a.circ(64, 82, 14, fur, o, 3)
    a.circ(136, 82, 14, fur, o, 3)
    a.circ(64, 82, 7, "#FFB0B8")
    a.circ(136, 82, 7, "#FFB0B8")
    a.eyes(108, xs=(80, 120), rx=9, ry=11, iris="#C08A4A", pupil=("#2A1808", "#0A0602"))
    a.path("M96 120 L104 120 L100 124 Z", "#FF8AA8", o, 1.4)
    # big cheeks full of cracker
    a.ell(66, 128, 16, 13, a.shade("#FFFBF2", "#FFE8C8", "#F0C890"), o, 2.5)
    a.ell(134, 128, 16, 13, a.shade("#FFFBF2", "#FFE8C8", "#F0C890"), o, 2.5)
    a.cheeks([(66, 130), (134, 130)], rx=8, ry=5, dots=False)
    a.mouth(100, 128, "cat", w=5, color=o)
    a.path("M96 132 H104 V137 H96 Z", "#FFFFFF", o, 1.2)
    # cracker held in paws
    a.path("M74 140 H126 V170 H74 Z", a.lin("#FFE8A8", "#E8B860"), "#8A5A1A", 3)
    for x in (84, 100, 116):
        for y in (150, 162):
            a.circ(x, y, 2, "#B8802A")
    a.ell(74, 150, 8, 6, fur, o, 2.5)
    a.ell(126, 150, 8, 6, fur, o, 2.5)


@chordoo("puddin")
def puddin(a):
    o = "#6A3A0A"
    a.ground(rx=56)
    # plate
    a.ell(100, 172, 74, 14, a.lin("#FFFFFF", "#D8E0F0"), "#8A98B8", 3)
    # wobbly pudding
    a.path("M46 164 C40 136 48 100 56 84 C70 66 130 66 144 84 C152 100 160 136 154 164 C130 172 70 172 46 164 Z",
           a.shade("#FFF0C0", "#FFC860", "#D88A20"), o, 3.5)
    # caramel top drip
    a.path("M56 84 C70 66 130 66 144 84 C146 96 140 104 136 96 C132 108 124 110 120 98 C114 112 104 110 100 98 C94 110 84 108 82 98 C76 110 64 104 64 94 C58 100 52 94 56 84 Z",
           a.lin("#C86A1A", "#8A3A0A"), "#5A2A0A", 2.5)
    # cream + cherry
    a.path("M80 74 C76 60 92 52 100 58 C108 52 124 60 120 74 Z", "#FFFFFF", "#C8B8A8", 2.5)
    a.circ(100, 50, 9, a.shade("#FFB0B0", "#E8203A", "#8A0A1A"), "#5A0A14", 2.5)
    a.line("M100 42 C102 34 108 30 114 30", "#3E6A1E", 2.2)
    a.eyes(124, xs=(82, 118), kind="happy", rx=9)
    a.mouth(100, 138, "open", w=8, color="#7A3E2E")
    a.cheeks([(66, 136), (134, 136)], "#FF8AA8", rx=8, ry=5)
    a.gloss(66, 112, 6, 12, rot=-10)
    for d in ("M34 120 q-6 6 0 12", "M166 120 q6 6 0 12", "M28 140 q-6 6 0 12", "M172 140 q6 6 0 12"):
        a.add(f'<path class="fx" d="{d}" stroke="#E8B860" stroke-width="2.5" fill="none" stroke-linecap="round"/>')


@chordoo("sushiro")
def sushiro(a):
    o = "#1A2A1A"
    a.ground(rx=60)
    # fish tail (salmon) and fins
    a.path("M152 120 L188 96 L184 124 L190 150 Z", a.lin("#FFB89A", "#FF7A5A"), "#8A3A1A", 3)
    a.path("M90 64 C100 46 120 48 126 62 Z", a.lin("#FFB89A", "#FF7A5A"), "#8A3A1A", 2.5)
    # seaweed-wrapped roll body (side view cylinder)
    a.path("M30 120 C30 84 60 66 96 66 C132 66 160 84 160 120 C160 156 132 174 96 174 C60 174 30 156 30 120 Z",
           a.lin("#3A5A3A", "#1A2E1A"), o, 3.5)
    # cut face: rice ring + salmon + cucumber
    a.circ(82, 120, 42, a.shade("#FFFFFF", "#FAF8F2", "#E0DCCC"), "#C8C0A8", 2.5)
    for x, y in ((56, 104), (64, 140), (100, 148), (108, 96), (52, 124), (90, 86), (112, 132)):
        a.ell(x, y, 3.5, 2.4, "#FFFFFF", "#D8D2C0", 1, rot=(x * 13) % 90)
    a.path("M64 112 C64 96 100 96 100 112 C100 128 64 128 64 112 Z", a.lin("#FFC0A8", "#FF7A5A"), "#C04A2A", 2)
    a.line("M70 106 L94 118 M70 116 L86 124", "#FFE0D0", 2)
    a.ell(80, 136, 7, 5, "#7CC850", "#2A5A1E", 1.5)
    # face on the side wall
    a.eyes(116, xs=(122, 144), rx=7, ry=9, iris="#FF7A5A", pupil=("#1A1A1A", "#060606"))
    a.mouth(134, 134, "smile", w=6, color="#FFFFFF")
    a.cheeks([(118, 132), (150, 130)], "#FF8AA8", rx=5, ry=3, dots=False)
    # chopsticks
    a.line("M30 30 L94 72 M40 22 L100 66", "#C8A070", 4)
    a.add('<path class="fx" d="M14 140 q8 -6 16 0 q8 6 16 0" stroke="#8AC8F0" stroke-width="2.5" fill="none"/>')


@chordoo("pretzlette")
def pretzlette(a):
    o = "#4A2408"
    a.ground(rx=64)
    br = a.lin("#E8A050", "#A85A1A")
    # pretzel knot as a thick stroke
    d = "M40 170 C30 120 50 70 96 76 C142 82 160 130 130 150 C104 168 78 140 96 110 C114 80 160 90 170 140 C176 160 168 176 150 178"
    a.add(f'<path d="{d}" fill="none" stroke="{o}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>')
    a.add(f'<path d="{d}" fill="none" stroke="{br}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>')
    a.add(f'<path d="{d}" fill="none" stroke="#FFD8A0" stroke-width="4" stroke-linecap="round" opacity=".5" transform="translate(-3 -4)"/>')
    # salt crystals
    for x, y in ((50, 120), (70, 82), (120, 84), (150, 116), (104, 128), (160, 160), (40, 150), (128, 150)):
        a.path(f"M{x - 3} {y - 2} H{x + 3} V{y + 3} H{x - 3} Z", "#FFFFFF", "#C8C0B0", 1)
    # snake head at the start
    a.path("M20 178 C14 162 24 150 40 152 C56 154 62 170 54 182 C46 192 26 190 20 178 Z", a.shade("#FFD8A0", "#E8A050", "#A85A1A"), o, 3)
    a.eye(32, 166, rx=6, ry=7, iris="#E8A050", pupil=("#2A1808", "#0A0602"))
    a.eye(48, 166, rx=6, ry=7, iris="#E8A050", pupil=("#2A1808", "#0A0602"))
    a.path("M36 182 Q40 186 44 182", "none", o, 2)
    a.line("M40 186 L40 192 M40 192 L36 196 M40 192 L44 196", "#E8405A", 1.8)
    a.cheeks([(26, 178), (54, 178)], rx=4, ry=3, dots=False)


@chordoo("waffly")
def waffly(a):
    o = "#5A3410"
    a.ground(rx=60)
    wf = a.shade("#FFE8A8", "#F0B860", "#B8782A")
    # tail
    a.path("M148 130 C164 122 170 108 164 96", "none", o, 10)
    a.path("M148 130 C164 122 170 108 164 96", "none", "#F0B860", 6)
    # legs
    for x in (64, 88, 120, 142):
        a.path(f"M{x - 9} 150 L{x - 9} 178 H{x + 9} L{x + 9} 150", wf, o, 3)
    # body: square waffle
    a.path("M50 108 H154 V160 H50 Z", wf, o, 3.5)
    for x in range(63, 154, 13):
        a.line(f"M{x} 110 V158", "#B8782A", 2, 0.6)
    for y in range(121, 160, 13):
        a.line(f"M52 {y} H152", "#B8782A", 2, 0.6)
    # syrup drips + butter pat
    a.path("M60 108 C80 100 128 100 148 108 V114 C144 124 140 124 138 114 C132 130 126 126 124 114 C112 120 104 120 100 114 C92 132 84 128 84 114 C76 120 66 118 60 114 Z", a.lin("#E88A2A", "#A84A0A"), "#6A2A04", 2)
    a.path("M110 98 H128 V108 H110 Z", "#FFF4A8", "#C8A020", 2)
    # head (round waffle)
    a.circ(56, 86, 34, wf, o)
    for k in (-18, -6, 6, 18):
        a.line(f"M{56 + k} 56 V116", "#B8782A", 2, 0.5)
        a.line(f"M26 {86 + k} H86", "#B8782A", 2, 0.5)
    a.circ(56, 86, 34, "none", o)
    # floppy ears with syrup tips
    a.path("M28 66 C12 70 10 100 22 108 C28 98 30 84 34 76 Z", "#C8883A", o, 3)
    a.path("M80 62 C96 60 102 90 94 100 C88 90 84 78 78 72 Z", "#C8883A", o, 3)
    a.ell(48, 104, 15, 10, "#FFF4D8", o, 2)
    a.ell(48, 98, 5, 4, "#3A2010")
    a.mouth(48, 106, "open", w=5, color="#7A3E2E")
    a.eyes(84, xs=(42, 68), rx=7, ry=9, iris="#E88A2A", pupil=("#2A1808", "#0A0602"))
    a.cheeks([(30, 98), (76, 98)], rx=5, ry=3, dots=False)


@chordoo("sirsprinkles")
def sirsprinkles(a):
    o = "#5A2A14"
    a.ground(rx=56)
    # legs + boots
    for x in (80, 120):
        limb(a, f"M{x} 160 L{x} 176", "#C8CCD8", "#3A3A4A", 9)
        a.ell(x, 180, 10, 5, "#3A3A4A")
    # donut body
    a.circ(100, 108, 56, a.shade("#FFE0B0", "#E8A860", "#A8682A"), o, 3.5)
    # pink icing with drips
    a.path("M50 100 C50 66 74 52 100 52 C126 52 150 66 150 100 C150 112 144 116 140 108 C136 120 130 122 126 112 C118 126 110 120 108 112 "
           "C100 124 92 124 88 112 C82 122 74 120 72 110 C66 120 58 118 58 108 C54 114 50 110 50 100 Z", a.shade("#FFE8F4", "#FF9AC8", "#E0609A"), "#A0306A", 2.5)
    a.circ(100, 108, 16, "#F6F4FF", o, 3)
    sprinkles(a, [(70, 74), (84, 62), (120, 64), (134, 80), (64, 94), (138, 98), (110, 56), (78, 86)])
    # helmet visor + plume
    a.path("M74 40 C74 22 126 22 126 40 V50 H74 Z", a.lin("#E8ECF8", "#9AA0B8"), "#3A3A4A", 2.5)
    a.line("M78 42 H122", "#3A3A4A", 3)
    a.path("M100 22 C96 6 110 -2 120 6 C110 8 106 14 104 22 Z", "#E8303A", "#6A0A14", 2)
    # eyes peeking through the visor slit
    a.circ(90, 42, 2.6, INK)
    a.circ(110, 42, 2.6, INK)
    # face on donut
    a.eyes(132, xs=(76, 124), rx=8, ry=10, iris="#FF9AC8", pupil=("#3A1A0A", "#120602"))
    a.mouth(100, 140, "grin", w=9, color=o)
    a.cheeks([(62, 140), (138, 140)], rx=6, ry=4, dots=False)
    # sprinkle shield
    a.path("M146 104 H184 V130 C184 150 166 160 165 162 C164 160 146 150 146 130 Z", a.lin("#FFFFFF", "#C8E8FF"), "#2A5A8A", 3)
    sprinkles(a, [(156, 114), (172, 116), (164, 128), (156, 140), (174, 136)])
    # sword (candy cane)
    a.line("M30 160 L46 70", "#FFFFFF", 7)
    a.add('<path d="M30 160 L46 70" stroke="#E8303A" stroke-width="7" stroke-dasharray="7 7"/>')
    a.line("M24 132 H48", "#FFD84D", 5)


@chordoo("cupcakey")
def cupcakey(a):
    o = "#5A1A3A"
    a.ground(rx=44)
    # wrapper
    a.path("M50 112 H150 L136 178 H64 Z", a.lin("#C8A8FF", "#8A5AE0"), "#3A1A7A", 3)
    for x in range(60, 150, 12):
        a.line(f"M{x} 114 L{x + (100 - x) * 0.14:.0f} 176", "#3A1A7A", 1.6, 0.5)
    # frosting swirls
    fr = a.shade("#FFFFFF", "#FFE0EE", "#F0A0C8")
    a.path("M40 116 C28 98 46 80 62 88 C58 66 86 52 100 66 C114 52 142 66 138 88 C154 80 172 98 160 116 C140 124 60 124 40 116 Z", fr, "#A0406A", 3)
    a.path("M60 74 C62 56 84 44 100 46 C116 44 138 56 140 74 C126 66 110 72 100 64 C90 72 74 66 60 74 Z", fr, "#A0406A", 3)
    sprinkles(a, [(70, 100), (86, 84), (116, 90), (132, 102), (100, 104), (56, 104), (144, 108)])
    # cherry hat (cherry wearing a tiny party hat)
    a.circ(100, 44, 14, a.shade("#FFB0B0", "#E8203A", "#8A0A1A"), "#5A0A14", 2.5)
    a.line("M100 30 C102 18 110 12 118 12", "#3E6A1E", 2.5)
    a.ell(120, 14, 7, 3.5, "#7CC850", "#2A5A1E", 1.5, rot=-20)
    a.gloss(94, 38, 4, 2)
    a.eyes(142, xs=(84, 116), rx=9, ry=11, iris="#B89AF0", pupil=("#2A1A4A", "#0A0614"))
    a.mouth(100, 160, "open", w=7, color="#7A2A4A")
    a.cheeks([(70, 156), (130, 156)], "#FF9AC8", rx=7, ry=4)
    # party popper confetti
    for x, y, c in ((24, 40, "#FFD84D"), (176, 50, "#6AC8FF"), (30, 150, "#8AE06A"), (172, 150, "#FF6A9A"), (160, 20, "#B89AF0")):
        a.add(f'<rect class="fx" x="{x}" y="{y}" width="6" height="10" fill="{c}" transform="rotate(35 {x} {y})"/>')


@chordoo("gumdrop")
def gumdrop(a):
    o = "#0E5A3A"
    a.ground(cy=188, rx=32)
    # bounce motion lines
    for y in (160, 172):
        a.line(f"M70 {y} Q100 {y + 4} 130 {y}", "#8AE0B8", 3, 0.7)
    body = a.shade("#E8FFF4", "#4AE0A0", "#0E9A6A")
    a.path("M100 20 C126 20 140 48 148 90 C154 120 152 140 136 146 C116 152 84 152 64 146 C48 140 46 120 52 90 C60 48 74 20 100 20 Z", body, o, 3.5)
    # sugar crystals
    for x, y in ((80, 50), (118, 46), (70, 80), (132, 84), (60, 120), (140, 118), (100, 36), (92, 136), (116, 134)):
        a.path(f"M{x - 2.5} {y - 2.5} H{x + 2.5} V{y + 2.5} H{x - 2.5} Z", "#FFFFFF", None, extra=' opacity=".85"')
    a.eyes(96, xs=(84, 116), rx=10, ry=12, iris="#4AE0A0", pupil=("#0A2A1A", "#020A06"), kind="star")
    a.mouth(100, 118, "open", w=8, color="#0E5A3A", tongue="#FF8AB0")
    a.cheeks([(70, 112), (130, 112)], "#FF9AC8", rx=7, ry=4)
    a.gloss(80, 46, 6, 12, rot=-20)
    for x, y in ((30, 60), (170, 70), (40, 110)):
        a.sparkle(x, y, 6, "#4AE0A0")


@chordoo("cocoabear")
def cocoabear(a):
    o = "#3A1E0A"
    a.ground(rx=60)
    # mug body
    a.path("M46 96 H140 V160 C140 176 128 182 112 182 H74 C58 182 46 176 46 160 Z", a.lin("#FF8A8A", "#D83A4A"), "#6A0A1E", 3.5)
    a.path("M140 112 C168 108 172 150 140 150", "none", "#6A0A1E", 12)
    a.path("M140 112 C168 108 172 150 140 150", "none", "#E85A6A", 7)
    # heart on mug
    a.add('<path d="M93 160 C80 150 84 140 93 146 C102 140 106 150 93 160 Z" fill="#FFFFFF"/>')
    # bear head made of cocoa rising from mug
    cocoa = a.shade("#D8A878", "#9A6A3A", "#5A3414")
    a.path("M48 98 C44 60 70 40 93 40 C116 40 142 60 138 98 Z", cocoa, o, 3.5)
    a.ell(93, 98, 47, 8, "#7A4A20", o, 3)
    # marshmallow ears
    for x in (58, 128):
        a.path(f"M{x - 12} 54 V40 C{x - 12} 32 {x + 12} 32 {x + 12} 40 V54 C{x + 12} 60 {x - 12} 60 {x - 12} 54 Z", a.shade("#FFFFFF", "#FAF6FF", "#D8D0E8"), "#8A7A9A", 2.5)
    a.ell(93, 80, 16, 11, "#E8C8A0", o, 2)
    a.ell(93, 75, 6, 4, "#3A1E0A")
    a.mouth(93, 82, "cat", w=5, color=o)
    a.eyes(64, xs=(76, 110), kind="happy", rx=8)
    a.cheeks([(64, 80), (122, 80)], rx=7, ry=4)
    # steam
    for x in (40, 150, 160):
        a.add(f'<path class="fx" d="M{x} 70 q-6 -10 0 -20 q6 -10 0 -20" stroke="#E0D0C8" stroke-width="3" fill="none" stroke-linecap="round"/>')


@chordoo("sundaesaur")
def sundaesaur(a):
    o = "#5A2A14"
    a.ground(rx=66)
    # tail
    a.path("M136 150 C160 156 180 146 192 128 C172 132 156 132 142 128 Z", a.shade("#FFFFFF", "#FFE0EE", "#F0A0C8"), "#A0406A", 3)
    # legs as cones (waffle)
    cone = a.lin("#F0C070", "#C8883A")
    for x in (78, 120):
        a.path(f"M{x - 13} 148 L{x} 182 L{x + 13} 148 Z", cone, "#7A4A14", 3)
        a.line(f"M{x - 8} 156 L{x + 4} 172 M{x + 8} 156 L{x - 4} 172", "#7A4A14", 1.4, 0.6)
    # body: scoops (strawberry, mint, vanilla)
    for cx, cy, r, c in ((76, 132, 30, ("#FFF0F6", "#FFA8C8", "#E0609A")), (126, 132, 30, ("#F0FFF6", "#9AE8C0", "#3AA87A")), (100, 120, 34, ("#FFFFF4", "#FFF0C8", "#E0C890"))):
        a.circ(cx, cy, r, a.shade(*c), o, 3)
    # cone spikes down the back
    for x, y, r in ((74, 92, -30), (100, 84, -5), (126, 90, 20), (148, 108, 45)):
        a.add(f'<path d="M{x - 9} {y + 6} L{x} {y - 18} L{x + 9} {y + 6} Z" fill="{cone}" stroke="#7A4A14" stroke-width="2.5" stroke-linejoin="round" transform="rotate({r} {x} {y})"/>')
    # chocolate drip on body
    a.path("M72 108 C88 100 112 100 128 108 C128 118 122 118 120 112 C116 124 110 120 108 112 C102 122 96 122 92 112 C88 120 80 120 80 112 C76 118 72 116 72 108 Z", "#7A3E1E", "#4A1E0A", 2)
    # head
    a.path("M20 80 C18 56 40 44 60 48 C80 52 86 70 80 86 C74 100 52 106 36 102 C26 98 20 90 20 80 Z", a.shade("#FFF0F6", "#FFA8C8", "#E0609A"), "#A0406A")
    a.circ(52, 44, 7, a.shade("#FFB0B0", "#E8203A", "#8A0A1A"), "#5A0A14", 2)
    a.eye(44, 74, rx=7, ry=9, iris="#FFA8C8", pupil=("#3A1A2A", "#12060E"))
    a.eye(64, 74, rx=6, ry=8, iris="#FFA8C8", pupil=("#3A1A2A", "#12060E"))
    a.mouth(40, 90, "smile", w=8, color="#A0406A")
    a.cheeks([(30, 86), (74, 86)], "#FF6AA8", rx=5, ry=3, dots=False)
    sprinkles(a, [(92, 128), (110, 140), (70, 146), (130, 144), (122, 120)])


@chordoo("gingerking")
def gingerking(a):
    o = "#5A2A0A"
    a.glow(100, 60, 60, "#FFE88A", 0.4)
    a.ground(rx=56)
    gb = a.shade("#F0B878", "#C87A3A", "#8A4A1A")
    # cape
    a.path("M60 84 C40 120 34 160 40 182 H160 C166 160 160 120 140 84 Z", a.lin("#C8203A", "#7A0A1E"), "#4A0410", 3)
    a.path("M56 86 C70 96 130 96 144 86 L146 96 C130 106 70 106 54 96 Z", "#FFFFFF", "#C8C0B0", 2)
    for x in (66, 84, 116, 134):
        a.circ(x, 98, 2, "#2A2A2A")
    # gingerbread body (classic cookie shape)
    a.path("M100 90 C80 90 76 96 68 104 C56 104 42 108 40 120 C40 130 56 132 66 128 L64 156 C58 170 60 182 72 182 C82 182 88 172 92 160 "
           "L108 160 C112 172 118 182 128 182 C140 182 142 170 136 156 L134 128 C144 132 160 130 160 120 C158 108 144 104 132 104 C124 96 120 90 100 90 Z", gb, o, 3.5)
    # icing squiggles + buttons
    a.path("M44 116 q4 -4 8 0 q4 4 8 0 M140 116 q4 -4 8 0 q4 4 8 0 M64 172 q4 -4 8 0 M128 172 q4 -4 8 0", "none", "#FFFFFF", 3)
    for y, c in ((116, "#E8303A"), (132, "#6AC88A"), (148, "#FFD84D")):
        a.circ(100, y, 5, c, "#FFFFFF", 2)
    # head
    a.circ(100, 64, 32, gb, o)
    a.eyes(62, xs=(88, 112), rx=7, ry=9, iris="#FFFFFF", pupil=("#2A1A0A", "#0A0602"))
    a.path("M84 76 Q100 90 116 76", "none", "#FFFFFF", 3.5)
    a.cheeks([(76, 76), (124, 76)], "#FF6A6A", rx=6, ry=4, dots=False)
    # icing crown with gumdrops
    a.path("M74 40 L76 16 L88 30 L100 10 L112 30 L124 16 L126 40 Z", "#FFFFFF", "#C8C0D8", 2.5)
    for x, y, c in ((76, 16, "#FF6A9A"), (100, 10, "#4AE0A0"), (124, 16, "#B89AF0")):
        a.circ(x, y, 5, c, "#3A2A4A", 1.5)
    # candy cane scepter
    a.line("M160 182 V64", "#FFFFFF", 7)
    a.add('<path d="M160 182 V64" stroke="#E8303A" stroke-width="7" stroke-dasharray="8 8"/>')
    a.path("M160 66 C160 46 184 46 184 66", "none", "#E8303A", 7)
    for x, y in ((24, 40), (180, 30), (24, 160)):
        a.sparkle(x, y, 6)

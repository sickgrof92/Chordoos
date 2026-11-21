import math
from artkit import chordoo, INK
from shapes import limb, star, flower

DS_O = "#5A3410"
SAND = ("#FFF6DC", "#F0D498", "#C8A050")


@chordoo("cactoo")
def cactoo(a):
    o = "#1E4A1E"
    a.ground(rx=44)
    # terracotta pot
    a.path("M64 150 H136 L128 182 H72 Z", a.lin("#F0985A", "#C8602A"), "#6A2A0A", 3)
    a.path("M60 142 H140 V154 H60 Z", "#E8804A", "#6A2A0A", 3)
    sk = a.shade("#C8F0A8", "#5EB84A", "#2A7A2A")
    # arms open for a careful hug
    a.path("M70 110 C52 112 44 100 44 84 C44 74 56 74 58 84 C58 94 62 98 72 98 Z", sk, o, 3)
    a.path("M130 104 C148 106 156 94 156 76 C156 66 144 66 142 76 C142 88 138 92 128 92 Z", sk, o, 3)
    # body
    a.path("M66 144 V80 C66 52 134 52 134 80 V144 Z", sk, o, 3.5)
    for x in (82, 100, 118):
        a.line(f"M{x} 66 V140", "#2A7A2A", 2, 0.45)
    # soft spines (little white dashes)
    for x, y in ((74, 90), (126, 90), (76, 120), (124, 124), (50, 88), (150, 80), (90, 62), (110, 62)):
        a.line(f"M{x} {y} l{-3 if x < 100 else 3} -3", "#FFFFFF", 2)
    # flower hat
    flower(a, 100, 52, 18, "#FF8AC0", "#FFD84D", "#A04A7A", n=6, w=1.6)
    a.eyes(96, xs=(86, 114), rx=8, ry=10, iris="#5EB84A", pupil=("#1A2A1A", "#060A06"))
    a.mouth(100, 114, "smile", w=6, color=o)
    a.cheeks([(76, 110), (124, 110)], "#FF9AB0", rx=6, ry=4)


@chordoo("fennix")
def fennix(a):
    fur = a.shade("#FFF4DC", "#F0C890", "#C08A4A")
    o = DS_O
    a.ground(rx=50)
    # tail
    a.path("M136 150 C164 152 178 130 172 108 C168 96 156 100 158 112 C162 126 150 138 132 140 Z", fur, o, 3)
    a.path("M170 108 C168 96 156 100 158 112", "#FFFBF2", o, 2)
    # body
    a.path("M62 152 C58 126 78 112 100 112 C122 112 142 126 138 152 C136 172 120 180 100 180 C80 180 64 172 62 152 Z", fur, o)
    a.path("M84 146 C84 130 116 130 116 146 C116 166 108 174 100 174 C92 174 84 166 84 146 Z", "#FFFBF2")
    a.ell(82, 178, 11, 6, "#FFFBF2", o, 2.5)
    a.ell(118, 178, 11, 6, "#FFFBF2", o, 2.5)
    # GIANT ears
    a.path("M74 70 C52 56 34 20 40 8 C60 12 84 40 90 62 Z", fur, o, 3)
    a.path("M126 70 C148 56 166 20 160 8 C140 12 116 40 110 62 Z", fur, o, 3)
    a.path("M74 62 C58 50 48 28 48 18 C62 24 78 42 84 58 Z", "#FFC8B8", None)
    a.path("M126 62 C142 50 152 28 152 18 C138 24 122 42 116 58 Z", "#FFC8B8", None)
    # head
    a.path("M64 84 C64 62 80 54 100 54 C120 54 136 62 136 84 C136 104 120 120 100 122 C80 120 64 104 64 84 Z", fur, o)
    a.path("M82 96 C86 90 114 90 118 96 C114 112 106 120 100 120 C94 120 86 112 82 96 Z", "#FFFBF2", None)
    a.eyes(84, xs=(86, 114), rx=8, ry=10, iris="#C08A4A", pupil=("#2A1808", "#0A0602"))
    a.circ(100, 104, 4, "#3A2010")
    a.mouth(100, 110, "cat", w=5, color=o)
    a.cheeks([(76, 100), (124, 100)], "#FFA8A8", rx=6, ry=4, dots=False)
    for x, y in ((20, 60), (180, 60)):
        a.add(f'<path class="fx" d="M{x} {y - 10} q{6 if x < 100 else -6} 10 0 20 M{x + (8 if x < 100 else -8)} {y - 6} q{4 if x < 100 else -4} 6 0 12" stroke="#C8A050" stroke-width="2.5" fill="none" stroke-linecap="round"/>')


@chordoo("sandy")
def sandy(a):
    o = "#7A5420"
    a.ground(rx=66)
    sand = a.shade(*SAND)
    # wave foam at base
    a.path("M10 178 C30 168 50 186 70 176 C90 166 110 186 130 176 C150 166 170 186 190 176 V190 H10 Z", "#8AD8F0", "#3A98C8", 2)
    # castle body
    a.path("M40 176 V100 H160 V176 Z", sand, o, 3.5)
    for x in (40, 66, 92, 118, 144):
        a.path(f"M{x} 100 V88 H{x + 16} V100", sand, o, 3)
    # towers
    for x in (36, 164):
        a.path(f"M{x - 16} 176 V72 H{x + 16} V176 Z", sand, o, 3)
        for k in (-16, -2, 8):
            a.path(f"M{x + k} 72 V62 H{x + k + 8} V72", sand, o, 2.5)
    a.path("M164 62 V36", o, 2.5)
    a.path("M164 36 L182 42 L164 48 Z", "#FF6A7A", "#8A1A2A", 2)
    # door mouth + window eyes
    a.path("M84 176 V150 C84 136 116 136 116 150 V176 Z", "#C8A050", o, 2.5)
    a.eyes(124, xs=(78, 122), rx=10, ry=12, iris="#C8A050", pupil=("#3A2A10", "#120A04"))
    a.mouth(100, 150, "smile", w=8, color=o)
    a.cheeks([(60, 140), (140, 140)], "#FFA8A8", rx=7, ry=4, dots=False)
    # shells
    a.path("M30 140 C30 130 44 130 44 140 Z", "#FFC8D8", "#A04A6A", 1.5)
    a.circ(146, 160, 5, "#FFE8A8", "#A07A2A", 1.5)
    for x in (60, 100, 140):
        a.circ(x, 112, 2, "#C8A050")


@chordoo("camelot")
def camelot(a):
    fur = a.shade("#FFF0D8", "#E8C088", "#B0843E")
    o = DS_O
    a.ground(rx=62)
    # long legs
    for x in (66, 82, 122, 138):
        a.path(f"M{x - 5} 130 L{x - 5} 176 H{x + 5} L{x + 5} 130", fur, o, 3)
        a.ell(x, 178, 8, 4, "#8A6030")
    # body
    a.ell(102, 124, 50, 26, fur, o)
    # water-bottle hump
    a.path("M84 104 C80 76 92 60 104 60 C116 60 128 76 124 104 Z", a.lin("#C8F0FF", "#6AC8F0", "#3A98D8"), "#1E5A8A", 3)
    a.path("M96 60 V48 H112 V60 Z", "#5AB8E8", "#1E5A8A", 2.5)
    a.path("M92 48 H116 V40 H92 Z", "#FF6A7A", "#8A1A2A", 2.5)
    a.path("M88 80 C96 76 112 76 120 80 V96 C112 100 96 100 88 96 Z", "#FFFFFF", None, extra=' opacity=".35"')
    a.line("M92 74 L100 70", "#FFFFFF", 3, 0.8)
    # tail tuft
    a.path("M150 120 C160 124 162 136 158 144", "none", o, 3)
    # neck + head
    a.path("M60 120 C50 100 48 76 54 60 L74 60 C72 80 74 100 80 112 Z", fur, o, 3)
    a.path("M30 60 C28 42 44 32 60 34 C76 36 80 50 76 62 C72 76 58 80 44 80 C34 78 30 70 30 60 Z", fur, o)
    a.ell(36, 68, 10, 8, "#FFF6E8", None)
    a.circ(32, 66, 1.6, o)
    a.mouth(38, 74, "smile", w=4, color=o)
    a.ell(66, 34, 5, 9, fur, o, 2.5, rot=30)
    a.eye(56, 52, rx=7, ry=9, iris="#B0843E", pupil=("#2A1808", "#0A0602"), lashes=2, side=-1)
    a.cheeks([(62, 66)], rx=5, ry=3, dots=False)
    a.circ(170, 34, 14, a.fade("#FFE88A", 0.9), extra=' class="fx"')


@chordoo("tumbleweed")
def tumbleweed(a):
    o = "#6A4A1E"
    a.ground(cx=110, rx=46)
    # tangled ball made of looping strokes
    import random
    rnd = random.Random(7)
    a.circ(110, 118, 54, a.shade("#F8E8C0", "#D8B878", "#9A7A3A"), o, 3)
    for i in range(14):
        ang = rnd.uniform(0, math.pi * 2)
        r = rnd.uniform(20, 50)
        x1, y1 = 110 + r * math.cos(ang), 118 + r * math.sin(ang)
        x2, y2 = 110 + r * math.cos(ang + 2.2), 118 + r * math.sin(ang + 2.2)
        cx, cy = 110 + rnd.uniform(-40, 40), 118 + rnd.uniform(-40, 40)
        a.line(f"M{x1:.1f} {y1:.1f} Q{cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}", "#8A6A2E", 2.5, 0.75)
    for k in range(10):
        ang = math.radians(k * 36 + 8)
        a.line(f"M{110 + 52 * math.cos(ang):.1f} {118 + 52 * math.sin(ang):.1f} l{8 * math.cos(ang):.1f} {8 * math.sin(ang):.1f}", o, 2.5)
    # face in a clear patch
    a.ell(110, 120, 30, 22, "#F8E8C0", None, extra=' opacity=".9"')
    a.eyes(116, xs=(98, 122), rx=7, ry=9, iris="#D8B878", pupil=("#2A1A0A", "#0A0602"), look=(2, 0))
    a.mouth(110, 130, "open", w=6, color="#7A3E2E")
    a.cheeks([(88, 128), (132, 128)], rx=5, ry=3, dots=False)
    # wind + dust
    for d in ("M10 90 Q30 80 50 90", "M4 120 Q24 110 44 120", "M14 150 Q30 142 46 150"):
        a.line(d, "#C8B898", 3, 0.8)
    for x, y in ((60, 180), (48, 172), (70, 186)):
        a.circ(x, y, 3, "#D8C8A0", extra=' class="fx"')


@chordoo("mirajj")
def mirajj(a):
    o = "#6A2A6A"
    a.glow(100, 96, 80, "#FFD8A8", 0.6)
    a.ground(rx=30)
    # shimmering wavy body (layers)
    for k, c in enumerate(("#FFE8C0", "#FFC8A8", "#FFB0D0")):
        a.path(f"M{60 + k * 6} {170 - k * 4} C{50 + k * 6} 130 {80 + k * 4} 120 {70 + k * 4} 90 C{62} 60 {84} 34 {100} 34 C{116} 34 {138} 60 {130 - k * 4} 90 "
               f"C{120 - k * 4} 120 {150 - k * 6} 130 {140 - k * 6} {170 - k * 4} C120 {160 - k * 4} 110 {176 - k * 4} 100 {166 - k * 4} C90 {176 - k * 4} 80 {160 - k * 4} {60 + k * 6} {170 - k * 4} Z",
               c, o if k == 0 else None, 3, f' opacity="{0.9 - k * 0.15:.2f}"')
    # wavy shimmer lines across
    for y in (120, 140, 156):
        a.path(f"M70 {y} q8 -5 15 0 q8 5 15 0 q8 -5 15 0 q8 5 15 0", "none", "#FFFFFF", 2.2, ' opacity=".8"')
    a.eyes(80, xs=(88, 112), rx=8, ry=10, iris="#FF9AC8", pupil=("#3A1A3A", "#120612"), look=(3, 0))
    a.mouth(100, 98, "smirk", w=7, color=o)
    a.cheeks([(76, 94), (124, 94)], "#FF9AC8", rx=6, ry=4, dots=False)
    # hide-and-seek: little hands covering? peeking duplicate faint copy
    a.path("M150 60 C150 40 180 40 180 60 C180 80 168 92 165 100 C160 92 150 80 150 60 Z", "#FFC8A8", None, extra=' class="fx" opacity=".35"')
    a.circ(160, 58, 2.5, o, extra=' class="fx" opacity=".5"')
    a.circ(170, 58, 2.5, o, extra=' class="fx" opacity=".5"')
    for x, y in ((24, 60), (30, 140)):
        a.sparkle(x, y, 5, "#FFFFFF")


@chordoo("scarabelle")
def scarabelle(a):
    o = "#4A2A00"
    a.glow(100, 44, 40, "#FFE88A", 0.7)
    a.ground(rx=60)
    # sun disk held above
    a.circ(100, 44, 28, a.shade("#FFFFF0", "#FFD84D", "#FF9A20"), "#A85A00", 3)
    for i in range(12):
        a.add(f'<path class="fx" d="M100 10 L104 2 L96 2 Z" fill="#FFC83A" transform="rotate({i * 30} 100 44)"/>')
    # front legs holding sun
    limb(a, "M78 98 L70 72 L80 62", "#3A2A00", o, 6)
    limb(a, "M122 98 L130 72 L120 62", "#3A2A00", o, 6)
    for x, d in ((66, -1), (134, 1), (72, -1), (128, 1)):
        a.line(f"M{x} 140 L{x + d * 16} 160 L{x + d * 20} 180", o, 4)
    # shell: golden with lapis bands
    gold = a.shade("#FFF6C8", "#E8B840", "#A07810")
    a.path("M46 140 C44 110 66 92 100 92 C134 92 156 110 154 140 C152 168 126 178 100 178 C74 178 48 168 46 140 Z", gold, o)
    a.line("M100 104 V176", o, 3)
    for y in (120, 142, 162):
        a.path(f"M{52 + (y - 120) * 0.1:.0f} {y} Q76 {y + 6} 98 {y}", "none", "#2A5AC8", 4)
        a.path(f"M102 {y} Q124 {y + 6} {148 - (y - 120) * 0.1:.0f} {y}", "none", "#2A5AC8", 4)
    a.gloss(70, 108, 12, 5)
    # head
    a.path("M74 100 C74 78 126 78 126 100 Z", a.shade("#4A5AA8", "#2A3A88", "#141E4A"), o, 3)
    a.eyes(90, xs=(90, 110), rx=6, ry=7, iris="#FFD84D", pupil=("#141E4A", "#060A18"))
    a.mouth(100, 98, "smile", w=4, color="#FFD84D")
    a.cheeks([(80, 96), (120, 96)], "#FF9AA8", rx=4, ry=3, dots=False)


@chordoo("dunewyrm")
def dunewyrm(a):
    o = "#6A4210"
    a.ground(rx=80)
    # sand surface
    a.path("M0 150 C40 138 70 156 100 146 C130 136 160 152 200 142 V200 H0 Z", a.lin("#FFE8B0", "#E8C070"), "#A87A30", 2.5, ' class="fx"')
    sk = a.shade("#FFE8B8", "#E8B060", "#A06A20")
    # coils diving in and out of sand
    for (x1, x2, top) in ((18, 70, 92), (110, 160, 100)):
        d = f"M{x1} 150 C{x1} {top} {x2} {top} {x2} 150"
        a.add(f'<path d="{d}" fill="none" stroke="{o}" stroke-width="30" stroke-linecap="butt"/>')
        a.add(f'<path d="{d}" fill="none" stroke="{sk}" stroke-width="24" stroke-linecap="butt"/>')
        # dune-ridge back stripes
        a.add(f'<path d="{d}" fill="none" stroke="#C88A30" stroke-width="4" stroke-dasharray="3 9" transform="translate(0 -6)"/>')
    # head rising
    a.path("M150 146 C146 112 150 80 164 64", "none", o, 30)
    a.path("M150 146 C146 112 150 80 164 64", "none", sk, 24)
    a.path("M142 60 C140 38 158 28 174 32 C192 36 198 54 190 70 C182 84 160 86 150 78 C144 74 142 68 142 60 Z", sk, o)
    # dune fin crest
    a.path("M150 40 C156 24 168 18 176 22 C170 26 168 32 172 36 Z", "#C88A30", o, 2)
    a.eye(162, 52, rx=7, ry=9, iris="#E8B060", pupil=("#2A1A0A", "#0A0602"))
    a.eye(180, 52, rx=6, ry=8, iris="#E8B060", pupil=("#2A1A0A", "#0A0602"))
    a.mouth(172, 70, "smile", w=8, color=o)
    a.cheeks([(152, 66), (190, 64)], "#FFA8A8", rx=5, ry=3, dots=False)
    # tail tip poking out
    a.path("M10 150 C6 140 8 130 14 126 C16 136 20 142 24 150 Z", sk, o, 2.5)
    for x, y in ((80, 130), (96, 120), (40, 170)):
        a.circ(x, y, 2.5, "#E8C070", extra=' class="fx"')


@chordoo("sphinxie")
def sphinxie(a):
    fur = a.shade("#FFF2D8", "#F0C878", "#C08A30")
    o = DS_O
    a.ground(rx=64)
    # lying sphinx pose: front paws forward
    a.path("M48 150 C44 124 70 112 104 112 C140 112 164 124 162 150 C160 172 136 178 104 178 C72 178 50 172 48 150 Z", fur, o)
    a.path("M30 170 C30 160 60 158 86 160 C92 168 90 178 84 180 H36 C30 180 28 176 30 170 Z", fur, o, 3)
    a.path("M164 150 C176 140 186 122 180 108", "none", o, 8)
    a.path("M164 150 C176 140 186 122 180 108", "none", "#F0C878", 4)
    # nemes headdress (striped blue/gold)
    a.path("M54 96 C48 60 70 36 100 36 C130 36 152 60 146 96 L156 140 H130 L124 104 H76 L70 140 H44 Z", "#FFD84D", "#8A5A00", 3)
    for k in range(5):
        x = 56 + k * 4
        a.line(f"M{x} {94 + k * 10} L{x - 4} {104 + k * 10}", "#2A5AC8", 0)
    for x1, x2 in ((50, 72), (128, 150)):
        for y in (104, 116, 128):
            a.line(f"M{x1 + (2 if x1 < 100 else 0)} {y} H{x2 - (2 if x1 > 100 else 0)}", "#2A5AC8", 4)
    # face
    a.path("M70 78 C70 56 130 56 130 78 C130 100 116 110 100 110 C84 110 70 100 70 78 Z", fur, o)
    a.path("M70 64 C80 48 120 48 130 64", "none", "#2A5AC8", 6)
    a.path("M76 60 L70 38 L88 54 Z M124 60 L130 38 L112 54 Z", fur, o, 2.5)
    a.eyes(80, xs=(88, 112), rx=7, ry=9, iris="#2A5AC8", pupil=("#1A1A3A", "#06060E"))
    a.line("M80 80 L74 84 M120 80 L126 84", INK, 2.5)
    a.path("M97 92 L103 92 L100 95 Z", "#FF9AA8")
    a.mouth(100, 98, "cat", w=5, color=o)
    a.cheeks([(78, 94), (122, 94)], "#FFA8A8", rx=5, ry=3, dots=False)
    # riddle question marks
    a.add('<text class="fx" x="158" y="40" font-size="24" font-weight="bold" font-family="sans-serif" fill="#2A5AC8">?</text>')
    a.add('<text class="fx" x="22" y="60" font-size="18" font-weight="bold" font-family="sans-serif" fill="#E8B840">?</text>')


@chordoo("pharaowl")
def pharaowl(a):
    feat = a.shade("#F0E0C8", "#C8A070", "#806040")
    o = "#3A2410"
    a.ground(rx=46)
    # body
    a.ell(100, 128, 46, 50, feat, o)
    a.path("M74 130 C74 112 126 112 126 130 C128 160 114 172 100 172 C86 172 72 160 74 130 Z", "#FFF4E0")
    for y in (134, 146, 158):
        for x in (88, 100, 112):
            a.path(f"M{x - 4} {y} Q{x} {y + 4} {x + 4} {y}", "none", "#C8A070", 1.6)
    # gold collar necklace
    a.path("M62 104 C80 120 120 120 138 104 L140 114 C120 132 80 132 60 114 Z", "#FFD84D", "#8A5A00", 2.5)
    for x in (72, 86, 100, 114, 128):
        a.circ(x, 118 + abs(100 - x) * -0.1, 3, "#2A5AC8")
    # wings
    a.path("M54 112 C40 126 40 154 56 166 C58 146 60 128 56 112 Z", feat, o, 3)
    a.path("M146 112 C160 126 160 154 144 166 C142 146 140 128 144 112 Z", feat, o, 3)
    a.path("M86 178 l-4 6 M92 178 v7 M108 178 v7 M114 178 l4 6", "none", "#E0A030", 3)
    # headdress
    a.path("M56 90 C50 54 72 32 100 32 C128 32 150 54 144 90 L150 116 H132 L126 92 H74 L68 116 H50 Z", "#FFD84D", "#8A5A00", 3)
    for x1, x2 in ((54, 72), (128, 146)):
        for y in (96, 106):
            a.line(f"M{x1} {y} H{x2}", "#2A5AC8", 4)
    # face disc
    a.path("M68 78 C68 56 132 56 132 78 C132 98 116 106 100 106 C84 106 68 98 68 78 Z", "#FFF4E0", o, 2.5)
    a.eyes(80, xs=(86, 114), rx=10, ry=12, iris="#FFC83A", pupil=("#2A1A0A", "#0A0602"))
    a.line("M74 80 L66 84 M126 80 L134 84", INK, 2.5)
    a.mouth(100, 94, "beak", w=6)
    # cobra emblem
    a.path("M96 40 C96 30 104 30 104 40 L102 52 H98 Z", "#2A5AC8", "#141E4A", 2)
    # scroll of stories
    a.path("M150 168 H182 V180 H150 Z", "#FFF4D8", "#8A6A2A", 2)
    a.circ(150, 174, 6, "#E8D0A0", "#8A6A2A", 2)
    a.circ(182, 174, 6, "#E8D0A0", "#8A6A2A", 2)


@chordoo("oasira")
def oasira(a):
    fur = a.shade("#FFF2D8", "#F0C070", "#B87A28")
    o = DS_O
    a.glow(100, 80, 90, "#C8F0FF", 0.45)
    a.ground(rx=70)
    # oasis mane: water ring with palm fronds
    mane = a.shade("#E8FAFF", "#7AD0F0", "#2A88C8")
    pts = []
    for i in range(20):
        ang = math.radians(i * 18)
        r = 62 if i % 2 == 0 else 52
        pts.append(f"{100 + r * math.cos(ang):.1f} {76 + r * math.sin(ang):.1f}")
    a.path("M" + " L".join(pts) + " Z", mane, "#1E5A8A", 3)
    for i in range(10):
        ang = math.radians(i * 36 + 18)
        a.path(f"M{100 + 50 * math.cos(ang):.1f} {76 + 50 * math.sin(ang):.1f} q4 6 0 10", "none", "#FFFFFF", 2, ' opacity=".8"')
    # palm fronds on top
    for ang in (-150, -120, -60, -30):
        a.add(f'<g transform="translate(100 24) rotate({ang})"><path d="M0 0 C10 -10 34 -10 46 0 C34 4 12 6 0 0 Z" fill="#5EB84A" stroke="#2A5A1E" stroke-width="2.5"/></g>')
    a.circ(96, 26, 5, "#8A5A2A", "#3A2010", 1.5)
    a.circ(106, 28, 5, "#8A5A2A", "#3A2010", 1.5)
    # body lying
    a.path("M40 156 C36 130 62 120 100 120 C138 120 166 130 162 156 C160 174 138 180 100 180 C62 180 42 174 40 156 Z", fur, o)
    a.ell(64, 176, 18, 8, fur, o, 2.5)
    a.ell(136, 176, 18, 8, fur, o, 2.5)
    a.path("M160 150 C176 146 184 132 180 120", "none", o, 8)
    a.path("M160 150 C176 146 184 132 180 120", "none", "#F0C070", 4)
    a.path("M180 120 C178 110 186 104 190 112 C192 120 186 124 180 120 Z", mane, "#1E5A8A", 2)
    # face
    a.circ(100, 80, 34, fur, o)
    a.circ(74, 54, 9, fur, o, 2.5)
    a.circ(126, 54, 9, fur, o, 2.5)
    a.eyes(76, xs=(86, 114), rx=8, ry=10, iris="#2A88C8", pupil=("#1A2A3A", "#060A0E"), kind="star")
    a.ell(100, 96, 13, 9, "#FFF8EC", o, 2)
    a.path("M95 90 L105 90 L100 95 Z", "#C87A6A")
    a.mouth(100, 100, "cat", w=5, color=o)
    a.cheeks([(74, 94), (126, 94)], "#FFA8A8", rx=6, ry=4, dots=False)
    # pool with lily
    a.ell(30, 184, 22, 5, "#7AD0F0", "#2A88C8", 2, extra=' class="fx"')
    for x, y in ((180, 40), (20, 40)):
        a.sparkle(x, y, 6, "#C8F0FF")

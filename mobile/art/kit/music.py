import math
from artkit import chordoo, INK
from shapes import limb, star, note

MU_O = "#2A1A4A"


@chordoo("drumbo")
def drumbo(a):
    o = "#5A0E1E"
    a.ground(rx=50)
    for x in (82, 118):
        limb(a, f"M{x} 160 L{x} 178", "#F0C8A8", "#6A3A2A", 9)
        a.ell(x, 180, 10, 5, "#3A3A5A")
    # drum shell
    a.path("M44 70 V150 C44 168 156 168 156 150 V70 Z", a.lin("#FF6A7A", "#C82A3E", x2=1, y2=0), o, 3.5)
    # zigzag cords
    a.path("M50 80 L66 150 L82 80 L98 150 L114 80 L130 150 L146 80", "none", "#FFD84D", 3)
    a.path("M44 80 C44 94 156 94 156 80 M44 146 C44 160 156 160 156 146", "none", "#FFD84D", 6)
    # drum head (top)
    a.ell(100, 70, 56, 18, a.shade("#FFFFFF", "#F6F2EA", "#D8D0C0"), o, 3.5)
    # face on the drum head
    a.eyes(68, xs=(86, 114), rx=6, ry=7, iris="#FF6A7A", pupil=("#2A0A10", "#0A0206"))
    a.mouth(100, 74, "smile", w=6, color=o)
    a.cheeks([(72, 74), (128, 74)], rx=5, ry=3, dots=False)
    # drumstick arms
    limb(a, "M46 110 C30 100 26 82 34 66", "#F0C8A8", "#6A3A2A", 8)
    limb(a, "M154 110 C170 100 174 82 166 66", "#F0C8A8", "#6A3A2A", 8)
    a.line("M34 66 L62 42", "#C8A070", 5)
    a.circ(64, 40, 5, "#FFFFFF", "#8A6A3A", 2)
    a.line("M166 66 L140 40", "#C8A070", 5)
    a.circ(138, 38, 5, "#FFFFFF", "#8A6A3A", 2)
    a.add('<text class="fx" x="86" y="32" font-size="16" font-weight="bold" font-family="sans-serif" fill="#C82A3E">ba-dum!</text>')


@chordoo("tootle")
def tootle(a):
    o = "#1E3A5A"
    a.ground(rx=40)
    feat = a.shade("#E8F8FF", "#8AD0F0", "#3A88C0")
    # tail feathers like flute keys
    a.path("M130 130 L176 118 L178 132 L176 146 L132 146 Z", a.lin("#E8ECF8", "#A8B0C8"), "#4A5068", 3)
    for x in (146, 158, 170):
        a.circ(x, 132, 3.5, "#4A5068")
    # body
    a.ell(100, 124, 42, 40, feat, o)
    a.ell(96, 136, 24, 22, "#FFFFFF", None, extra=' opacity=".7"')
    a.path("M72 112 C58 124 60 148 74 156 C78 140 80 126 78 114 Z", feat, o, 3)
    a.path("M88 162 l-3 14 M88 176 l-6 4 M88 176 l4 4 M112 162 l3 14 M115 176 l-4 4 M115 176 l6 4", "none", "#FFA020", 3)
    # head with long whistle beak
    a.circ(98, 80, 28, feat, o)
    a.path("M120 78 L168 72 L168 86 L122 92 Z", a.lin("#F0F2F8", "#B8BED0"), "#4A5068", 2.5)
    a.circ(140, 82, 2.5, "#4A5068")
    a.circ(152, 80, 2.5, "#4A5068")
    a.eye(98, 76, rx=8, ry=10, iris="#8AD0F0", pupil=("#1E2A4A", "#06080E"), kind="happy")
    a.cheeks([(108, 94)], rx=6, ry=4, dots=False)
    a.path("M90 54 C88 42 96 36 104 40 C100 44 100 50 102 54", feat, o, 2.5)
    note(a, 176, 54, 0.8, "#3A88C0")
    note(a, 186, 30, 0.7, "#8AD0F0", double=True)


@chordoo("maraca")
def maraca(a):
    a.ground(rx=66)
    for cx, col, o, kind, tilt in ((64, ("#FFF0C8", "#FFC83A", "#D88A00"), "#6A4200", "happy", -14), (136, ("#E8FFE8", "#6AD88A", "#2A9A5A"), "#0E5A2A", "glossy", 14)):
        a.add(f'<g transform="rotate({tilt} {cx} 120)">')
        # handle
        a.path(f"M{cx - 7} 130 H{cx + 7} L{cx + 6} 178 C{cx + 6} 184 {cx - 6} 184 {cx - 6} 178 Z", a.lin("#E8C890", "#B8884A", x2=1, y2=0), "#6A4A1A", 2.5)
        # bulb
        a.ell(cx, 92, 34, 42, a.shade(*col), o, 3.5)
        # painted pattern
        a.path(f"M{cx - 32} 92 L{cx - 22} 82 L{cx - 12} 92 L{cx - 2} 82 L{cx + 8} 92 L{cx + 18} 82 L{cx + 28} 92", "none", "#FFFFFF", 3)
        a.path(f"M{cx - 30} 108 Q{cx} 118 {cx + 30} 108", "none", "#E8405A", 3)
        a.add('</g>')
        a.eyes(66, xs=(cx - 12, cx + 12), kind=kind, rx=6, ry=8, iris=col[1], pupil=("#2A1A0A", "#0A0602"))
        a.mouth(cx, 78, "open", w=6, color="#7A3E2E")
        a.cheeks([(cx - 20, 78), (cx + 20, 78)], rx=5, ry=3, dots=False)
    for x, y in ((100, 40), (100, 70), (24, 30), (176, 30)):
        a.add(f'<path class="fx" d="M{x - 6} {y} q3 -6 6 0 q3 6 6 0" stroke="#B89AF0" stroke-width="2.5" fill="none" stroke-linecap="round"/>')


@chordoo("kazoo")
def kazoo(a):
    o = "#3A1A5A"
    a.ground(rx=56)
    # kazoo-shaped body (tapered tube), as beetle shell
    shell = a.lin("#FFB0E0", "#E85AB0", "#A02A78")
    a.path("M30 120 C30 104 40 98 60 96 L150 88 C170 88 178 104 178 116 C178 130 170 144 150 144 L60 138 C40 136 30 132 30 120 Z", shell, o, 3.5)
    # kazoo turret on top
    a.path("M100 92 L104 64 H128 L132 90 Z", a.lin("#FFE84D", "#E0A800"), "#6A4A00", 3)
    a.ell(116, 64, 13, 5, "#FFF6A8", "#6A4A00", 2.5)
    # legs
    for x in (62, 88, 118, 144):
        a.line(f"M{x} 140 L{x - 6} 160 L{x - 2} 180", o, 4)
    # face at the narrow end (left)
    a.eye(48, 112, rx=7, ry=9, iris="#FF5AB0", pupil=("#2A0A1E", "#0A0206"))
    a.eye(66, 110, rx=6, ry=8, iris="#FF5AB0", pupil=("#2A0A1E", "#0A0206"))
    a.mouth(54, 126, "o", w=7, color=o)
    a.cheeks([(40, 124)], rx=5, ry=3, dots=False)
    a.line("M44 98 C38 82 30 76 22 76 M58 96 C58 80 54 70 48 66", o, 2.5)
    a.gloss(108, 104, 22, 5, rot=-4)
    # buzz waves
    for i, x in enumerate((140, 160)):
        a.add(f'<path class="fx" d="M{x} {50 - i * 12} q6 -6 12 0 q6 6 12 0" stroke="#E85AB0" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    note(a, 24, 70, 0.8, "#E85AB0")


@chordoo("pianopus")
def pianopus(a):
    o = "#1E1A4A"
    a.ground(rx=70)
    sk = a.shade("#E8D8FF", "#9A7AE8", "#5A3AA8")
    # piano keys row along the bottom (the octopus sits behind)
    a.path("M10 150 H190 V184 H10 Z", "#FFFFFF", o, 3)
    for x in range(10, 191, 18):
        a.line(f"M{x} 150 V184", o, 1.8)
    for x in range(22, 186, 18):
        if (x // 18) % 7 not in (2, 6):
            a.path(f"M{x} 150 H{x + 11} V170 H{x} Z", "#2A2A3A")
    # 8 tentacles resting on keys
    for i in range(8):
        x0 = 54 + i * 13
        xe = 18 + i * 23
        a.line(f"M{x0} 120 C{x0} 136 {xe} 132 {xe} 154", o, 12)
        a.line(f"M{x0} 120 C{x0} 136 {xe} 132 {xe} 154", "#9A7AE8", 8)
    # head
    a.path("M50 110 C44 60 72 28 100 28 C128 28 156 60 150 110 C148 128 128 134 100 134 C72 134 52 128 50 110 Z", sk, o)
    for x, y in ((74, 58), (128, 62), (138, 88)):
        a.circ(x, y, 4, "#C8B0FF", extra=' opacity=".8"')
    a.eyes(90, xs=(82, 118), kind="happy", rx=9)
    a.mouth(100, 106, "open", w=7, color="#5A1A4A")
    a.cheeks([(66, 102), (134, 102)], "#FF9AD0", rx=8, ry=5)
    a.gloss(78, 50, 12, 6)
    # bow tie
    a.path("M100 124 L86 116 L86 132 Z M100 124 L114 116 L114 132 Z", "#2A2A3A", o, 2)
    note(a, 26, 60, 1, "#9A7AE8", double=True)
    note(a, 172, 44, 0.9, "#5A3AA8")


@chordoo("guitarmadillo")
def guitarmadillo(a):
    o = "#4A2408"
    a.ground(rx=66)
    sk = a.shade("#F0D8C0", "#C8A080", "#8A6A4A")
    # legs
    for x in (60, 84, 120, 144):
        a.path(f"M{x - 8} 150 L{x - 8} 178 H{x + 8} L{x + 8} 150", sk, o, 3)
    # guitar-body shell
    wood = a.shade("#FFD8A0", "#E89A4A", "#A85A1A")
    a.path("M40 140 C28 120 38 92 62 92 C76 92 82 100 96 100 C110 100 118 86 140 86 C166 86 176 114 166 136 C158 156 128 160 104 158 C80 158 50 158 40 140 Z", wood, o, 3.5)
    a.circ(104, 124, 14, "#3A1E0A", o, 2.5)
    a.circ(104, 124, 18, "none", "#FFE8C0", 2)
    # bridge + strings + neck as tail
    a.path("M68 130 H80 V140 H68 Z", "#3A1E0A")
    a.path("M74 132 L196 98 M74 135 L196 102 M74 138 L196 106", "none", "#F0F0F0", 1.2)
    a.path("M150 100 L196 88 L198 110 L154 118 Z", "#6A3A14", o, 2.5)
    for x in (168, 180, 192):
        a.line(f"M{x} {93 - (x - 168) * 0.2} V{86 - (x - 168) * 0.2}", "#FFD84D", 3)
    # head
    a.path("M8 124 C6 104 22 92 38 96 C52 100 56 118 50 130 C44 142 14 144 8 124 Z", sk, o)
    a.ell(16, 96, 6, 12, sk, o, 2.5, rot=-30)
    a.ell(36, 92, 6, 12, sk, o, 2.5, rot=20)
    a.eye(24, 114, kind="happy", rx=6)
    a.eye(42, 114, kind="happy", rx=5)
    a.mouth(30, 130, "smile", w=6, color=o)
    a.cheeks([(18, 128), (46, 126)], rx=4, ry=3, dots=False)
    note(a, 120, 50, 1, "#E89A4A")
    note(a, 60, 40, 0.8, "#A85A1A", double=True)


@chordoo("trumpetal")
def trumpetal(a):
    o = "#5A3A00"
    a.ground(rx=40)
    # stem + leaves
    a.line("M100 184 V120", "#3E8A2E", 6)
    a.path("M100 160 C80 150 64 156 56 168 C74 172 88 168 100 160 Z", a.shade("#D6F5A8", "#7CC850", "#3E8A2E"), "#2A5A1E", 2.5)
    a.path("M100 146 C120 136 136 142 144 154 C126 158 112 154 100 146 Z", a.shade("#D6F5A8", "#7CC850", "#3E8A2E"), "#2A5A1E", 2.5)
    # flower-trumpet bell (brass petals)
    a.path("M92 126 L88 84 C68 80 40 66 34 40 C56 46 70 44 82 36 C90 50 110 50 118 36 C130 44 144 46 166 40 C160 66 132 80 112 84 L108 126 Z",
           a.shade("#FFF6C8", "#FFC83A", "#C88A00"), o, 3.5)
    a.path("M50 48 C70 60 130 60 150 48 C140 62 120 70 100 70 C80 70 60 62 50 48 Z", "#C88A00", None, extra=' opacity=".45"')
    # valves
    for x in (94, 100, 106):
        a.line(f"M{x} 96 V88", "#8A5A00", 3)
        a.circ(x, 86, 3, "#FFE8A0", "#8A5A00", 1.4)
    a.eyes(106, xs=(92, 108), rx=5, ry=6, iris="#FFC83A", pupil=("#2A1A00", "#0A0600"))
    a.mouth(100, 116, "o", w=5, color=o)
    # fanfare
    for d in ("M40 24 L28 12", "M100 26 V8", "M160 24 L172 12"):
        a.line(d, "#FFC83A", 3, 0.9)
    note(a, 26, 92, 0.9, "#C88A00")
    note(a, 166, 96, 0.9, "#C88A00", double=True)
    # sun rising behind
    a.circ(170, 170, 16, a.fade("#FFB86A", 0.9), extra=' class="fx"')


@chordoo("harpy")
def harpy(a):
    o = "#2A3A6A"
    a.glow(100, 100, 80, "#E8F0FF", 0.5)
    a.ground(rx=56)
    # water ripple
    a.ell(100, 178, 70, 8, "#C8E8FF", "#8AB8E8", 2)
    feat = a.shade("#FFFFFF", "#F2F4FF", "#B8C0E0")
    # harp wing: golden frame with strings
    a.path("M120 140 C110 96 120 50 160 30 C170 60 172 110 150 146 Z", "none", "#C88A00", 5)
    for k in range(6):
        x = 128 + k * 6
        a.line(f"M{x} {140 - k * 2} L{x + 4} {62 - k * 4}", "#FFE8A0", 1.6)
    a.path("M120 140 C110 96 120 50 160 30", "none", "#FFC83A", 3)
    # body
    a.path("M40 140 C40 116 66 108 96 112 C124 116 150 126 150 146 C150 166 120 174 94 172 C64 170 40 162 40 140 Z", feat, o)
    a.path("M54 130 C70 118 90 120 104 132 C88 134 70 138 54 130 Z", "#E0E6FF", o, 2)
    # long neck curve + head
    a.path("M56 128 C40 100 38 68 58 52 C70 42 88 46 90 58", "none", o, 15)
    a.path("M56 128 C40 100 38 68 58 52 C70 42 88 46 90 58", "none", "#F6F8FF", 10)
    a.circ(78, 54, 18, feat, o, 3)
    a.path("M94 54 L112 60 L94 64 Z", "#FFA040", "#8A4A00", 2)
    a.path("M92 50 C90 46 86 46 84 48", "none", INK, 3)
    a.eye(76, 52, kind="sleepy", rx=6)
    a.cheeks([(84, 62)], rx=5, ry=3, dots=False)
    # tiny crown of a swan
    a.path("M70 38 L72 28 L78 34 L82 26 L86 36 Z", "#FFC83A", "#8A5A00", 1.6)
    note(a, 26, 52, 0.8, "#8AB8E8")
    note(a, 176, 160, 0.8, "#8AB8E8", double=True)


@chordoo("bassoon")
def bassoon(a):
    o = "#2A1408"
    a.ground(rx=56)
    wood = a.lin("#C88A4A", "#7A4A1A", x2=1, y2=0)
    # long upright bassoon body coiled as snake
    d = "M60 180 C60 150 140 150 140 120 C140 90 60 96 60 66 C60 46 80 36 96 40"
    a.add(f'<path d="{d}" fill="none" stroke="{o}" stroke-width="34" stroke-linecap="round"/>')
    a.add(f'<path d="{d}" fill="none" stroke="{wood}" stroke-width="28" stroke-linecap="round"/>')
    # silver key bands
    for t in ((76, 162), (122, 138), (122, 104), (74, 84)):
        a.circ(t[0], t[1], 5, "#E8ECF8", "#4A5068", 2)
    a.line("M64 150 L88 156 M118 118 L140 112", "#C8CCD8", 3)
    # bocal (crook) as tongue/reed + head
    a.path("M94 26 C110 14 132 18 140 34 C146 48 136 62 120 62 C104 62 92 50 94 26 Z", a.shade("#E8B880", "#B87A3A", "#7A4A1A"), o, 3)
    a.line("M140 40 C156 40 168 30 172 18", "#C8CCD8", 4)
    a.path("M170 20 L180 10 L178 22 Z", "#FFE8A0", "#8A6A00", 1.5)
    a.eye(110, 36, kind="sleepy", rx=6)
    a.eye(128, 34, kind="sleepy", rx=5)
    a.mouth(122, 50, "o", w=8, color=o)
    a.cheeks([(104, 48), (138, 46)], rx=4, ry=3, dots=False)
    # deep low notes
    note(a, 160, 90, 1.2, "#7A4A1A")
    note(a, 26, 120, 1.1, "#7A4A1A", double=True)
    a.add('<text class="fx" x="132" y="150" font-size="14" font-weight="bold" font-family="sans-serif" fill="#7A4A1A">bwomp</text>')


@chordoo("discodile")
def discodile(a):
    sk = a.shade("#D8FFB8", "#6AC84A", "#2E7A22")
    o = "#123A0A"
    a.ground(rx=56)
    # disco ball + light spots
    a.line("M100 0 V12", "#8A8AA8", 2)
    a.circ(100, 24, 12, a.shade("#FFFFFF", "#C8C8E0", "#7A7A9A"), "#4A4A6A", 2)
    a.path("M88 24 H112 M100 12 V36 M91 16 L109 32 M109 16 L91 32", "none", "#FFFFFF", 1, ' opacity=".7"')
    for x, y, c in ((30, 50, "#FF6AD8"), (170, 60, "#6AE8FF"), (40, 120, "#FFE84D"), (176, 130, "#FF6AD8")):
        a.circ(x, y, 6, c, extra=' class="fx" opacity=".7"')
    # tail
    a.path("M124 160 C150 168 176 160 188 146 C168 148 150 146 134 140 Z", sk, o, 3)
    # legs in bell-bottoms
    for x, sx in ((84, -1), (116, 1)):
        a.path(f"M{x - 10} 140 L{x + sx * 4 - 14} 182 H{x + sx * 4 + 14} L{x + 10} 140 Z", a.lin("#FFFFFF", "#E0E0F0"), "#3A3A5A", 2.5)
    # white disco suit body
    a.path("M70 150 C64 116 76 92 100 92 C124 92 136 116 130 150 Z", a.lin("#FFFFFF", "#E8E8F4"), "#3A3A5A", 3)
    a.path("M88 94 L100 120 L112 94", "none", "#3A3A5A", 2.5)
    a.path("M92 94 L100 112 L108 94 Z", sk, None)
    a.line("M74 132 H126", "#FFD84D", 5)
    # pointing disco arm up, other on hip
    limb(a, "M124 104 L146 78 L156 48", "#FFFFFF", "#3A3A5A", 11)
    a.circ(157, 44, 6, sk, o, 2)
    limb(a, "M76 104 L58 120 L72 134", "#FFFFFF", "#3A3A5A", 11)
    # crocodile head with long snout
    a.path("M70 60 C66 40 86 30 104 34 C120 36 128 50 126 62 L168 66 C176 68 176 82 168 84 L108 90 C88 92 72 82 70 60 Z", sk, o)
    a.path("M120 84 L126 78 L132 84 L138 78 L144 84 L150 78 L156 84", "none", "#FFFFFF", 2)
    a.circ(166, 70, 2, o)
    # shades
    a.path("M76 52 H120 L116 64 C110 70 100 68 98 60 C96 68 86 70 80 64 Z", a.lin("#FF6AD8", "#8A2AE8", x2=1, y2=0), "#1A1A2A", 2.5)
    a.line("M82 56 L88 56", "#FFFFFF", 2)
    a.mouth(110, 80, "smile", w=10, color=o)


@chordoo("maestro")
def maestro(a):
    fur = a.shade("#5A5A6A", "#2E2E3A", "#121218")
    o = "#06060A"
    a.ground(rx=50)
    # baton tail raised
    a.path("M130 150 C158 148 172 120 168 90", "none", o, 10)
    a.path("M130 150 C158 148 172 120 168 90", "none", "#2E2E3A", 6)
    a.line("M168 90 L176 40", "#FFFFFF", 4)
    a.circ(168, 92, 4, "#E8E8F0", o, 1.5)
    a.sparkle(178, 34, 6)
    # tuxedo body sitting upright
    a.path("M60 180 C54 144 66 108 100 106 C134 108 146 144 140 180 Z", fur, o)
    a.path("M86 108 L100 180 L114 108 Z", "#FFFFFF", None)
    a.path("M100 116 L90 110 L90 122 Z M100 116 L110 110 L110 122 Z", "#E8303A", "#6A0A14", 1.6)
    for y in (134, 150, 166):
        a.circ(100, y, 2.5, "#2E2E3A")
    a.ell(80, 180, 12, 6, "#FFFFFF", o, 2.5)
    a.ell(120, 180, 12, 6, "#FFFFFF", o, 2.5)
    # arms conducting
    limb(a, "M68 124 C52 112 46 96 50 82", "#2E2E3A", o, 10)
    a.circ(50, 78, 6, "#FFFFFF", o, 2)
    limb(a, "M132 124 C144 128 150 136 152 146", "#2E2E3A", o, 10)
    # head
    a.circ(100, 76, 32, fur, o)
    a.path("M74 58 L70 28 L94 48 Z", fur, o, 3)
    a.path("M126 58 L130 28 L106 48 Z", fur, o, 3)
    a.path("M76 52 L74 36 L86 46 Z", "#FFB0C8", None)
    a.path("M124 52 L126 36 L114 46 Z", "#FFB0C8", None)
    a.path("M84 90 C84 80 116 80 116 90 C116 100 106 104 100 104 C94 104 84 100 84 90 Z", "#FFFFFF", None)
    a.eyes(74, xs=(88, 112), kind="happy", rx=7)
    a.path("M96 88 L104 88 L100 92 Z", "#FF8AB0")
    a.mouth(100, 94, "cat", w=5, color=o)
    # whiskers + fancy mustache curl
    for sx in (1, -1):
        a.line(f"M{100 + sx * 16} 92 L{100 + sx * 36} 88 M{100 + sx * 16} 96 L{100 + sx * 36} 98", "#C8C8D8", 1.6)
    note(a, 24, 50, 0.9, "#5A5A6A")
    note(a, 30, 130, 0.8, "#5A5A6A", double=True)


@chordoo("symphonix")
def symphonix(a):
    o = "#3A1A5A"
    a.glow(100, 96, 88, "#FFD8F0", 0.45)
    a.ground(rx=40)
    feat = a.shade("#FFF0FA", "#FF9AD0", "#C84A98")
    # music-note tail feathers fanning
    cols = ["#FF6A9A", "#FFB03A", "#FFD84D", "#6AD88A", "#5AB8FF", "#B87AF0"]
    for i, ang in enumerate(range(-150, -20, 26)):
        rad = math.radians(ang)
        x2, y2 = 100 + 78 * math.cos(rad), 132 + 78 * math.sin(rad)
        a.line(f"M100 132 L{x2:.1f} {y2:.1f}", "#3A1A5A", 4)
        a.ell(round(x2 - 5, 1), round(y2 + 3, 1), 9, 7, cols[i % 6], o, 2.5, rot=-20)
        a.path(f"M{x2 + 3:.1f} {y2 + 2:.1f} V{y2 - 18:.1f} Q{x2 + 10:.1f} {y2 - 12:.1f} {x2 + 14:.1f} {y2 - 8:.1f}", "none", o, 2.5)
    # wings
    a.path("M64 128 C48 140 48 164 62 172 C66 156 70 142 72 132 Z", feat, o, 3)
    a.path("M136 128 C152 140 152 164 138 172 C134 156 130 142 128 132 Z", feat, o, 3)
    # body
    a.ell(100, 140, 38, 40, feat, o)
    a.ell(100, 150, 22, 24, "#FFFFFF", None, extra=' opacity=".6"')
    # treble-clef crest on head
    a.path("M100 86 C88 76 92 56 106 56 C118 58 116 76 104 76 C96 76 96 66 102 64 M104 76 C110 86 106 100 98 98", "none", "#B87AF0", 4)
    a.eyes(128, xs=(88, 112), rx=8, ry=10, iris="#B87AF0", pupil=("#2A1A4A", "#0A0614"), kind="star")
    a.mouth(100, 144, "beak", w=7)
    a.cheeks([(78, 142), (122, 142)], rx=6, ry=4, dots=False)
    a.path("M90 180 l-3 6 M96 180 v7 M104 180 v7 M110 180 l3 6", "none", "#FFA020", 3)


@chordoo("melodia")
def melodia(a):
    o = "#3A1A6A"
    a.glow(100, 96, 96, "#E8D0FF", 0.55)
    # swirl of staff lines around her
    for k in range(5):
        a.add(f'<path class="fx" d="M6 {130 + k * 5} C50 {90 + k * 5} 80 {170 + k * 5} 120 {120 + k * 5} C150 {84 + k * 5} 176 {110 + k * 5} 196 {80 + k * 5}" stroke="#C8A8F0" stroke-width="1.4" fill="none" opacity=".8"/>')
    a.ground(rx=36)
    # wings
    w = a.lin("#FFFFFF", "#E8D8FF", "#B89AF0")
    a.path("M94 98 C72 66 36 60 30 84 C36 104 70 108 92 104 Z", w, o, 2.5)
    a.path("M106 98 C128 66 164 60 170 84 C164 104 130 108 108 104 Z", w, o, 2.5)
    # dress shaped like a bell / note head
    a.path("M88 100 C76 130 66 156 70 170 C86 176 114 176 130 170 C134 156 124 130 112 100 Z", a.lin("#C89AFF", "#7A4AD8"), o, 3)
    for y in (130, 146, 160):
        a.path(f"M{80 - (y - 130) * 0.2} {y} Q100 {y + 6} {120 + (y - 130) * 0.2} {y}", "none", "#FFFFFF", 1.6, ' opacity=".6"')
    # head + hair as a treble swirl
    skin = a.shade("#FFF4EC", "#F8D8C8", "#D8A898")
    a.circ(100, 76, 22, skin, "#6A3A3A", 2.5)
    a.path("M78 74 C74 46 128 44 124 72 C132 62 136 48 126 40 C116 30 92 30 82 42 C76 50 76 62 78 74 Z", a.lin("#FFB0E0", "#B87AF0"), o, 2.5)
    a.path("M124 64 C138 70 140 90 128 98", "none", "#B87AF0", 5)
    a.eyes(78, xs=(92, 108), kind="happy", rx=6)
    a.mouth(100, 90, "o", w=6, color="#A04A5A")
    a.cheeks([(86, 86), (114, 86)], rx=5, ry=3, dots=False)
    star(a, 100, 34, 6, "#FFF6A8", "#8A6A00", 1.4)
    # floating notes all around
    for x, y, s, c, dbl in ((28, 50, 1, "#FF6AB0", False), (172, 40, 1.1, "#6AB8FF", True), (20, 110, 0.9, "#FFC83A", True),
                            (178, 110, 0.9, "#6AD88A", False), (40, 170, 0.8, "#B87AF0", False), (160, 172, 0.8, "#FF6AB0", True)):
        note(a, x, y, s, c, dbl)

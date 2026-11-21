from artkit import chordoo, INK


@chordoo("cinder")
def cinder(a):
    fur = a.shade("#FFE0B0", "#FF9A4A", "#E0602A")
    o = "#A8401A"
    a.ground()
    # smoky tail
    smoke = a.lin("#9C8FB8", "#D8D0EA", x1=0, y1=1, x2=1, y2=0)
    a.path("M138 150 C160 150 170 132 162 120 C176 116 180 98 168 92 C172 80 160 70 150 78 C146 92 150 104 142 112 C136 124 130 138 138 150 Z", smoke, "#6E6488", 3)
    a.circ(166, 86, 3, "#FFB13D", extra=' class="fx"')
    a.circ(176, 104, 2.4, "#FF7A1A", extra=' class="fx"')
    # body sitting
    a.path("M62 176 C56 146 70 120 100 120 C130 120 144 146 138 176 Z", fur, o)
    a.ell(100, 156, 22, 18, "#FFF1DE")
    # paws
    for x in (80, 120):
        a.ell(x, 176, 14, 9, fur, o, 3.5)
        a.line(f"M{x - 4} 172 V178 M{x + 4} 172 V178", o, 2)
    # floppy ears
    a.path("M64 70 C44 70 38 104 50 118 C60 112 68 96 74 82 Z", "#C24A1E", o)
    a.path("M136 70 C156 70 162 104 150 118 C140 112 132 96 126 82 Z", "#C24A1E", o)
    # head
    a.path("M100 44 C134 44 148 66 148 90 C148 116 128 130 100 130 C72 130 52 116 52 90 C52 66 66 44 100 44 Z", fur, o)
    a.path("M92 46 Q100 30 108 46 Q102 40 100 44 Q98 40 92 46 Z", "#FFD23F", "#E0602A", 2)  # flame tuft
    a.ell(100, 108, 22, 16, "#FFF1DE")
    a.gloss(74, 64)
    a.cheeks([(66, 104), (134, 104)], "#FF5A3C")
    a.eyes(88, xs=(80, 120), rx=10, ry=12, iris="#FFB13D", pupil=("#5A2A12", "#1F0C04"))
    a.ell(100, 103, 6, 4.5, "#3A1A0C")
    a.mouth(100, 110, "open", w=7, color="#6B2010")
    # collar with flame tag
    a.path("M70 126 Q100 138 130 126 L130 132 Q100 144 70 132 Z", "#3D5AFE", "#1A1866", 2.5)
    a.path("M100 136 C106 142 104 150 100 152 C96 150 94 142 100 136 Z", "#FFD23F", "#B37A00", 2)


@chordoo("toastie")
def toastie(a):
    mm = a.shade("#FFFFFF", "#FFF2E6", "#E8D5C4")
    top = a.lin("#E8A050", "#B8682A")
    a.ground(rx=46)
    # stick
    a.path("M128 150 L170 188", "none", "#8A5A34", 7)
    a.path("M128 150 L170 188", "none", "#B98252", 3)
    # marshmallow body (squishy cylinder)
    a.path("M56 76 C56 64 144 64 144 76 L146 152 C146 168 54 168 54 152 Z", mm, "#B89C86")
    a.path("M56 76 C56 88 144 88 144 76 C144 64 56 64 56 76 Z", top, "#8A4A1E")
    a.path("M62 80 C74 90 92 92 104 88", "none", "#FFE0A8", 2.5, ' opacity=".7"')
    a.ell(100, 72, 20, 5, "#F5C27A", extra=' opacity=".7"')
    # little stubby arms
    a.ell(50, 128, 9, 12, mm, "#B89C86", 3, rot=20)
    a.ell(150, 128, 9, 12, mm, "#B89C86", 3, rot=-20)
    # nervous sweat drop
    a.path("M148 92 C152 100 152 106 148 108 C144 106 144 100 148 92 Z", "#9BE3FF", "#3A9AD9", 2)
    a.cheeks([(70, 132), (130, 132)], "#FF8FA3")
    a.eyes(116, xs=(82, 118), rx=9, ry=11, iris="#C98A5A", pupil=("#4A3022", "#1A0E08"))
    a.mouth(100, 134, "o", w=8)
    a.gloss(68, 100, 6, 14, rot=0, op=0.7)


@chordoo("wickit")
def wickit(a):
    wax = a.shade("#FFFDF5", "#FFE9C7", "#F0C890")
    a.ground(rx=40)
    a.glow(100, 42, 40, "#FFC23D", 0.5)
    # candle body with drips
    a.path("M68 84 C68 76 132 76 132 84 L134 168 C134 178 66 178 66 168 Z", wax, "#C89A5A")
    a.path("M68 86 C70 100 76 102 76 92 C78 110 86 112 86 96 C90 104 96 104 98 92 L132 86 C130 104 124 106 122 94 C120 110 112 108 112 96 Z", "#FFFFFF", None, extra=' opacity=".6"')
    # holder
    a.path("M52 168 C52 160 148 160 148 168 L146 178 C146 184 54 184 54 178 Z", a.lin("#FFD86B", "#D99A1F"), "#9A6A10")
    a.path("M148 166 C164 162 170 176 156 180", "none", "#9A6A10", 4)
    # wick + flame hat
    a.line("M100 78 V66", INK, 3)
    a.path("M100 14 C118 34 122 52 112 64 C106 70 94 70 88 64 C78 52 82 34 100 14 Z", a.lin("#FFF6A8", "#FFB13D", "#FF6A2A"), "#D9541A", 3)
    a.path("M100 36 C108 46 108 56 104 62 C100 64 96 62 94 58 C92 50 94 44 100 36 Z", "#FFFBE0", None)
    # tiny arms
    a.line("M68 118 Q54 112 50 100", "#C89A5A", 6)
    a.line("M68 118 Q54 112 50 100", wax, 3)
    a.line("M132 118 Q146 124 150 134", "#C89A5A", 6)
    a.line("M132 118 Q146 124 150 134", wax, 3)
    a.cheeks([(78, 128), (122, 128)], "#FF9A7A", rx=9, ry=6)
    a.eyes(112, xs=(86, 114), rx=8, ry=10, iris="#FFB13D", pupil=("#5A3A12", "#1F1004"))
    a.mouth(100, 128, "smile", w=6)
    a.sparkle(150, 40, 6)
    a.sparkle(52, 58, 4, "#FFFFFF")


@chordoo("flarefin")
def flarefin(a):
    lava = a.shade("#FFE07A", "#FF7A2A", "#C8321E", cx=0.35, cy=0.35)
    o = "#7A1E12"
    a.glow(100, 104, 80, "#FF7A2A", 0.35)
    # tail
    a.path("M54 104 C34 80 18 78 12 84 C22 96 22 112 12 124 C18 130 34 128 54 104 Z", a.lin("#FFD23F", "#FF5A2A", x2=1, y2=0), o)
    # fins
    a.path("M96 66 C104 42 124 34 136 40 C128 50 124 60 124 72 Z", a.lin("#FFD23F", "#FF5A2A"), o, 3)
    a.path("M100 140 C104 158 118 166 128 162 C122 154 120 146 120 138 Z", a.lin("#FF5A2A", "#FFD23F"), o, 3)
    # body
    a.path("M48 104 C56 72 100 60 136 68 C166 74 182 92 182 106 C182 124 162 140 128 142 C92 144 56 136 48 104 Z", lava, o)
    # lava cracks
    a.line("M74 92 L84 102 L78 114 M98 80 L104 94 L96 104 L102 118 M120 120 L126 130", "#FFF2A0", 2.6)
    a.line("M74 92 L84 102 L78 114 M98 80 L104 94 L96 104 L102 118 M120 120 L126 130", "#8A2A12", 1, 0.5)
    a.gloss(124, 80, 14, 6, rot=-10)
    a.eye(150, 98, rx=11, ry=12, iris="#FFE07A", pupil=("#5A1A0A", "#200604"))
    a.ell(172, 116, 3.5, 3, "#7A1E12")
    a.mouth(162, 124, "smile", w=6, color="#7A1E12")
    a.cheeks([(146, 120)], "#FFE07A", rx=8, ry=5)
    # bubbles of heat
    for x, y, r in ((40, 60, 6), (56, 42, 4), (30, 40, 3)):
        a.circ(x, y, r, "#FFE7B8", "#FF8A3D", 2, extra=' class="fx"')


@chordoo("smolder")
def smolder(a):
    skin = a.shade("#FF9A7A", "#E84A3A", "#A82A2A")
    o = "#5E1414"
    a.ground(rx=70)
    # warm rock
    a.path("M30 178 C30 160 60 150 100 150 C140 150 172 160 172 178 Z", a.lin("#8A8098", "#5A5070"), "#3B3450", 3)
    a.line("M60 160 L70 166 M130 158 L140 164", "#FF8A3D", 2.4, 0.8)
    # tail curl
    a.path("M146 150 C176 146 186 124 172 110 C166 104 156 108 160 116 C166 126 156 138 138 140 Z", skin, o)
    # body lying
    a.path("M40 146 C40 124 70 112 104 112 C136 112 156 124 156 142 C156 154 132 160 98 160 C64 160 40 158 40 146 Z", skin, o)
    # ember spots
    for x, y, r in ((80, 124, 5), (100, 120, 4), (120, 126, 5), (138, 132, 3.5), (64, 132, 3.5)):
        a.circ(x, y, r, "#FFC23D", "#FF6A2A", 1.5)
    # legs
    for x in (66, 128):
        a.ell(x, 160, 11, 6, skin, o, 3)
    # head resting
    a.path("M18 132 C18 106 40 92 62 94 C86 96 96 112 92 130 C88 148 70 154 50 152 C30 150 18 146 18 132 Z", skin, o)
    a.gloss(40, 104, 10, 5)
    a.eye(46, 122, rx=7, ry=8, kind="sleepy")
    a.eye(72, 120, rx=7, ry=8, kind="sleepy")
    a.cheeks([(36, 136), (80, 136)], "#FFB13D", rx=7, ry=5)
    a.mouth(58, 136, "smile", w=6, color=o)
    # zzz smoke
    a.add('<text class="fx" x="88" y="84" font-size="16" font-weight="800" fill="#9C8FB8" font-family="sans-serif">z</text>')
    a.add('<text class="fx" x="100" y="66" font-size="22" font-weight="800" fill="#9C8FB8" font-family="sans-serif">Z</text>')


@chordoo("chilipip")
def chilipip(a):
    red = a.shade("#FF9A8A", "#F03A2A", "#B01818")
    o = "#6E0A0A"
    a.ground(rx=40)
    # pepper body (curved)
    a.path("M76 60 C56 76 56 116 72 146 C86 172 116 182 126 170 C134 160 120 150 116 132 C112 110 120 86 116 66 C110 50 90 48 76 60 Z", red, o)
    a.path("M84 72 C74 90 74 120 84 140", "none", "#FFFFFF", 4, ' opacity=".45"')
    # stem + leaf hair
    a.path("M96 54 C96 40 104 30 116 28", "none", "#2E7D3E", 6)
    a.path("M96 54 C96 40 104 30 116 28", "none", "#5CBF5A", 3)
    a.path("M100 46 C86 30 66 30 60 40 C72 48 86 50 100 46 Z", a.lin("#9BE07A", "#3FAF5A"), "#2E7D3E", 2.5)
    a.path("M104 42 C116 24 138 24 144 34 C132 44 118 46 104 42 Z", a.lin("#9BE07A", "#3FAF5A"), "#2E7D3E", 2.5)
    a.path("M74 58 C82 50 112 50 118 60 C108 66 84 66 74 58 Z", "#3FAF5A", "#2E7D3E", 2.5)
    # arms (crossed attitude)
    a.line("M68 112 Q86 122 104 112", o, 6)
    a.line("M68 112 Q86 122 104 112", "#F03A2A", 3)
    # face
    a.eye(80, 92, rx=8, ry=9, kind="angry", iris="#FFC23D", pupil=("#4A0A0A", "#1A0202"), side=1)
    a.eye(106, 90, rx=8, ry=9, kind="angry", iris="#FFC23D", pupil=("#4A0A0A", "#1A0202"), side=-1)
    a.mouth(94, 104, "smirk", w=7, color=o)
    a.cheeks([(72, 104), (114, 100)], "#FFB13D", rx=7, ry=5, dots=False)
    # heat lines
    a.line("M140 80 Q146 74 140 68 Q134 62 140 56 M152 96 Q158 90 152 84 Q146 78 152 72", "#FF6A2A", 2.6, 0.8)


@chordoo("kettlewick")
def kettlewick(a):
    pot = a.shade("#FFE0EC", "#FF8FB8", "#D04A7A")
    o = "#7A1E44"
    a.ground(rx=56)
    # tail as handle (dragon tail loop)
    a.path("M146 96 C176 92 182 132 152 142", "none", o, 10)
    a.path("M146 96 C176 92 182 132 152 142", "none", "#FF8FB8", 5)
    a.path("M150 140 L164 150 L148 152 Z", "#FFD23F", o, 2.5)
    # wings
    a.path("M70 90 C50 70 34 76 32 90 C42 88 46 96 42 104 C52 100 58 106 60 112 Z", a.lin("#FFD6E6", "#FF8FB8"), o, 3)
    # body (teapot)
    a.path("M56 120 C56 90 76 76 104 76 C132 76 152 90 152 120 C152 156 130 172 104 172 C78 172 56 156 56 120 Z", pot, o)
    a.path("M62 132 C80 140 128 140 146 132", "none", "#FFFFFF", 3, ' opacity=".6"')
    for x in (78, 104, 130):
        a.circ(x, 150, 4, "#FFE14D", "#B37A00", 1.5)
    # lid with dragon horns
    a.path("M74 80 C74 64 134 64 134 80 Z", a.lin("#FFE0EC", "#FF8FB8"), o, 3)
    a.circ(104, 60, 7, "#FFD23F", "#B37A00", 2.5)
    a.path("M80 70 L72 50 L88 64 Z M128 70 L136 50 L120 64 Z", "#FFF3D0", "#B5822E", 2.5)
    # spout snout with steam
    a.path("M56 118 C40 116 30 104 22 90 C30 88 36 92 40 98 C46 104 52 106 58 106 Z", pot, o, 3)
    a.path("M18 80 Q10 70 18 62 Q26 54 18 46", "none", "#D8D0EA", 4, ' class="fx"')
    a.path("M30 72 Q24 64 30 58", "none", "#D8D0EA", 3, ' class="fx"')
    # feet
    for x in (82, 126):
        a.ell(x, 172, 12, 7, pot, o, 3)
    a.gloss(80, 92)
    a.cheeks([(78, 124), (136, 124)], "#FF5A8A")
    a.eyes(110, xs=(94, 124), rx=9, ry=11, iris="#FF8FB8", pupil=("#4A1230", "#1A0410"), kind="happy")
    a.mouth(110, 126, "open", w=6, color=o)
    # music note
    a.line("M168 50 V34 L180 30 V46", o, 2.5)
    a.ell(165, 51, 4, 3, o)
    a.ell(177, 47, 4, 3, o)


@chordoo("pyrowl")
def pyrowl(a):
    feather = a.shade("#FFD8A8", "#E8884A", "#A8502A")
    o = "#5A2412"
    a.ground(rx=48)
    # book stack
    a.path("M56 168 H144 V182 H56 Z", "#3D5AFE", "#1A1866", 3)
    a.path("M62 156 H138 V168 H62 Z", "#22B573", "#0F6A40", 3)
    a.line("M60 175 H140 M66 162 H134", "#FFFFFF", 1.6, 0.7)
    # wings with fire tips
    for s in (1, -1):
        x = 100 - 48 * s
        a.path(f"M{100 - 30 * s} 92 C{x} 96 {x - 6 * s} 130 {x + 4 * s} 150 C{x + 14 * s} 146 {100 - 34 * s} 130 {100 - 30 * s} 92 Z", feather, o, 3)
        a.path(f"M{x + 4 * s} 150 C{x - 10 * s} 156 {x - 16 * s} 140 {x - 8 * s} 128 C{x - 4 * s} 138 {x} 142 {x + 4 * s} 150 Z", a.lin("#FFE14D", "#FF5A2A"), "#C2401E", 2.2)
    # body
    a.path("M100 50 C136 50 150 80 148 112 C146 146 126 160 100 160 C74 160 54 146 52 112 C50 80 64 50 100 50 Z", feather, o)
    a.path("M100 104 C120 104 132 120 130 140 C122 154 78 154 70 140 C68 120 80 104 100 104 Z", "#FFF1DE")
    for y in (118, 130, 142):
        a.line(f"M86 {y} Q90 {y + 4} 94 {y} M106 {y} Q110 {y + 4} 114 {y}", "#E8C49A", 2)
    # ear tufts as flames
    a.path("M62 66 C54 46 60 30 70 24 C70 40 78 50 84 58 Z", a.lin("#FFE14D", "#FF5A2A"), "#C2401E", 2.5)
    a.path("M138 66 C146 46 140 30 130 24 C130 40 122 50 116 58 Z", a.lin("#FFE14D", "#FF5A2A"), "#C2401E", 2.5)
    # facial disc + glasses
    a.ell(80, 84, 20, 19, "#FFF1DE")
    a.ell(120, 84, 20, 19, "#FFF1DE")
    a.eye(80, 84, rx=11, ry=12, iris="#FF8A3D", pupil=("#5A2010", "#1A0804"))
    a.eye(120, 84, rx=11, ry=12, iris="#FF8A3D", pupil=("#5A2010", "#1A0804"))
    a.circ(80, 84, 16, "none", "#B37A00", 3)
    a.circ(120, 84, 16, "none", "#B37A00", 3)
    a.line("M96 82 Q100 78 104 82", "#B37A00", 3)
    a.mouth(100, 100, "beak", w=6)
    a.gloss(72, 62, 9, 4)
    # feet on books
    a.line("M88 158 L84 158 M88 158 L88 162 M112 158 L116 158 M112 158 L112 162", "#E0A030", 3)
    a.glow(160, 40, 18, "#FFC23D", 0.5)
    a.sparkle(160, 40, 6)


@chordoo("magmole")
def magmole(a):
    fur = a.shade("#8E7AA8", "#5E4A78", "#3A2A52")
    o = "#22163A"
    rock = a.lin("#FFB13D", "#E84A2A", "#8A1E12")
    # dirt mound
    a.path("M14 186 C24 150 60 140 100 140 C140 140 176 150 186 186 Z", a.lin("#A8794A", "#6E4A2A"), "#4A2E16", 3)
    for x, y in ((40, 172), (150, 170), (120, 182), (70, 180)):
        a.circ(x, y, 3, "#4A2E16")
    # body emerging
    a.path("M54 150 C50 100 70 64 100 64 C130 64 150 100 146 150 Z", fur, o)
    a.path("M76 150 C76 120 86 104 100 104 C114 104 124 120 124 150 Z", "#B8A8D0", None, extra=' opacity=".55"')
    # big claws on mound
    for s in (1, -1):
        x = 100 - 42 * s
        a.path(f"M{x} 140 C{x - 20 * s} 142 {x - 26 * s} 156 {x - 16 * s} 160 C{x - 6 * s} 162 {x + 10 * s} 156 {x + 12 * s} 148 Z", "#FFD6E6", o, 3)
        for k in range(3):
            cx = x - 20 * s + k * 7 * s
            a.path(f"M{cx} 158 L{cx - 2 * s} 168 L{cx + 4 * s} 159 Z", "#FFF3D0", "#8A6A2A", 1.6)
    # lava rock nose
    a.path("M88 106 C88 96 112 96 112 106 C112 118 104 122 100 122 C96 122 88 118 88 106 Z", rock, "#6E1E12", 3)
    a.line("M94 104 L100 110 L106 104", "#FFF2A0", 2)
    # tiny eyes + hard hat
    a.eye(82, 92, rx=5, ry=5, kind="dot", pupil=("#1A1226", "#120B22"))
    a.eye(118, 92, rx=5, ry=5, kind="dot", pupil=("#1A1226", "#120B22"))
    a.path("M64 74 C64 46 136 46 136 74 Z", a.lin("#FFE14D", "#F5A300"), "#9A6A10", 3)
    a.path("M56 76 H144 V82 H56 Z", "#F5A300", "#9A6A10", 2.5)
    a.circ(100, 60, 8, "#FFFBE0", "#9A6A10", 2)
    a.circ(100, 60, 4, "#FFE14D")
    a.cheeks([(72, 110), (128, 110)], "#FF8FB8", rx=8, ry=5)
    a.mouth(100, 128, "smile", w=6, color="#FFD6E6")


@chordoo("sunmane")
def sunmane(a):
    fur = a.shade("#FFE8B0", "#FFC24A", "#E8902A")
    o = "#9A4A12"
    a.glow(100, 92, 90, "#FFB13D", 0.45)
    a.ground(rx=56)
    # sun-ray mane
    rays = []
    import math
    for i in range(16):
        ang = i * math.pi * 2 / 16
        r1, r2 = 46, 70 if i % 2 == 0 else 60
        x1, y1 = 100 + r1 * math.cos(ang - 0.18), 88 + r1 * math.sin(ang - 0.18)
        x2, y2 = 100 + r2 * math.cos(ang), 88 + r2 * math.sin(ang)
        x3, y3 = 100 + r1 * math.cos(ang + 0.18), 88 + r1 * math.sin(ang + 0.18)
        rays.append(f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} L{x3:.1f} {y3:.1f} Z")
    a.path(" ".join(rays), a.lin("#FFE14D", "#FF7A2A"), "#C2501E", 2.5)
    a.circ(100, 88, 50, a.lin("#FF9A3D", "#FF6A2A"), "#C2501E", 3)
    # body + paws
    a.path("M68 176 C62 146 76 128 100 128 C124 128 138 146 132 176 Z", fur, o)
    for x in (82, 118):
        a.ell(x, 176, 14, 8, fur, o, 3)
    a.path("M132 160 C156 160 166 144 160 134", "none", o, 6)
    a.path("M132 160 C156 160 166 144 160 134", "none", "#FFC24A", 3)
    a.circ(160, 130, 7, "#FF7A2A", "#C2501E", 2.5)
    # face
    a.path("M100 52 C126 52 138 70 138 90 C138 112 122 124 100 124 C78 124 62 112 62 90 C62 70 74 52 100 52 Z", fur, o)
    a.circ(70, 60, 9, fur, o, 3)
    a.circ(130, 60, 9, fur, o, 3)
    a.circ(70, 60, 4, "#FF9A7A")
    a.circ(130, 60, 4, "#FF9A7A")
    a.ell(100, 106, 18, 13, "#FFF3DA")
    a.gloss(80, 70, 8, 4)
    a.eyes(88, xs=(84, 116), rx=9, ry=11, iris="#FF7A2A", pupil=("#5A2A0A", "#1F0C02"))
    a.path("M94 100 L106 100 L100 107 Z", "#7A3A2A", "#5A2A1A", 1.5)
    a.mouth(100, 110, "open", w=7, color="#6B2010")
    a.cheeks([(72, 104), (128, 104)], "#FF5A3C", rx=9, ry=6)
    a.sparkle(24, 40, 6)
    a.sparkle(176, 150, 5, "#FFFFFF")


@chordoo("phoenixa")
def phoenixa(a):
    plume = a.shade("#FFF2B0", "#FF8A3D", "#E8304A")
    o = "#8A1230"
    a.glow(100, 100, 90, "#FF8A3D", 0.4)
    # ribbon tail feathers
    for d, c in (("M92 140 C70 170 40 176 22 168 C40 160 56 150 70 132", "#FFC23D"),
                 ("M100 146 C100 176 84 192 66 194 C78 180 84 164 86 146", "#FF5A8A"),
                 ("M108 140 C130 170 160 176 178 168 C160 160 144 150 130 132", "#A24BFF")):
        a.path(d + " Z", c, o, 3)
        a.circ(float(d.split()[-2]) if False else 0, 0, 0, "none")
    for x, y, c in ((26, 168, "#FFC23D"), (68, 192, "#FF5A8A"), (174, 168, "#A24BFF")):
        a.circ(x, y, 7, "#FFFFFF", c, 3)
        a.circ(x, y, 3, c)
    # wings raised
    a.path("M70 96 C40 60 20 56 14 70 C26 70 30 80 24 90 C36 88 40 98 34 108 C48 104 58 110 66 120 Z", a.lin("#FFE14D", "#FF6A2A", "#E8304A"), o, 3)
    a.path("M130 96 C160 60 180 56 186 70 C174 70 170 80 176 90 C164 88 160 98 166 108 C152 104 142 110 134 120 Z", a.lin("#FFE14D", "#FF6A2A", "#E8304A"), o, 3)
    # body
    a.path("M100 58 C128 58 140 84 138 108 C136 134 120 148 100 148 C80 148 64 134 62 108 C60 84 72 58 100 58 Z", plume, o)
    a.path("M100 104 C114 104 124 116 122 132 C116 142 84 142 78 132 C76 116 86 104 100 104 Z", "#FFF2C4")
    # crest
    a.path("M94 60 C82 40 84 22 94 14 C96 30 100 40 104 50 C108 34 118 24 130 22 C122 38 114 50 108 62 Z", a.lin("#FFE14D", "#FF5A2A"), o, 3)
    a.circ(94, 14, 4, "#FFE14D", o, 2)
    a.circ(130, 22, 4, "#FFE14D", o, 2)
    a.gloss(80, 76, 9, 5)
    a.eyes(90, xs=(86, 114), rx=9, ry=11, iris="#FFC23D", pupil=("#5A1020", "#1F0408"), kind="star", lashes=2)
    a.mouth(100, 102, "beak", w=6)
    a.cheeks([(76, 104), (124, 104)], "#FF5A8A", rx=8, ry=5)
    a.sparkle(30, 30, 7)
    a.sparkle(170, 30, 6, "#FFFFFF")
    a.sparkle(160, 120, 5)


@chordoo("volcanor")
def volcanor(a):
    rock = a.lin("#7A6E90", "#4A3F60", "#2A2240")
    o = "#160F26"
    a.glow(100, 110, 92, "#FF5A2A", 0.4)
    a.ground(rx=70)
    # legs
    for x in (68, 132):
        a.path(f"M{x - 18} 150 L{x - 22} 182 L{x + 22} 182 L{x + 18} 150 Z", rock, o, 3.5)
    # volcano body
    a.path("M40 164 L72 52 L128 52 L160 164 Z", rock, o)
    a.path("M72 52 L128 52 L120 64 L80 64 Z", "#2A2240", o, 3)
    # lava flows
    lava = a.lin("#FFF2A0", "#FF8A3D", "#E8304A")
    a.path("M84 62 C86 80 76 92 80 110 C82 120 90 118 90 108 C90 92 98 80 96 62 Z", lava, "#8A1E12", 2.5)
    a.path("M114 62 C112 74 122 86 118 100 C116 108 110 106 110 98 C110 86 104 76 106 62 Z", lava, "#8A1E12", 2.5)
    # crater lava pool + smoke crown
    a.ell(100, 56, 26, 6, lava, "#8A1E12", 2.5)
    smoke = a.lin("#E8E2F5", "#A89CC4")
    a.path("M74 50 C60 40 66 22 82 26 C82 10 104 6 110 20 C122 8 142 18 134 34 C148 38 142 56 126 50 Z", smoke, "#6E6488", 3)
    for x in (88, 104, 120):
        a.path(f"M{x - 6} 30 L{x} 18 L{x + 6} 30 Z", "#FFC93C", "#A86A0A", 2)
    # arms (boulders)
    a.path("M46 112 C26 112 18 132 24 148 C32 160 48 158 54 146 Z", rock, o, 3.5)
    a.path("M154 112 C174 112 182 132 176 148 C168 160 152 158 146 146 Z", rock, o, 3.5)
    # face glowing
    a.eye(84, 126, rx=9, ry=9, kind="glow", iris="#FFC23D", pupil=("#FFF2A0", "#FF8A3D"))
    a.eye(116, 126, rx=9, ry=9, kind="glow", iris="#FFC23D", pupil=("#FFF2A0", "#FF8A3D"))
    a.mouth(100, 142, "grin", w=10, color="#8A1E12")
    a.line("M62 90 L70 96 M132 98 L140 92 M56 140 L64 136", "#FF8A3D", 2.2, 0.8)
    a.sparkle(26, 70, 6, "#FFC23D")
    a.sparkle(176, 76, 5, "#FFC23D")

from artkit import chordoo, INK

WATER_O = "#1E4E8A"


@chordoo("drip")
def drip(a):
    body = a.shade("#E6F8FF", "#7FD0FF", "#3A8EE0")
    a.ground(rx=40)
    # umbrella
    a.line("M132 40 V112 Q132 120 124 120", "#6E4A2A", 3.5)
    a.path("M92 50 C96 24 168 24 172 50 C164 44 156 44 152 50 C146 44 138 44 132 50 C126 44 118 44 112 50 C106 44 98 44 92 50 Z", a.lin("#FFD84D", "#FF8A3D"), "#B8501A", 3)
    a.line("M132 26 V20", "#6E4A2A", 3)
    # body drop
    a.path("M92 54 C110 80 140 108 140 136 C140 162 120 178 96 178 C72 178 52 162 52 136 C52 108 76 80 92 54 Z", body, WATER_O)
    a.gloss(74, 112, 8, 14, rot=-20, op=0.6)
    a.ell(130, 120, 9, 6, body, WATER_O, 3, rot=-30)  # arm holding
    a.eyes(132, xs=(80, 110), rx=10, ry=12, iris="#7FD0FF", pupil=("#1E3A6E", "#0A1630"))
    a.mouth(95, 150, "smile", w=7, color="#1E3A6E")
    a.cheeks([(68, 148), (122, 148)], "#FF8FB0", rx=8, ry=5)
    # rain drops
    for x, y in ((30, 60), (50, 30), (180, 90), (20, 110)):
        a.path(f"M{x} {y} C{x + 4} {y + 6} {x + 4} {y + 10} {x} {y + 11} C{x - 4} {y + 10} {x - 4} {y + 6} {x} {y} Z", "#9BE3FF", "#3A9AD9", 1.5, ' class="fx"')


@chordoo("shellby")
def shellby(a):
    skin = a.shade("#D8F5C8", "#8AD27A", "#4E9E4A")
    o = "#2A5A2A"
    a.ground(rx=66)
    # legs
    for x in (56, 84, 120, 148):
        a.ell(x, 168, 13, 12, skin, o, 3)
    # head
    a.path("M146 120 C150 96 168 88 182 98 C194 108 190 132 174 140 C162 146 148 140 146 120 Z", skin, o)
    a.eye(168, 112, rx=7, ry=9, iris="#8AD27A", pupil=("#1E3A1E", "#0A160A"))
    a.mouth(178, 128, "smile", w=5, color=o)
    a.cheeks([(160, 128)], "#FF8FB0", rx=6, ry=4)
    # shell (seashell swirl dome)
    sh = a.lin("#FFE8F0", "#FFB0C8", "#E07A9A")
    a.path("M30 150 C30 96 60 70 100 70 C140 70 160 100 160 150 Z", sh, "#9A3A5A")
    a.line("M100 150 C96 120 74 110 64 124 C56 136 70 146 80 140 C88 134 82 124 76 128", "#9A3A5A", 3)
    for d in ("M52 150 C52 118 66 96 84 86", "M120 150 C128 118 126 94 112 76", "M140 150 C146 124 144 104 132 88"):
        a.line(d, "#C2507A", 2.4, 0.7)
    a.path("M26 150 H164 V158 Q95 166 26 158 Z", "#FFD6E6", "#9A3A5A", 3)
    a.gloss(66, 90, 14, 6)
    a.sparkle(40, 50, 5, "#FFFFFF")


@chordoo("splashpup")
def splashpup(a):
    fur = a.shade("#E8D2B8", "#A8784E", "#6E4A2A")
    o = "#3A2414"
    # water ring
    a.ell(100, 176, 78, 14, a.lin("#9BE3FF", "#4AB2E8"), "#2A82C0", 3)
    a.line("M30 174 Q40 168 50 174 M150 176 Q160 170 170 176", "#FFFFFF", 2.5, 0.8)
    # body floating on back
    a.path("M40 150 C40 124 70 110 104 110 C140 110 164 124 164 148 C164 168 136 176 102 176 C68 176 40 170 40 150 Z", fur, o)
    a.path("M70 150 C70 132 86 124 104 124 C124 124 138 132 138 150 C138 162 122 168 104 168 C86 168 70 162 70 150 Z", "#F5E6D2")
    # starfish hug
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        r = 22 if i % 2 == 0 else 10
        pts.append(f"{104 + r * math.cos(ang):.1f} {142 + r * math.sin(ang):.1f}")
    a.path("M" + " L".join(pts) + " Z", a.lin("#FFB0C8", "#FF6A8A"), "#B8304A", 2.5)
    for x, y in ((100, 136), (110, 140), (104, 148)):
        a.circ(x, y, 1.8, "#FFFFFF")
    # paws on starfish
    a.ell(84, 136, 9, 7, fur, o, 3, rot=-20)
    a.ell(124, 136, 9, 7, fur, o, 3, rot=20)
    # head
    a.path("M60 84 C60 56 80 42 104 42 C128 42 148 56 148 84 C148 108 128 120 104 120 C80 120 60 108 60 84 Z", fur, o)
    a.circ(66, 58, 8, fur, o, 3)
    a.circ(142, 58, 8, fur, o, 3)
    a.ell(104, 98, 22, 15, "#F5E6D2")
    a.gloss(78, 58, 9, 4)
    a.eyes(80, xs=(86, 122), rx=9, ry=11, iris="#8AD0FF", pupil=("#3A2414", "#140A04"))
    a.ell(104, 92, 7, 5, "#2A1A0E")
    a.mouth(104, 100, "cat", w=7, color=o)
    a.line("M80 98 L66 96 M80 102 L66 104 M128 98 L142 96 M128 102 L142 104", o, 1.6)
    a.cheeks([(72, 96), (136, 96)], "#FF8FA3", rx=8, ry=5, dots=False)
    for x, y in ((30, 140), (176, 138), (40, 120)):
        a.circ(x, y, 4, "#E6F8FF", "#4AB2E8", 1.5, extra=' class="fx"')


@chordoo("krilla")
def krilla(a):
    body = a.shade("#F2E0FF", "#C48CFF", "#8A4ADB")
    o = "#4A1E8A"
    a.ground(rx=66)
    socks = ["#FF6B4A", "#22B573", "#FFC23D", "#3A86FF", "#FF4D8D", "#14B8A6", "#A24BFF", "#FF8A3D"]
    xs = [30, 48, 66, 86, 114, 134, 152, 170]
    for i, x in enumerate(xs):
        bend = 10 if i % 2 else -10
        a.path(f"M{100 + (x - 100) * 0.35} 120 C{x + bend} 140 {x - bend} 158 {x} 168", "none", o, 13)
        a.path(f"M{100 + (x - 100) * 0.35} 120 C{x + bend} 140 {x - bend} 158 {x} 168", "none", "#C48CFF", 8)
        a.ell(x, 170, 9, 8, socks[i], INK, 2.5)
        a.line(f"M{x - 7} 166 H{x + 7}", "#FFFFFF", 2, 0.8)
    # head dome
    a.path("M48 104 C48 58 72 34 100 34 C128 34 152 58 152 104 C152 124 130 132 100 132 C70 132 48 124 48 104 Z", body, o)
    for x, y, r in ((70, 60, 5), (132, 66, 4), (124, 48, 3), (60, 82, 3)):
        a.circ(x, y, r, "#E8D2FF", None)
    a.gloss(74, 52, 12, 6)
    a.eyes(96, xs=(80, 120), rx=11, ry=13, iris="#FF8FD8", pupil=("#3A1E6E", "#140A2E"))
    a.mouth(100, 114, "open", w=6, color="#3A1E6E")
    a.cheeks([(64, 110), (136, 110)], "#FF6FB0")
    a.add('<text class="fx" x="158" y="44" font-size="20" fill="#FF4D8D" font-family="sans-serif">♥</text>')


@chordoo("bubblun")
def bubblun(a):
    body = a.shade("#FFF8D6", "#FFD84D", "#E8A020")
    o = "#8A5A0A"
    a.ell(100, 186, 50, 6, INK, extra=' opacity=".1"')
    # tail + fins
    a.path("M30 100 C14 84 8 90 10 100 C8 110 14 116 30 100 Z", a.lin("#FFB0C8", "#FF6A8A"), "#B8304A", 3)
    a.path("M100 30 C92 18 108 14 112 26 Z", "#FF6A8A", "#B8304A", 2.5)
    # spikes
    import math
    sp = []
    for i in range(18):
        ang = i * math.pi * 2 / 18
        bx, by = 100 + 66 * math.cos(ang), 100 + 66 * math.sin(ang)
        tx, ty = 100 + 80 * math.cos(ang), 100 + 80 * math.sin(ang)
        lx, ly = 100 + 64 * math.cos(ang - 0.08), 100 + 64 * math.sin(ang - 0.08)
        sp.append(f"M{lx:.1f} {ly:.1f} L{tx:.1f} {ty:.1f} L{bx:.1f} {by:.1f}")
    a.path(" ".join(sp), "#FFF2C4", o, 2.5)
    a.circ(100, 100, 68, body, o, 3.5)
    a.path("M52 120 C64 150 136 150 148 120 C140 160 60 160 52 120 Z", "#FFFFFF", None, extra=' opacity=".6"')
    for x, y in ((70, 70), (130, 66), (60, 100), (142, 100), (100, 56)):
        a.circ(x, y, 5, "#FF8A3D", None, extra=' opacity=".7"')
    a.gloss(74, 58, 14, 7)
    a.eyes(98, xs=(80, 120), rx=13, ry=15, iris="#7FD0FF", pupil=("#1E3A6E", "#0A1630"))
    a.mouth(100, 124, "o", w=12, color="#8A3A0A")
    a.cheeks([(62, 120), (138, 120)], "#FF8FA3")
    a.add('<text class="fx" x="150" y="40" font-size="26" font-weight="900" fill="#FF6A8A" font-family="sans-serif">!</text>')


@chordoo("seahop")
def seahop(a):
    body = a.shade("#FFE0F0", "#FF9AC8", "#D85A9A")
    o = "#7A1E52"
    a.glow(100, 100, 80, "#7FD0FF", 0.3)
    # curly tail
    a.path("M110 140 C122 160 120 182 100 184 C84 184 80 166 92 160 C102 156 106 168 98 170", "none", o, 12)
    a.path("M110 140 C122 160 120 182 100 184 C84 184 80 166 92 160 C102 156 106 168 98 170", "none", "#FF9AC8", 7)
    # back fin
    a.path("M128 90 C150 84 158 104 146 118 C140 110 134 104 126 104 Z", a.lin("#FFE14D", "#FFB0C8"), o, 3)
    # body
    a.path("M100 40 C130 40 140 64 132 86 C126 104 134 120 126 138 C118 154 96 156 86 140 C78 126 88 112 84 100 C70 98 60 88 62 74 C66 54 80 40 100 40 Z", body, o)
    a.path("M92 108 C104 104 116 112 116 126 C112 138 98 140 92 130 Z", "#FFF2F8")
    for y in (114, 122, 130):
        a.line(f"M96 {y} H112", "#FFB0C8", 2)
    # snout
    a.path("M66 76 C52 76 38 80 32 86 C40 92 54 92 66 88 Z", body, o, 3)
    a.circ(32, 87, 3, o)
    # crown
    a.path("M88 42 L86 24 L96 34 L104 18 L110 34 L120 26 L118 44 Z", a.lin("#FFF3A0", "#FFC93C"), "#A86A0A", 2.5)
    a.circ(104, 30, 3, "#4DD6FF")
    a.gloss(112, 54, 8, 4)
    a.eye(96, 68, rx=10, ry=12, iris="#7FD0FF", pupil=("#3A1E4E", "#140A1E"), lashes=2)
    a.cheeks([(84, 86)], "#FF5A9A", rx=8, ry=5)
    for x, y, r in ((46, 50, 6), (36, 30, 4), (160, 56, 5), (170, 36, 3)):
        a.circ(x, y, r, "#E6F8FF", "#4AB2E8", 1.8, extra=' class="fx"')


@chordoo("tidewing")
def tidewing(a):
    top = a.lin("#7FD0FF", "#3A6EE0", "#1E2E8A")
    o = "#101A4E"
    a.glow(100, 100, 86, "#4AB2E8", 0.35)
    # tail
    a.path("M100 140 C102 160 110 178 126 190", "none", o, 5)
    a.path("M100 140 C102 160 110 178 126 190", "none", "#3A6EE0", 2)
    # wings / body (diamond)
    a.path("M100 52 C120 60 150 70 186 96 C160 112 132 120 112 140 C104 146 96 146 88 140 C68 120 40 112 14 96 C50 70 80 60 100 52 Z", top, o)
    # wave patterns
    for d in ("M40 94 Q50 86 60 94 Q70 102 80 94", "M120 94 Q130 86 140 94 Q150 102 160 94", "M66 112 Q76 104 86 112", "M114 112 Q124 104 134 112"):
        a.line(d, "#BFEFFF", 2.6, 0.8)
    a.circ(52, 84, 3, "#FFFFFF", extra=' opacity=".7"')
    a.circ(150, 84, 3, "#FFFFFF", extra=' opacity=".7"')
    # head lobes
    a.path("M86 58 C82 46 88 38 94 40 C94 48 96 52 98 56 Z", top, o, 2.5)
    a.path("M114 58 C118 46 112 38 106 40 C106 48 104 52 102 56 Z", top, o, 2.5)
    a.gloss(80, 70, 14, 5, rot=-15)
    a.eyes(80, xs=(88, 112), rx=7, ry=8, iris="#7FD0FF", pupil=("#101A4E", "#04081E"))
    a.mouth(100, 96, "smile", w=7, color="#BFEFFF")
    a.cheeks([(78, 92), (122, 92)], "#FF8FD8", rx=6, ry=4, dots=False)
    for x, y, r in ((30, 150, 5), (170, 146, 4), (40, 170, 3)):
        a.circ(x, y, r, "#E6F8FF", "#4AB2E8", 1.6, extra=' class="fx"')


@chordoo("coralie")
def coralie(a):
    body = a.shade("#FFE6DA", "#FF9A80", "#E0604A")
    o = "#8A2A1A"
    a.ground(rx=46)
    # coral antlers
    coral = a.lin("#FFB0C8", "#FF5A7A")
    for s in (1, -1):
        a.path(f"M{100 - 20 * s} 62 C{100 - 30 * s} 46 {100 - 44 * s} 40 {100 - 50 * s} 24", "none", "#B8304A", 10)
        a.path(f"M{100 - 20 * s} 62 C{100 - 30 * s} 46 {100 - 44 * s} 40 {100 - 50 * s} 24", "none", "#FF7A9A", 6)
        a.path(f"M{100 - 36 * s} 44 C{100 - 46 * s} 44 {100 - 56 * s} 50 {100 - 64 * s} 46", "none", "#B8304A", 8)
        a.path(f"M{100 - 36 * s} 44 C{100 - 46 * s} 44 {100 - 56 * s} 50 {100 - 64 * s} 46", "none", "#FF7A9A", 4)
        for x, y in ((100 - 50 * s, 22), (100 - 66 * s, 46)):
            a.circ(x, y, 5, "#FFB0C8", "#B8304A", 2)
    # tail fin (mermaid-ish)
    a.path("M100 140 C94 160 72 170 60 182 C80 184 94 178 100 168 C106 178 120 184 140 182 C128 170 106 160 100 140 Z", a.lin("#7FE0D0", "#2AB0A0"), "#126A60", 3)
    # body
    a.path("M100 56 C128 56 142 78 140 104 C138 132 122 148 100 148 C78 148 62 132 60 104 C58 78 72 56 100 56 Z", body, o)
    for x, y in ((74, 124), (126, 126), (90, 138), (114, 138)):
        a.circ(x, y, 3.2, "#FFFFFF", extra=' opacity=".7"')
    # broom made of seaweed
    a.line("M140 150 L166 96", "#8A5A34", 4)
    a.path("M160 100 C156 84 168 74 176 80 C172 86 176 94 172 102 Z", "#3FAF5A", "#2E7D3E", 2)
    a.ell(144, 132, 8, 7, body, o, 3)
    a.gloss(80, 74, 10, 5)
    a.eyes(98, xs=(84, 116), rx=9, ry=11, iris="#7FE0D0", pupil=("#5A1A12", "#1F0804"), lashes=2)
    a.mouth(100, 116, "smile", w=6, color=o)
    a.cheeks([(72, 112), (128, 112)], "#FF5A7A", rx=8, ry=5)


@chordoo("gurgle")
def gurgle(a):
    skin = a.shade("#D8FFE0", "#6FD48A", "#2E9E5A")
    o = "#1A5A30"
    # lily pad
    a.path("M20 170 C20 150 60 140 100 140 C140 140 180 150 180 170 C180 186 140 192 100 192 C60 192 20 186 20 170 Z M100 166 L140 150", a.lin("#7FD06A", "#3FA04A"), "#2A6A2A", 3)
    # legs
    a.path("M50 164 C40 150 52 140 66 146 L74 162 Z", skin, o, 3)
    a.path("M150 164 C160 150 148 140 134 146 L126 162 Z", skin, o, 3)
    # body
    a.path("M54 140 C50 110 70 94 100 94 C130 94 150 110 146 140 C142 160 122 166 100 166 C78 166 58 160 54 140 Z", skin, o)
    a.ell(100, 142, 26, 18, "#F2FFE8")
    # head with eye bumps
    a.path("M46 96 C46 70 68 60 100 60 C132 60 154 70 154 96 C154 112 130 122 100 122 C70 122 46 112 46 96 Z", skin, o)
    a.circ(72, 64, 18, skin, o, 3.5)
    a.circ(128, 64, 18, skin, o, 3.5)
    a.ell(100, 76, 30, 10, skin)
    a.eye(72, 64, rx=11, ry=12, iris="#FFE14D", pupil=("#1A3A1A", "#061006"))
    a.eye(128, 64, rx=11, ry=12, iris="#FFE14D", pupil=("#1A3A1A", "#061006"))
    a.line("M62 100 Q100 122 138 100", o, 3)
    a.cheeks([(58, 102), (142, 102)], "#FF8FB0", rx=9, ry=6)
    # lily pad hat
    a.path("M72 50 C72 40 128 40 128 50 C128 56 72 56 72 50 Z", a.lin("#7FD06A", "#3FA04A"), "#2A6A2A", 2.5)
    a.path("M100 40 C94 30 104 22 112 28 C110 36 104 40 100 40 Z", "#FFB0E0", "#C2408A", 2)
    # music notes
    a.line("M162 50 V36 L172 33 V47", o, 2.2)
    a.ell(159, 51, 3.5, 2.6, o)
    a.ell(169, 48, 3.5, 2.6, o)


@chordoo("nautilux")
def nautilux(a):
    sh = a.lin("#FFF2E0", "#FFC8A0", "#E08A5A")
    o = "#6E3A1A"
    a.glow(100, 96, 92, "#7FF0FF", 0.4)
    # tentacles
    for i, x in enumerate((44, 56, 68, 80)):
        a.path(f"M{x + 10} 128 C{x} 146 {x + 10} 160 {x - 4} 176", "none", "#C2507A", 8)
        a.path(f"M{x + 10} 128 C{x} 146 {x + 10} 160 {x - 4} 176", "none", "#FF9AB8", 4)
    # shell spiral
    a.path("M100 30 C150 30 180 66 176 108 C172 150 136 172 100 168 C70 164 52 140 56 114 C60 92 80 80 100 84 C118 88 126 104 120 118 C114 130 100 130 94 122", sh, o)
    a.path("M100 30 C150 30 180 66 176 108 C172 150 136 172 100 168", "none", o, 3.5)
    for d in ("M120 34 C128 60 134 84 130 110", "M150 46 C150 76 150 100 140 130", "M170 80 C160 106 152 130 132 154"):
        a.line(d, "#C2804A", 3, 0.8)
    # lantern glow inside
    a.glow(146, 92, 26, "#FFF2A0", 0.9)
    a.circ(146, 92, 10, a.lin("#FFFFFF", "#FFF2A0"), "#E0A030", 2)
    # face on body opening
    a.path("M36 110 C36 92 52 80 72 82 C90 84 100 98 98 116 C96 134 82 142 66 142 C48 142 36 128 36 110 Z", a.shade("#FFE0EC", "#FF9AB8", "#D05A8A"), "#8A1E4A")
    a.eye(56, 106, rx=8, ry=10, iris="#7FF0FF", pupil=("#2A1A3E", "#0A0614"), kind="star")
    a.eye(82, 106, rx=8, ry=10, iris="#7FF0FF", pupil=("#2A1A3E", "#0A0614"), kind="star")
    a.mouth(69, 124, "smile", w=5, color="#8A1E4A")
    a.cheeks([(48, 122), (90, 122)], "#FF5A9A", rx=6, ry=4, dots=False)
    a.sparkle(30, 40, 6, "#7FF0FF")
    a.sparkle(186, 160, 5, "#FFFFFF")


@chordoo("leviathorn")
def leviathorn(a):
    scale = a.lin("#7FE0D0", "#2A9AB8", "#1E4E8A", x2=1, y2=1)
    o = "#0E2A4E"
    # waves
    for y, c in ((176, "#4AB2E8"), (188, "#2A82C0")):
        a.path(f"M0 {y} Q20 {y - 10} 40 {y} T80 {y} T120 {y} T160 {y} T200 {y} V200 H0 Z", c, None)
    # serpent coils out of water
    a.path("M20 180 C20 150 52 150 52 176", "none", o, 24)
    a.path("M20 180 C20 150 52 150 52 176", "none", "#2A9AB8", 17)
    a.path("M80 180 C80 140 120 140 120 176", "none", o, 26)
    a.path("M80 180 C80 140 120 140 120 176", "none", "#2A9AB8", 19)
    # neck + head
    a.path("M146 182 C144 140 150 100 140 76", "none", o, 30)
    a.path("M146 182 C144 140 150 100 140 76", "none", "#3AB0C8", 23)
    for y in (100, 118, 136, 154):
        a.line(f"M136 {y} Q146 {y + 4} 156 {y}", "#BFF5F0", 2, 0.8)
    # fin crest
    a.path("M160 60 C182 64 186 84 176 100 C172 92 168 88 162 88 C172 102 172 120 160 130 C158 112 152 104 150 98 Z", a.lin("#FFB0E0", "#C24AE0"), "#6A1E8A", 3)
    a.path("M120 58 C122 36 150 26 168 40 C180 50 176 72 160 80 C146 88 120 82 120 58 Z", scale, o)
    a.path("M120 64 C104 62 92 66 88 74 C96 82 112 82 126 76 Z", scale, o, 3)
    a.gloss(140, 40, 8, 4)
    a.eye(146, 56, rx=8, ry=10, iris="#FFE14D", pupil=("#0E2A4E", "#040C1E"))
    a.ell(92, 72, 2, 1.6, o)
    a.mouth(104, 76, "smile", w=6, color=o)
    a.cheeks([(132, 70)], "#FF8FD8", rx=6, ry=4)
    # splashes
    for x, y in ((60, 140), (110, 128), (170, 150), (34, 150)):
        a.path(f"M{x} {y} C{x + 4} {y + 6} {x + 4} {y + 10} {x} {y + 11} C{x - 4} {y + 10} {x - 4} {y + 6} {x} {y} Z", "#E6F8FF", "#4AB2E8", 1.5, ' class="fx"')


@chordoo("abyssa")
def abyssa(a):
    body = a.lin("#5A6AE0", "#2A2E8A", "#14104E", x2=0.4, y2=1)
    o = "#080628"
    a.glow(100, 100, 96, "#7F8CFF", 0.4)
    # moon
    a.circ(36, 36, 16, a.lin("#FFF8D6", "#FFE08A"), "#C8A040", 2.5)
    a.circ(30, 32, 3, "#E8C870", extra=' opacity=".7"')
    # tail flukes
    a.path("M160 96 C176 76 194 72 196 80 C188 88 186 96 192 104 C186 112 176 112 160 104 Z", body, o, 3)
    # whale body
    a.path("M16 112 C16 74 56 54 100 56 C140 58 166 80 166 104 C166 134 136 156 96 156 C52 156 16 144 16 112 Z", body, o)
    a.path("M24 124 C40 146 100 152 140 140 C120 158 50 158 24 124 Z", "#BFC8FF", None, extra=' opacity=".5"')
    for y in (132, 140, 146):
        a.line(f"M{40 + (y - 132)} {y} Q90 {y + 8} {130 - (y - 132)} {y}", "#8A96FF", 1.8, 0.6)
    # stars on body
    for x, y, r in ((70, 72, 3), (100, 66, 2.2), (124, 80, 2.8), (140, 70, 2), (86, 88, 2), (112, 96, 2.4), (60, 92, 1.8)):
        a.circ(x, y, r, "#FFF8D6")
    a.sparkle(96, 78, 5, "#FFFFFF")
    # fin
    a.path("M82 130 C70 150 74 166 88 168 C94 156 96 144 94 132 Z", body, o, 3)
    # spout of stars
    a.line("M56 58 C52 44 56 34 64 28 M56 58 C60 44 70 38 78 36", "#BFC8FF", 3)
    a.sparkle(64, 26, 6)
    a.sparkle(80, 34, 5, "#FFFFFF")
    a.eye(46, 104, rx=9, ry=10, iris="#7FD0FF", pupil=("#14104E", "#04020E"), kind="star")
    a.mouth(40, 124, "smile", w=10, color="#BFC8FF")
    a.cheeks([(32, 116)], "#FF8FD8", rx=7, ry=4, dots=False)
    a.sparkle(176, 40, 6)
    a.sparkle(150, 22, 4, "#FFFFFF")
    a.sparkle(186, 140, 4, "#FFFFFF")

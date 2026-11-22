"""Creature-style (v2) sample set. Built by build_v2.py into art/v2/."""
from artkit import chordoo
from creature import INK2, cel, flat, ink, feye, fang, claws, shadow

FLAME = ("#FFF3A0", "#FFB52E", "#FF5A1F")


def flame_fill(a):
    return a.lin(*FLAME, x1=0, y1=0, x2=0, y2=1)


# ---------------------------------------------------------------- fire line
@chordoo("emberpup")
def emberpup(a):
    org, orgS, orgL = "#FF8A2A", "#C8501A", "#FFC27A"
    crm, crmS = "#FFF0D6", "#E2C29A"
    shadow(a, 104, 186, 56)
    # tail curling up behind, flame tip
    cel(a, "M124 168 C162 170 184 140 178 108 C174 90 160 84 150 92 C162 106 160 132 138 146 Z", org, orgS, orgL)
    flat(a, "M150 96 C142 80 152 66 148 50 C160 58 164 66 166 76 C170 68 176 66 178 58 C186 74 184 92 176 100 C168 106 156 104 150 96 Z", flame_fill(a), "#9A2A08", 3)
    # body sitting
    cel(a, "M70 180 C62 150 66 120 92 108 C116 100 138 116 140 142 C142 162 136 176 128 182 Z", org, orgS, orgL)
    cel(a, "M84 116 C74 132 78 152 92 160 C100 148 108 138 106 118 Z", crm, crmS)
    # front legs
    for x in (82, 108):
        cel(a, f"M{x - 8} 148 L{x - 9} 180 C{x - 9} 186 {x + 9} 186 {x + 9} 180 L{x + 8} 150 Z", org, orgS, shift=(6, 0))
        claws(a, x, 182, 3, 4, 5)
    # ember spots
    for x, y in ((120, 128), (128, 144), (114, 160)):
        a.circ(x, y, 3, "#FFE07A")
    # ears
    cel(a, "M60 58 L44 12 L82 46 Z", org, orgS)
    flat(a, "M44 12 L50 30 L58 26 Z", "#3A1A14", INK2, 2)
    cel(a, "M104 44 L126 6 L130 58 Z", org, orgS)
    flat(a, "M126 6 L120 22 L128 26 Z", "#3A1A14", INK2, 2)
    # head
    cel(a, "M48 86 C46 60 66 44 90 44 C114 44 132 60 130 82 C128 100 114 112 92 112 C70 112 50 104 48 86 Z", org, orgS, orgL)
    # cheek fluff spikes and muzzle
    flat(a, "M126 80 L144 86 L130 92 L140 102 L120 102 Z", crm, INK2, 3)
    flat(a, "M50 84 C38 86 30 94 34 102 C42 110 62 108 74 100 C70 92 60 86 50 84 Z", crm, INK2, 3)
    a.ell(34, 94, 5, 4, "#2A1414")
    ink(a, "M44 106 Q56 104 68 98", 3)
    fang(a, 60, 103, 6)
    # eyes + brows
    feye(a, 74, 76, 10, 9, "#FFC21A", 1, (-2, 1), "round", 10)
    feye(a, 106, 74, 9, 8, "#FFC21A", -1, (-3, 1), "round", 10)
    ink(a, "M62 62 L84 66", 3.5)
    ink(a, "M98 64 L116 60", 3.5)


@chordoo("blazehound")
def blazehound(a):
    org, orgS, orgL = "#F46A22", "#B23A12", "#FFB06A"
    dark = "#3A1C1A"
    shadow(a, 104, 186, 76)
    # flame tail
    flat(a, "M150 112 C172 100 188 78 182 50 C176 66 170 74 162 78 C172 64 170 48 160 40 C160 66 150 86 138 100 Z", flame_fill(a), "#9A2A08", 3)
    # far legs (darker)
    for d in ("M80 136 L84 178 H96 L94 138", "M142 136 C150 148 150 160 144 168 L150 180 H138 L134 166 C138 158 136 148 130 140"):
        cel(a, d + " Z", orgS, "#8A2A0C")
    # body
    cel(a, "M56 112 C72 94 128 94 152 106 C168 114 170 136 156 146 C130 152 86 152 64 146 C52 140 48 122 56 112 Z", org, orgS, orgL)
    flat(a, "M70 142 C90 148 130 148 150 142 L148 148 C126 154 90 154 70 148 Z", "#FFD9B0", None, 0)
    # near legs
    for d in ("M62 132 L56 178 H74 L78 138", "M124 134 C140 142 144 158 136 166 L142 182 H126 L120 168 C124 160 120 148 112 140"):
        cel(a, d + " Z", org, orgS)
    a.ell(64, 179, 12, 6, org, INK2, 3.5)
    a.ell(134, 182, 12, 6, org, INK2, 3.5)
    claws(a, 64, 183, 3, 4, 5)
    claws(a, 134, 186, 3, 4, 5)
    # dark stripes
    for x in (100, 116, 132):
        flat(a, f"M{x} 100 L{x - 6} 116 L{x + 2} 114 Z", dark, None, 0)
    # flame mane
    flat(a, "M60 64 C66 46 84 42 92 26 C96 42 92 52 100 56 C106 44 118 42 122 34 C124 54 114 66 120 78 C110 92 94 100 78 106 C82 92 76 80 60 64 Z", flame_fill(a), "#9A2A08", 3)
    # head in profile facing left
    cel(a, "M20 88 C18 72 32 60 52 58 C70 56 84 64 88 78 C90 96 78 106 60 106 C48 106 38 102 22 100 C18 96 18 92 20 88 Z", org, orgS, orgL)
    cel(a, "M64 64 L84 30 L86 72 Z", org, orgS)
    flat(a, "M84 30 L78 44 L86 48 Z", dark, INK2, 2)
    a.ell(22, 88, 5, 4, "#2A1414")
    flat(a, "M24 98 C36 104 50 104 62 98 C56 108 34 110 24 98 Z", "#FFF0D6", INK2, 2.5)
    ink(a, "M24 97 Q44 104 62 96", 3)
    fang(a, 34, 99, 5)
    fang(a, 52, 99, 5)
    feye(a, 52, 78, 9, 7, "#FFE04A", -1, (-3, 0), "slit", 14)
    ink(a, "M40 68 L62 70", 4)
    # ember sparks
    for x, y in ((150, 26), (176, 92), (110, 20)):
        a.circ(x, y, 3, "#FFB52E", extra=' class="fx"')


@chordoo("infernox")
def infernox(a):
    red, redS, redL = "#D8401E", "#8E1E10", "#FF8A4A"
    rock, rockS = "#4A3A40", "#2A2028"
    a.glow(100, 70, 90, "#FF7A2A", 0.5)
    shadow(a, 100, 188, 80)
    # flame burst behind the head
    flat(a, "M100 6 C112 22 108 34 122 40 C132 26 146 24 158 12 C156 34 146 46 150 60 C164 56 176 60 188 54 C178 74 160 82 150 90 "
         "L50 90 C40 82 22 74 12 54 C24 60 36 56 50 60 C54 46 44 34 42 12 C54 24 68 26 78 40 C92 34 88 22 100 6 Z", flame_fill(a), "#9A2A08", 3)
    # body
    cel(a, "M38 186 C28 152 40 112 70 100 C90 92 110 92 130 100 C160 112 172 152 162 186 Z", red, redS, redL)
    # lava cracks on chest
    flat(a, "M74 186 C70 160 78 132 100 126 C122 132 130 160 126 186 Z", "#F08A4A", None, 0, ' opacity=".55"')
    ink(a, "M100 116 L94 132 L104 146 L98 164 M94 132 L80 140 M104 146 L120 150", 5, "#FFD23A")
    ink(a, "M100 116 L94 132 L104 146 L98 164 M94 132 L80 140 M104 146 L120 150", 2, "#FFF6C0")
    # shoulder armor
    cel(a, "M30 124 C32 98 58 86 80 94 C78 114 62 130 38 136 Z", rock, rockS)
    cel(a, "M170 124 C168 98 142 86 120 94 C122 114 138 130 162 136 Z", rock, rockS)
    for x, y in ((44, 108), (156, 108)):
        flat(a, f"M{x - 6} {y + 6} L{x} {y - 14} L{x + 6} {y + 6} Z", "#6A5A62", INK2, 2.5)
    # forelegs
    cel(a, "M48 146 L42 186 H76 L74 150 Z", red, redS)
    cel(a, "M152 146 L158 186 H124 L126 150 Z", red, redS)
    a.ell(58, 184, 22, 9, red, INK2, 4)
    a.ell(142, 184, 22, 9, red, INK2, 4)
    claws(a, 58, 188, 3, 6, 9)
    claws(a, 142, 188, 3, 6, 9)
    # horns
    cel(a, "M72 56 C56 46 46 30 50 10 C62 24 72 30 86 40 Z", "#F2E6D0", "#B8A68A")
    cel(a, "M128 56 C144 46 154 30 150 10 C138 24 128 30 114 40 Z", "#F2E6D0", "#B8A68A")
    # head
    cel(a, "M64 80 C62 56 78 40 100 40 C122 40 138 56 136 80 C134 100 120 114 100 114 C80 114 66 100 64 80 Z", red, redS, redL)
    flat(a, "M66 62 C80 54 92 60 100 66 C108 60 120 54 134 62 L132 70 C120 64 110 68 100 74 C90 68 80 64 68 70 Z", rock, INK2, 3)
    feye(a, 85, 78, 9, 7, "#FFE04A", 1, (1, 0), "slit", 18, glow=True)
    feye(a, 115, 78, 9, 7, "#FFE04A", -1, (-1, 0), "slit", 18, glow=True)
    flat(a, "M82 98 Q100 108 118 98 Q100 116 82 98 Z", "#3A0A0A", INK2, 3)
    fang(a, 88, 100, 6)
    fang(a, 112, 100, 6)
    a.ell(94, 92, 2.5, 2, INK2)
    a.ell(106, 92, 2.5, 2, INK2)


# ---------------------------------------------------------------- water
@chordoo("riptide")
def riptide(a):
    blu, bluS, bluL = "#2E7FD8", "#1A4A94", "#7CC4FF"
    wht, whtS = "#EAF6FF", "#B4CCE0"
    shadow(a, 104, 186, 62)
    # tail
    cel(a, "M118 158 C150 166 178 158 192 136 C186 132 176 140 168 140 C182 126 180 116 176 110 C164 132 148 142 128 142 Z", blu, bluS, bluL)
    # far leg
    cel(a, "M110 146 C124 158 124 170 116 182 H132 C138 168 136 152 124 142 Z", bluS, "#10305E")
    # body
    cel(a, "M68 150 C60 120 70 92 100 88 C130 92 140 120 130 150 C122 164 78 164 68 150 Z", blu, bluS, bluL)
    cel(a, "M82 108 C78 128 82 150 98 156 C112 150 118 128 112 108 Z", wht, whtS)
    for y in (122, 134, 146):
        ink(a, f"M86 {y} Q98 {y + 3} 110 {y}", 2, "#9AB4CC")
    # near leg (digitigrade)
    cel(a, "M78 144 C68 160 74 170 66 182 H86 C90 168 96 158 94 146 Z", blu, bluS)
    claws(a, 76, 183, 3, 5, 6)
    claws(a, 124, 183, 3, 5, 6)
    # arm with fin blade, raised
    flat(a, "M56 98 L28 80 L42 110 Z", "#5AB4FF", INK2, 3)
    cel(a, "M76 104 C64 100 54 104 50 114 L60 120 C64 114 70 112 78 114 Z", blu, bluS)
    claws(a, 52, 118, 3, 4, 4, down=True)
    # back fins
    flat(a, "M126 96 L150 82 L138 110 Z", "#5AB4FF", INK2, 3)
    flat(a, "M134 118 L160 112 L142 132 Z", "#5AB4FF", INK2, 3)
    # head (shark-like)
    cel(a, "M68 68 C68 44 92 32 114 36 C138 40 152 56 150 70 C142 86 122 92 100 92 C82 92 70 84 68 68 Z", blu, bluS, bluL)
    flat(a, "M96 38 L104 6 L126 42 Z", "#5AB4FF", INK2, 3)
    flat(a, "M98 80 C114 90 136 86 150 70 C140 92 112 98 98 80 Z", wht, INK2, 2.5)
    for x in (108, 118, 128, 138):
        fang(a, x, 82 - (x - 108) * 0.25, 5)
    ink(a, "M98 80 C114 88 134 84 150 70", 3)
    for x in (72, 78):
        ink(a, f"M{x} 78 l-2 10", 2.2, "#10305E")
    feye(a, 92, 60, 9, 7, "#FFE04A", 1, (2, 0), "slit", 14)
    feye(a, 120, 56, 8, 6, "#FFE04A", -1, (2, 0), "slit", 14)
    for x, y in ((24, 140), (180, 40), (40, 40)):
        a.circ(x, y, 5, "none", "#7CC4FF", 2.5, extra=' class="fx"')


# ---------------------------------------------------------------- plant
@chordoo("thornback")
def thornback(a):
    grn, grnS, grnL = "#5AA83E", "#2E6A24", "#A8E07A"
    leaf, leafS = "#3E8A3A", "#1E5020"
    shadow(a, 100, 186, 84)
    # leaf plates on the back
    for x, y, h, r in ((64, 104, 34, -24), (88, 96, 44, -10), (114, 96, 46, 6), (138, 104, 38, 22), (158, 118, 28, 40)):
        a.add(f'<g transform="rotate({r} {x} {y + 8})">')
        cel(a, f"M{x} {y + 10} C{x - 14} {y - 6} {x - 8} {y - h * 0.8} {x} {y - h} C{x + 8} {y - h * 0.8} {x + 14} {y - 6} {x} {y + 10} Z", leaf, leafS, "#7CC850", w=3, shift=(5, 0))
        ink(a, f"M{x} {y + 6} L{x} {y - h * 0.8}", 1.8, "#BCE89A")
        a.add('</g>')
    # tail with thorn club
    cel(a, "M156 132 C176 132 188 124 194 112 C190 128 180 142 158 146 Z", grn, grnS)
    for x, y, r in ((188, 110, -30), (196, 120, 20), (184, 126, 80)):
        flat(a, f"M{x - 4} {y + 2} L{x} {y - 10} L{x + 4} {y + 2} Z", "#E8D8B0", INK2, 2, f' transform="rotate({r} {x} {y})"')
    # far legs
    cel(a, "M64 140 L62 176 H78 L80 142 Z", grnS, "#1E4A1A")
    cel(a, "M134 142 L136 176 H152 L150 140 Z", grnS, "#1E4A1A")
    # body
    cel(a, "M36 138 C36 112 78 98 118 100 C150 102 168 120 164 142 C150 156 66 158 36 138 Z", grn, grnS, grnL)
    flat(a, "M48 146 C80 156 140 156 160 146 L156 152 C130 162 78 162 50 152 Z", "#D8E8A8", None, 0)
    # thorny vine around body
    ink(a, "M44 124 C70 140 100 112 130 128 C146 136 156 128 162 122", 4, "#6A4A22")
    for x, y in ((62, 132), (96, 120), (126, 126), (150, 132)):
        flat(a, f"M{x} {y} L{x + 3} {y - 9} L{x + 6} {y} Z", "#E8D8B0", INK2, 1.8)
    # near legs
    for x in (52, 116):
        cel(a, f"M{x - 10} 140 L{x - 12} 180 H{x + 12} L{x + 10} 142 Z", grn, grnS)
        claws(a, x, 181, 3, 5, 7)
    # head
    cel(a, "M6 128 C6 110 22 100 40 102 C58 104 64 118 60 132 C56 146 32 150 18 146 C10 142 6 136 6 128 Z", grn, grnS, grnL)
    flat(a, "M20 102 L16 84 L30 100 Z", "#E8D8B0", INK2, 2.5)
    flat(a, "M34 100 L36 80 L44 102 Z", "#E8D8B0", INK2, 2.5)
    flat(a, "M8 132 C18 138 32 140 46 136 C40 146 20 148 8 132 Z", "#D8E8A8", INK2, 2.5)
    ink(a, "M8 132 Q28 140 46 134", 3)
    fang(a, 22, 136, 4)
    feye(a, 34, 120, 9, 7, "#FF6A3A", -1, (-2, 0), "slit", 16)
    ink(a, "M22 108 L46 112", 4)
    # flower bud blooming on the back
    for k in range(5):
        a.add(f'<ellipse cx="100" cy="60" rx="5" ry="9" fill="#FF6A8A" stroke="{INK2}" stroke-width="2" transform="rotate({k * 72} 100 68)"/>')
    a.circ(100, 68, 4, "#FFD84D", INK2, 1.5)


# ---------------------------------------------------------------- electric
@chordoo("arcferret")
def arcferret(a):
    yel, yelS, yelL = "#FFCF2E", "#D0861A", "#FFF0A0"
    dark = "#2E2A44"
    shadow(a, 100, 186, 76)
    # bolt-segment tail
    flat(a, "M150 124 L164 96 L154 92 L172 58 L162 54 L184 18 L178 54 L190 56 L174 90 L184 94 L164 128 Z", yel, INK2, 3.5)
    flat(a, "M164 96 L154 92 L172 58 L162 54 L176 32", "none", dark, 3)
    # arched body (bridge pose)
    cel(a, "M40 150 C40 118 70 94 104 96 C138 98 162 118 162 150 C154 160 140 160 134 150 C128 132 116 124 100 124 C84 124 72 132 66 150 C58 160 46 160 40 150 Z", yel, yelS, yelL)
    # dark saddle stripe with zigzag edge
    flat(a, "M64 106 C84 96 120 96 144 108 L136 116 L128 110 L118 118 L108 110 L98 118 L88 110 L78 118 L70 112 Z", dark, INK2, 2.5)
    # legs
    for x in (48, 66, 136, 154):
        cel(a, f"M{x - 7} 148 L{x - 8} 178 H{x + 8} L{x + 7} 148 Z", yel, yelS, shift=(5, 0))
        a.ell(x, 179, 10, 5, yel, INK2, 3)
        claws(a, x, 182, 3, 4, 5)
    # head turned to viewer
    cel(a, "M14 106 C12 86 28 74 46 74 C64 74 78 86 76 106 C74 122 60 132 44 132 C26 132 14 122 14 106 Z", yel, yelS, yelL)
    # ears
    for x, s in ((22, 1), (68, -1)):
        cel(a, f"M{x} 86 L{x - s * 4} 56 L{x + s * 16} 76 Z", yel, yelS)
    # lightning mask marking
    flat(a, "M18 94 L34 98 L28 104 L44 104 L60 104 L54 98 L72 94 L64 108 L46 112 L26 108 Z", dark, INK2, 2)
    feye(a, 32, 100, 8, 7, "#5AE8FF", 1, (1, 0), "slit", 12)
    feye(a, 58, 100, 8, 7, "#5AE8FF", -1, (-1, 0), "slit", 12)
    flat(a, "M38 118 C42 126 50 126 54 118 Z", "#3A1A2A", INK2, 2.5)
    fang(a, 42, 118, 4)
    a.ell(46, 113, 3, 2, INK2)
    # sparks
    for x, y, r in ((90, 70, 0), (110, 64, 30), (20, 50, -20)):
        a.add(f'<path class="fx" d="M{x} {y} l6 -10 l-2 8 l8 -2 l-8 12 l2 -8 z" fill="#5AE8FF" stroke="{INK2}" stroke-width="1.5" transform="rotate({r} {x} {y})"/>')


# ---------------------------------------------------------------- sky
@chordoo("galecrest")
def galecrest(a):
    sl, slS, slL = "#5A7AB8", "#33497A", "#9AB8F0"
    shadow(a, 100, 188, 50)
    # wings raised
    cel(a, "M88 100 C62 62 30 48 6 52 C22 62 18 70 30 76 C14 84 22 94 38 94 C26 102 38 112 54 110 C62 118 76 116 88 112 Z", sl, slS, slL)
    cel(a, "M116 98 C134 58 164 34 194 34 C180 46 186 54 174 62 C190 66 184 80 168 82 C180 92 168 102 152 100 C146 110 130 110 118 110 Z", sl, slS, slL)
    for d in ("M30 76 L70 100", "M38 94 L76 106", "M174 62 L130 96", "M168 82 L128 104"):
        ink(a, d, 2, "#22305A")
    # tail feathers
    flat(a, "M88 158 L76 186 L96 176 L100 190 L106 176 L124 186 L112 158 Z", slS, INK2, 3)
    # body
    cel(a, "M72 152 C62 124 72 94 100 90 C128 94 138 124 128 152 C120 168 80 168 72 152 Z", sl, slS, slL)
    cel(a, "M84 110 C80 128 84 150 100 158 C114 150 118 128 114 110 Z", "#F2F4FA", "#C0C6D8")
    for y in (122, 134, 146):
        ink(a, f"M88 {y} l6 3 l6 -3 l6 3 l6 -3", 2, "#5A6A8A")
    # talons
    for x in (90, 110):
        ink(a, f"M{x} 160 L{x} 178", 7, INK2)
        ink(a, f"M{x} 160 L{x} 178", 4, "#FFC83A")
        claws(a, x, 179, 3, 5, 6, color="#2A2030")
    # head
    cel(a, "M78 76 C76 52 94 40 112 42 C128 44 136 60 132 76 C128 92 114 98 100 98 C88 98 80 90 78 76 Z", sl, slS, slL)
    # storm crest
    flat(a, "M118 46 L150 18 L140 40 L170 30 L146 56 L160 56 L130 70 Z", "#E8EEFF", INK2, 3)
    flat(a, "M150 18 L140 40 L170 30", "none", "#FFD23A", 2.5)
    # hooked beak
    flat(a, "M82 68 C66 66 56 76 58 92 C64 84 72 82 82 86 Z", "#FFC83A", INK2, 3)
    flat(a, "M58 92 C58 86 60 82 64 80 L66 88 Z", "#3A2A20", INK2, 1.5)
    # dark eye stripe
    flat(a, "M86 70 C96 64 112 64 122 72 L118 80 C108 76 96 76 88 80 Z", "#22305A", None, 0)
    feye(a, 100, 70, 9, 7, "#FFB020", -1, (-3, 0), "round", 18)
    ink(a, "M86 58 L112 62", 4.5)
    for d in ("M14 140 Q30 132 44 140", "M156 150 Q170 142 186 150"):
        a.add(f'<path class="fx" d="{d}" stroke="#9AB8F0" stroke-width="3" fill="none" stroke-linecap="round"/>')


# ---------------------------------------------------------------- rock / crystal
@chordoo("gravion")
def gravion(a):
    st, stS, stL = "#9A8E86", "#5E544E", "#D0C6BC"
    cy, cyS = "#7AE0F0", "#2E98B8"
    shadow(a, 100, 188, 86)
    # crystal cluster on the back
    for x, w, h, r in ((96, 16, 42, -14), (114, 20, 58, -2), (132, 16, 44, 12), (148, 12, 30, 26)):
        a.add(f'<g transform="rotate({r} {x} 92)">')
        cel(a, f"M{x - w / 2} 92 L{x - w / 2} {92 - h * 0.7} L{x} {92 - h} L{x + w / 2} {92 - h * 0.7} L{x + w / 2} 92 Z", "#B98AF0", "#6A3AB8", "#E8D8FF", w=3, shift=(w / 2, 0))
        a.add('</g>')
    # far legs
    cel(a, "M70 140 L68 180 H86 L86 142 Z", stS, "#3A322E")
    cel(a, "M148 140 L150 180 H168 L166 140 Z", stS, "#3A322E")
    # armored body with bands
    cel(a, "M34 150 C28 110 60 84 106 84 C150 84 178 110 172 150 C160 168 48 168 34 150 Z", st, stS, stL)
    for x in (70, 96, 122, 148):
        ink(a, f"M{x} 88 C{x - 6} 110 {x - 6} 140 {x} 162", 3)
    # near legs
    for x in (54, 128):
        cel(a, f"M{x - 13} 146 L{x - 14} 184 H{x + 14} L{x + 13} 148 Z", st, stS)
        claws(a, x, 185, 3, 6, 8)
    # head
    cel(a, "M6 132 C6 106 26 94 48 96 C70 98 80 116 76 134 C72 152 48 160 30 156 C14 152 6 144 6 132 Z", st, stS, stL)
    flat(a, "M24 98 C36 90 56 92 66 102 L58 108 C48 102 36 102 28 106 Z", stS, INK2, 2.5)
    # crystal horns
    cel(a, "M10 116 L4 70 L22 60 L28 108 Z", cy, cyS, "#E0FAFF", w=3, shift=(8, 0))
    cel(a, "M30 104 L32 80 L42 76 L42 102 Z", cy, cyS, w=3, shift=(5, 0))
    feye(a, 46, 120, 8, 6, "#FF5A3A", -1, (-2, 0), "slit", 18)
    ink(a, "M10 140 Q26 146 44 140", 3)
    for x, y in ((26, 32), (180, 60)):
        a.add(f'<path class="fx" d="M{x} {y - 7} L{x + 4} {y} L{x} {y + 7} L{x - 4} {y} Z" fill="{cy}" stroke="{INK2}" stroke-width="1.5"/>')


# ---------------------------------------------------------------- shadow / spooky
@chordoo("shadewisp")
def shadewisp(a):
    pu, puS, puL = "#4A3A78", "#2A1E4E", "#7A6AB0"
    glow = "#6AFFE0"
    a.glow(100, 110, 90, "#7A5AE8", 0.35)
    shadow(a, 100, 188, 50)
    # three wisp tails
    for d, c in (("M86 160 C50 160 20 140 22 108 C24 90 36 80 46 86 C36 100 44 120 62 126 C50 112 54 94 66 88 C64 110 74 130 92 140 Z", "#5A3AA8"),
                 ("M114 160 C150 160 180 140 178 108 C176 90 164 80 154 86 C164 100 156 120 138 126 C150 112 146 94 134 88 C136 110 126 130 108 140 Z", "#5A3AA8"),
                 ("M100 150 C88 120 96 92 112 76 C110 96 120 104 126 92 C132 112 120 136 110 152 Z", "#3E2A88")):
        flat(a, d, c, INK2, 3)
    for d in ("M40 110 C40 124 52 132 62 126", "M160 110 C160 124 148 132 138 126"):
        ink(a, d, 3, glow, 0.9)
    # body sitting
    cel(a, "M64 184 C56 152 66 120 100 116 C134 120 144 152 136 184 Z", pu, puS, puL)
    cel(a, "M86 128 C80 144 84 164 100 172 C116 164 120 144 114 128 Z", "#6A5AA0", "#3E2E70")
    for x in (82, 118):
        cel(a, f"M{x - 8} 156 L{x - 9} 184 H{x + 9} L{x + 8} 158 Z", pu, puS, shift=(5, 0))
        claws(a, x, 185, 3, 4, 5, color="#C8C0E8")
    # ears
    cel(a, "M64 72 L52 18 L92 58 Z", pu, puS)
    cel(a, "M136 72 L148 18 L108 58 Z", pu, puS)
    flat(a, "M60 58 L56 32 L78 54 Z", "#1A1030", None, 0)
    flat(a, "M140 58 L144 32 L122 54 Z", "#1A1030", None, 0)
    # head with pointed muzzle
    cel(a, "M58 86 C56 64 76 50 100 50 C124 50 144 64 142 86 C140 104 122 118 100 130 C78 118 60 104 58 86 Z", pu, puS, puL)
    # glowing markings
    for d in ("M100 56 L100 74", "M62 96 L78 100", "M138 96 L122 100", "M92 60 L96 70 M108 60 L104 70"):
        ink(a, d, 3, glow)
    feye(a, 84, 86, 9, 7, glow, 1, (1, 0), "slit", 16, glow=True)
    feye(a, 116, 86, 9, 7, glow, -1, (-1, 0), "slit", 16, glow=True)
    a.ell(100, 116, 4, 3, INK2)
    ink(a, "M90 120 Q100 126 110 120", 2.5)
    fang(a, 94, 122, 4)
    fang(a, 106, 122, 4)
    for x, y in ((30, 50), (170, 44), (176, 160)):
        a.circ(x, y, 5, glow, extra=' class="fx" opacity=".8"')
        a.glow(x, y, 12, glow, 0.6)

"""Create clean, original visual aids for the 2017 MDCAT diagram questions.

These are purpose-built study diagrams, not crops of the source paper.  Keeping
the redraws in code makes them reproducible and avoids publishing source-scan
watermarks or unrelated page content.
"""

import os
import re
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django  # noqa: E402

django.setup()

from content.models import Question, QuestionImage  # noqa: E402


OUTPUT_DIR = Path("media/question_images")
SIZE = (1800, 1200)
INK = "#172033"
BLUE = "#1867b8"
GREEN = "#16866a"
RED = "#c44545"

FONT = "C:/Windows/Fonts/arial.ttf"
BOLD = "C:/Windows/Fonts/arialbd.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def clean_stem(text):
    text = re.sub(r"\s*\[Diagram/graph required[^]]*\]", "", text)
    text = re.sub(r"\s*\([^)]*(?:shown|figure|diagram|graph)[^)]*\)", "", text, flags=re.I)
    return " ".join(text.split())


def multiline(draw, text, box, fnt, fill=INK, spacing=8):
    x, y, width = box
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=fnt) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def arrow(draw, a, b, fill=INK, width=5):
    draw.line((a, b), fill=fill, width=width)
    x1, y1 = b
    x0, y0 = a
    dx, dy = x1 - x0, y1 - y0
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux, uy = dx / length, dy / length
    left = (x1 - 18 * ux + 10 * uy, y1 - 18 * uy - 10 * ux)
    right = (x1 - 18 * ux - 10 * uy, y1 - 18 * uy + 10 * ux)
    draw.polygon([b, left, right], fill=fill)


def axes(draw, origin, xlen=500, ylen=330, xlabel="x", ylabel="y"):
    x, y = origin
    arrow(draw, (x, y), (x + xlen, y), INK, 4)
    arrow(draw, (x, y), (x, y - ylen), INK, 4)
    draw.text((x + xlen + 12, y - 18), xlabel, font=font(28), fill=INK)
    draw.text((x - 26, y - ylen - 42), ylabel, font=font(28), fill=INK)


def draw_ecg(draw):
    x, y = 180, 610
    draw.line((x, y, x + 1320, y), fill="#96a1b4", width=3)
    points = [(x, y), (x+130,y), (x+175,y-42), (x+220,y), (x+350,y), (x+388,y+35), (x+420,y-235), (x+455,y+110), (x+510,y), (x+700,y), (x+790,y-68), (x+885,y), (x+1320,y)]
    draw.line(points, fill=BLUE, width=8, joint="curve")
    draw.text((x+395, y-300), "QRS complex", font=font(34, True), fill=BLUE)
    draw.text((x+1020, y+40), "time", font=font(28), fill=INK)


def draw_stomach(draw):
    draw.rounded_rectangle((660, 360, 1050, 790), radius=170, outline=BLUE, width=12)
    draw.line((830, 180, 830, 370), fill=BLUE, width=28)
    draw.arc((880, 680, 1240, 900), 180, 330, fill=BLUE, width=16)
    draw.text((810, 140), "oesophagus", font=font(28), fill=INK)
    draw.text((1140, 760), "duodenum", font=font(28), fill=INK)
    draw.ellipse((1035, 690, 1065, 720), fill=RED)
    arrow(draw, (1240, 600), (1060, 705), RED, 4)
    draw.text((1260, 570), "a", font=font(42, True), fill=RED)


def draw_gastric_gland(draw):
    # Cross-section of a gastric pit/gland: oxyntic (parietal) cells are the
    # large, rounded cells along the secretory portion of the gland.
    draw.line((700, 300, 1100, 300), fill=BLUE, width=12)
    draw.text((700, 250), "stomach mucosa", font=font(30), fill=INK)
    draw.arc((720, 280, 1080, 820), 0, 180, fill=BLUE, width=12)
    draw.arc((720, 410, 1080, 920), 0, 180, fill=BLUE, width=12)
    draw.line((720, 550, 720, 780), fill=BLUE, width=12)
    draw.line((1080, 550, 1080, 780), fill=BLUE, width=12)
    for x, y in [(765, 500), (820, 605), (900, 650), (980, 605), (1035, 500)]:
        draw.ellipse((x - 42, y - 56, x + 42, y + 56), fill="#f8d7bd", outline=GREEN, width=6)
        draw.ellipse((x - 10, y - 15, x + 10, y + 15), fill="#b16b5d")
    draw.text((770, 810), "gastric gland", font=font(32, True), fill=INK)
    arrow(draw, (1320, 440), (1035, 500), RED, 4)
    draw.text((1340, 405), "x", font=font(44, True), fill=RED)


def draw_lungs(draw):
    draw.line((900, 260, 900, 480), fill=BLUE, width=28)
    draw.line((900, 430, 700, 540), fill=BLUE, width=18)
    draw.line((900, 430, 1100, 540), fill=BLUE, width=18)
    draw.ellipse((470, 470, 870, 880), outline=BLUE, width=12)
    draw.ellipse((930, 470, 1330, 880), outline=BLUE, width=12)
    draw.arc((520, 730, 1280, 1030), 190, 350, fill=GREEN, width=16)
    arrow(draw, (1380, 870), (1120, 900), RED, 4)
    draw.text((1400, 830), "Y", font=font(44, True), fill=RED)


def draw_work_graph(draw):
    axes(draw, (350, 900), 900, 520, "distance", "force")
    points = [(430,800), (690,520), (1050,520), (1190,800), (430,800)]
    draw.line(points, fill=BLUE, width=8, joint="curve")
    draw.text((670, 630), "enclosed area", font=font(32), fill=GREEN)


def draw_double_slit(draw):
    draw.line((420, 300, 420, 900), fill=INK, width=12)
    draw.line((405, 510, 435, 510), fill="white", width=28)
    draw.line((405, 690, 435, 690), fill="white", width=28)
    draw.text((350, 470), "A", font=font(34, True), fill=INK)
    draw.text((350, 700), "B", font=font(34, True), fill=INK)
    draw.line((1370, 250, 1370, 950), fill=INK, width=8)
    for y in range(350, 900, 110):
        draw.ellipse((1338, y, 1402, y+48), fill="#b8d9f3")
    draw.line((435,510,1370,590), fill=BLUE, width=3)
    draw.line((435,690,1370,590), fill=BLUE, width=3)
    draw.ellipse((1350, 570, 1390, 610), fill=RED)
    draw.text((1420, 565), "P", font=font(34, True), fill=RED)


def draw_inverse_square(draw):
    axes(draw, (350, 900), 950, 540, "distance x", "force F")
    pts = [(400,390),(470,460),(550,560),(670,665),(820,750),(1020,810),(1250,845)]
    draw.line(pts, fill=BLUE, width=8, joint="curve")
    draw.text((780, 420), "F is proportional to 1 / x^2", font=font(38, True), fill=GREEN)


def resistor(draw):
    return


def draw_resistor_network(draw):
    a, b = (360, 640), (1420, 640)
    draw.text((300, 615), "A", font=font(38, True), fill=INK)
    draw.text((1450, 615), "B", font=font(38, True), fill=INK)
    nodes=[(520,460),(900,360),(1260,460),(520,820),(900,920),(1260,820)]
    for start,end in zip(nodes, nodes[1:3]): draw.line((start,end),fill=BLUE,width=7)
    for start,end in zip(nodes[3:], nodes[4:]): draw.line((start,end),fill=BLUE,width=7)
    draw.line((a,nodes[0]),fill=BLUE,width=7); draw.line((a,nodes[3]),fill=BLUE,width=7)
    draw.line((nodes[2],b),fill=BLUE,width=7); draw.line((nodes[5],b),fill=BLUE,width=7)
    draw.line((nodes[1],nodes[4]),fill=BLUE,width=7)
    for x,y in nodes:
        draw.rectangle((x-25,y-12,x+25,y+12), fill="white", outline=INK, width=4)
        draw.text((x-35,y-65), "10 ohm", font=font(22), fill=INK)


def draw_field(draw):
    draw.ellipse((520, 330, 1280, 940), outline=BLUE, width=12)
    draw.line((900, 250, 900, 1020), fill=INK, width=20)
    arrow(draw, (900,880), (900,400), RED, 7)
    for r in (180, 300, 420):
        draw.arc((900-r, 635-r, 900+r, 635+r), 30, 330, fill=GREEN, width=7)
    draw.text((960, 390), "current", font=font(30), fill=RED)
    draw.text((680, 1000), "magnetic field lines", font=font(30), fill=GREEN)


def draw_rectifier(draw):
    pts=[(500,620),(900,350),(1300,620),(900,900),(500,620)]
    draw.line(pts, fill=BLUE, width=8)
    for x,y,label in [(690,480,"D1"),(1110,480,"D2"),(1110,760,"D3"),(690,760,"D4")]:
        draw.polygon([(x-24,y-20),(x-24,y+20),(x+22,y)], outline=INK, fill="white")
        draw.line((x+24,y-27,x+24,y+27),fill=INK,width=5)
        draw.text((x-28,y+45),label,font=font(25),fill=INK)
    draw.text((350, 600), "AC", font=font(34, True), fill=RED)
    draw.text((850, 250), "+", font=font(40, True), fill=RED)
    draw.text((850, 940), "−", font=font(40, True), fill=RED)


def draw_ke_graph(draw):
    for ox, oy, flat in [(300,500,True),(1000,500,False)]:
        axes(draw,(ox,oy+280),330,230,"intensity I","K.E. E")
        if flat: draw.line((ox+40,oy+110,ox+300,oy+110),fill=BLUE,width=7)
        else: draw.line((ox+40,oy+250,ox+290,oy+60),fill=BLUE,width=7)
    draw.text((390, 800), "A", font=font(32,True),fill=INK); draw.text((1090,800), "B",font=font(32,True),fill=INK)


def draw_energy(draw):
    axes(draw,(300,900),1200,520,"reaction progress","energy")
    draw.arc((480,370,1040,1030),180,360,fill=RED,width=8)
    draw.arc((520,560,1000,1030),180,360,fill=GREEN,width=8)
    draw.text((700,330),"uncatalysed",font=font(30),fill=RED)
    draw.text((710,620),"catalysed",font=font(30),fill=GREEN)


def draw_cytosine(draw):
    """A clear structural formula for cytosine (2-oxo-4-aminopyrimidine)."""
    pts = [(780, 410), (1010, 410), (1130, 610), (1010, 810), (780, 810), (660, 610)]
    draw.line(pts + [pts[0]], fill=BLUE, width=8, joint="curve")
    # Double bonds in the pyrimidine ring.
    draw.line((800, 435, 980, 435), fill=INK, width=3)
    draw.line((1094, 625, 990, 790), fill=INK, width=3)
    draw.text((735, 375), "N", font=font(42, True), fill=INK)
    draw.text((1070, 570), "N", font=font(42, True), fill=INK)
    draw.line((660, 610, 510, 610), fill=INK, width=6)
    draw.line((660, 630, 510, 630), fill=INK, width=3)
    draw.text((410, 580), "O", font=font(44, True), fill=RED)
    draw.line((780, 410, 690, 275), fill=INK, width=6)
    draw.text((540, 215), "NH₂", font=font(42, True), fill=GREEN)
    draw.text((690, 900), "pyrimidine base", font=font(30), fill=INK)


def draw_iupac_structure(draw):
    points = [(360, 660), (540, 530), (720, 660), (900, 530), (1080, 660), (1260, 530), (1440, 660)]
    draw.line(points, fill=BLUE, width=9, joint="curve")
    for i, (x, y) in enumerate(points, start=1):
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=INK)
        draw.text((x - 12, y + 26), str(i), font=font(24), fill=INK)
    draw.line((540, 530, 540, 340), fill=INK, width=6)
    draw.text((505, 265), "Cl", font=font(42, True), fill=RED)
    draw.line((900, 530, 900, 340), fill=INK, width=6)
    draw.text((845, 265), "CH₃", font=font(38, True), fill=GREEN)
    draw.text((620, 800), "longest chain: heptane", font=font(30), fill=INK)


def panel(draw, box, label):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=20, outline="#bdc9d8", width=4, fill="#fbfdff")
    draw.text((x1 + 22, y1 + 16), label, font=font(32, True), fill=BLUE)


def draw_friedel_crafts_options(draw):
    draw.text((580, 285), "C₆H₆  +  CH₃CH₂COCl     AlCl₃", font=font(36, True), fill=INK)
    arrow(draw, (970, 350), (1170, 350), BLUE, 5)
    draw.text((1220, 325), "product?", font=font(32, True), fill=INK)
    choices = [
        ("A", "C₆H₅–CH(CO–C₂H₅)"),
        ("B", "C₆H₅–CH(CO–CH₃)"),
        ("C", "C₆H₅–CH(O–C₂H₅)"),
        ("D", "C₆H₅–CO–C₂H₅"),
    ]
    boxes = [(240, 470, 860, 660), (940, 470, 1560, 660), (240, 720, 860, 910), (940, 720, 1560, 910)]
    for (label, structure), box in zip(choices, boxes):
        panel(draw, box, label)
        draw.text((box[0] + 100, box[1] + 90), structure, font=font(31, True), fill=INK)


def draw_cyanohydrin_options(draw):
    draw.text((440, 310), "CH₃–C(=O)–C₂H₅  +  HCN", font=font(40, True), fill=INK)
    arrow(draw, (840, 375), (1080, 375), BLUE, 5)
    draw.text((820, 410), "NaCN / HCl", font=font(28), fill=GREEN)
    draw.text((1120, 340), "Y", font=font(40, True), fill=RED)
    choices = [
        ("A", "CH₃–C(OH)(CN)–C₂H₅"),
        ("B", "CH₃–C(OH)(CN)–H"),
        ("C", "CH₃–C(OH)(CN)–CH₃"),
        ("D", "CH₃–C(OH)(NH₂)–C₂H₅"),
    ]
    boxes = [(190, 500, 900, 690), (930, 500, 1640, 690), (190, 740, 900, 930), (930, 740, 1640, 930)]
    for (label, structure), box in zip(choices, boxes):
        panel(draw, box, label)
        draw.text((box[0] + 100, box[1] + 90), structure, font=font(30, True), fill=INK)


def draw_terylene_options(draw):
    choices = [
        ("A", "HOOC–C₆H₄–COOH  +  HO–CH₂CH₂–OH"),
        ("B", "HOOC–C₆H₄–COOH  +  HO–C₆H₄–OH"),
        ("C", "HOOC–(CH₂)₄–COOH  +  HO–CH₂CH₂–OH"),
        ("D", "HOOC–(CH₂)₄–COOH  +  HO–C₆H₄–OH"),
    ]
    boxes = [(150, 320, 870, 580), (930, 320, 1650, 580), (150, 650, 870, 910), (930, 650, 1650, 910)]
    for (label, structure), box in zip(choices, boxes):
        panel(draw, box, label)
        y = box[1] + 100
        for line in textwrap.wrap(structure, width=28):
            draw.text((box[0] + 85, y), line, font=font(29, True), fill=INK)
            y += 48


def mini_axes(draw, origin, label):
    x, y = origin
    draw.line((x, y, x + 340, y), fill=INK, width=4)
    draw.line((x, y, x, y - 220), fill=INK, width=4)
    draw.text((x + 130, y + 15), label, font=font(32, True), fill=BLUE)


def draw_boiling_graphs(draw):
    # Series III (group-V hydrides) shows the NH3 anomaly due to H-bonding.
    for origin, label in [((220, 820), "I"), ((730, 820), "II"), ((1240, 820), "III")]:
        mini_axes(draw, origin, label)
    draw.line([(280, 760), (380, 710), (480, 580), (560, 520)], fill=BLUE, width=7)
    draw.line([(790, 750), (900, 680), (1010, 625), (1120, 580)], fill=BLUE, width=7)
    draw.line([(1300, 570), (1410, 690), (1520, 645), (1620, 550)], fill=BLUE, width=7)
    draw.text((1300, 850), "NH₃   PH₃   AsH₃   SbH₃", font=font(20), fill=INK)
    draw.text((1220, 360), "high NH₃ boiling point", font=font(27, True), fill=GREEN)
    arrow(draw, (1440, 400), (1310, 570), GREEN, 4)


def draw_period3(draw):
    axes(draw,(350,900),1100,500,"atomic number (Na → Ar)","property")
    pts=[(420,430),(530,510),(660,600),(800,680),(950,740),(1100,780),(1280,810)]
    draw.line(pts,fill=BLUE,width=8,joint="curve")


def draw_melting(draw):
    axes(draw,(350,900),1100,520,"consecutive atomic numbers","melting point")
    pts=[(420,780),(560,680),(700,600),(820,250),(950,700),(1080,740),(1240,780)]
    draw.line(pts,fill=BLUE,width=8,joint="curve")
    for (x, y), label in zip([pts[1], pts[2], pts[3], pts[4]], ["A", "B", "C", "D"]):
        draw.text((x - 12, y - 55), label, font=font(32, True), fill=RED)
    for x, _ in pts:
        draw.line((x, 890, x, 910), fill=INK, width=3)


def draw_formula(draw, formula):
    draw.rounded_rectangle((250, 380, 1550, 780), 35, outline=BLUE, width=7)
    draw.text((420, 515), formula, font=font(48, True), fill=INK)


# Use ASCII formula notation in the generated PNGs.  Arial on Windows does not
# reliably contain the Unicode subscript glyphs, which otherwise render as boxes.
def draw_cytosine_clean(draw):
    pts = [(780, 410), (1010, 410), (1130, 610), (1010, 810), (780, 810), (660, 610)]
    draw.line(pts + [pts[0]], fill=BLUE, width=8, joint="curve")
    draw.line((800, 435, 980, 435), fill=INK, width=3)
    draw.line((1094, 625, 990, 790), fill=INK, width=3)
    draw.text((735, 375), "N", font=font(42, True), fill=INK)
    draw.text((1070, 570), "N", font=font(42, True), fill=INK)
    draw.line((660, 610, 510, 610), fill=INK, width=6)
    draw.line((660, 630, 510, 630), fill=INK, width=3)
    draw.text((410, 580), "O", font=font(44, True), fill=RED)
    draw.line((780, 410, 690, 275), fill=INK, width=6)
    draw.text((540, 215), "NH2", font=font(42, True), fill=GREEN)
    draw.text((690, 900), "pyrimidine base", font=font(30), fill=INK)


def draw_choice_grid(draw, heading, choices, font_size=30):
    draw.text((360, 285), heading, font=font(36, True), fill=INK)
    boxes = [(190, 470, 900, 660), (930, 470, 1640, 660), (190, 720, 900, 910), (930, 720, 1640, 910)]
    for (label, value), box in zip(choices, boxes):
        panel(draw, box, label)
        draw.text((box[0] + 96, box[1] + 87), value, font=font(font_size, True), fill=INK)


def draw_friedel_crafts_clean(draw):
    draw_choice_grid(
        draw,
        "C6H6 + CH3CH2COCl     AlCl3     ->     product?",
        [("A", "C6H5-CH(CO-C2H5)"), ("B", "C6H5-CH(CO-CH3)"),
         ("C", "C6H5-CH(O-C2H5)"), ("D", "C6H5-CO-C2H5")],
        31,
    )


def draw_cyanohydrin_clean(draw):
    draw_choice_grid(
        draw,
        "CH3-C(=O)-C2H5 + HCN     NaCN / HCl     ->     Y",
        [("A", "CH3-C(OH)(CN)-C2H5"), ("B", "CH3-C(OH)(CN)-H"),
         ("C", "CH3-C(OH)(CN)-CH3"), ("D", "CH3-C(OH)(NH2)-C2H5")],
        29,
    )


def draw_terylene_clean(draw):
    choices = [
        ("A", ["HOOC-C6H4-COOH +", "HO-CH2CH2-OH"]),
        ("B", ["HOOC-C6H4-COOH +", "HO-C6H4-OH"]),
        ("C", ["HOOC-(CH2)4-COOH +", "HO-CH2CH2-OH"]),
        ("D", ["HOOC-(CH2)4-COOH +", "HO-C6H4-OH"]),
    ]
    boxes = [(150, 320, 870, 580), (930, 320, 1650, 580), (150, 650, 870, 910), (930, 650, 1650, 910)]
    for (label, lines), box in zip(choices, boxes):
        panel(draw, box, label)
        for offset, line in enumerate(lines):
            draw.text((box[0] + 85, box[1] + 95 + 55 * offset), line, font=font(29, True), fill=INK)


def draw_boiling_clean(draw):
    for origin, label in [((220, 820), "I"), ((730, 820), "II"), ((1240, 820), "III")]:
        mini_axes(draw, origin, label)
    draw.line([(280, 760), (380, 710), (480, 580), (560, 520)], fill=BLUE, width=7)
    draw.line([(790, 750), (900, 680), (1010, 625), (1120, 580)], fill=BLUE, width=7)
    draw.line([(1300, 570), (1410, 690), (1520, 645), (1620, 550)], fill=BLUE, width=7)
    draw.text((1290, 850), "NH3   PH3   AsH3   SbH3", font=font(19), fill=INK)
    draw.text((1210, 360), "high NH3 boiling point", font=font(27, True), fill=GREEN)
    arrow(draw, (1440, 400), (1310, 570), GREEN, 4)


def draw_iupac_clean(draw):
    points = [(360, 660), (540, 530), (720, 660), (900, 530), (1080, 660), (1260, 530), (1440, 660)]
    draw.line(points, fill=BLUE, width=9, joint="curve")
    for i, (x, y) in enumerate(points, start=1):
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=INK)
        draw.text((x - 12, y + 26), str(i), font=font(24), fill=INK)
    draw.line((540, 530, 540, 340), fill=INK, width=6)
    draw.text((505, 265), "Cl", font=font(42, True), fill=RED)
    draw.line((900, 530, 900, 340), fill=INK, width=6)
    draw.text((845, 265), "CH3", font=font(38, True), fill=GREEN)
    draw.text((620, 800), "longest chain: heptane", font=font(30), fill=INK)


DRAWERS = {
    1396: draw_ecg, 1460: draw_cytosine_clean,
    1472: draw_stomach, 1474: draw_gastric_gland, 1475: draw_lungs,
    1482: draw_work_graph, 1492: draw_double_slit, 1497: draw_inverse_square,
    1502: draw_resistor_network, 1503: draw_field, 1512: draw_rectifier,
    1515: draw_ke_graph, 1554: draw_energy, 1555: draw_period3,
    1556: draw_melting, 1567: draw_iupac_clean,
    1568: draw_friedel_crafts_clean,
    1583: draw_cyanohydrin_clean,
    1591: draw_terylene_clean,
    1599: draw_boiling_clean,
}


def create(question):
    image = Image.new("RGB", SIZE, "white")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((35, 35, 1765, 1165), 30, outline="#d7e0eb", width=4)
    heading = f"MDCAT 2017 • Question {question.id}"
    draw.text((95, 80), heading, font=font(30, True), fill=BLUE)
    multiline(draw, clean_stem(question.question_text), (95, 135, 1610), font(38, True))
    DRAWERS[question.id](draw)
    options = [question.option_a, question.option_b, question.option_c, question.option_d]
    y = 1015
    for idx, option in enumerate(options):
        x = 120 if idx % 2 == 0 else 920
        oy = y + (idx // 2) * 70
        multiline(draw, f"{'ABCD'[idx]}. {option}", (x, oy, 720), font(26))
    path = OUTPUT_DIR / f"q{question.id}_clean_redraw.png"
    image.save(path, "PNG", optimize=True)
    return path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for question_id in DRAWERS:
        question = Question.objects.get(id=question_id)
        path = create(question)
        QuestionImage.objects.filter(question=question).delete()
        QuestionImage.objects.create(
            question=question,
            image=f"question_images/{path.name}",
            source_name="Original clean educational redraw",
            source_year=2017,
        )
        question.is_visual_required = True
        question.save(update_fields=["is_visual_required"])
        print(f"created {path}")


if __name__ == "__main__":
    main()

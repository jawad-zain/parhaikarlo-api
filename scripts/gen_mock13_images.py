"""Generate the 5 diagram/graph images referenced by mdcat_mock13.py's
image-based questions:
  Q8   Biology  - bar graph of enzyme activity with 3 different metal-ion
                  cofactors (Tube1=Zn2+, Tube2=Mg2+, Tube3=Ca2+); Tube 2
                  (Mg2+) shows highest activity -> enzyme needs Mg2+.
  Q14  Biology  - labeled plant cell (A=mitochondrion, B=nucleus,
                  C=chloroplast w/ grana stacks, D=vacuole); asks which
                  is C -> chloroplast.
  Q110 Chemistry- pH titration curve, HCl (strong acid) added to NH3
                  (weak base). Starts high pH (~11), equivalence point
                  BELOW pH 7 (salt NH4Cl is weakly acidic), plateaus low
                  at high acid volume.
  Q154 Physics  - R1(8 ohm) + R2(8 ohm) in SERIES (=16 ohm), that
                  combination in PARALLEL with R3(16 ohm) -> total = 8 ohm.
  Q162 Physics  - plane mirror ray diagram: object in front of mirror,
                  virtual image forms an equal distance BEHIND the
                  mirror, same size, laterally inverted.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, Rectangle

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q8: Enzyme activity bar graph across 3 metal-ion cofactors.
# Tube 1 = Zn2+ (low), Tube 2 = Mg2+ (high), Tube 3 = Ca2+ (low-medium)
# ---------------------------------------------------------------
def enzyme_cofactor_bar_graph():
    fig, ax = plt.subplots(figsize=(7, 5.5))
    tubes = ["Tube 1\n(Zn2+)", "Tube 2\n(Mg2+)", "Tube 3\n(Ca2+)"]
    activity = [22, 88, 34]
    colors = ["#7a9cc6", "#2e7d32", "#c69a2e"]
    bars = ax.bar(tubes, activity, color=colors, edgecolor="black", linewidth=1.4, width=0.55)
    for b, v in zip(bars, activity):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v}", ha="center", fontsize=11, fontweight="bold")

    ax.set_ylim(0, 100)
    ax.set_ylabel("Relative Enzyme Activity (%)", fontsize=12)
    ax.set_title("Enzyme Activity with Different Metal-Ion Cofactors", fontsize=13.5, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(0, color="black", linewidth=1)

    save(fig, "q13_enzyme_cofactor_bar_graph.png")


# ---------------------------------------------------------------
# Q14: Plant cell diagram labeled A, B, C, D.
#   A = mitochondrion (oval, double membrane, cristae)
#   B = nucleus (large circle, nucleolus inside)
#   C = chloroplast (oval, double membrane, internal grana stacks) <- ANSWER
#   D = vacuole (large, central, membrane-bound sac)
# ---------------------------------------------------------------
def plant_cell_diagram():
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Plant Cell", fontsize=15, fontweight="bold")

    # outer cell wall + membrane (rounded rectangle-ish cell)
    ax.add_patch(Ellipse((5, 5), 8.6, 8.2, facecolor="#eef7ea", edgecolor="#2d5a27", linewidth=3))
    ax.add_patch(Ellipse((5, 5), 8.1, 7.7, facecolor="none", edgecolor="#6fae63", linewidth=1.2))

    # D: central vacuole (large sac, mostly central)
    vac_center = (5, 4.8)
    ax.add_patch(Ellipse(vac_center, 4.6, 4.2, facecolor="#dff0fb", edgecolor="#3f7fa6", linewidth=1.8))
    ax.text(5, 4.8, "Vacuole", ha="center", va="center", fontsize=10, color="#2a5b78")

    # B: nucleus (upper-left region)
    nuc_center = (2.6, 7.2)
    ax.add_patch(Circle(nuc_center, 1.05, facecolor="#8b1a4a", edgecolor="#5a0f30", linewidth=1.6, zorder=4))
    ax.add_patch(Circle(nuc_center, 0.32, facecolor="#5a0f30", edgecolor="black", linewidth=1, zorder=5))

    # A: mitochondrion (lower-left region) -- oval with cristae folds
    mito_center = (2.6, 2.4)
    ax.add_patch(Ellipse(mito_center, 1.9, 1.0, facecolor="#f4c07a", edgecolor="#a06a1f", linewidth=1.8, zorder=4))
    for i in range(4):
        xoff = -0.55 + i * 0.35
        ax.plot([mito_center[0] + xoff, mito_center[0] + xoff],
                 [mito_center[1] - 0.32, mito_center[1] + 0.32], color="#a06a1f", linewidth=1.3, zorder=5)

    # C: chloroplast (right region) -- double membrane oval with grana stacks
    chl_center = (7.6, 5.8)
    ax.add_patch(Ellipse(chl_center, 2.1, 1.3, facecolor="#c8e6c9", edgecolor="#1b5e20", linewidth=2.0, zorder=4))
    ax.add_patch(Ellipse(chl_center, 1.85, 1.05, facecolor="none", edgecolor="#1b5e20", linewidth=0.9, zorder=4))
    rng = np.random.default_rng(3)
    for gx in [-0.55, -0.15, 0.25, 0.6]:
        gy = chl_center[1] + rng.uniform(-0.15, 0.15)
        for k in range(3):
            ax.add_patch(Rectangle((chl_center[0] + gx - 0.09, gy - 0.28 + k * 0.11), 0.18, 0.09,
                                    facecolor="#2e7d32", edgecolor="#1b5e20", linewidth=0.5, zorder=5))

    def label(letter, tx, ty, target, color="black"):
        ax.annotate(letter, xy=target, xytext=(tx, ty), fontsize=15, fontweight="bold",
                    ha="center", va="center", color=color,
                    arrowprops=dict(arrowstyle="-", color="black", lw=1.2),
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6), zorder=6)

    label("A", 0.6, 1.2, mito_center)
    label("B", 0.6, 8.6, nuc_center)
    label("C", 9.3, 8.3, chl_center)
    label("D", 9.3, 3.4, (7.2, 3.6))

    ax.text(5, 0.35, "A = mitochondrion   B = nucleus   C = chloroplast (grana stacks)   D = vacuole",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q13_plant_cell_diagram_abcd.png")


# ---------------------------------------------------------------
# Q110: Titration curve -- strong acid (HCl) added to a weak base
# (ammonia, NH3) solution.
#   - Starting pH is basic but NOT extremely high (weak base), ~11.
#   - A gently-sloping buffering region as NH3/NH4+ buffer forms.
#   - A steep drop through the equivalence point.
#   - Equivalence point pH is BELOW 7 (salt NH4Cl hydrolyzes, weakly acidic).
#   - Beyond equivalence, curve flattens out at low pH (excess strong acid).
# ---------------------------------------------------------------
def titration_weak_base_strong_acid():
    veq = 25.0  # mL of HCl at equivalence
    v = np.linspace(0.01, 50, 400)

    ph = np.piecewise(
        v,
        [v < veq, v >= veq],
        [
            lambda v: 11.2 - 3.6 * (v / veq) ** 1.7,   # basic region draining toward eq point
            lambda v: 5.2 - 3.9 * (1 - np.exp(-(v - veq) / 6.0)),  # sharp drop then leveling off, acidic
        ],
    )
    ph = np.clip(ph, 1.0, 11.5)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(v, ph, color="#2e7d32", linewidth=2.6)
    ax.axhline(7, color="gray", linewidth=0.9, linestyle=":")
    ax.text(1, 7.15, "pH 7 (neutral)", fontsize=9, color="gray")

    eq_ph = 5.2
    ax.axvline(veq, color="#a8332c", linewidth=1.0, linestyle="--")
    ax.plot(veq, eq_ph, "o", color="#a8332c", markersize=7, zorder=5)
    ax.annotate("Equivalence point\n(pH < 7, salt is weakly acidic)", xy=(veq, eq_ph),
                xytext=(veq + 6, eq_ph + 2.3), fontsize=9.5, color="#a8332c",
                arrowprops=dict(arrowstyle="-", color="#a8332c"))

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 12.5)
    ax.set_xlabel("Volume of HCl added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_title("Titration Curve: Strong Acid (HCl) added to Weak Base (NH3)", fontsize=13, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    save(fig, "q13_titration_weak_base_strong_acid.png")


# ---------------------------------------------------------------
# Q154: R1 (8 ohm) and R2 (8 ohm) in SERIES (-> 16 ohm), that
# combination in PARALLEL with R3 (16 ohm) -> total = 8 ohm.
# ---------------------------------------------------------------
def circuit_r1r2_series_r3_parallel():
    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.add_patch(plt.Circle((1, 3.5), 0.6, facecolor="white", edgecolor="black", linewidth=2))
    ax.text(1, 3.78, "+", ha="center", va="center", fontsize=13)
    ax.text(1, 3.22, "-", ha="center", va="center", fontsize=13)
    ax.text(1, 2.6, "Battery", ha="center", va="center", fontsize=11)

    def resistor(x0, y0, x1, y1, label):
        n = 7
        xs = np.linspace(x0, x1, n)
        ys = np.linspace(y0, y1, n)
        zig = np.array([0, 1, -1, 1, -1, 1, 0]) * 0.18
        if abs(x1 - x0) > abs(y1 - y0):
            ys = ys + zig
        else:
            xs = xs + zig
        ax.plot(xs, ys, color="black", linewidth=2)
        midx, midy = (x0 + x1) / 2, (y0 + y1) / 2
        if abs(x1 - x0) > abs(y1 - y0):
            ax.text(midx, midy + 0.5, label, ha="center", fontsize=11)
        else:
            ax.text(midx + 0.95, midy, label, ha="center", fontsize=11)

    # lead from battery up to the top rail
    ax.plot([1, 1], [4.1, 6], color="black", linewidth=2)
    ax.plot([1, 3], [6, 6], color="black", linewidth=2)

    # --- top branch: R1 + R2 in series ---
    ax.plot([3, 4.4], [6, 6], color="black", linewidth=2)
    resistor(4.4, 6, 6.0, 6, "R1 = 8 Ω")
    ax.plot([6.0, 6.9], [6, 6], color="black", linewidth=2)
    resistor(6.9, 6, 8.5, 6, "R2 = 8 Ω")
    ax.plot([8.5, 9.2], [6, 6], color="black", linewidth=2)

    # --- bottom branch: R3 alone (parallel with the R1+R2 series pair) ---
    ax.plot([3, 3], [6, 1.2], color="black", linewidth=2)
    ax.plot([3, 4.4], [1.2, 1.2], color="black", linewidth=2)
    resistor(4.4, 1.2, 6.0, 1.2, "R3 = 16 Ω")
    ax.plot([6.0, 9.2], [1.2, 1.2], color="black", linewidth=2)
    ax.plot([9.2, 9.2], [1.2, 6], color="black", linewidth=2)

    # return to battery
    ax.plot([1, 1], [2.9, 0.5], color="black", linewidth=2)
    ax.plot([1, 9.2], [0.5, 0.5], color="black", linewidth=2)
    ax.plot([9.2, 9.2], [0.5, 1.2], color="black", linewidth=2)

    ax.text(5, 0.05, "R1 + R2 (series) = 16 Ω  ∥  R3 = 16 Ω  =>  total = 8 Ω",
            ha="center", fontsize=9.5, style="italic")

    save(fig, "q13_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: Plane mirror ray diagram.
#   Object placed at distance d in front of a plane mirror.
#   Image is virtual, upright, same size, formed at distance d BEHIND
#   the mirror, and laterally inverted (shown via a mirrored "F"-like
#   asymmetric marker so the inversion is visually obvious).
# ---------------------------------------------------------------
def plane_mirror_diagram():
    d = 3.2       # object distance in front of mirror
    obj_h = 1.6   # object height (base at mirror axis / ground line)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-d - 1.5, d + 1.5)
    ax.set_ylim(-0.8, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Plane Mirror", fontsize=15, fontweight="bold")

    # ground/base line
    ax.axhline(0, color="black", linewidth=1.0)

    # mirror: vertical line at x=0, with hatching behind it (silvered back)
    ax.plot([0, 0], [-0.6, obj_h + 1.2], color="#2f6f9f", linewidth=4, solid_capstyle="butt")
    for hy in np.arange(-0.55, obj_h + 1.15, 0.22):
        ax.plot([0, 0.22], [hy, hy + 0.22], color="#2f6f9f", linewidth=1.0)

    obj_x = -d
    img_x = d

    # object: upright arrow with a flag near the tip to show orientation
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.8))
    ax.plot([obj_x, obj_x + 0.28], [obj_h - 0.15, obj_h - 0.15], color="#1a7a3a", linewidth=2.2)
    ax.text(obj_x, obj_h + 0.3, "Object", color="#1a7a3a", fontsize=13, ha="center")
    ax.annotate("", xy=(-0.05, -0.55), xytext=(obj_x, -0.55),
                arrowprops=dict(arrowstyle="<->", color="#333", linewidth=1.1))
    ax.text(obj_x / 2, -0.72, "d", ha="center", fontsize=11, color="#333")

    # virtual image: same height, laterally inverted (flag points opposite
    # side, i.e. toward the object side, at the same height) -- dashed
    ax.annotate("", xy=(img_x, obj_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.6, linestyle="dashed"))
    ax.plot([img_x, img_x - 0.28], [obj_h - 0.15, obj_h - 0.15], color="#a8332c", linewidth=2.0, linestyle="dashed")
    ax.text(img_x, obj_h + 0.3, "Virtual Image", color="#a8332c", fontsize=13, ha="center")
    ax.annotate("", xy=(0.05, -0.55), xytext=(img_x, -0.55),
                arrowprops=dict(arrowstyle="<->", color="#333", linewidth=1.1, linestyle="dashed"))
    ax.text(img_x / 2, -0.72, "d", ha="center", fontsize=11, color="#333")

    # two incident rays from the object tip to the mirror, reflecting to
    # an eye position, with dashed backward extensions meeting behind the
    # mirror at the image tip.
    eye = (2.4, 0.55)
    for hit_y in [obj_h * 0.55, obj_h * 0.95]:
        # incident ray: object tip -> point on mirror
        ax.plot([obj_x, 0], [obj_h, hit_y], color="#555", linewidth=1.3)
        # reflected ray: mirror point -> eye
        ax.plot([0, eye[0]], [hit_y, eye[1]], color="#555", linewidth=1.3)
        # dashed backward extension behind mirror to the virtual image tip
        ax.plot([0, img_x], [hit_y, obj_h], color="#999", linewidth=1.0, linestyle="dotted")

    # eye symbol
    ax.add_patch(Ellipse(eye, 0.5, 0.28, facecolor="white", edgecolor="black", linewidth=1.3, zorder=5))
    ax.add_patch(Circle(eye, 0.08, facecolor="black", zorder=6))
    ax.text(eye[0], eye[1] - 0.35, "Eye", ha="center", fontsize=9.5, color="#333")

    ax.text(0, obj_h + 1.35,
            "Image distance behind mirror = object distance in front (d = d);\n"
            "virtual, upright, same size, laterally inverted",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q13_plane_mirror_diagram.png")


if __name__ == "__main__":
    enzyme_cofactor_bar_graph()
    plant_cell_diagram()
    titration_weak_base_strong_acid()
    circuit_r1r2_series_r3_parallel()
    plane_mirror_diagram()

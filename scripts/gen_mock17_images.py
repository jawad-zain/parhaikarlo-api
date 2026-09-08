"""Generate the 5 diagram images referenced by mdcat_mock17.py's
image-based questions:
  Q12  Biology  - plasma-membrane cross-section labeled W/X/Y/Z:
                  W = phospholipid bilayer, X = integral/transmembrane
                  protein spanning the membrane, Y = peripheral protein
                  on the surface, Z = cholesterol embedded in the
                  bilayer.
  Q65  Biology  - heart cross-section with valves labeled 1-4:
                  1 = tricuspid (right atrium <-> right ventricle),
                  2 = bicuspid/mitral (left atrium <-> left ventricle),
                  3 = aortic, 4 = pulmonary. Right side of the heart
                  drawn on the viewer's LEFT (anatomical convention).
  Q100 Chemistry - reaction energy-profile diagram: products lower
                  energy than reactants (exothermic), Ea and delta H
                  both marked.
  Q154 Physics  - R1 (6 ohm) and R2 (3 ohm) in parallel (-> 2 ohm),
                  that combination in series with R3 (4 ohm) ->
                  total = 6 ohm. No dangling components.
  Q162 Physics  - concave mirror, object placed exactly at the center
                  of curvature C: real, inverted, same-size image
                  formed at C. Correct bulge-toward-object sign
                  convention x(y) = -k*y**2.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch, Circle, Wedge, Arc
from matplotlib.lines import Line2D

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: plasma-membrane cross-section, labeled W/X/Y/Z.
# ---------------------------------------------------------------
def membrane_crosssection():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Plasma Membrane Cross-Section", fontsize=15, fontweight="bold")

    rng = np.random.default_rng(3)
    head_y_top, head_y_bot = 4.6, 2.2
    xs = np.linspace(0.8, 12.2, 46)

    # W: phospholipid bilayer -- two rows of head/tail phospholipids
    for x in xs:
        # top leaflet
        ax.add_patch(Circle((x, head_y_top), 0.16, facecolor="#f2c14e", edgecolor="#8a6d1a", linewidth=0.8, zorder=3))
        ax.plot([x, x], [head_y_top - 0.16, head_y_top - 0.95], color="#8a6d1a", linewidth=1.3, zorder=2)
        # bottom leaflet
        ax.add_patch(Circle((x, head_y_bot), 0.16, facecolor="#f2c14e", edgecolor="#8a6d1a", linewidth=0.8, zorder=3))
        ax.plot([x, x], [head_y_bot + 0.16, head_y_bot + 0.95], color="#8a6d1a", linewidth=1.3, zorder=2)

    ax.annotate("W", xy=(2.0, head_y_top), xytext=(2.0, 6.3), fontsize=15, fontweight="bold", ha="center",
                bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6),
                arrowprops=dict(arrowstyle="-", color="black"))
    ax.text(2.0, 0.7, "W: Phospholipid bilayer", ha="center", fontsize=9.5)

    # X: integral/transmembrane protein spanning full width
    px = 5.6
    ax.add_patch(Rectangle((px - 0.55, head_y_bot - 0.5), 1.1, (head_y_top - head_y_bot) + 1.0,
                            facecolor="#5b8fb9", edgecolor="#1f3f5c", linewidth=2.0, zorder=4,
                            joinstyle="round"))
    ax.text(px, (head_y_top + head_y_bot) / 2, "X", fontsize=13, fontweight="bold", ha="center",
            va="center", color="white", zorder=5)
    ax.annotate("", xy=(px, 6.1), xytext=(px, head_y_top + 1.1),
                arrowprops=dict(arrowstyle="-", color="black"))
    ax.text(px, 6.3, "X", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(px, 0.7, "X: Integral (transmembrane)\nprotein", ha="center", fontsize=9.5)

    # Y: peripheral protein sitting on the outer surface only
    py = 9.2
    yx = 8.7
    blob = Ellipse((yx, head_y_top + 0.75), 1.1, 0.6, facecolor="#c0693f", edgecolor="#7a3d20",
                    linewidth=2.0, zorder=4)
    ax.add_patch(blob)
    ax.annotate("", xy=(yx, 6.1), xytext=(yx, head_y_top + 1.15),
                arrowprops=dict(arrowstyle="-", color="black"))
    ax.text(yx, 6.3, "Y", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(yx, 0.7, "Y: Peripheral protein\n(surface only)", ha="center", fontsize=9.5)

    # Z: cholesterol molecule embedded within the bilayer
    zx = 11.0
    ax.add_patch(Rectangle((zx - 0.16, head_y_bot - 0.2), 0.32, (head_y_top - head_y_bot) + 0.4,
                            facecolor="#7fbf7f", edgecolor="#2e6b2e", linewidth=1.8, zorder=4))
    ax.annotate("", xy=(zx, 6.1), xytext=(zx, head_y_top + 0.6),
                arrowprops=dict(arrowstyle="-", color="black"))
    ax.text(zx, 6.3, "Z", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(zx, 0.7, "Z: Cholesterol\n(embedded in bilayer)", ha="center", fontsize=9.5)

    ax.text(6.5, 1.6, "Outside cell", ha="center", fontsize=9, style="italic", color="#555")
    ax.text(6.5, 5.3, "", ha="center")
    ax.text(0.6, head_y_top + 0.35, "outer leaflet", fontsize=8, color="#555")
    ax.text(0.6, head_y_bot - 0.35, "inner leaflet", fontsize=8, color="#555")

    save(fig, "q_membrane_crosssection_diagram.png")


# ---------------------------------------------------------------
# Q65: heart cross-section, valves labeled 1-4. Anatomical
# convention: the heart's right side (right atrium, right ventricle,
# tricuspid valve) is drawn on the viewer's LEFT.
# ---------------------------------------------------------------
def heart_tricuspid_valve():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Heart Cross-Section (anterior view)", fontsize=15, fontweight="bold")

    # overall heart outline
    outline = Ellipse((5, 5), 8.6, 8.6, facecolor="#f7d6d6", edgecolor="#7a1f1f", linewidth=2.5, zorder=0)
    ax.add_patch(outline)

    # septum dividing left/right halves
    ax.plot([5, 5], [1.2, 8.8], color="#7a1f1f", linewidth=2.2, zorder=1)

    # Right atrium (viewer's LEFT, upper) -- deoxygenated blood, drawn lighter blue
    ra = Ellipse((3.0, 7.0), 3.4, 2.6, facecolor="#a9c9e8", edgecolor="#2c5d8a", linewidth=2, zorder=2)
    ax.add_patch(ra)
    ax.text(3.0, 7.0, "Right\nAtrium", ha="center", va="center", fontsize=9)

    # Right ventricle (viewer's LEFT, lower)
    rv = Ellipse((3.2, 3.0), 4.0, 3.6, facecolor="#7fa8d1", edgecolor="#2c5d8a", linewidth=2, zorder=2)
    ax.add_patch(rv)
    ax.text(3.2, 2.6, "Right\nVentricle", ha="center", va="center", fontsize=9)

    # Left atrium (viewer's RIGHT, upper) -- oxygenated, drawn red
    la = Ellipse((7.0, 7.0), 3.4, 2.6, facecolor="#e8a9a9", edgecolor="#7a1f1f", linewidth=2, zorder=2)
    ax.add_patch(la)
    ax.text(7.0, 7.0, "Left\nAtrium", ha="center", va="center", fontsize=9)

    # Left ventricle (viewer's RIGHT, lower) -- thicker wall
    lv = Ellipse((6.9, 3.0), 3.7, 4.0, facecolor="#d16a6a", edgecolor="#7a1f1f", linewidth=3, zorder=2)
    ax.add_patch(lv)
    ax.text(6.9, 2.6, "Left\nVentricle", ha="center", va="center", fontsize=9, color="white")

    def valve_marker(x, y, num, label):
        ax.add_patch(Ellipse((x, y), 0.55, 0.3, facecolor="white", edgecolor="black", linewidth=2, zorder=5))
        ax.text(x, y, str(num), ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)

    # Valve 1: TRICUSPID -- between right atrium and right ventricle
    valve_marker(3.1, 5.05, 1, "tricuspid")
    # Valve 2: BICUSPID/MITRAL -- between left atrium and left ventricle
    valve_marker(6.95, 5.05, 2, "mitral")
    # Valve 3: AORTIC -- at the outlet of the left ventricle (top)
    valve_marker(6.3, 8.7, 3, "aortic")
    # Valve 4: PULMONARY -- at the outlet of the right ventricle (top)
    valve_marker(3.6, 8.7, 4, "pulmonary")

    ax.text(5, 0.4,
            "Valve 1 (tricuspid) lies between the right atrium and right ventricle.",
            ha="center", fontsize=10, style="italic", color="#333")

    save(fig, "q_heart_tricuspid_valve_diagram.png")


# ---------------------------------------------------------------
# Q100: reaction energy-profile diagram -- exothermic (products
# lower in energy than reactants), Ea and delta H both marked.
# ---------------------------------------------------------------
def energy_profile_exothermic():
    x = np.linspace(0, 10, 400)
    reactant_e = 5.0
    ts_e = 8.5
    product_e = 2.0

    y = np.piecewise(
        x,
        [x < 4, (x >= 4) & (x < 6), x >= 6],
        [
            lambda xv: reactant_e + (ts_e - reactant_e) * (xv / 4) ** 2,
            lambda xv: ts_e,
            lambda xv: product_e + (ts_e - product_e) * ((10 - xv) / 4) ** 2,
        ],
    )
    y_smooth = y  # keep simple piecewise-parabolic shape (still a clean single-hump curve)

    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.plot(x, y_smooth, color="#1a5276", linewidth=3)
    ax.set_xlabel("Reaction progress", fontsize=12)
    ax.set_ylabel("Potential energy", fontsize=12)
    ax.set_title("Reaction Energy Profile", fontsize=14, fontweight="bold")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    # dashed reference lines
    ax.plot([0, 4], [reactant_e, reactant_e], "--", color="gray", linewidth=1)
    ax.plot([6, 10], [product_e, product_e], "--", color="gray", linewidth=1)
    ax.plot([0, 5], [ts_e, ts_e], ":", color="gray", linewidth=0.8)

    # Ea arrow: reactants -> transition state peak
    ax.annotate("", xy=(4.3, ts_e), xytext=(4.3, reactant_e),
                arrowprops=dict(arrowstyle="<->", color="#c0392b", linewidth=2))
    ax.text(4.6, (reactant_e + ts_e) / 2, "Ea\n(activation\nenergy)", fontsize=9.5, color="#c0392b")

    # delta H arrow: reactants -> products
    ax.annotate("", xy=(9.4, product_e), xytext=(9.4, reactant_e),
                arrowprops=dict(arrowstyle="<->", color="#1a7a3a", linewidth=2))
    ax.text(9.5, (reactant_e + product_e) / 2, "ΔH\n(negative)", fontsize=9.5, color="#1a7a3a")

    ax.text(1.5, reactant_e - 0.6, "Reactants", ha="center", fontsize=10)
    ax.text(5, ts_e + 0.4, "Transition\nstate", ha="center", fontsize=9)
    ax.text(8.5, product_e - 0.6, "Products", ha="center", fontsize=10)

    ax.text(5, -0.9, "Products are LOWER in energy than reactants → exothermic reaction",
            ha="center", fontsize=10, style="italic", color="#333")

    save(fig, "q_energy_profile_diagram.png")


# ---------------------------------------------------------------
# Q154: R1 (6 ohm) and R2 (3 ohm) in PARALLEL (-> 2 ohm), that
# combination in SERIES with R3 (4 ohm) -> total = 6 ohm.
# ---------------------------------------------------------------
def circuit_r1r2_parallel_r3_series():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Circuit: R1 ∥ R2 (parallel), in series with R3", fontsize=14, fontweight="bold")

    def wire(x0, y0, x1, y1):
        ax.plot([x0, x1], [y0, y1], color="black", linewidth=2.2, zorder=1)

    def resistor(x0, y0, x1, y1, label):
        n = 6
        if abs(x1 - x0) > abs(y1 - y0):
            xs = np.linspace(x0, x1, 2 * n + 1)
            ys = np.array([y0 + ((-1) ** i) * 0.22 for i in range(len(xs))])
            ys[0] = ys[-1] = y0
            ax.plot(xs, ys, color="#a8332c", linewidth=2.2, zorder=2)
            ax.text((x0 + x1) / 2, y0 + 0.5, label, ha="center", fontsize=10.5, fontweight="bold", color="#a8332c")
        else:
            ys = np.linspace(y0, y1, 2 * n + 1)
            xs = np.array([x0 + ((-1) ** i) * 0.22 for i in range(len(ys))])
            xs[0] = xs[-1] = x0
            ax.plot(xs, ys, color="#a8332c", linewidth=2.2, zorder=2)
            ax.text(x0 + 0.55, (y0 + y1) / 2, label, fontsize=10.5, fontweight="bold", color="#a8332c")

    left_x, right_x = 1.2, 10.8
    top_y, bot_y = 5.6, 1.0

    # battery on the left side (vertical)
    batt_y0, batt_y1 = 2.6, 4.0
    wire(left_x, top_y, left_x, batt_y1)
    wire(left_x, batt_y0, left_x, bot_y)
    ax.plot([left_x - 0.35, left_x + 0.35], [batt_y1 - 0.05, batt_y1 - 0.05], color="black", linewidth=3)
    ax.plot([left_x - 0.2, left_x + 0.2], [batt_y1 - 0.35, batt_y1 - 0.35], color="black", linewidth=1.6)
    ax.plot([left_x - 0.35, left_x + 0.35], [batt_y0 + 0.35, batt_y0 + 0.35], color="black", linewidth=1.6)
    ax.plot([left_x - 0.2, left_x + 0.2], [batt_y0 + 0.05, batt_y0 + 0.05], color="black", linewidth=3)
    ax.text(left_x - 0.9, (batt_y0 + batt_y1) / 2, "V", fontsize=12, fontweight="bold")

    node_a_x = 3.0   # start of parallel section
    node_b_x = 5.6   # end of parallel section, start of R3
    node_c_x = right_x

    wire(left_x, top_y, node_a_x, top_y)
    wire(node_a_x, top_y, node_a_x, bot_y)  # vertical bus down to the parallel branches

    # Parallel branch 1: R1 (6 ohm), upper
    branch1_y = 4.6
    wire(node_a_x, branch1_y, node_a_x + 0.6, branch1_y)
    resistor(node_a_x + 0.6, branch1_y, node_a_x + 2.0, branch1_y, "R1 = 6 Ω")
    wire(node_a_x + 2.0, branch1_y, node_b_x, branch1_y)

    # Parallel branch 2: R2 (3 ohm), lower
    branch2_y = 2.0
    wire(node_a_x, branch2_y, node_a_x + 0.6, branch2_y)
    resistor(node_a_x + 0.6, branch2_y, node_a_x + 2.0, branch2_y, "R2 = 3 Ω")
    wire(node_a_x + 2.0, branch2_y, node_b_x, branch2_y)

    # vertical connectors joining branches at node_a and node_b
    wire(node_a_x, branch1_y, node_a_x, branch2_y)
    wire(node_b_x, branch1_y, node_b_x, branch2_y)
    ax.plot(node_a_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_a_x, branch2_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch2_y, "o", color="black", markersize=5, zorder=4)

    # node_b connects up to the top rail, then R3 in series, then to the right rail
    wire(node_b_x, branch1_y, node_b_x, top_y)
    wire(node_b_x, top_y, node_b_x + 0.6, top_y)
    resistor(node_b_x + 0.6, top_y, node_b_x + 2.2, top_y, "R3 = 4 Ω")
    wire(node_b_x + 2.2, top_y, node_c_x, top_y)

    wire(node_c_x, top_y, node_c_x, bot_y)
    wire(left_x, bot_y, node_c_x, bot_y)

    ax.plot(left_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(left_x, bot_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, bot_y, "o", color="black", markersize=5, zorder=4)

    ax.text(6, 0.3,
            "R1 ∥ R2 = 2 Ω, then + R3 (series) = 6 Ω total",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_circuit_r1r2_parallel_r3_series_v3.png")


# ---------------------------------------------------------------
# Q162: concave mirror, object placed exactly at the center of
# curvature C. Real, inverted, same-size image formed at C.
# Correct bulge-toward-object sign convention: x(y) = -k*y**2.
# ---------------------------------------------------------------
def concave_mirror_object_at_c():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-4, 4)
    ax.axis("off")
    ax.set_title("Concave Mirror: Object at the Center of Curvature (C)", fontsize=14, fontweight="bold")

    mirror_x = 6.0
    f = 2.0      # focal length
    R = 2 * f    # radius of curvature = 4.0
    C_x = mirror_x - R
    F_x = mirror_x - f

    # principal axis
    ax.plot([-1, 11], [0, 0], color="gray", linewidth=1.0, linestyle="--", zorder=1)

    # mirror surface: concave, bulging TOWARD the object (to the left)
    yy = np.linspace(-3.2, 3.2, 200)
    k = 0.06
    xx = mirror_x - k * yy ** 2   # negative coefficient -> bulges toward the object (correct concave convention)
    ax.plot(xx, yy, color="#1a1a1a", linewidth=3, zorder=3)
    # hatching on the back (convex/silvered) side
    for i in range(0, len(yy), 12):
        ax.plot([xx[i], xx[i] + 0.35], [yy[i], yy[i]], color="#1a1a1a", linewidth=0.8, zorder=2)

    # mark C and F
    ax.plot(C_x, 0, "o", color="#c0392b", markersize=6, zorder=5)
    ax.text(C_x, -0.4, "C", ha="center", fontsize=11, fontweight="bold", color="#c0392b")
    ax.plot(F_x, 0, "o", color="#1a5276", markersize=6, zorder=5)
    ax.text(F_x, -0.4, "F", ha="center", fontsize=11, fontweight="bold", color="#1a5276")
    ax.text(mirror_x, -0.4, "P", ha="center", fontsize=10, color="#333")

    # object: upright arrow at C
    obj_h = 1.6
    obj_x = C_x
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.6))
    ax.text(obj_x - 0.4, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=10, ha="center")

    # image: inverted arrow, also at C (real image forms back at C when object is at C)
    img_h = -1.6
    img_x = C_x
    ax.annotate("", xy=(img_x + 0.15, img_h), xytext=(img_x + 0.15, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.2, linestyle="--"))
    ax.text(img_x + 0.55, img_h - 0.3, "Image\n(real, inverted,\nsame size)", color="#a8332c", fontsize=9, ha="center")

    # ray 1: parallel to axis from object tip -> reflects through F
    ax.plot([obj_x, mirror_x - k * obj_h ** 2], [obj_h, obj_h], color="#333", linewidth=1.4, zorder=4)
    mirror_hit_x = mirror_x - k * obj_h ** 2
    dx, dy = mirror_hit_x - F_x, 0 - 0
    # extend the reflected ray from the mirror-hit point through F and onward to the image tip
    ax.plot([mirror_hit_x, img_x + 0.15], [obj_h, img_h], color="#333", linewidth=1.4, zorder=4)

    # ray 2: through C, reflects straight back on itself
    ax.plot([obj_x, mirror_x], [obj_h, 0], color="#666", linewidth=1.2, linestyle=":", zorder=4)
    ax.plot([mirror_x, img_x + 0.15], [0, img_h], color="#666", linewidth=1.2, linestyle=":", zorder=4)

    ax.text(5, -3.6,
            "Object at C → real, inverted image of the SAME size, also formed at C.",
            ha="center", fontsize=10, style="italic", color="#333")

    save(fig, "q_concave_mirror_object_at_c.png")


if __name__ == "__main__":
    membrane_crosssection()
    heart_tricuspid_valve()
    energy_profile_exothermic()
    circuit_r1r2_parallel_r3_series()
    concave_mirror_object_at_c()

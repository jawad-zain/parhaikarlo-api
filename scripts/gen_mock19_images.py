"""Generate the 5 diagram images referenced by mdcat_mock_19.py's
image-based questions:
  Q12  Biology  - chloroplast cross-section labeled P/Q/R/S:
                  P = outer membrane, Q = granum (stack of thylakoids),
                  R = stroma, S = inner membrane.
  Q65  Biology  - heart cross-section labeled 1-4: 1 = right atrium,
                  2 = right ventricle, 3 = left atrium, 4 = aorta
                  (arising from the left ventricle).
  Q124 Chemistry - solubility-vs-temperature curve for a solid solute
                  (solubility rises steadily with temperature).
  Q154 Physics  - R1 (4 ohm) and R2 (4 ohm) in PARALLEL (-> 2 ohm),
                  that combination in SERIES with R3 (2 ohm) ->
                  total = 2 + 2 = 4 ohm. No dangling components.
  Q162 Physics  - concave mirror, object placed BETWEEN F and C:
                  real, inverted, magnified image formed beyond C on
                  the same side as the object, computed via the real
                  mirror formula 1/v = 1/f - 1/u (not eyeballed).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle, Wedge
from matplotlib.lines import Line2D

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: chloroplast cross-section, labeled P/Q/R/S.
# P = outer membrane, Q = granum (stack of thylakoids), R = stroma,
# S = inner membrane.
# ---------------------------------------------------------------
def chloroplast_crosssection():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Chloroplast Cross-Section", fontsize=15, fontweight="bold")

    cx, cy = 6.5, 4.3
    outer_w, outer_h = 10.8, 5.6

    # P: outer membrane (smooth outer boundary)
    outer = Ellipse((cx, cy), outer_w, outer_h, facecolor="#c9e8b0", edgecolor="#2c5d1f",
                     linewidth=3.0, zorder=1)
    ax.add_patch(outer)

    # thin gap between outer and inner membrane
    inter = Ellipse((cx, cy), outer_w - 0.55, outer_h - 0.55, facecolor="#e6f5db",
                     edgecolor="none", zorder=2)
    ax.add_patch(inter)

    # S: inner membrane boundary + R: stroma fill inside it
    matrix_w, matrix_h = outer_w - 1.3, outer_h - 1.3
    stroma = Ellipse((cx, cy), matrix_w, matrix_h, facecolor="#a9d18e", edgecolor="none", zorder=3)
    ax.add_patch(stroma)
    inner_boundary = Ellipse((cx, cy), matrix_w + 0.05, matrix_h + 0.05, facecolor="none",
                              edgecolor="#2c5d1f", linewidth=2.2, zorder=3.5)
    ax.add_patch(inner_boundary)

    # Q: grana -- stacks of thylakoid discs scattered through the stroma
    rng = np.random.default_rng(11)
    grana_centers = []
    n_grana = 5
    gx_positions = np.linspace(cx - matrix_w / 2 + 1.3, cx + matrix_w / 2 - 1.3, n_grana)
    for i, gx in enumerate(gx_positions):
        gy = cy + (0.9 if i % 2 == 0 else -0.9) + rng.uniform(-0.3, 0.3)
        grana_centers.append((gx, gy))
        n_discs = 5
        disc_w, disc_h = 0.85, 0.16
        for d in range(n_discs):
            dy = gy + (d - n_discs / 2) * (disc_h + 0.05)
            ax.add_patch(Ellipse((gx, dy), disc_w, disc_h, facecolor="#2c5d1f",
                                  edgecolor="#173a12", linewidth=0.8, zorder=4))
        # thin membrane connecting adjacent grana (stroma lamellae)
        if i > 0:
            px, py = grana_centers[i - 1]
            ax.plot([px + disc_w / 2, gx - disc_w / 2], [py, gy], color="#2c5d1f",
                     linewidth=1.2, zorder=3.8)

    def label(letter, xy, xytext):
        ax.annotate(letter, xy=xy, xytext=xytext, fontsize=15, fontweight="bold", ha="center",
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6),
                    arrowprops=dict(arrowstyle="-", color="black"))

    # P points to the outer membrane edge
    label("P", (cx - outer_w / 2, cy), (cx - outer_w / 2 - 1.4, cy + 2.0))
    # Q points to one of the grana stacks
    gx0, gy0 = grana_centers[1]
    label("Q", (gx0, gy0 + 0.5), (gx0 - 0.4, cy + 3.3))
    # R points into the stroma fill (away from any granum)
    label("R", (cx + 0.2, cy - 1.6), (cx + 3.3, cy - 2.8))
    # S points to the inner membrane boundary
    label("S", (cx, cy - matrix_h / 2), (cx - 2.2, cy - 3.4))

    ax.text(6.5, 0.3,
            "P = outer membrane | Q = granum (thylakoids) | R = stroma | S = inner membrane",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_chloroplast_crosssection_diagram.png")


# ---------------------------------------------------------------
# Q65: heart cross-section labeled 1-4. 1 = right atrium,
# 2 = right ventricle, 3 = left atrium, 4 = aorta.
# ---------------------------------------------------------------
def heart_crosssection_aorta():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Heart Cross-Section (anterior view)", fontsize=15, fontweight="bold")

    outline = Ellipse((5, 4.7), 8.6, 8.0, facecolor="#f7d6d6", edgecolor="#7a1f1f", linewidth=2.5, zorder=0)
    ax.add_patch(outline)

    ax.plot([5, 5], [1.0, 8.2], color="#7a1f1f", linewidth=2.2, zorder=1)

    # Right atrium (viewer's LEFT, upper) -- deoxygenated blood, lighter blue -- structure 1
    ra = Ellipse((3.0, 6.7), 3.4, 2.6, facecolor="#a9c9e8", edgecolor="#2c5d8a", linewidth=2, zorder=2)
    ax.add_patch(ra)
    ax.text(3.0, 6.7, "Right\nAtrium", ha="center", va="center", fontsize=9)

    # Right ventricle (viewer's LEFT, lower) -- structure 2
    rv = Ellipse((3.2, 2.8), 4.0, 3.4, facecolor="#7fa8d1", edgecolor="#2c5d8a", linewidth=2, zorder=2)
    ax.add_patch(rv)
    ax.text(3.2, 2.4, "Right\nVentricle", ha="center", va="center", fontsize=9)

    # Left atrium (viewer's RIGHT, upper) -- oxygenated, red -- structure 3
    la = Ellipse((7.0, 6.7), 3.4, 2.6, facecolor="#e8a9a9", edgecolor="#7a1f1f", linewidth=2, zorder=2)
    ax.add_patch(la)
    ax.text(7.0, 6.7, "Left\nAtrium", ha="center", va="center", fontsize=9)

    # Left ventricle (viewer's RIGHT, lower) -- thicker wall
    lv = Ellipse((6.9, 2.8), 3.7, 3.8, facecolor="#d16a6a", edgecolor="#7a1f1f", linewidth=3, zorder=2)
    ax.add_patch(lv)
    ax.text(6.9, 2.4, "Left\nVentricle", ha="center", va="center", fontsize=9, color="white")

    # Aorta: the large artery arising from the left ventricle, arching up and over -- structure 4
    aorta_xs = [6.4, 6.2, 5.7, 5.2, 5.0, 5.3]
    aorta_ys = [4.6, 7.6, 8.9, 8.9, 7.6, 6.0]
    ax.plot(aorta_xs, aorta_ys, color="#8a1a1a", linewidth=9, solid_capstyle="round", zorder=1.5)
    ax.plot(aorta_xs, aorta_ys, color="#c96a6a", linewidth=5, solid_capstyle="round", zorder=1.6)

    def numbered_marker(x, y, num):
        ax.add_patch(Circle((x, y), 0.32, facecolor="white", edgecolor="black", linewidth=2, zorder=6))
        ax.text(x, y, str(num), ha="center", va="center", fontsize=12, fontweight="bold", zorder=7)

    def leader(x0, y0, x1, y1):
        ax.plot([x0, x1], [y0, y1], color="black", linewidth=1.2, zorder=5)

    # label 1: right atrium
    leader(3.0, 7.5, 1.4, 9.2)
    numbered_marker(1.4, 9.2, 1)

    # label 2: right ventricle
    leader(2.0, 2.0, 0.9, 0.7)
    numbered_marker(0.9, 0.7, 2)

    # label 3: left atrium
    leader(7.6, 7.4, 8.7, 9.0)
    numbered_marker(8.7, 9.0, 3)

    # label 4: aorta (arch, top center-left)
    leader(5.5, 8.9, 5.5, 9.6)
    numbered_marker(5.5, 9.6, 4)

    ax.text(5, 0.3,
            "1 = right atrium | 2 = right ventricle | 3 = left atrium | 4 = aorta (from left ventricle)",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q_heart_crosssection_aorta_diagram.png")


# ---------------------------------------------------------------
# Q124: solubility curve of a solid solute -- solubility rises
# steadily as temperature increases.
# ---------------------------------------------------------------
def solubility_curve():
    T = np.linspace(0, 100, 200)
    S = 12 + 0.75 * T + 0.010 * T ** 1.55

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, S, color="#a83232", linewidth=2.8)
    ax.fill_between(T, 0, S, color="#f3d0d0", alpha=0.4)

    ax.set_xlabel("Temperature (°C)", fontsize=12)
    ax.set_ylabel("Solubility (g per 100 mL water)", fontsize=12)
    ax.set_title("Solubility Curve of a Solid Solute", fontsize=14, fontweight="bold")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, max(S) * 1.1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.25)

    t_hi, t_lo = 80, 30
    s_hi = 12 + 0.75 * t_hi + 0.010 * t_hi ** 1.55
    s_lo = 12 + 0.75 * t_lo + 0.010 * t_lo ** 1.55

    for t0, s0 in ((t_hi, s_hi), (t_lo, s_lo)):
        ax.plot([t0, t0], [0, s0], color="gray", linestyle=":", linewidth=1)
        ax.plot([0, t0], [s0, s0], color="gray", linestyle=":", linewidth=1)
        ax.plot(t0, s0, "o", color="#1a5276", markersize=6)

    # dashed horizontal line at the saturated-at-high-temperature concentration,
    # showing it now sits ABOVE the curve at the lower temperature (excess solute)
    ax.plot([0, t_hi], [s_hi, s_hi], color="#c0392b", linestyle="--", linewidth=1.4)
    ax.annotate("same concentration held\nwhile cooling -> now above\nthe curve at the lower T\n(supersaturated, excess precipitates)",
                xy=(t_lo, s_hi), xytext=(38, max(S) * 0.92),
                fontsize=9, color="#c0392b",
                arrowprops=dict(arrowstyle="->", color="#c0392b"))

    ax.text(50, -max(S) * 0.16,
            "Solubility increases steadily with temperature (cooling a saturated solution\n"
            "at constant concentration pushes it above the curve -> excess solute precipitates).",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q_solubility_curve_saturation_diagram.png")


# ---------------------------------------------------------------
# Q154: R1 (4 ohm) and R2 (4 ohm) in PARALLEL (-> 2 ohm), that
# combination in SERIES with R3 (2 ohm) -> total = 4 ohm.
# ---------------------------------------------------------------
def circuit_parallel_then_series():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Circuit: R1 ∥ R2, in series with R3", fontsize=14, fontweight="bold")

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

    node_a_x = 3.0   # start of parallel section (R1 ∥ R2)
    node_b_x = 6.4   # end of parallel section, feeds into R3
    node_c_x = right_x

    wire(left_x, top_y, node_a_x, top_y)
    wire(node_a_x, top_y, node_a_x, bot_y)  # vertical bus down to the parallel branches

    # Parallel branch 1: R1 (4 ohm), upper
    branch1_y = 4.6
    wire(node_a_x, branch1_y, node_a_x + 0.6, branch1_y)
    resistor(node_a_x + 0.6, branch1_y, node_a_x + 2.4, branch1_y, "R1 = 4 Ω")
    wire(node_a_x + 2.4, branch1_y, node_b_x, branch1_y)

    # Parallel branch 2: R2 (4 ohm), lower
    branch2_y = 2.0
    wire(node_a_x, branch2_y, node_a_x + 0.6, branch2_y)
    resistor(node_a_x + 0.6, branch2_y, node_a_x + 2.4, branch2_y, "R2 = 4 Ω")
    wire(node_a_x + 2.4, branch2_y, node_b_x, branch2_y)

    # vertical connectors joining branches at node_a and node_b
    wire(node_a_x, branch1_y, node_a_x, branch2_y)
    wire(node_b_x, branch1_y, node_b_x, branch2_y)
    ax.plot(node_a_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_a_x, branch2_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch2_y, "o", color="black", markersize=5, zorder=4)

    # node_b merges to a single top-rail line, then R3 in series before the right rail
    wire(node_b_x, branch1_y, node_b_x, top_y)
    wire(node_b_x, top_y, node_b_x + 0.6, top_y)
    resistor(node_b_x + 0.6, top_y, node_b_x + 2.4, top_y, "R3 = 2 Ω")
    wire(node_b_x + 2.4, top_y, node_c_x, top_y)

    wire(node_c_x, top_y, node_c_x, bot_y)
    wire(left_x, bot_y, node_c_x, bot_y)

    ax.plot(left_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(left_x, bot_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, bot_y, "o", color="black", markersize=5, zorder=4)

    ax.text(6, 0.3,
            "R1 ∥ R2 = (4×4)/(4+4) = 2 Ω, + R3 (2 Ω) in series = 4 Ω total",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_circuit_parallel_then_series.png")


# ---------------------------------------------------------------
# Q162: concave mirror, object placed BETWEEN F and C. Real,
# inverted, magnified image forms beyond C on the same side as the
# object. Computed via the real mirror formula 1/v = 1/f - 1/u.
# ---------------------------------------------------------------
def concave_mirror_object_between_f_and_c():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(-8, 8)
    ax.set_ylim(-5, 5)
    ax.axis("off")
    ax.set_title("Concave Mirror: Object Between F and C", fontsize=14, fontweight="bold")

    mirror_x = 4.5
    f = 2.0        # focal length
    R = 2 * f      # radius of curvature = 4.0
    C_x = mirror_x - R    # C at 0.5
    F_x = mirror_x - f    # F at 2.5

    u = 3.0        # object distance from mirror, between F (2.0) and C (4.0)
    obj_x = mirror_x - u

    # real mirror formula: 1/v = 1/f - 1/u
    v = 1 / (1 / f - 1 / u)     # = 1/(1/2 - 1/3) = 6.0
    img_x = mirror_x - v
    m = -v / u                  # magnification, negative -> inverted
    obj_h = 1.4
    img_h = m * obj_h

    # principal axis
    ax.plot([-8, 8], [0, 0], color="gray", linewidth=1.0, linestyle="--", zorder=1)

    # mirror surface: concave, bulging TOWARD the object (to the right)
    yy = np.linspace(-3.4, 3.4, 200)
    k = 0.06
    xx = mirror_x - k * yy ** 2   # negative coefficient -> bulges toward the object (correct concave convention)
    ax.plot(xx, yy, color="#1a1a1a", linewidth=3, zorder=3)
    for i in range(0, len(yy), 12):
        ax.plot([xx[i], xx[i] + 0.35], [yy[i], yy[i]], color="#1a1a1a", linewidth=0.8, zorder=2)

    # mark C and F
    ax.plot(C_x, 0, "o", color="#c0392b", markersize=6, zorder=5)
    ax.text(C_x, -0.4, "C", ha="center", fontsize=11, fontweight="bold", color="#c0392b")
    ax.plot(F_x, 0, "o", color="#1a5276", markersize=6, zorder=5)
    ax.text(F_x, -0.4, "F", ha="center", fontsize=11, fontweight="bold", color="#1a5276")
    ax.text(mirror_x, -0.4, "P", ha="center", fontsize=10, color="#333")

    # object: upright arrow, between F and C
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.6))
    ax.text(obj_x, obj_h + 0.3, "Object", color="#1a7a3a", fontsize=10, ha="center")

    # image: inverted, magnified arrow, formed beyond C on the same side as the object
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.4, linestyle="--"))
    ax.text(img_x, img_h - 0.4, "Image", color="#a8332c", fontsize=10, ha="center")

    # ray 1: parallel to axis from object tip -> reflects through F -> onward to image tip
    mirror_hit_x = mirror_x - k * obj_h ** 2
    ax.plot([obj_x, mirror_hit_x], [obj_h, obj_h], color="#333", linewidth=1.4, zorder=4)
    ax.plot([mirror_hit_x, img_x], [obj_h, img_h], color="#333", linewidth=1.4, zorder=4)

    # ray 2: through C, reflects straight back on itself, extended out to the image tip
    mirror_hit2_x = mirror_x - k * 0 ** 2
    # ray from object tip through C, hitting the mirror
    slope = (0 - obj_h) / (C_x - obj_x)
    hit_y2 = obj_h + slope * (mirror_x - obj_x)
    ax.plot([obj_x, mirror_x], [obj_h, hit_y2], color="#666", linewidth=1.2, linestyle=":", zorder=4)
    ax.plot([mirror_x, img_x], [hit_y2, img_h], color="#666", linewidth=1.2, linestyle=":", zorder=4)

    ax.text(0, -4.4,
            f"u = {u:.1f} (between F and C), v = {v:.1f} (beyond C) -> real, inverted, magnified image",
            ha="center", fontsize=10, style="italic", color="#333")

    save(fig, "q_concave_mirror_object_between_f_and_c.png")


if __name__ == "__main__":
    chloroplast_crosssection()
    heart_crosssection_aorta()
    solubility_curve()
    circuit_parallel_then_series()
    concave_mirror_object_between_f_and_c()

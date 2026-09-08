"""Generate the 5 diagram images referenced by mdcat_mock_18.py's
image-based questions:
  Q12  Biology  - mitochondrion cross-section labeled W/X/Y/Z:
                  W = outer membrane, X = inner membrane (folded into
                  cristae), Y = matrix, Z = intermembrane space.
  Q72  Biology  - nephron diagram labeled 1-4: 1 = glomerulus (tuft of
                  capillaries), 2 = Bowman's capsule, 3 = proximal
                  convoluted tubule, 4 = loop of Henle.
  Q111 Chemistry - acid-base titration curve (pH vs volume of base
                  added), equivalence point marked at the midpoint of
                  the steep rise.
  Q154 Physics  - R1 (3 ohm) and R2 (3 ohm) in SERIES (-> 6 ohm), that
                  combination in PARALLEL with R3 (6 ohm) ->
                  total = (6*6)/(6+6) = 3 ohm. No dangling components.
  Q162 Physics  - convex lens, object placed beyond 2F: real, inverted,
                  diminished image formed between F and 2F on the far
                  side, computed via the real thin-lens formula
                  1/v = 1/f - 1/u (not eyeballed).
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
# Q12: mitochondrion cross-section, labeled W/X/Y/Z.
# W = outer membrane, X = inner membrane (cristae), Y = matrix,
# Z = intermembrane space.
# ---------------------------------------------------------------
def mitochondrion_crosssection():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Mitochondrion Cross-Section", fontsize=15, fontweight="bold")

    cx, cy = 6.5, 4.3
    outer_w, outer_h = 10.8, 5.6

    # W: outer membrane (smooth outer boundary)
    outer = Ellipse((cx, cy), outer_w, outer_h, facecolor="#f3d9c4", edgecolor="#8a4b1f",
                     linewidth=3.0, zorder=1)
    ax.add_patch(outer)

    # Z: intermembrane space -- thin gap between outer and inner membrane
    inter = Ellipse((cx, cy), outer_w - 0.55, outer_h - 0.55, facecolor="#fbeee2",
                     edgecolor="none", zorder=2)
    ax.add_patch(inter)

    # Y: matrix -- the interior fill
    matrix_w, matrix_h = outer_w - 1.3, outer_h - 1.3
    matrix = Ellipse((cx, cy), matrix_w, matrix_h, facecolor="#e8b98f", edgecolor="none", zorder=3)
    ax.add_patch(matrix)

    # X: inner membrane folded into cristae -- draw as finger-like folds
    # projecting inward from the inner-membrane boundary, alternating top/bottom.
    n_cristae = 5
    fold_xs = np.linspace(cx - matrix_w / 2 + 1.1, cx + matrix_w / 2 - 1.1, n_cristae)
    for i, fx in enumerate(fold_xs):
        depth = matrix_h * 0.62
        top = (i % 2 == 0)
        if top:
            y0 = cy + matrix_h / 2 - 0.15
            y1 = y0 - depth
        else:
            y0 = cy - matrix_h / 2 + 0.15
            y1 = y0 + depth
        width = 0.9
        xs = [fx - width / 2, fx, fx + width / 2]
        ys = [y0, y1, y0]
        ax.plot(xs, ys, color="#8a4b1f", linewidth=4.5, solid_capstyle="round", zorder=4)
        ax.plot(xs, ys, color="#c97a3a", linewidth=2.6, solid_capstyle="round", zorder=5)

    # boundary of inner membrane itself (the envelope the cristae fold from)
    inner_boundary = Ellipse((cx, cy), matrix_w + 0.05, matrix_h + 0.05, facecolor="none",
                              edgecolor="#8a4b1f", linewidth=2.2, zorder=3.5)
    ax.add_patch(inner_boundary)

    def label(letter, xy, xytext):
        ax.annotate(letter, xy=xy, xytext=xytext, fontsize=15, fontweight="bold", ha="center",
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6),
                    arrowprops=dict(arrowstyle="-", color="black"))

    # W points to the outer membrane edge
    label("W", (cx - outer_w / 2, cy), (cx - outer_w / 2 - 1.4, cy + 2.0))
    # X points to a crista fold
    label("X", (fold_xs[1], cy + matrix_h / 2 - 0.15 - (matrix_h * 0.62) * 0.6),
          (fold_xs[1] + 0.3, cy - 3.3))
    # Y points into the matrix fill (away from any crista)
    label("Y", (cx + 1.8, cy - 0.3), (cx + 3.3, cy + 2.6))
    # Z points to the thin gap between outer and inner membrane
    label("Z", (cx, cy + outer_h / 2 - 0.3), (cx - 2.0, cy + 3.4))

    ax.text(6.5, 0.4,
            "W = outer membrane | X = inner membrane (cristae) | Y = matrix | Z = intermembrane space",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_mitochondrion_crosssection_diagram.png")


# ---------------------------------------------------------------
# Q72: nephron diagram, labeled 1-4. 1 = glomerulus, 2 = Bowman's
# capsule, 3 = proximal convoluted tubule, 4 = loop of Henle.
# ---------------------------------------------------------------
def nephron_glomerulus():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Nephron Diagram", fontsize=15, fontweight="bold")

    # Bowman's capsule: cup-shaped structure (structure 2)
    capsule_center = (3.0, 7.5)
    capsule = Wedge(capsule_center, 1.3, 200, 340, width=0.5, facecolor="#d8c4e8",
                     edgecolor="#5c3a7a", linewidth=2.0, zorder=2)
    ax.add_patch(capsule)

    # Glomerulus: tuft of capillaries sitting inside the capsule cup (structure 1)
    rng = np.random.default_rng(7)
    glom_center = (3.0, 7.35)
    for _ in range(14):
        ang = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.15, 0.65)
        x0 = glom_center[0] + r * np.cos(ang)
        y0 = glom_center[1] + r * np.sin(ang) * 0.6
        ang2 = ang + rng.uniform(-1.0, 1.0)
        r2 = rng.uniform(0.15, 0.65)
        x1 = glom_center[0] + r2 * np.cos(ang2)
        y1 = glom_center[1] + r2 * np.sin(ang2) * 0.6
        ax.plot([x0, x1], [y0, y1], color="#c0392b", linewidth=2.2, zorder=3, solid_capstyle="round")

    # afferent/efferent arterioles feeding the glomerulus
    ax.annotate("", xy=(glom_center[0] - 0.7, glom_center[1] + 0.5), xytext=(1.0, 9.2),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.2))
    ax.annotate("", xy=(1.0, 6.0), xytext=(glom_center[0] - 0.7, glom_center[1] - 0.3),
                arrowprops=dict(arrowstyle="-|>", color="#2c5d8a", linewidth=2.2))

    # Proximal convoluted tubule: coiled tube leading out of the capsule (structure 3)
    pct_center = (5.2, 7.0)
    theta = np.linspace(0, 4.5 * np.pi, 300)
    r_spiral = 0.05 + 0.13 * theta / theta.max()
    px = pct_center[0] + r_spiral * np.cos(theta) * 3.2
    py = pct_center[1] + r_spiral * np.sin(theta) * 1.6
    ax.plot(px, py, color="#c97a3a", linewidth=2.2, zorder=2)

    # Loop of Henle: hairpin loop descending and ascending (structure 4)
    loop_top_y = 5.6
    loop_bottom_y = 1.3
    lx0, lx1 = 5.6, 6.6
    ax.plot([lx0, lx0], [loop_top_y, loop_bottom_y], color="#2c8a5d", linewidth=3.0, zorder=2)
    ax.plot([lx1, lx1], [loop_bottom_y, loop_top_y], color="#2c8a5d", linewidth=3.0, zorder=2)
    theta2 = np.linspace(np.pi, 2 * np.pi, 50)
    hx = (lx0 + lx1) / 2 + (lx1 - lx0) / 2 * np.cos(theta2)
    hy = loop_bottom_y - 0.05 + 0.15 * np.sin(theta2 - np.pi)
    ax.plot(hx, hy, color="#2c8a5d", linewidth=3.0, zorder=2)

    # connect PCT -> descending limb, ascending limb -> collecting duct (off to the right)
    ax.plot([px[-1], lx0], [py[-1], loop_top_y], color="#c97a3a", linewidth=2.0, zorder=2)
    ax.plot([lx1, 8.5], [loop_top_y, loop_top_y + 0.5], color="#2c8a5d", linewidth=2.2, zorder=2)
    ax.plot([8.5, 9.2], [loop_top_y + 0.5, 8.5], color="#555", linewidth=2.2, zorder=2)

    def numbered_marker(x, y, num):
        ax.add_patch(Circle((x, y), 0.32, facecolor="white", edgecolor="black", linewidth=2, zorder=6))
        ax.text(x, y, str(num), ha="center", va="center", fontsize=12, fontweight="bold", zorder=7)

    def leader(x0, y0, x1, y1):
        ax.plot([x0, x1], [y0, y1], color="black", linewidth=1.2, zorder=5)

    # label 1: glomerulus
    leader(glom_center[0] + 0.4, glom_center[1] + 0.2, 3.0, 9.5)
    numbered_marker(3.0, 9.5, 1)

    # label 2: Bowman's capsule
    leader(2.0, 6.9, 0.9, 5.8)
    numbered_marker(0.9, 5.8, 2)

    # label 3: proximal convoluted tubule
    leader(5.4, 7.4, 6.5, 9.3)
    numbered_marker(6.5, 9.3, 3)

    # label 4: loop of Henle
    leader(6.1, 3.0, 8.6, 2.5)
    numbered_marker(8.6, 2.5, 4)

    ax.text(6, 0.3,
            "1 = glomerulus | 2 = Bowman's capsule | 3 = proximal convoluted tubule | 4 = loop of Henle",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q_nephron_glomerulus_diagram.png")


# ---------------------------------------------------------------
# Q111: acid-base titration curve. pH vs volume of base added, with
# the equivalence point at the midpoint of the steep pH rise.
# ---------------------------------------------------------------
def titration_curve():
    fig, ax = plt.subplots(figsize=(8.5, 6))

    v = np.linspace(0, 50, 500)
    v_eq = 25.0
    # sigmoid-shaped titration curve: starts acidic (~pH 2), sharp rise
    # around v_eq, levels off basic (~pH 12)
    steepness = 1.3
    pH = 2.0 + 10.0 / (1 + np.exp(-steepness * (v - v_eq) * 0.55))

    ax.plot(v, pH, color="#1a5276", linewidth=3)
    ax.set_xlabel("Volume of base added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_title("Acid-Base Titration Curve", fontsize=14, fontweight="bold")
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)

    # equivalence point marker at v_eq, on the curve
    idx_eq = np.argmin(np.abs(v - v_eq))
    pH_eq = pH[idx_eq]
    ax.plot(v_eq, pH_eq, "o", color="#c0392b", markersize=9, zorder=5)
    ax.annotate("Equivalence point", xy=(v_eq, pH_eq), xytext=(v_eq + 6, pH_eq - 2.5),
                fontsize=10.5, color="#c0392b", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#c0392b"))

    ax.axvline(v_eq, color="gray", linestyle="--", linewidth=1)
    ax.axhline(pH_eq, color="gray", linestyle="--", linewidth=1)

    ax.text(6, 1.0, "Buffer\nregion", ha="center", fontsize=9, style="italic", color="#555")
    ax.text(44, 12.5, "Excess\nbase", ha="center", fontsize=9, style="italic", color="#555")

    ax.text(25, -1.8,
            "Equivalence point: moles of acid = moles of base added (steepest part of the curve)",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_titration_curve_equivalence_point.png")


# ---------------------------------------------------------------
# Q154: R1 (3 ohm) and R2 (3 ohm) in SERIES (-> 6 ohm), that
# combination in PARALLEL with R3 (6 ohm) -> total = 3 ohm.
# ---------------------------------------------------------------
def circuit_series_then_parallel():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Circuit: R1 + R2 (series), in parallel with R3", fontsize=14, fontweight="bold")

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
    node_b_x = 7.6   # end of parallel section
    node_c_x = right_x

    wire(left_x, top_y, node_a_x, top_y)
    wire(node_a_x, top_y, node_a_x, bot_y)  # vertical bus down to the parallel branches

    # Parallel branch 1: R1 (3 ohm) then R2 (3 ohm) in series, upper
    branch1_y = 4.6
    wire(node_a_x, branch1_y, node_a_x + 0.6, branch1_y)
    resistor(node_a_x + 0.6, branch1_y, node_a_x + 2.0, branch1_y, "R1 = 3 Ω")
    wire(node_a_x + 2.0, branch1_y, node_a_x + 2.5, branch1_y)
    resistor(node_a_x + 2.5, branch1_y, node_a_x + 3.9, branch1_y, "R2 = 3 Ω")
    wire(node_a_x + 3.9, branch1_y, node_b_x, branch1_y)

    # Parallel branch 2: R3 (6 ohm), lower
    branch2_y = 2.0
    wire(node_a_x, branch2_y, node_a_x + 0.6, branch2_y)
    resistor(node_a_x + 0.6, branch2_y, node_a_x + 2.0, branch2_y, "R3 = 6 Ω")
    wire(node_a_x + 2.0, branch2_y, node_b_x, branch2_y)

    # vertical connectors joining branches at node_a and node_b
    wire(node_a_x, branch1_y, node_a_x, branch2_y)
    wire(node_b_x, branch1_y, node_b_x, branch2_y)
    ax.plot(node_a_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_a_x, branch2_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch1_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_b_x, branch2_y, "o", color="black", markersize=5, zorder=4)

    # node_b connects up to the top rail then across to the right rail
    wire(node_b_x, branch1_y, node_b_x, top_y)
    wire(node_b_x, top_y, node_c_x, top_y)

    wire(node_c_x, top_y, node_c_x, bot_y)
    wire(left_x, bot_y, node_c_x, bot_y)

    ax.plot(left_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(left_x, bot_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_c_x, bot_y, "o", color="black", markersize=5, zorder=4)

    ax.text(6, 0.3,
            "R1 + R2 (series) = 6 Ω, ∥ R3 (6 Ω) = (6×6)/(6+6) = 3 Ω total",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_circuit_series_then_parallel_v2.png")


# ---------------------------------------------------------------
# Q162: convex lens, object placed beyond 2F. Real, inverted,
# diminished image formed between F and 2F on the far side.
# Computed via the real thin-lens formula 1/v = 1/f - 1/u.
# ---------------------------------------------------------------
def convex_lens_object_beyond_2f():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1, 15)
    ax.set_ylim(-4, 4)
    ax.axis("off")
    ax.set_title("Convex Lens: Object Beyond 2F", fontsize=14, fontweight="bold")

    lens_x = 7.0
    f = 2.0          # focal length
    obj_x = 1.0      # object position (beyond 2F, i.e. more than 2f = 4.0 from lens)
    u = lens_x - obj_x   # object distance = 6.0 (> 2f)

    # thin-lens formula: 1/v = 1/f - 1/u  (using the convention where
    # object distance u and image distance v are both measured as
    # positive magnitudes on their respective sides of the lens)
    v = 1 / (1 / f - 1 / u)   # = 1/(1/2 - 1/6) = 1/(1/3) = 3.0
    img_x = lens_x + v

    obj_h = 1.6
    # magnification m = -v/u (real image on real convex lens with
    # object beyond 2f is inverted and diminished since v < u)
    m = -v / u
    img_h = m * obj_h

    # principal axis
    ax.plot([-1, 15], [0, 0], color="gray", linewidth=1.0, linestyle="--", zorder=1)

    # lens: biconvex, drawn as a vertical double-arrow lens symbol
    ax.plot([lens_x, lens_x], [-3.0, 3.0], color="#1a5276", linewidth=3, zorder=3)
    ax.annotate("", xy=(lens_x, 3.0), xytext=(lens_x - 0.35, 2.6),
                arrowprops=dict(arrowstyle="-", color="#1a5276", linewidth=3))
    ax.annotate("", xy=(lens_x, 3.0), xytext=(lens_x + 0.35, 2.6),
                arrowprops=dict(arrowstyle="-", color="#1a5276", linewidth=3))
    ax.annotate("", xy=(lens_x, -3.0), xytext=(lens_x - 0.35, -2.6),
                arrowprops=dict(arrowstyle="-", color="#1a5276", linewidth=3))
    ax.annotate("", xy=(lens_x, -3.0), xytext=(lens_x + 0.35, -2.6),
                arrowprops=dict(arrowstyle="-", color="#1a5276", linewidth=3))

    # mark F and 2F on both sides
    for sign, label_prefix in [(-1, "left"), (1, "right")]:
        fx = lens_x + sign * f
        f2x = lens_x + sign * 2 * f
        ax.plot(fx, 0, "o", color="#1a5276", markersize=5, zorder=5)
        ax.text(fx, -0.35, "F", ha="center", fontsize=10, fontweight="bold", color="#1a5276")
        ax.plot(f2x, 0, "o", color="#c0392b", markersize=5, zorder=5)
        ax.text(f2x, -0.35, "2F", ha="center", fontsize=10, fontweight="bold", color="#c0392b")

    # object: upright arrow, beyond 2F on the left
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.6))
    ax.text(obj_x, obj_h + 0.3, "Object", color="#1a7a3a", fontsize=10, ha="center")

    # image: inverted, diminished arrow between F and 2F on the right
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.4, linestyle="--"))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=10, ha="center")

    # ray 1: parallel to axis from object tip -> refracts through F on far side
    far_fx = lens_x + f
    ax.plot([obj_x, lens_x], [obj_h, obj_h], color="#333", linewidth=1.3, zorder=4)
    ax.plot([lens_x, img_x], [obj_h, img_h], color="#333", linewidth=1.3, zorder=4)

    # ray 2: through the optical center, undeviated
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#666", linewidth=1.1, linestyle=":", zorder=4)

    ax.text(6.5, -3.6,
            f"u = {u:.1f} (beyond 2F), v = {v:.1f} (between F and 2F) → real, inverted, diminished image",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_convex_lens_object_beyond_2f.png")


if __name__ == "__main__":
    mitochondrion_crosssection()
    nephron_glomerulus()
    titration_curve()
    circuit_series_then_parallel()
    convex_lens_object_beyond_2f()

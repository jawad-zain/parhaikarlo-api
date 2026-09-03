"""Generate the 5 diagram images referenced by mdcat_mock_16.py's
image-based questions:
  Q12  Biology  - endomembrane system secretory pathway: labeled 1-4
                  (nuclear envelope/rough ER, Golgi apparatus,
                  secretory vesicle, plasma membrane) with arrows
                  showing the correct flow 1 -> 2 -> 3 -> 4.
  Q33  Biology  - autosomal-recessive pedigree chart: two unaffected
                  (carrier, Aa) parents have one affected (aa) child
                  among unaffected/carrier children, trait appears in
                  both sexes and skips generations.
  Q121 Chemistry - solubility-vs-temperature curve for a solid salt:
                  solubility (g/100 mL water) rising with temperature
                  (the typical shape for most ionic solids), correctly
                  labeled axes.
  Q154 Physics  - circuit: R1 (3 ohm) in series with R2 (5 ohom) forms
                  one branch; that branch is in parallel with R3 (8
                  ohm). No dangling components.
  Q162 Physics  - convex lens: parallel rays (parallel to principal
                  axis) refracted by the lens and converging at a
                  single point on the axis -- the principal focus (F).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.lines import Line2D

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: endomembrane secretory pathway. Structures labeled 1-4:
# 1 = nuclear envelope / rough ER, 2 = Golgi apparatus,
# 3 = secretory vesicle, 4 = plasma membrane. Arrows show the correct
# pathway order: 1 -> 2 -> 3 -> 4.
# ---------------------------------------------------------------
def endomembrane_secretory_pathway():
    fig, ax = plt.subplots(figsize=(10.5, 6))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Endomembrane System: Secretory Pathway", fontsize=15, fontweight="bold")

    # 1: nucleus + rough ER (stack of membranes with ribosome dots)
    nuc = Circle((1.9, 3.5), 1.05, facecolor="#cfe0f3", edgecolor="#2c5d8a", linewidth=2.2, zorder=2)
    ax.add_patch(nuc)
    ax.text(1.9, 3.5, "Nucleus", ha="center", va="center", fontsize=8.5)
    rng = np.random.default_rng(6)
    for i in range(4):
        y = 4.7 + i * 0.28
        xs = np.linspace(0.8, 3.2, 40)
        ys = y + 0.08 * np.sin(xs * 3 + i)
        ax.plot(xs, ys, color="#2c5d8a", linewidth=1.6, zorder=2)
        for _ in range(6):
            px = rng.uniform(0.9, 3.1)
            ax.plot(px, y + 0.08 * np.sin(px * 3 + i) + 0.05, ".", color="#333", markersize=3, zorder=3)
    ax.text(1.9, 6.2, "1", fontsize=16, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(1.9, 0.55, "Nuclear envelope /\nRough ER", ha="center", fontsize=9)

    # 2: Golgi apparatus (stacked curved cisternae)
    gx = 5.3
    for i in range(5):
        cy = 3.5 + (i - 2) * 0.42
        arc = np.linspace(-1.0, 1.0, 60)
        ys = cy + 0.35 * np.sin(arc * 1.6)
        xs = gx + arc * 0.9
        ax.plot(xs, ys, color="#8a4fa0", linewidth=2.0, zorder=2)
    ax.text(gx, 6.2, "2", fontsize=16, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(gx, 0.55, "Golgi apparatus", ha="center", fontsize=9)

    # 3: secretory vesicle (small circle budding from Golgi)
    vx, vy = 7.9, 3.5
    ves = Circle((vx, vy), 0.5, facecolor="#f9d97a", edgecolor="#a67c1a", linewidth=2.0, zorder=2)
    ax.add_patch(ves)
    ax.text(vx, 6.2, "3", fontsize=16, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text(vx, 0.55, "Secretory vesicle", ha="center", fontsize=9)

    # 4: plasma membrane (curved line at right edge with protein released outside)
    mx0, mx1 = 10.4, 12.4
    ys_mem = np.linspace(1.6, 5.4, 60)
    xs_mem = mx0 + 0.12 * np.sin((ys_mem - 1.6) * 2.2)
    ax.plot(xs_mem, ys_mem, color="#1a7a3a", linewidth=3.2, zorder=2)
    ax.text((mx0 + mx1) / 2 + 0.3, 6.2, "4", fontsize=16, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.6))
    ax.text((mx0 + mx1) / 2 + 0.3, 0.55, "Plasma membrane", ha="center", fontsize=9)
    ax.plot(12.0, 3.5, "o", color="#c0392b", markersize=8, zorder=4)
    ax.text(12.35, 3.5, "secreted\nprotein", fontsize=7.5, color="#c0392b", va="center")

    # arrows showing flow 1 -> 2 -> 3 -> 4
    def arrow(x0, y0, x1, y1):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color="#1a1a1a", linewidth=2.4))

    arrow(3.3, 3.5, 4.35, 3.5)
    arrow(6.25, 3.5, 7.35, 3.5)
    arrow(8.45, 3.5, 10.3, 3.5)

    save(fig, "q_endomembrane_system_diagram.png")


# ---------------------------------------------------------------
# Q33: autosomal-recessive pedigree. Two unaffected (carrier, Aa)
# parents in generation I have children in generation II: one
# affected (aa, filled), others unaffected/carriers (open). Trait
# appears in both sexes and skips a generation (grandparents
# unaffected non-carriers -> shown simply as founders here as
# carriers themselves per an autosomal recessive pattern).
# ---------------------------------------------------------------
def pedigree_autosomal_recessive():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis("off")
    ax.set_title("Pedigree Chart: Autosomal Recessive Trait", fontsize=15, fontweight="bold")

    def square(x, y, filled, half=False):
        s = 0.55
        rect = Rectangle((x - s / 2, y - s / 2), s, s, facecolor=("#333" if filled else "white"),
                          edgecolor="black", linewidth=1.8, zorder=3)
        ax.add_patch(rect)
        if half:
            ax.add_patch(Rectangle((x - s / 2, y - s / 2), s / 2, s, facecolor="#333",
                                    edgecolor="none", zorder=4))
            ax.add_patch(Rectangle((x - s / 2, y - s / 2), s, s, facecolor="none",
                                    edgecolor="black", linewidth=1.8, zorder=5))

    def circle(x, y, filled, half=False):
        r = 0.3
        c = Circle((x, y), r, facecolor=("#333" if filled else "white"), edgecolor="black",
                    linewidth=1.8, zorder=3)
        ax.add_patch(c)
        if half:
            wedge = Circle((x, y), r, facecolor="none", edgecolor="black", linewidth=1.8, zorder=5)
            ax.add_patch(wedge)
            ax.add_patch(Rectangle((x - r, y - r), r, 2 * r, facecolor="#333", edgecolor="none", zorder=4))

    def line(x0, y0, x1, y1, **kw):
        ax.plot([x0, x1], [y0, y1], color="black", linewidth=1.6, zorder=1, **kw)

    # Generation I: unaffected carrier parents (Aa x Aa)
    y1 = 6.0
    p1x, p2x = 4.0, 6.0
    square(p1x, y1, filled=False)
    circle(p2x, y1, filled=False)
    line(p1x, y1, p2x, y1)
    ax.text(p1x, y1 + 0.55, "Aa\n(unaffected, carrier)", ha="center", fontsize=8)
    ax.text(p2x, y1 + 0.55, "Aa\n(unaffected, carrier)", ha="center", fontsize=8)
    ax.text(0.6, y1, "I", fontsize=13, fontweight="bold")

    # Generation II: 4 children -- 1 affected (aa) daughter, 1 affected
    # (aa) son analog omitted; show classic 1:2:1 sample -- one
    # affected son, two unaffected/carrier children, one affected
    # daughter (both sexes affected, consistent with autosomal
    # inheritance).
    y2 = 3.2
    mid = (p1x + p2x) / 2
    line(mid, y1, mid, y1 - 0.7)
    kids_x = [2.6, 4.2, 5.8, 7.4]
    line(kids_x[0], y2 + 0.7, kids_x[-1], y2 + 0.7)
    line(mid, y1 - 0.7, mid, y2 + 0.7)
    for kx in kids_x:
        line(kx, y2 + 0.7, kx, y2 + 0.35)

    square(kids_x[0], y2, filled=True)     # affected son (aa)
    circle(kids_x[1], y2, filled=False)    # unaffected daughter (AA or Aa)
    square(kids_x[2], y2, filled=False)    # unaffected son
    circle(kids_x[3], y2, filled=True)     # affected daughter (aa)

    labels2 = ["aa\n(affected)", "unaffected", "unaffected", "aa\n(affected)"]
    for kx, lab in zip(kids_x, labels2):
        ax.text(kx, y2 - 0.65, lab, ha="center", fontsize=8)
    ax.text(0.6, y2, "II", fontsize=13, fontweight="bold")

    ax.text(5.5, 1.0,
            "Unaffected parents (both carriers, Aa) -> affected children (aa) of both sexes;\n"
            "consistent with autosomal recessive inheritance (25% of offspring expected affected).",
            ha="center", fontsize=9.5, style="italic", color="#333")

    # legend
    ax.add_patch(Rectangle((8.6, 6.6), 0.35, 0.35, facecolor="white", edgecolor="black", linewidth=1.5))
    ax.text(9.1, 6.78, "unaffected male", fontsize=8, va="center")
    ax.add_patch(Rectangle((8.6, 6.0), 0.35, 0.35, facecolor="#333", edgecolor="black", linewidth=1.5))
    ax.text(9.1, 6.18, "affected male", fontsize=8, va="center")
    ax.add_patch(Circle((8.775, 5.45), 0.19, facecolor="white", edgecolor="black", linewidth=1.5))
    ax.text(9.1, 5.45, "unaffected female", fontsize=8, va="center")
    ax.add_patch(Circle((8.775, 4.9), 0.19, facecolor="#333", edgecolor="black", linewidth=1.5))
    ax.text(9.1, 4.9, "affected female", fontsize=8, va="center")

    save(fig, "q_pedigree_autosomal_recessive.png")


# ---------------------------------------------------------------
# Q121: solubility (g / 100 mL water) vs temperature curve for a solid
# salt -- rising with temperature (typical for most ionic solids such
# as KNO3).
# ---------------------------------------------------------------
def solubility_curve():
    T = np.linspace(0, 100, 200)
    # smooth, monotonically increasing, slightly concave-up curve
    S = 15 + 0.9 * T + 0.012 * T ** 1.6

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, S, color="#1a5276", linewidth=2.8)
    ax.fill_between(T, 0, S, color="#cfe0f3", alpha=0.4)

    ax.set_xlabel("Temperature (°C)", fontsize=12)
    ax.set_ylabel("Solubility (g per 100 mL water)", fontsize=12)
    ax.set_title("Solubility Curve of a Solid Salt", fontsize=14, fontweight="bold")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, max(S) * 1.1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.25)

    for t0 in (20, 60, 90):
        s0 = 15 + 0.9 * t0 + 0.012 * t0 ** 1.6
        ax.plot([t0, t0], [0, s0], color="gray", linestyle=":", linewidth=1)
        ax.plot([0, t0], [s0, s0], color="gray", linestyle=":", linewidth=1)
        ax.plot(t0, s0, "o", color="#c0392b", markersize=5)

    ax.annotate("solubility rises as\ntemperature increases", xy=(70, 15 + 0.9 * 70 + 0.012 * 70 ** 1.6),
                xytext=(35, max(S) * 0.85), fontsize=10, color="#1a5276",
                arrowprops=dict(arrowstyle="->", color="#1a5276"))

    save(fig, "q_solubility_curve_graph.png")


# ---------------------------------------------------------------
# Q154: R1 (3 ohm) in series with R2 (5 ohm) forms one branch; that
# branch is in parallel with R3 (8 ohm). Battery drives current
# through both branches, which reconnect at a common node.
# ---------------------------------------------------------------
def circuit_r1r2_series_r3_parallel():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Circuit: R1 + R2 (series) in parallel with R3", fontsize=14, fontweight="bold")

    left_x, right_x = 1.2, 10.8
    top_y, bot_y = 5.6, 1.0

    def wire(x0, y0, x1, y1):
        ax.plot([x0, x1], [y0, y1], color="black", linewidth=2.2, zorder=1)

    # battery on the left side (vertical), symbol between top and bottom rail
    batt_y0, batt_y1 = 2.6, 4.0
    wire(left_x, top_y, left_x, batt_y1)
    wire(left_x, batt_y0, left_x, bot_y)
    # battery plates
    ax.plot([left_x - 0.35, left_x + 0.35], [batt_y1 - 0.05, batt_y1 - 0.05], color="black", linewidth=3)
    ax.plot([left_x - 0.2, left_x + 0.2], [batt_y1 - 0.35, batt_y1 - 0.35], color="black", linewidth=1.6)
    ax.plot([left_x - 0.35, left_x + 0.35], [batt_y0 + 0.35, batt_y0 + 0.35], color="black", linewidth=1.6)
    ax.plot([left_x - 0.2, left_x + 0.2], [batt_y0 + 0.05, batt_y0 + 0.05], color="black", linewidth=3)
    ax.text(left_x - 0.9, (batt_y0 + batt_y1) / 2, "V", fontsize=12, fontweight="bold")

    # top and bottom rails
    node_top_l, node_top_r = 3.0, 8.6
    wire(left_x, top_y, node_top_l, top_y)
    wire(node_top_r, top_y, right_x, top_y)
    wire(right_x, top_y, right_x, bot_y)
    wire(left_x, bot_y, right_x, bot_y)

    def resistor(x0, y0, x1, y1, label):
        # zig-zag resistor symbol along a horizontal or vertical segment
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

    # Branch A (top): R1 series R2, drawn along the top rail between node_top_l and node_top_r
    r1_x0, r1_x1 = node_top_l, 5.0
    r2_x0, r2_x1 = 5.6, node_top_r
    wire(node_top_l, top_y, r1_x0, top_y)
    resistor(r1_x0, top_y, r1_x1, top_y, "R1 = 3 Ω")
    wire(r1_x1, top_y, r2_x0, top_y)
    resistor(r2_x0, top_y, r2_x1, top_y, "R2 = 5 Ω")
    wire(r2_x1, top_y, node_top_r, top_y)

    # connect the branch A endpoints down to the main left/right rails
    wire(node_top_l, top_y, node_top_l, 3.3)
    wire(node_top_r, top_y, node_top_r, 3.3)
    wire(node_top_l, 3.3, node_top_r, 3.3)
    ax.plot(node_top_l, 3.3, "o", color="black", markersize=5, zorder=4)
    ax.plot(node_top_r, 3.3, "o", color="black", markersize=5, zorder=4)

    # Branch B (bottom): R3 alone, in parallel between the same two nodes
    r3_x0, r3_x1 = 5.0, 6.6
    branch_b_y = 2.0
    wire(node_top_l, 3.3, node_top_l, branch_b_y)
    wire(node_top_l, branch_b_y, r3_x0, branch_b_y)
    resistor(r3_x0, branch_b_y, r3_x1, branch_b_y, "R3 = 8 Ω")
    wire(r3_x1, branch_b_y, node_top_r, branch_b_y)
    wire(node_top_r, branch_b_y, node_top_r, 3.3)

    ax.plot(left_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(left_x, bot_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(right_x, top_y, "o", color="black", markersize=5, zorder=4)
    ax.plot(right_x, bot_y, "o", color="black", markersize=5, zorder=4)

    ax.text(6, 0.35,
            "R1 + R2 (series, top branch) = 8 Ω, in parallel with R3 = 8 Ω  ->  total = 4 Ω",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_circuit_r1r2_series_r3_parallel.png")


# ---------------------------------------------------------------
# Q162: convex lens with parallel rays (parallel to the principal
# axis) converging at the principal focus F after refraction.
# ---------------------------------------------------------------
def convex_lens_parallel_rays_focus():
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Convex Lens: Parallel Rays Converging at the Principal Focus",
                 fontsize=14, fontweight="bold")

    axis_y = 3.0
    lens_x = 6.0
    f = 3.0  # focal length in plot units
    focus_x = lens_x + f

    # principal axis
    ax.plot([0.3, 11.7], [axis_y, axis_y], color="gray", linewidth=1.0, linestyle="--", zorder=1)

    # bi-convex lens shape
    lens_half_h = 2.1
    ys = np.linspace(axis_y - lens_half_h, axis_y + lens_half_h, 100)
    bulge = 0.35 * np.sqrt(1 - (ys - axis_y) ** 2 / lens_half_h ** 2)
    ax.fill(np.concatenate([lens_x + bulge, (lens_x - bulge)[::-1]]),
             np.concatenate([ys, ys[::-1]]), color="#cfe8f7", edgecolor="#1a5276", linewidth=2.0, zorder=2)
    # lens tips (arrows marking the lens symbol style)
    ax.plot([lens_x, lens_x], [axis_y - lens_half_h - 0.15, axis_y + lens_half_h + 0.15],
            color="#1a5276", linewidth=0, zorder=1)

    # incoming parallel rays (above and below axis, plus one on axis)
    ray_ys = [axis_y + 1.5, axis_y + 0.75, axis_y, axis_y - 0.75, axis_y - 1.5]
    for ry in ray_ys:
        # incoming ray: parallel to axis, from left edge to the lens
        ax.annotate("", xy=(lens_x, ry), xytext=(0.3, ry),
                    arrowprops=dict(arrowstyle="-", color="#a8332c", linewidth=1.8))
        # refracted ray: bends toward the focus (except the central ray, undeviated)
        if abs(ry - axis_y) < 1e-6:
            ax.annotate("", xy=(11.7, ry), xytext=(lens_x, ry),
                        arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=1.8))
        else:
            ax.annotate("", xy=(focus_x, axis_y), xytext=(lens_x, ry),
                        arrowprops=dict(arrowstyle="-", color="#a8332c", linewidth=1.8))
            # continue straight past the focus, diverging onward
            dx, dy = focus_x - lens_x, axis_y - ry
            ext_x, ext_y = focus_x + dx * 0.9, axis_y + dy * 0.9
            ax.annotate("", xy=(ext_x, ext_y), xytext=(focus_x, axis_y),
                        arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=1.8))

    # focus point F
    ax.plot(focus_x, axis_y, "o", color="#1a1a1a", markersize=7, zorder=5)
    ax.text(focus_x, axis_y - 0.35, "F\n(principal focus)", ha="center", fontsize=10, fontweight="bold")

    # also mark the symmetric point on the other side for reference (2nd focal point, unused by rays)
    other_focus_x = lens_x - f
    ax.plot(other_focus_x, axis_y, "o", color="#888", markersize=5, zorder=4)
    ax.text(other_focus_x, axis_y - 0.35, "F'", ha="center", fontsize=9, color="#666")

    ax.text(lens_x, axis_y + lens_half_h + 0.4, "Convex lens", ha="center", fontsize=10.5)
    ax.text(6, 0.4,
            "Rays parallel to the principal axis refract through the convex lens and\n"
            "converge at a single point on the axis: the principal focus (focal point).",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_convex_lens_parallel_rays_focus.png")


if __name__ == "__main__":
    endomembrane_secretory_pathway()
    pedigree_autosomal_recessive()
    solubility_curve()
    circuit_r1r2_series_r3_parallel()
    convex_lens_parallel_rays_focus()

"""Generate the 5 diagram/graph images referenced by mdcat_mock11.py's
image-based questions:
  Q23  Biology  - cell in metaphase of mitosis (chromosomes aligned singly
                  at the metaphase plate, spindle fibers from both poles)
  Q72  Biology  - labeled nephron cross-section (1-5: afferent arteriole,
                  glomerulus, Bowman's capsule, PCT, loop of Henle)
  Q93  Chemistry- solid/liquid/gas phase diagram showing the triple point
  Q154 Physics  - R1(4)+R2(12) in parallel, then in series with R3(1) -> 4 ohm
  Q162 Physics  - concave mirror ray diagram, object beyond C -> real,
                  inverted, diminished image between F and C
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, Circle

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q23: Cell in METAPHASE of mitosis. Chromosomes (each with 2 sister
# chromatids joined at a centromere) aligned SINGLY along the metaphase
# plate (cell equator), spindle fibers radiating from two opposite poles
# and attaching to each chromosome's centromere/kinetochore.
# ---------------------------------------------------------------
def mitosis_metaphase_stage():
    fig, ax = plt.subplots(figsize=(8, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Cell Division Stage", fontsize=15, fontweight="bold")

    # cell outline
    ax.add_patch(Ellipse((5, 4), 8.6, 5.6, facecolor="#eef6fb", edgecolor="black", linewidth=1.8))

    # two centrosomes (spindle poles) at opposite ends
    pole_left = (1.1, 4)
    pole_right = (8.9, 4)
    for px, py in (pole_left, pole_right):
        ax.plot(px, py, "o", color="#333", markersize=7)
        for dphi in np.linspace(-35, 35, 5):
            ang = np.deg2rad(dphi)
            ax.plot(px, py, marker=(2, 0, np.rad2deg(np.arctan2(0, 1))), markersize=1)

    # metaphase plate (equator) — chromosomes aligned SINGLY along the
    # center, attached to spindle fibers from both poles
    n_chrom = 6
    ys = np.linspace(2.0, 6.0, n_chrom)
    for y in ys:
        # each chromosome: X-shaped pair of sister chromatids at the
        # equator (classic metaphase chromosome look)
        ax.plot([5 - 0.28, 5 + 0.28], [y - 0.28, y + 0.28], color="#8b1a4a", linewidth=3.2)
        ax.plot([5 - 0.28, 5 + 0.28], [y + 0.28, y - 0.28], color="#8b1a4a", linewidth=3.2)
        ax.plot(5, y, "o", color="#5a0f30", markersize=4)  # centromere

        # spindle fibers from both poles to the centromere
        ax.plot([pole_left[0], 5], [pole_left[1], y], color="#3a7a3a", linewidth=1.0, alpha=0.8)
        ax.plot([pole_right[0], 5], [pole_right[1], y], color="#3a7a3a", linewidth=1.0, alpha=0.8)

    ax.axvline(5, color="#888", linestyle="--", linewidth=1.2, ymin=0.08, ymax=0.92)
    ax.text(5, 0.7, "metaphase plate (cell equator)", ha="center", fontsize=9, style="italic", color="#555")
    ax.text(pole_left[0], pole_left[1] - 0.55, "spindle pole", ha="center", fontsize=9, color="#333")
    ax.text(pole_right[0], pole_right[1] - 0.55, "spindle pole", ha="center", fontsize=9, color="#333")
    ax.text(5, 7.1, "Chromosomes aligned singly at the equator,\nattached to spindle fibers from both poles",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_mitosis_metaphase_stage.png")


# ---------------------------------------------------------------
# Q72: Nephron diagram labeled 1-5:
#   1 = afferent arteriole (brings blood IN to the glomerulus)
#   2 = glomerulus (capillary tuft -- site of filtration UNDER PRESSURE)
#   3 = Bowman's capsule (collects the filtrate around the glomerulus)
#   4 = proximal convoluted tubule (PCT)
#   5 = loop of Henle
# ---------------------------------------------------------------
def nephron_diagram():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Nephron Structure", fontsize=15, fontweight="bold")

    # --- Bowman's capsule (cup shape) around the glomerulus ---
    capsule_center = (3.2, 6.6)
    capsule_r = 1.15
    theta = np.linspace(np.deg2rad(210), np.deg2rad(-30), 60)
    cx = capsule_center[0] + capsule_r * np.cos(theta)
    cy = capsule_center[1] + capsule_r * np.sin(theta)
    ax.plot(cx, cy, color="#555", linewidth=2.4)

    # glomerulus: tangled capillary tuft inside the capsule
    rng = np.random.default_rng(11)
    for _ in range(24):
        a = rng.uniform(capsule_center[0] - 0.75, capsule_center[0] + 0.75)
        b = rng.uniform(capsule_center[1] - 0.55, capsule_center[1] + 0.5)
        r = rng.uniform(0.08, 0.16)
        ax.add_patch(Circle((a, b), r, facecolor="#c0392b", edgecolor="#7a1f16", linewidth=0.5, alpha=0.85))

    # afferent arteriole: connects from upper-left INTO the glomerulus
    aff_start = (0.6, 8.3)
    aff_end = (capsule_center[0] - 0.55, capsule_center[1] + 0.35)
    ax.annotate("", xy=aff_end, xytext=aff_start,
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.8))

    # efferent arteriole: connects OUT of the glomerulus to the upper-right
    eff_start = (capsule_center[0] + 0.55, capsule_center[1] + 0.35)
    eff_end = (5.4, 8.3)
    ax.annotate("", xy=eff_end, xytext=eff_start,
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.2))

    # --- Proximal convoluted tubule (PCT): coiled tube connected directly
    # to the bottom of Bowman's capsule, leading down toward the loop ---
    capsule_outlet = (capsule_center[0], capsule_center[1] - capsule_r)
    pct_t = np.linspace(0, 3.5 * np.pi, 220)
    pct_cx, pct_cy = 3.2, 5.15
    pct_x = pct_cx + 0.5 * np.cos(pct_t)
    pct_y = pct_cy + 1.0 - 0.9 * (pct_t / pct_t.max()) + 0.32 * np.sin(pct_t)
    # stitch PCT start onto the capsule outlet
    pct_x = np.concatenate(([capsule_outlet[0]], pct_x))
    pct_y = np.concatenate(([capsule_outlet[1]], pct_y))
    ax.plot(pct_x, pct_y, color="#2e7d32", linewidth=2.2)
    pct_end = (pct_x[-1], pct_y[-1])

    # --- Loop of Henle: a continuous U-shaped tube starting where the PCT
    # ends, descending, hairpin turn, then ascending back up ---
    descend_top = pct_end
    descend_bottom = (5.2, 1.0)
    hairpin_end = (6.6, 1.0)
    ascend_top = (6.6, 4.6)
    ax.plot([descend_top[0], 5.2, 5.2], [descend_top[1], descend_top[1] - 0.3, descend_bottom[1]],
            color="#1b5e8a", linewidth=2.4)  # descending limb, joined to PCT end
    ax.plot([5.2, hairpin_end[0]], [1.0, 1.0], color="#1b5e8a", linewidth=2.4)  # hairpin turn
    ax.plot([6.6, 6.6], [1.0, 4.6], color="#7a3ba8", linewidth=2.4)  # ascending limb

    # --- Distal convoluted tubule + collecting duct: continues from the
    # top of the ascending limb up to the collecting duct on the right ---
    ax.plot([6.6, 8.6], [4.6, 6.0], color="#333333", linewidth=2.0)
    ax.plot([8.6, 8.6], [6.0, 8.6], color="#333333", linewidth=2.2)
    ax.annotate("", xy=(8.6, 0.6), xytext=(8.6, 6.0),
                arrowprops=dict(arrowstyle="-|>", color="#333333", linewidth=2.2))
    ax.text(8.9, 0.55, "to collecting duct / ureter", fontsize=8.5, color="#333", va="center")

    def label(num, tx, ty, target):
        ax.annotate(str(num), xy=target, xytext=(tx, ty), fontsize=13, fontweight="bold",
                    ha="center", va="center",
                    arrowprops=dict(arrowstyle="-", color="black", lw=1),
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5))

    label(1, 0.5, 9.0, (aff_start[0] + 0.15, aff_start[1] - 0.15))         # afferent arteriole
    label(2, 1.2, 5.9, (capsule_center[0] - 0.35, capsule_center[1] - 0.05))  # glomerulus
    label(3, 5.4, 7.6, (capsule_center[0] + capsule_r * 0.7, capsule_center[1] + capsule_r * 0.55))  # Bowman's capsule
    label(4, 1.0, 4.0, (pct_cx - 0.55, pct_cy + 0.2))          # PCT
    label(5, 7.9, 2.6, (6.6, 2.8))                              # loop of Henle

    save(fig, "q_nephron_diagram.png")


# ---------------------------------------------------------------
# Q93: Phase diagram (pressure vs temperature) with solid, liquid, gas
# regions, the triple point (all three phases coexist in equilibrium),
# and the critical point marked.
# ---------------------------------------------------------------
def phase_diagram_triple_point():
    fig, ax = plt.subplots(figsize=(7.5, 6))

    T = np.linspace(0, 10, 300)
    triple_T, triple_P = 3.0, 2.5
    critical_T, critical_P = 8.5, 8.0

    # solid-liquid boundary (steep, roughly vertical, from triple point up)
    sl_T = np.array([triple_T, triple_T + 0.15, triple_T + 0.3])
    sl_P = np.array([triple_P, 5.5, 9.5])
    ax.plot(sl_T, sl_P, color="black", linewidth=2)

    # liquid-gas boundary (from triple point to critical point)
    lg_T = np.linspace(triple_T, critical_T, 100)
    lg_P = triple_P + (critical_P - triple_P) * ((lg_T - triple_T) / (critical_T - triple_T)) ** 0.7
    ax.plot(lg_T, lg_P, color="black", linewidth=2)

    # solid-gas boundary (sublimation curve, from origin-ish to triple point)
    sg_T = np.linspace(0.3, triple_T, 100)
    sg_P = triple_P * ((sg_T - 0.3) / (triple_T - 0.3)) ** 1.6
    ax.plot(sg_T, sg_P, color="black", linewidth=2)

    ax.plot(triple_T, triple_P, "o", color="#a8332c", markersize=8, zorder=5)
    ax.annotate("Triple Point", xy=(triple_T, triple_P), xytext=(triple_T - 1.6, triple_P - 1.3),
                fontsize=11, color="#a8332c", fontweight="bold",
                arrowprops=dict(arrowstyle="-", color="#a8332c"))

    ax.plot(critical_T, critical_P, "o", color="#1b6e6e", markersize=8, zorder=5)
    ax.annotate("Critical Point", xy=(critical_T, critical_P), xytext=(critical_T - 1.0, critical_P + 0.6),
                fontsize=11, color="#1b6e6e", fontweight="bold",
                arrowprops=dict(arrowstyle="-", color="#1b6e6e"))

    ax.text(1.2, 0.6, "SOLID", fontsize=13, fontweight="bold", color="#333")
    ax.text(6.2, 2.5, "LIQUID", fontsize=13, fontweight="bold", color="#333")
    ax.text(6.0, 0.5, "GAS", fontsize=13, fontweight="bold", color="#333")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Temperature", fontsize=12)
    ax.set_ylabel("Pressure", fontsize=12)
    ax.set_title("Phase Diagram: Solid / Liquid / Gas", fontsize=14, fontweight="bold")
    save(fig, "q_phase_diagram_triple_point.png")


# ---------------------------------------------------------------
# Q154: R1 = 4 ohm and R2 = 12 ohm in PARALLEL (-> 3 ohm), that
# combination in SERIES with R3 = 1 ohm -> total = 4 ohm.
# ---------------------------------------------------------------
def circuit_r1r2_parallel_r3_series_v2():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.add_patch(plt.Circle((1, 3), 0.6, facecolor="white", edgecolor="black", linewidth=2))
    ax.text(1, 3.28, "+", ha="center", va="center", fontsize=13)
    ax.text(1, 2.72, "-", ha="center", va="center", fontsize=13)
    ax.text(1, 1.9, "Battery", ha="center", va="center", fontsize=11)

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
            ax.text(midx, midy + 0.55, label, ha="center", fontsize=11)
        else:
            ax.text(midx + 0.95, midy, label, ha="center", fontsize=11)

    # lead from battery up into the parallel section
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    # R1 (4 ohm) -- left branch of the parallel pair
    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 4 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    # R2 (12 ohm) -- right branch of the parallel pair
    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 12 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    # top and bottom rails joining the two parallel branches
    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)

    # R3 (1 ohm) in series after the parallel combination
    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 1 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    # return to battery
    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    ax.text(5, 0.05, "R1 ∥ R2 = 3 Ω, then + R3 (series) = 4 Ω total", ha="center", fontsize=9, style="italic")

    save(fig, "q_circuit_r1r2_parallel_r3_series_v2.png")


# ---------------------------------------------------------------
# Q162: Concave mirror, object beyond C -> real, inverted, diminished
# image, formed between F and C (matches the correct answer B).
# Distinct f / object placement from earlier mocks' concave-mirror
# diagrams so the rendered PNG isn't byte-identical (see mdcat-mock-tests
# memory on duplicate images).
# ---------------------------------------------------------------
def concave_mirror_beyond_c_ray_diagram():
    f = 1.6
    R = 2 * f
    obj_x, obj_h = -5.0 * f, 2.2   # well beyond C

    u_mag = abs(obj_x)
    v_mag = 1.0 / (1.0 / f - 1.0 / u_mag)
    img_x = -v_mag
    img_h = -obj_h * (v_mag / u_mag)  # inverted, diminished since v_mag < u_mag

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 2.5)
    ax.set_ylim(min(img_h, 0) - 1.5, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave Mirror (Object beyond C)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # Concave mirror: center of curvature C is on the SAME side as the
    # object, so the mirror surface bulges TOWARD the object at the edges
    # -- a NEGATIVE-coefficient parabola x(y) = -k*y**2 (a positive
    # coefficient would draw a convex mirror instead).
    yy = np.linspace(-2.6, 2.6, 100)
    xx = -0.09 * yy**2
    ax.plot(xx, yy, color="#2f6f9f", linewidth=3)

    for x, lbl in [(-R, "C"), (-f, "F"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # image (red, inverted, diminished, between F and C)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis -> reflects through F -> image tip
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)

    # ray 2: through C, reflects back on itself (passes through image tip too)
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    save(fig, "q_concave_mirror_beyond_c_ray_diagram.png")


if __name__ == "__main__":
    mitosis_metaphase_stage()
    nephron_diagram()
    phase_diagram_triple_point()
    circuit_r1r2_parallel_r3_series_v2()
    concave_mirror_beyond_c_ray_diagram()

"""Generate the 5 diagram images referenced by mdcat_mock_20.py's
image-based questions:
  Q12  Biology  - labeled plant cell (J=nucleus, K=cell wall, L=chloroplast,
                  M=central vacuole) identifying the central vacuole
  Q65  Biology  - simplified circulatory pathway (W=pulmonary artery,
                  X=pulmonary vein, Y=vena cava, Z=aorta) identifying the
                  pulmonary artery as the only artery carrying deoxygenated
                  blood
  Q124 Chemistry- phase diagram (P vs T) showing the triple point and the
                  critical-point/supercritical region
  Q154 Physics  - three identical 6 ohm resistors, all in parallel -> 2 ohm
  Q162 Physics  - convex lens ray diagram, object exactly at F -> emergent
                  rays parallel, no real image formed

Filenames for the phase diagram and the object-at-F lens diagram are
prefixed with "mock20_" because mocks 11 and 8 already used the generic
names for their own (differently-styled) versions of the same physics
scenarios -- see mdcat-mock-tests memory on the duplicate-image-name/hash
gotcha.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: plant cell, J=nucleus, K=cell wall, L=chloroplast, M=central vacuole
# (the correct answer). Central vacuole drawn large, taking up most of the
# cell interior, as is biologically typical of a mature plant cell.
# ---------------------------------------------------------------
def plant_cell_vacuole_diagram():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of a Plant Cell", fontsize=16, fontweight="bold")

    # cell wall (outer rigid boundary) + plasma membrane just inside it
    ax.add_patch(FancyBboxPatch((0.6, 0.8), 8.8, 8.4, boxstyle="round,pad=0,rounding_size=0.5",
                                 facecolor="#f2f9e8", edgecolor="#4a6b1f", linewidth=5))
    ax.add_patch(FancyBboxPatch((1.0, 1.2), 8.0, 7.6, boxstyle="round,pad=0,rounding_size=0.4",
                                 facecolor="#f2f9e8", edgecolor="#8fae5a", linewidth=1.3))

    # large central vacuole (dominant feature of a mature plant cell)
    ax.add_patch(Ellipse((5.2, 4.6), 5.6, 4.8, facecolor="#cdeaf5", edgecolor="#4f9bb8", linewidth=1.8))

    # nucleus, off to one side
    ax.add_patch(Ellipse((2.1, 7.2), 1.7, 1.5, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((2.2, 7.15), 0.65, 0.65, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    # a couple of chloroplasts
    for cx, cy, ang in [(7.9, 6.6, -15), (7.7, 2.6, 12)]:
        ax.add_patch(Ellipse((cx, cy), 1.3, 0.7, angle=ang, facecolor="#4c8f3f", edgecolor="#2e5c26", linewidth=1.3))

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(2.1, 7.2, 0.4, 9.2, "J")     # nucleus
    label(0.7, 5.0, -0.7, 5.0, "K")    # cell wall
    label(7.9, 6.6, 9.5, 7.8, "L")     # chloroplast
    label(5.2, 3.2, 5.2, 0.4, "M")     # central vacuole (correct answer)

    save(fig, "q_plant_cell_vacuole_diagram.png")


# ---------------------------------------------------------------
# Q65: simplified circulatory pathway loop.
#   Heart (center) -> W (pulmonary artery, deoxygenated) -> Lungs
#   Lungs -> X (pulmonary vein, oxygenated) -> Heart
#   Heart -> Z (aorta, oxygenated) -> Body
#   Body -> Y (vena cava, deoxygenated) -> Heart
# W is the only ARTERY carrying deoxygenated blood (correct answer).
# ---------------------------------------------------------------
def circulatory_pathway_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Simplified Circulatory Pathway", fontsize=15, fontweight="bold")

    # heart box (center)
    ax.add_patch(FancyBboxPatch((3.7, 4.0), 2.6, 2.0, boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor="#f5c6c6", edgecolor="#8b1a1a", linewidth=2))
    ax.text(5.0, 5.0, "HEART", ha="center", va="center", fontsize=12, fontweight="bold")

    # lungs box (top)
    ax.add_patch(FancyBboxPatch((3.9, 7.6), 2.2, 1.6, boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor="#d6e8f7", edgecolor="#2f6f9f", linewidth=2))
    ax.text(5.0, 8.4, "LUNGS", ha="center", va="center", fontsize=12, fontweight="bold")

    # body box (bottom)
    ax.add_patch(FancyBboxPatch((3.9, 0.6), 2.2, 1.6, boxstyle="round,pad=0.05,rounding_size=0.3",
                                 facecolor="#e8ddc9", edgecolor="#8a6a2a", linewidth=2))
    ax.text(5.0, 1.4, "REST OF\nBODY", ha="center", va="center", fontsize=11, fontweight="bold")

    def arrow(x0, y0, x1, y1, color):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=18,
                                      linewidth=2.5, color=color))

    # W: heart -> lungs, deoxygenated (pulmonary artery) -- left side, going up
    arrow(3.9, 6.0, 3.9, 7.6, "#4a4aa0")
    ax.text(3.0, 6.9, "W", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black"))

    # X: lungs -> heart, oxygenated (pulmonary vein) -- right side, coming down
    arrow(6.1, 7.6, 6.1, 6.0, "#c0392b")
    ax.text(7.0, 6.9, "X", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black"))

    # Z: heart -> body, oxygenated (aorta) -- right side, going down
    arrow(6.1, 4.0, 6.1, 2.2, "#c0392b")
    ax.text(7.0, 3.1, "Z", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black"))

    # Y: body -> heart, deoxygenated (vena cava) -- left side, coming up
    arrow(3.9, 2.2, 3.9, 4.0, "#4a4aa0")
    ax.text(3.0, 3.1, "Y", fontsize=15, fontweight="bold", ha="center",
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black"))

    ax.text(5.0, 9.55, "blue arrows = deoxygenated   red arrows = oxygenated",
            ha="center", fontsize=9, style="italic", color="#444")

    save(fig, "q_circulatory_pathway_pulmonary_artery_diagram.png")


# ---------------------------------------------------------------
# Q124: Phase diagram (P vs T) with triple point and critical point,
# styled distinctly from mock11's version (different coordinates, dashed
# supercritical-region shading, different color scheme) to avoid an
# MD5-identical render.
# ---------------------------------------------------------------
def phase_diagram_triple_point_mock20():
    fig, ax = plt.subplots(figsize=(7.5, 6))

    triple_T, triple_P = 2.2, 1.8
    critical_T, critical_P = 7.6, 7.2

    # solid-liquid boundary (steep, slightly forward-leaning)
    sl_T = np.array([triple_T, triple_T + 0.25, triple_T + 0.5])
    sl_P = np.array([triple_P, 5.0, 9.6])
    ax.plot(sl_T, sl_P, color="#222", linewidth=2.2)

    # liquid-gas boundary (triple point -> critical point)
    lg_T = np.linspace(triple_T, critical_T, 100)
    lg_P = triple_P + (critical_P - triple_P) * ((lg_T - triple_T) / (critical_T - triple_T)) ** 0.75
    ax.plot(lg_T, lg_P, color="#222", linewidth=2.2)

    # solid-gas sublimation curve
    sg_T = np.linspace(0.2, triple_T, 100)
    sg_P = triple_P * ((sg_T - 0.2) / (triple_T - 0.2)) ** 1.7
    ax.plot(sg_T, sg_P, color="#222", linewidth=2.2)

    # shade the supercritical-fluid region beyond the critical point
    ax.fill_between([critical_T, 10], critical_P, 10, color="#e8d9f2", alpha=0.6, zorder=0)
    ax.text(8.7, 9.0, "supercritical\nfluid", ha="center", fontsize=9.5, fontweight="bold",
            color="#6a3a8a", style="italic")

    ax.plot(triple_T, triple_P, "o", color="#b5451b", markersize=9, zorder=5)
    ax.annotate("Triple Point", xy=(triple_T, triple_P), xytext=(triple_T - 0.3, triple_P - 1.4),
                fontsize=11, color="#b5451b", fontweight="bold",
                arrowprops=dict(arrowstyle="-", color="#b5451b"))

    ax.plot(critical_T, critical_P, "s", color="#1f6f4a", markersize=9, zorder=5)
    ax.annotate("Critical Point", xy=(critical_T, critical_P), xytext=(critical_T - 3.0, critical_P + 1.1),
                fontsize=11, color="#1f6f4a", fontweight="bold",
                arrowprops=dict(arrowstyle="-", color="#1f6f4a"))

    ax.text(0.9, 0.5, "SOLID", fontsize=13, fontweight="bold", color="#333")
    ax.text(5.2, 2.2, "LIQUID", fontsize=13, fontweight="bold", color="#333")
    ax.text(5.5, 0.4, "GAS", fontsize=13, fontweight="bold", color="#333")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Temperature", fontsize=12)
    ax.set_ylabel("Pressure", fontsize=12)
    ax.set_title("Phase Diagram: Triple Point & Critical Region", fontsize=14, fontweight="bold")
    save(fig, "q_mock20_phase_diagram_triple_point.png")


# ---------------------------------------------------------------
# Q154: THREE identical 6 ohm resistors, all connected in PARALLEL with
# each other (not series+parallel like earlier mocks) -> 1/R = 3*(1/6),
# R = 2 ohm.
# ---------------------------------------------------------------
def circuit_three_parallel_resistors():
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.set_xlim(0, 11)
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
            ax.text(midx - 0.95, midy, label, ha="center", fontsize=11)

    # top rail from battery
    ax.plot([1, 1], [3.6, 5.2], color="black", linewidth=2)
    ax.plot([1, 9.5], [5.2, 5.2], color="black", linewidth=2)
    # bottom rail
    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 9.5], [0.5, 0.5], color="black", linewidth=2)
    ax.plot([9.5, 9.5], [5.2, 0.5], color="black", linewidth=2)

    # three parallel branches, each a 6 ohm resistor
    for x, lbl in [(3.5, "R1 = 6 Ω"), (5.5, "R2 = 6 Ω"), (7.5, "R3 = 6 Ω")]:
        ax.plot([x, x], [5.2, 4.3], color="black", linewidth=2)
        resistor(x, 4.3, x, 1.4, lbl)
        ax.plot([x, x], [1.4, 0.5], color="black", linewidth=2)

    ax.text(5.5, 0.05, "R1 ∥ R2 ∥ R3, each 6 Ω  ->  1/R = 3 x (1/6)  ->  R = 2 Ω",
            ha="center", fontsize=9.5, style="italic")

    save(fig, "q_circuit_three_parallel_resistors.png")


# ---------------------------------------------------------------
# Q162: Convex lens, object placed exactly at F. Both standard
# construction rays must emerge from the lens with the SAME slope
# (-obj_h/f), i.e. genuinely parallel to each other on the far side
# (image at infinity, no real image formed) -- the well-documented
# mock-tests "object-at-F" bug class (see gen_mock5_images.py). Styled
# distinctly (different colors/labels) from mock5's version to avoid an
# MD5-identical render, and given a unique filename since mock8 already
# used the generic "q_convex_lens_object_at_f.png" name for its own
# object-at-F rendering.
# ---------------------------------------------------------------
def convex_lens_object_at_f_mock20():
    f = 2.4
    obj_x, obj_h = -f, 1.6

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-7.5, 7.5)
    ax.set_ylim(-2.8, 3.8)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object at F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [-3.4, 3.4], color="#3f7f4f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.4, lbl, ha="center", fontsize=12, color="gray")

    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.28, "Object (at F)", color="#a8332c", fontsize=13, ha="center")

    # Object at F -> both standard rays emerge with the same slope
    # (-obj_h/f) after the lens, i.e. parallel to each other.
    slope_emergent = -obj_h / f

    # ray 1: parallel to axis into the lens, then refracts through the far
    # focal point and continues at slope_emergent beyond it
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#222", linewidth=1.7)
    ax.plot([0, 7], [obj_h, obj_h + slope_emergent * 7], color="#222", linewidth=1.7)

    # ray 2: through the optical center, undeviated
    slope2 = obj_h / obj_x
    ax.plot([obj_x, 7], [obj_h, slope2 * 7], color="#222", linewidth=1.7, linestyle="--")

    ax.text(5.2, obj_h + 0.35, "emergent rays\nparallel to each other\n(image at infinity)",
            color="#222", fontsize=10, ha="center")

    save(fig, "q_mock20_convex_lens_object_at_f.png")


if __name__ == "__main__":
    plant_cell_vacuole_diagram()
    circulatory_pathway_diagram()
    phase_diagram_triple_point_mock20()
    circuit_three_parallel_resistors()
    convex_lens_object_at_f_mock20()

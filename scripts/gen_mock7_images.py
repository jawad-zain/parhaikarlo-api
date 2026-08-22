"""Generate the 5 diagram/graph images referenced by mdcat_mock_7.py's
image-based questions (Q8 enzyme-activity-vs-pH comparison X vs Y,
Q14 animal cell J/K/L/M with J=rough ER, Q110 weak-acid/strong-base
titration buffer region, Q154 R1+R2 series then parallel with R3,
Q162 concave mirror object beyond C).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q8: enzyme X peaks ~pH 2 (stomach, pepsin-like), enzyme Y peaks ~pH 8
# (small intestine, e.g. trypsin-like)
# ---------------------------------------------------------------
def enzyme_ph_comparison():
    ph = np.linspace(0, 14, 400)
    x_act = 100 * np.exp(-((ph - 2) ** 2) / (2 * 1.1 ** 2))
    y_act = 100 * np.exp(-((ph - 8) ** 2) / (2 * 1.3 ** 2))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(ph, x_act, color="#a8332c", linewidth=2.5, label="Enzyme X")
    ax.plot(ph, y_act, color="#1b6e6e", linewidth=2.5, label="Enzyme Y")
    ax.set_title("Enzyme Activity vs pH: Enzyme X and Enzyme Y", fontsize=14, fontweight="bold")
    ax.set_xlabel("pH", fontsize=12)
    ax.set_ylabel("Relative Enzyme Activity (%)", fontsize=12)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 110)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q7_enzyme_ph_comparison_graph.png")


# ---------------------------------------------------------------
# Q14: animal cell, J=rough ER (ribosome-studded membranes), K=smooth ER,
# L=Golgi apparatus, M=lysosome
# ---------------------------------------------------------------
def cell_diagram_jklm():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of an Animal Cell", fontsize=16, fontweight="bold")

    ax.add_patch(Ellipse((5, 5), 8.6, 7.6, facecolor="#fdf6e3", edgecolor="#6b5b1e", linewidth=2.5))

    # nucleus (not labeled, background context)
    ax.add_patch(Ellipse((5, 5.3), 1.8, 1.8, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))

    # rough ER (J) -- wavy membrane stack with dots (ribosomes) near nucleus
    for i in range(4):
        xs = np.linspace(2.5, 4.0, 25)
        ys = (6.6 - i * 0.28) + 0.08 * np.sin(np.linspace(0, 3 * np.pi, 25))
        ax.plot(xs, ys, color="#2f6f9f", linewidth=1.8)
        for xdot in xs[::5]:
            ax.plot(xdot, ys[list(xs).index(xdot)] + 0.06, "o", color="#333", markersize=1.8)

    # smooth ER (K) -- similar wavy membrane, no dots, lower region
    for i in range(3):
        xs = np.linspace(2.4, 3.9, 25)
        ys = (3.6 - i * 0.28) + 0.08 * np.sin(np.linspace(0, 3 * np.pi, 25))
        ax.plot(xs, ys, color="#5aa0c9", linewidth=1.8)

    # Golgi apparatus (L)
    for i in range(5):
        xs = np.linspace(6.0, 8.0, 30)
        ys = (5.6 - i * 0.32) + 0.12 * np.sin(np.linspace(0, np.pi, 30))
        ax.plot(xs, ys, color="#1b6e6e", linewidth=2.2)

    # lysosome (M)
    ax.add_patch(Ellipse((7.0, 3.0), 1.0, 1.0, facecolor="#e6c34a", edgecolor="#a8842a", linewidth=1.5))

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(3.2, 6.5, 1.4, 7.6, "J")
    label(3.1, 3.5, 1.4, 2.3, "K")
    label(7.0, 5.2, 8.7, 6.3, "L")
    label(7.0, 3.0, 8.7, 1.8, "M")

    save(fig, "q7_cell_diagram_jklm.png")


# ---------------------------------------------------------------
# Q110: weak acid + strong base titration, buffer region flat before
# steep jump near equivalence at 25 mL
# ---------------------------------------------------------------
def titration_buffer_region_graph():
    v = np.linspace(0, 50, 400)
    ph = 4.2 + 1.3 * np.log10(np.clip(v, 0.5, None) / np.clip(25 - v, 0.01, None) + 1e-9)
    ph = np.nan_to_num(ph, nan=8.9, posinf=12.6, neginf=1.2)
    jump = 8.9 + 3.9 / (1 + np.exp(-0.9 * (v - 25)))
    ph = np.where(v > 20, jump, ph)
    ph = np.clip(ph, 3.0, 12.9)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#6b3fa0", linewidth=2.5)
    ax.axvspan(4, 20, color="#6b3fa0", alpha=0.08)
    ax.text(11, 4.0, "buffering\nregion", fontsize=10, color="#6b3fa0", ha="center")
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.set_title("Titration of a Weak Acid with NaOH", fontsize=14, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q7_titration_buffer_region_graph.png")


# ---------------------------------------------------------------
# Q154: R1(6) + R2(3) in series = 9, in parallel with R3(9) -> 4.5 ohm
# ---------------------------------------------------------------
def circuit_diagram_r1r2r3():
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
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
            ax.text(midx + 1.05, midy, label, ha="center", fontsize=11)

    # branch A: R1 then R2 in series (top branch)
    ax.plot([1, 1], [3.6, 5.2], color="black", linewidth=2)
    ax.plot([1, 3], [5.2, 5.2], color="black", linewidth=2)
    resistor(3, 5.2, 4.8, 5.2, "R1 = 6 Ω")
    resistor(4.8, 5.2, 6.6, 5.2, "R2 = 3 Ω")
    ax.plot([6.6, 8.5], [5.2, 5.2], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5.2, 0.5], color="black", linewidth=2)

    # branch B: R3 alone (bottom branch, parallel to A)
    ax.plot([1, 1], [2.4, 1.3], color="black", linewidth=2)
    ax.plot([1, 3.8], [1.3, 1.3], color="black", linewidth=2)
    resistor(3.8, 1.3, 5.6, 1.3, "R3 = 9 Ω")
    ax.plot([5.6, 8.5], [1.3, 1.3], color="black", linewidth=2)

    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)
    ax.plot([1, 1], [1.3, 0.5], color="black", linewidth=0)  # already connected via 2.4->1.3

    save(fig, "q7_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: concave mirror, object beyond C -> real, inverted, diminished,
# image between F and C
# ---------------------------------------------------------------
def concave_mirror_diagram_beyond_c():
    # Different scenario/geometry from mock_6's beyond-C mirror diagram
    # (distinct f, object distance and height) so the rendered PNG isn't
    # byte-identical -- see mdcat-mock-tests memory on duplicate images.
    f = 2.5
    R = 2 * f
    obj_x, obj_h = -4.5 * f, 2.0

    u_mag = abs(obj_x)
    v_mag = 1.0 / (1.0 / f - 1.0 / u_mag)
    img_x = -v_mag
    img_h = -obj_h * (v_mag / u_mag)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 3)
    ax.set_ylim(min(img_h, 0) - 1.5, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave Mirror (Object beyond C)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # Concave mirror: center of curvature C is on the SAME side as the
    # object, so the surface bulges toward the object at the edges --
    # NEGATIVE-coefficient parabola (a positive coefficient draws a
    # convex mirror shape instead).
    yy = np.linspace(-3.0, 3.0, 100)
    xx = -0.07 * yy**2
    ax.plot(xx, yy, color="#3a5f8f", linewidth=3)

    for x, lbl in [(-R, "C"), (-f, "F"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=13, ha="center")

    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    save(fig, "q7_concave_mirror_diagram_beyond_c.png")


if __name__ == "__main__":
    enzyme_ph_comparison()
    cell_diagram_jklm()
    titration_buffer_region_graph()
    circuit_diagram_r1r2r3()
    concave_mirror_diagram_beyond_c()

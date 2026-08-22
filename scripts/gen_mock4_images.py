"""Generate the 5 diagram/graph images referenced by mdcat_mock_4.py's
image-based questions (Q8, Q14, Q110, Q154, Q162).
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
# Q8: enzyme activity vs temperature, peak near 37C
# ---------------------------------------------------------------
def enzyme_temp_graph():
    t = np.linspace(0, 65, 400)
    rate = np.where(
        t <= 37,
        100 * (1 - np.exp(-t / 11)),
        100 * np.exp(-((t - 37) ** 2) / (2 * 6.0 ** 2)),
    )
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(t, rate, color="#1b6e6e", linewidth=2.5)
    ax.fill_between(t, rate, color="#1b6e6e", alpha=0.08)
    ax.set_title("Effect of Temperature on Enzyme Activity", fontsize=15, fontweight="bold")
    ax.set_xlabel("Temperature (°C)", fontsize=12)
    ax.set_ylabel("Rate of Enzyme Activity (%)", fontsize=12)
    ax.set_xlim(0, 65)
    ax.set_ylim(0, 110)
    ax.grid(alpha=0.3)
    save(fig, "q4_enzyme_temp_graph.png")


# ---------------------------------------------------------------
# Q14: animal cell, P=nucleus, Q=mitochondrion, R=Golgi, S=lysosome
# ---------------------------------------------------------------
def cell_diagram_pqrs():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of an Animal Cell", fontsize=16, fontweight="bold")

    ax.add_patch(Ellipse((5, 5), 8.6, 7.6, facecolor="#fdf6e3", edgecolor="#6b5b1e", linewidth=2.5))

    # nucleus (P)
    ax.add_patch(Ellipse((3.6, 5.6), 2.6, 2.6, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((3.75, 5.5), 1.0, 1.0, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    # lysosome (S)
    ax.add_patch(Ellipse((6.9, 7.0), 1.0, 1.0, facecolor="#e6c34a", edgecolor="#a8842a", linewidth=1.5))

    # mitochondrion (Q) - with visible cristae
    cx, cy, ang = 6.6, 3.3, 20
    ax.add_patch(Ellipse((cx, cy), 1.7, 0.85, angle=ang, facecolor="#d97a55", edgecolor="#a8482a", linewidth=1.5))
    for off in (-0.35, 0, 0.35):
        ax.plot(
            [cx - 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang)),
             cx + 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang))],
            [cy - 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang)),
             cy + 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang))],
            color="#7a2e14", linewidth=1,
        )

    # golgi stack (R)
    for i in range(5):
        xs = np.linspace(5.6, 7.6, 30)
        ys = (2.9 - i * 0.32) + 0.12 * np.sin(np.linspace(0, np.pi, 30))
        ax.plot(xs, ys, color="#1b6e6e", linewidth=2.2)

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(3.75, 5.5, 1.6, 6.5, "P")
    label(6.6, 3.3, 8.7, 2.2, "Q")
    label(6.6, 2.6, 8.7, 1.0, "R")
    label(6.9, 7.0, 8.7, 8.0, "S")

    save(fig, "q4_cell_diagram_pqrs.png")


# ---------------------------------------------------------------
# Q110: titration curve, 25 mL HCl titrated with NaOH, equivalence at 25 mL
# ---------------------------------------------------------------
def titration_curve_naoh_hcl():
    # Same scenario as mock_1's Q110 (strong acid + strong base, 25 mL,
    # equivalence at 25 mL) produced a byte-identical PNG there -- give this
    # one a distinct steepness/color/marker style so the two mocks don't
    # ship the exact same image file for two different questions.
    v = np.linspace(0, 50, 400)
    ph = 1.5 + 11.5 / (1 + np.exp(-0.65 * (v - 25)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#6b3fa0", linewidth=2.5)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.plot(25, 7, "o", color="#6b3fa0", markersize=7, zorder=5)
    ax.set_title("Titration Curve: HCl (25 mL) titrated with NaOH", fontsize=14, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q4_titration_curve_naoh_hcl.png")


# ---------------------------------------------------------------
# Q154: R1(3) || R2(3) = 1.5, in series with R3(2) -> 3.5 ohm
# ---------------------------------------------------------------
def circuit_diagram_r1r2r3():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.add_patch(plt.Circle((1, 3), 0.6, facecolor="white", edgecolor="black", linewidth=2))
    ax.text(1, 3.28, "+", ha="center", va="center", fontsize=13)
    ax.text(1, 2.72, "-", ha="center", va="center", fontsize=13)
    ax.text(1, 1.9, "12 V", ha="center", va="center", fontsize=12)

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

    # R1 and R2 in parallel first (left block), then in series with R3 (right)
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 3 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 3 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)   # join parallel top nodes
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)  # join parallel bottom nodes

    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 2 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q4_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: convex lens, object beyond 2F -> real, inverted, diminished
# ---------------------------------------------------------------
def lens_diagram_object_beyond_2f():
    f = 2.0
    obj_x, obj_h = -3 * f, 1.5   # beyond 2F

    slope2 = obj_h / obj_x
    img_x = 1.0 / (1.0 / f + 1.0 / obj_x)
    img_h = slope2 * img_x

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 2 * f + 2)
    ax.set_ylim(img_h - 1.5, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object beyond 2F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [img_h - 1.2, obj_h + 1.2], color="#2f6f9f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # real image (red, inverted, diminished)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis -> refracts through far focal point -> image tip
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)

    # ray 2: through optical center, undeviated
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    save(fig, "q4_lens_diagram_object_beyond_2f.png")


if __name__ == "__main__":
    enzyme_temp_graph()
    cell_diagram_pqrs()
    titration_curve_naoh_hcl()
    circuit_diagram_r1r2r3()
    lens_diagram_object_beyond_2f()

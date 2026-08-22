"""Generate the 5 diagram/graph images referenced by mdcat_mock_1.py's
image-based questions (Q8, Q10, Q110, Q154, Q162). These recreate the
diagrams supplied for this mock in matplotlib since the pasted images
couldn't be saved to disk directly.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q8: enzyme activity vs temperature
# ---------------------------------------------------------------
def enzyme_graph():
    t = np.linspace(0, 70, 400)
    rate = np.where(
        t <= 40,
        100 * (1 - np.exp(-t / 12)),
        100 * np.exp(-((t - 40) ** 2) / (2 * 6.5 ** 2)),
    )
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(t, rate, color="#1b6e6e", linewidth=2.5)
    ax.fill_between(t, rate, color="#1b6e6e", alpha=0.08)
    ax.set_title("Effect of Temperature on Enzyme Activity", fontsize=15, fontweight="bold")
    ax.set_xlabel("Temperature (°C)", fontsize=12)
    ax.set_ylabel("Rate of Enzyme Activity (%)", fontsize=12)
    ax.set_xlim(0, 70)
    ax.set_ylim(0, 110)
    ax.grid(alpha=0.3)
    save(fig, "q_enzyme_graph.png")


# ---------------------------------------------------------------
# Q10: animal cell diagram, A=mitochondrion, B=nucleus, C=ER/golgi, D=ribosomes
# ---------------------------------------------------------------
def cell_diagram():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of an Animal Cell", fontsize=16, fontweight="bold")

    # cell membrane
    ax.add_patch(Ellipse((5, 5), 8.6, 7.6, facecolor="#fdf6e3", edgecolor="#6b5b1e", linewidth=2.5))

    # nucleus (B)
    ax.add_patch(Ellipse((3.6, 5.6), 2.6, 2.6, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((3.75, 5.5), 1.0, 1.0, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    # unlabeled vesicle (light blue, top right)
    ax.add_patch(Ellipse((6.9, 7.0), 1.1, 1.1, facecolor="#bfe3f0", edgecolor="#5aa9c4", linewidth=1.5))

    # mitochondria (A - upper, plus a second unlabeled lower one)
    for cx, cy, ang in [(6.7, 5.8, -20), (6.6, 3.3, 20)]:
        m = Ellipse((cx, cy), 1.7, 0.85, angle=ang, facecolor="#d97a55", edgecolor="#a8482a", linewidth=1.5)
        ax.add_patch(m)
        for off in (-0.35, 0, 0.35):
            ax.plot(
                [cx - 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang)),
                 cx + 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang))],
                [cy - 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang)),
                 cy + 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang))],
                color="#7a2e14", linewidth=1,
            )

    # ER (wavy line connecting nucleus to mitochondrion) + ribosome dots on it
    xs = np.linspace(4.5, 6.2, 60)
    ys = 6.2 + 0.35 * np.sin(np.linspace(0, 3 * np.pi, 60))
    ax.plot(xs, ys, color="#2f6f8f", linewidth=2)
    for i in range(0, 60, 6):
        ax.plot(xs[i], ys[i] + 0.12, "o", color="black", markersize=3)

    # golgi-like stacks (C, lower middle) + free ribosome dots (D)
    for i in range(5):
        ax.plot([3.7, 5.7], [2.6 - i * 0.22, 2.6 - i * 0.22], color="#1b6e6e", linewidth=2.5)
    for dx, dy in [(1.9, 2.9), (2.1, 2.5), (1.7, 2.3), (2.3, 2.1)]:
        ax.plot(dx, dy, "o", color="black", markersize=4)

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(6.7, 5.8, 8.7, 6.3, "A")
    label(3.75, 5.5, 1.6, 6.5, "B")
    label(4.7, 2.05, 4.7, 0.7, "C")
    label(2.0, 2.6, 0.7, 1.3, "D")

    save(fig, "q_cell_diagram.png")


# ---------------------------------------------------------------
# Q110: titration curve, HCl (25 mL) titrated with NaOH, equivalence at 25 mL
# ---------------------------------------------------------------
def titration_curve():
    v = np.linspace(0, 50, 400)
    ph = 1.5 + 11.5 / (1 + np.exp(-0.9 * (v - 25)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#a8332c", linewidth=2.5)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.set_title("Titration Curve: HCl (25 mL) titrated with NaOH", fontsize=14, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.3)
    save(fig, "q_titration_curve.png")


# ---------------------------------------------------------------
# Q154: circuit R1(series)=4, R2 || R3 = 6,6
# ---------------------------------------------------------------
def circuit_diagram():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # source
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
            ax.text(midx, midy + 0.55, label, ha="center", fontsize=12)
        else:
            ax.text(midx + 0.9, midy, label, ha="center", fontsize=12)

    # wires + R1 across the top
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)
    resistor(3, 5, 5, 5, "R1 = 4 Ω")
    ax.plot([5, 5], [5, 5], color="black", linewidth=2)
    ax.plot([5, 5], [5, 0.5], color="black", linewidth=2)  # node drop (junction)
    ax.plot([5, 8.5], [5, 5], color="black", linewidth=2)

    # R2 branch (parallel, straight down at x=5)
    resistor(5, 4.0, 5, 1.7, "R2 = 6 Ω")
    ax.plot([5, 5], [1.7, 0.5], color="black", linewidth=2)

    # R3 branch (parallel, straight down at x=8.5)
    ax.plot([8.5, 8.5], [5, 4.0], color="black", linewidth=2)
    resistor(8.5, 4.0, 8.5, 1.7, "R3 = 6 Ω")
    ax.plot([8.5, 8.5], [1.7, 0.5], color="black", linewidth=2)

    # bottom rail back to source
    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q_circuit_diagram.png")


# ---------------------------------------------------------------
# Q162: convex lens ray diagram, object at 2F -> image at 2F, real/inverted/same size
# ---------------------------------------------------------------
def lens_diagram():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-4, 4)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object placed at 2F)", fontsize=15, fontweight="bold")

    f = 2.0
    obj_x, obj_h = -2 * f, 2.2
    img_x, img_h = 2 * f, -2.2

    # principal axis
    ax.axhline(0, color="black", linewidth=1.2)
    # lens (double arrow vertical line)
    ax.plot([0, 0], [-3.2, 3.2], color="#2f6f9f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.35, lbl, ha="center", fontsize=12, color="gray" if abs(x) == 2 * f else "black")

    # object arrow (green)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.35, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # image arrow (red, inverted)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.45, "Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis -> refracts through far focal point -> image tip
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)

    # ray 2: through optical center, undeviated (dashed)
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    # ray 3: through near focal point -> emerges parallel to axis -> image tip
    ax.plot([obj_x, 0], [obj_h, 0], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [0, img_h], color="#333", linewidth=1.6)

    save(fig, "q_lens_diagram.png")


if __name__ == "__main__":
    enzyme_graph()
    cell_diagram()
    titration_curve()
    circuit_diagram()
    lens_diagram()

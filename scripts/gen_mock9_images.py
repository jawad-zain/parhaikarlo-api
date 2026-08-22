"""Generate the 5 diagram/graph images referenced by mdcat_mock_9.py's
image-based questions (Q8 rate-vs-enzyme-concentration linear graph,
Q14 animal cell W/X/Y/Z with Z=lysosome, Q110 strong-acid/strong-base
titration, Q154 R1||R2 series R3, Q162 convex/diverging mirror diagram).
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
# Q8: initial reaction rate vs enzyme concentration, substrate in excess
# -- linear relationship
# ---------------------------------------------------------------
def enzyme_concentration_graph():
    e = np.linspace(0, 10, 100)
    rate = 9.5 * e
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(e, rate, color="#1b6e6e", linewidth=2.5)
    ax.set_title("Initial Reaction Rate vs Enzyme Concentration\n(Substrate in Excess)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Enzyme Concentration", fontsize=12)
    ax.set_ylabel("Initial Reaction Rate", fontsize=12)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q9_enzyme_concentration_graph.png")


# ---------------------------------------------------------------
# Q14: animal cell, W=nucleus, X=mitochondrion, Y=Golgi, Z=lysosome
# ---------------------------------------------------------------
def cell_diagram_wxyz():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of an Animal Cell", fontsize=16, fontweight="bold")

    ax.add_patch(Ellipse((5, 5), 8.6, 7.6, facecolor="#fdf6e3", edgecolor="#6b5b1e", linewidth=2.5))

    # nucleus (W)
    ax.add_patch(Ellipse((3.4, 5.7), 2.6, 2.6, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((3.55, 5.6), 1.0, 1.0, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    # mitochondrion (X)
    cx, cy, ang = 6.7, 6.6, -15
    ax.add_patch(Ellipse((cx, cy), 1.7, 0.85, angle=ang, facecolor="#d97a55", edgecolor="#a8482a", linewidth=1.5))
    for off in (-0.35, 0, 0.35):
        ax.plot(
            [cx - 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang)),
             cx + 0.5 * np.cos(np.radians(ang)) - off * np.sin(np.radians(ang))],
            [cy - 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang)),
             cy + 0.5 * np.sin(np.radians(ang)) + off * np.cos(np.radians(ang))],
            color="#7a2e14", linewidth=1,
        )

    # golgi stack (Y)
    for i in range(5):
        xs = np.linspace(5.6, 7.4, 30)
        ys = (3.4 - i * 0.32) + 0.12 * np.sin(np.linspace(0, np.pi, 30))
        ax.plot(xs, ys, color="#1b6e6e", linewidth=2.2)

    # lysosome (Z)
    ax.add_patch(Ellipse((2.9, 2.6), 1.0, 1.0, facecolor="#e6c34a", edgecolor="#a8842a", linewidth=1.5))

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(3.55, 5.6, 1.6, 7.6, "W")
    label(6.7, 6.6, 8.7, 7.7, "X")
    label(6.5, 3.1, 8.7, 2.4, "Y")
    label(2.9, 2.6, 1.2, 1.2, "Z")

    save(fig, "q9_cell_diagram_wxyz.png")


# ---------------------------------------------------------------
# Q110: strong acid (HCl) + strong base (NaOH), equivalence pH = 7.0
# ---------------------------------------------------------------
def titration_strong_acid_strong_base():
    v = np.linspace(0, 50, 400)
    ph = 1.0 + 12.9 / (1 + np.exp(-0.75 * (v - 25)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#c2622f", linewidth=2.8)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.plot(25, 7, "o", color="#c2622f", markersize=7, zorder=5)
    ax.text(26, 5.8, "equivalence point\n(pH = 7.0)", fontsize=10, color="#c2622f")
    ax.set_title("Titration Curve: Strong Acid (HCl) with Strong Base (NaOH)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q9_titration_strong_acid_strong_base.png")


# ---------------------------------------------------------------
# Q154: R1(10) || R2(15) = 6, in series with R3(2) -> 8 ohm
# ---------------------------------------------------------------
def circuit_diagram_r1r2r3():
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

    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 10 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 15 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 2 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q9_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: convex (diverging) mirror -- image always virtual, upright,
# diminished, formed behind the mirror, regardless of object distance.
# ---------------------------------------------------------------
def convex_mirror_diagram():
    f = 2.0  # magnitude; convex mirror has virtual focus behind mirror
    obj_x, obj_h = -5.0, 1.6

    u_mag = abs(obj_x)
    # convex mirror formula (virtual focus): 1/v - 1/u = 1/f (magnitudes,
    # image always virtual/behind mirror) -> v = (f*u)/(f+u)
    v_mag = (f * u_mag) / (f + u_mag)
    img_x = v_mag  # behind the mirror (positive side, away from object)
    img_h = obj_h * (v_mag / u_mag)  # upright, diminished

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 4)
    ax.set_ylim(-1.0, obj_h + 1.2)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex (Diverging) Mirror", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # Convex mirror: center of curvature C is BEHIND the mirror (opposite
    # side from the object), so the surface recedes away from the object
    # at the edges -- POSITIVE-coefficient parabola (a negative
    # coefficient draws a concave mirror shape instead).
    yy = np.linspace(-2.2, 2.2, 100)
    xx = 0.09 * yy**2
    ax.plot(xx, yy, color="#3a5f8f", linewidth=3)

    for x, lbl in [(f, "F"), (2 * f, "C"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h + 0.25, "Image\n(virtual)", color="#a8332c", fontsize=11, ha="center")

    # ray 1: parallel to axis, reflects as if diverging from focal point F
    # (behind mirror) -- draw incident ray, then the reflected ray and its
    # backward extension (dashed) meeting the image
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    # reflected ray direction: appears to come from F; slope beyond mirror
    slope_reflected = obj_h / f
    ax.plot([0, 3.5], [obj_h, obj_h - slope_reflected * 3.5], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    # ray 2: directed toward C (behind mirror), reflects straight back
    slope2 = (0 - obj_h) / (2 * f - obj_x)
    mirror_y_at_0 = obj_h + slope2 * (0 - obj_x)
    ax.plot([obj_x, 0], [obj_h, mirror_y_at_0], color="#333", linewidth=1.2, linestyle=":")
    ax.plot([0, img_x], [mirror_y_at_0, img_h], color="#333", linewidth=1.2, linestyle=":")

    save(fig, "q9_convex_mirror_diagram.png")


if __name__ == "__main__":
    enzyme_concentration_graph()
    cell_diagram_wxyz()
    titration_strong_acid_strong_base()
    circuit_diagram_r1r2r3()
    convex_mirror_diagram()

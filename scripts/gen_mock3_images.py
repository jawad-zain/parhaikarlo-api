"""Generate the 5 diagram/graph images referenced by mdcat_mock_3.py's
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
# Q8: enzyme activity vs pH, sharp peak near pH 2 (pepsin-like, stomach)
# ---------------------------------------------------------------
def enzyme_ph_graph():
    ph = np.linspace(0, 14, 400)
    activity = 100 * np.exp(-((ph - 2) ** 2) / (2 * 0.9 ** 2))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(ph, activity, color="#1b6e6e", linewidth=2.5)
    ax.fill_between(ph, activity, color="#1b6e6e", alpha=0.08)
    ax.set_title("Effect of pH on Enzyme Activity", fontsize=15, fontweight="bold")
    ax.set_xlabel("pH", fontsize=12)
    ax.set_ylabel("Rate of Enzyme Activity (%)", fontsize=12)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 110)
    ax.grid(alpha=0.3)
    save(fig, "q_enzyme_ph_graph.png")


# ---------------------------------------------------------------
# Q14: animal cell, W=mitochondrion, X=Golgi, Y=nucleus, Z=lysosome
# ---------------------------------------------------------------
def cell_diagram_wxyz():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of an Animal Cell", fontsize=16, fontweight="bold")

    ax.add_patch(Ellipse((5, 5), 8.6, 7.6, facecolor="#fdf6e3", edgecolor="#6b5b1e", linewidth=2.5))

    # nucleus (Y)
    ax.add_patch(Ellipse((3.6, 5.6), 2.6, 2.6, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((3.75, 5.5), 1.0, 1.0, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    # lysosome (Z) - small circle
    ax.add_patch(Ellipse((6.9, 7.0), 1.0, 1.0, facecolor="#e6c34a", edgecolor="#a8842a", linewidth=1.5))

    # mitochondrion (W)
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

    # golgi stack (X) - flattened membrane sacs, curved
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

    label(6.6, 3.3, 8.7, 2.2, "W")
    label(6.6, 2.6, 8.7, 1.0, "X")
    label(3.75, 5.5, 1.6, 6.5, "Y")
    label(6.9, 7.0, 8.7, 8.0, "Z")

    save(fig, "q_cell_diagram_wxyz.png")


# ---------------------------------------------------------------
# Q110: titration curve, 20 mL NaOH titrated with HCl -- pH falls from high to low
# ---------------------------------------------------------------
def titration_curve_hcl_naoh():
    v = np.linspace(0, 40, 400)
    ph = 13 - 11.5 / (1 + np.exp(-0.9 * (v - 20)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#a8332c", linewidth=2.5)
    ax.axvline(20, color="gray", linestyle="--", linewidth=1.2)
    ax.set_title("Titration Curve: NaOH (20 mL) titrated with HCl", fontsize=14, fontweight="bold")
    ax.set_xlabel("Volume of HCl added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.3)
    save(fig, "q_titration_curve_hcl_naoh.png")


# ---------------------------------------------------------------
# Q154: R1(4) + R2(2) in series = 6, parallel with R3(6) -> 3 ohm
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

    # top rail: R1 then R2 in series, into the right node
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 2.5], [5, 5], color="black", linewidth=2)
    resistor(2.5, 5, 4.2, 5, "R1 = 4 Ω")
    resistor(4.2, 5, 5.9, 5, "R2 = 2 Ω")
    ax.plot([5.9, 8.5], [5, 5], color="black", linewidth=2)

    # right branch node drops down through R3, parallel to (R1+R2)
    ax.plot([8.5, 8.5], [5, 4.0], color="black", linewidth=2)
    resistor(8.5, 4.0, 8.5, 1.7, "R3 = 6 Ω")
    ax.plot([8.5, 8.5], [1.7, 0.5], color="black", linewidth=2)

    # bottom rail back to source
    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: convex lens, object between F and lens -> virtual, upright, magnified
# ---------------------------------------------------------------
def lens_diagram_object_inside_f():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-6.5, 8.5)
    ax.set_ylim(-3, 5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object between F and Lens)", fontsize=14, fontweight="bold")

    f = 2.0
    obj_x, obj_h = -1.2, 1.0   # between lens (0) and F (-f)

    # Virtual image = intersection of the backward extensions of:
    #  ray 1 emergent line: y = obj_h - (obj_h/f)*x   (parallel-in, through F-out)
    #  ray 2 line (through center, undeviated): y = (obj_h/obj_x)*x
    slope2 = obj_h / obj_x
    img_x = 1.0 / (1.0 / f + 1.0 / obj_x)
    img_h = slope2 * img_x

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [-3.2, 3.8], color="#2f6f9f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.35, lbl, ha="center", fontsize=12, color="gray")

    # object (green)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.3, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # virtual image (red, upright, magnified, same side as object)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h + 0.3, "Virtual Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis from object tip -> real refracted ray toward F on the far side
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, 3.5], [obj_h, obj_h - (obj_h / f) * 3.5], color="#333", linewidth=1.6)
    # backward extension (dashed) of that emergent ray to the virtual image tip
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    # ray 2: through optical center, undeviated -- real forward portion solid,
    # backward portion (object -> virtual image) dashed
    ax.plot([obj_x, 3.5], [obj_h, slope2 * 3.5], color="#333", linewidth=1.6)
    ax.plot([img_x, obj_x], [img_h, obj_h], color="#333", linewidth=1.2, linestyle="--")

    save(fig, "q_lens_diagram_object_inside_f.png")


if __name__ == "__main__":
    enzyme_ph_graph()
    cell_diagram_wxyz()
    titration_curve_hcl_naoh()
    circuit_diagram_r1r2r3()
    lens_diagram_object_inside_f()

"""Generate the 5 diagram images referenced by mdcat_phy_practice2.py's
image-based questions (all Physics, standalone practice bank #2):

  Q19  Vectors & Equilibrium - vector A on a coordinate grid with
       components Ax=6, Ay=8 labeled -> magnitude 10, angle 53.1 deg.
  Q134 Current Electricity   - R1(5 ohm)+R2(5 ohm) in SERIES, that
       series branch in PARALLEL with R3(10 ohm) -> total 5 ohm.
  Q146 Electromagnetism      - straight wire (I=5A) perpendicular to a
       uniform magnetic field (B=0.2T, into the page) over 0.5 m of its
       length -> F = BIL = 0.5 N, direction via the right-hand rule.
  Q158 Electromagnetic Induction & AC - step-up transformer,
       Np=100 turns (primary) < Ns=400 turns (secondary), Vp=20V AC ->
       Vs = Vp*(Ns/Np) = 80V.
  Q194 Optics - concave mirror, object BETWEEN the focal point (F) and
       the mirror (i.e. "within F") -> virtual, upright, magnified
       image formed behind the mirror. Derived via the mirror formula
       1/v + 1/u = 1/f (real-is-positive convention), not eyeballed.

Filenames were checked against the existing mdcat-content/images/
directory before writing this script -- none collide with any prior
mock/past-paper/practice image.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q19: Vector A with components Ax=6, Ay=8 on a coordinate grid.
# Magnitude = sqrt(6^2+8^2) = 10, angle = atan(8/6) = 53.13 deg.
# ---------------------------------------------------------------
def vector_components_diagram():
    ax_val, ay_val = 6, 8
    mag = (ax_val**2 + ay_val**2) ** 0.5
    angle = np.degrees(np.arctan2(ay_val, ax_val))

    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 10)
    ax.set_aspect("equal")
    ax.set_title("Vector A on a Coordinate Grid", fontsize=14, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.grid(True, linestyle=":", color="#bbb", linewidth=0.7)

    # component: Ax (horizontal, dashed)
    ax.annotate("", xy=(ax_val, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.2))
    ax.text(ax_val / 2, -0.55, f"Ax = {ax_val}", color="#1a7a3a", fontsize=12, ha="center")

    # component: Ay (vertical, dashed, drawn from the tip of Ax up to A's tip)
    ax.annotate("", xy=(ax_val, ay_val), xytext=(ax_val, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.2, linestyle="dashed"))
    ax.text(ax_val + 0.3, ay_val / 2, f"Ay = {ay_val}", color="#a8332c", fontsize=12, va="center")

    # resultant vector A (from origin to tip)
    ax.annotate("", xy=(ax_val, ay_val), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1f4e9c", linewidth=3))
    ax.text(ax_val * 0.4, ay_val * 0.55, "A", color="#1f4e9c", fontsize=16, fontweight="bold")

    # angle arc at origin between +x axis and vector A
    theta = np.linspace(0, np.radians(angle), 40)
    r = 1.3
    ax.plot(r * np.cos(theta), r * np.sin(theta), color="#555", linewidth=1.3)
    ax.text(1.8, 0.55, f"{angle:.1f}°", color="#555", fontsize=11)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    save(fig, "q_vector_components_diagram.png")


# ---------------------------------------------------------------
# Q134: R1(5) and R2(5) in SERIES, forming one branch; that whole
# branch is in PARALLEL with R3(10). Total = 1/(1/10 + 1/10) = 5 ohm.
# ---------------------------------------------------------------
def circuit_series_then_parallel():
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
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
            ax.text(midx + 1.0, midy, label, ha="center", fontsize=11)

    # lead from battery up to the top rail, which splits into two branches
    ax.plot([1, 1], [3.6, 5.4], color="black", linewidth=2)
    ax.plot([1, 3], [5.4, 5.4], color="black", linewidth=2)

    # branch A: top node -> R1 -> R2 -> bottom node (series branch)
    ax.plot([3, 3], [5.4, 4.6], color="black", linewidth=2)
    resistor(3, 4.6, 3, 3.4, "R1 = 5 Ω")
    ax.plot([3, 3], [3.4, 2.6], color="black", linewidth=2)
    resistor(3, 2.6, 3, 1.4, "R2 = 5 Ω")
    ax.plot([3, 3], [1.4, 0.6], color="black", linewidth=2)

    # branch B: top node -> R3 -> bottom node (parallel branch)
    ax.plot([3, 5.6], [5.4, 5.4], color="black", linewidth=2)
    ax.plot([5.6, 5.6], [5.4, 3.6], color="black", linewidth=2)
    resistor(5.6, 3.6, 5.6, 1.9, "R3 = 10 Ω")
    ax.plot([5.6, 5.6], [1.9, 0.6], color="black", linewidth=2)
    ax.plot([3, 5.6], [0.6, 0.6], color="black", linewidth=2)

    # right-side wire back to the battery
    ax.plot([5.6, 8.5], [5.4, 5.4], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5.4, 0.6], color="black", linewidth=2)
    ax.plot([1, 1], [2.4, 0.6], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.6, 0.6], color="black", linewidth=2)

    ax.text(5, 0.05,
            "R1 + R2 (series) = 10 Ω, in parallel with R3 = 10 Ω → total = 5 Ω",
            ha="center", fontsize=9, style="italic")

    save(fig, "q_circuit_series_parallel_physics200.png")


# ---------------------------------------------------------------
# Q146: Straight current-carrying wire perpendicular to a uniform
# magnetic field. I = 5 A (to the right, +x), B = 0.2 T into the page
# (-z), over L = 0.5 m of wire. F = BIL = 0.2*5*0.5 = 0.5 N.
# Direction by the right-hand rule: F = I L(+x) x B(-z) = I L B (+y)
# i.e. the force on the wire is straight UP (away from the field
# region as drawn), for current-to-the-right / field-into-the-page.
# ---------------------------------------------------------------
def wire_in_magnetic_field_diagram():
    I, B, L = 5, 0.2, 0.5
    F = B * I * L

    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 6)
    ax.axis("off")
    ax.set_title("Current-Carrying Wire in a Uniform Magnetic Field", fontsize=13, fontweight="bold")

    # shaded field region (into the page), shown with x symbols
    field_x0, field_x1 = 1.5, 6.5
    field_y0, field_y1 = 1, 4
    ax.add_patch(plt.Rectangle((field_x0, field_y0), field_x1 - field_x0, field_y1 - field_y0,
                                facecolor="#eef2fb", edgecolor="#7a8fc0", linewidth=1.5, zorder=0))
    xs = np.linspace(field_x0 + 0.5, field_x1 - 0.5, 6)
    ys = np.linspace(field_y0 + 0.5, field_y1 - 0.5, 4)
    for yv in ys:
        for xv in xs:
            ax.plot(xv, yv, marker="x", color="#4a5a8a", markersize=9, markeredgewidth=2, zorder=1)
    ax.text((field_x0 + field_x1) / 2, field_y1 + 0.35, "B = 0.2 T (into the page)",
            color="#4a5a8a", fontsize=11, ha="center")

    # the wire, horizontal, running through the field region, current to the right
    wire_y = (field_y0 + field_y1) / 2
    ax.plot([0, 8], [wire_y, wire_y], color="black", linewidth=3, zorder=2)
    ax.annotate("", xy=(field_x1 + 1.2, wire_y), xytext=(field_x1 + 0.2, wire_y),
                arrowprops=dict(arrowstyle="-|>", color="black", linewidth=2.5), zorder=3)
    ax.text(0.5, wire_y + 0.45, "I = 5 A", color="black", fontsize=12, ha="center", zorder=3)

    # mark the 0.5 m segment of wire inside the field, below the whole
    # field box so it doesn't overlap the x-symbols or the wire itself
    label_y = field_y0 - 0.55
    ax.annotate("", xy=(field_x1, label_y), xytext=(field_x0, label_y),
                arrowprops=dict(arrowstyle="<->", color="#333", linewidth=1.3))
    ax.text((field_x0 + field_x1) / 2, label_y - 0.3, "L = 0.5 m", color="#333", fontsize=10, ha="center")

    # resultant force on the wire, straight up (right-hand rule: I(+x) x B(-z) = +y)
    force_x = field_x1 - 0.8
    ax.annotate("", xy=(force_x, wire_y + 2.3), xytext=(force_x, wire_y),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=3), zorder=4)
    ax.text(force_x + 0.4, wire_y + 2.3, f"F = BIL = {F:.2f} N", color="#a8332c",
            fontsize=12, fontweight="bold")

    save(fig, "q_wire_in_magnetic_field_diagram.png")


# ---------------------------------------------------------------
# Q158: Step-up transformer, Np=100 turns (primary, fewer loops drawn)
# < Ns=400 turns (secondary, more loops drawn), Vp=20V AC.
# Vs = Vp * (Ns/Np) = 20 * (400/100) = 80 V.
# ---------------------------------------------------------------
def transformer_diagram():
    Np, Ns, Vp = 100, 400, 20
    Vs = Vp * (Ns / Np)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.6, 7)
    ax.axis("off")
    ax.set_title("Step-Up Transformer", fontsize=14, fontweight="bold")

    # laminated iron core: two vertical bars joined top and bottom
    core_x0, core_x1 = 5.3, 6.3
    core_y0, core_y1 = 1, 6
    for x in (core_x0, core_x1):
        ax.add_patch(plt.Rectangle((x - 0.15, core_y0), 0.3, core_y1 - core_y0,
                                    facecolor="#cfcfcf", edgecolor="black", linewidth=1.3, zorder=1))
    ax.add_patch(plt.Rectangle((core_x0 - 0.15, core_y1 - 0.3), core_x1 - core_x0 + 0.3, 0.3,
                                facecolor="#cfcfcf", edgecolor="black", linewidth=1.3, zorder=1))
    ax.add_patch(plt.Rectangle((core_x0 - 0.15, core_y0), core_x1 - core_x0 + 0.3, 0.3,
                                facecolor="#cfcfcf", edgecolor="black", linewidth=1.3, zorder=1))

    def coil(x, n_loops, y0, y1, color, side):
        ys = np.linspace(y0, y1, n_loops + 1)
        r = 0.35
        for i in range(n_loops):
            yc = (ys[i] + ys[i + 1]) / 2
            theta = np.linspace(0, 2 * np.pi, 40)
            if side == "left":
                xx = x - r * np.cos(theta)
            else:
                xx = x + r * np.cos(theta)
            yy = yc + (ys[i + 1] - ys[i]) / 2 * np.sin(theta)
            ax.plot(xx, yy, color=color, linewidth=2, zorder=2)
        ax.plot([x, x], [y0 - 0.4, y0], color=color, linewidth=2, zorder=2)
        ax.plot([x, x], [y1, y1 + 0.4], color=color, linewidth=2, zorder=2)

    # primary coil: 100 turns -> fewer loops drawn (4), on the left of the core
    coil(core_x0 - 0.35, 4, 1.6, 5.4, "#1f4e9c", "left")
    # secondary coil: 400 turns -> more loops drawn (10), on the right of the core
    coil(core_x1 + 0.35, 10, 1.2, 5.8, "#a8332c", "right")

    ax.text(core_x0 - 1.3, 0.65, f"Primary\nNp = {Np} turns", color="#1f4e9c", fontsize=10.5,
            ha="center", fontweight="bold")
    ax.text(core_x1 + 1.3, 0.65, f"Secondary\nNs = {Ns} turns", color="#a8332c", fontsize=10.5,
            ha="center", fontweight="bold")

    # AC source symbol on the primary side
    ax.add_patch(plt.Circle((core_x0 - 2.3, 3.5), 0.5, facecolor="white", edgecolor="#1f4e9c", linewidth=2))
    xx_wave = np.linspace(-0.3, 0.3, 60)
    ax.plot(core_x0 - 2.3 + xx_wave, 3.5 + 0.22 * np.sin(xx_wave * 18), color="#1f4e9c", linewidth=1.6)
    ax.plot([core_x0 - 2.3, core_x0 - 0.35 - 0.4], [4.0, 5.4], color="#1f4e9c", linewidth=2)
    ax.plot([core_x0 - 2.3, core_x0 - 0.35 - 0.4], [3.0, 1.6], color="#1f4e9c", linewidth=2)
    ax.text(core_x0 - 2.3, 2.55, f"Vp = {Vp} V (AC)", color="#1f4e9c", fontsize=10.5, ha="center")

    # output leads on the secondary side (open circuit, showing Vs)
    ax.plot([core_x1 + 0.35 + 0.4, core_x1 + 2.3], [5.8, 5.0], color="#a8332c", linewidth=2)
    ax.plot([core_x1 + 0.35 + 0.4, core_x1 + 2.3], [1.2, 2.0], color="#a8332c", linewidth=2)
    ax.text(core_x1 + 2.3, 3.5, f"Vs = ?", color="#a8332c", fontsize=11, ha="center", fontweight="bold")
    ax.text(core_x1 + 2.3, 0.0, f"(answer: Vs = {Vs:.0f} V)", color="#333", fontsize=9, ha="center", style="italic")

    save(fig, "q_transformer_primary_secondary_diagram.png")


# ---------------------------------------------------------------
# Q194: Concave mirror, object BETWEEN F and the mirror (i.e. within
# F) -> virtual, upright, magnified image behind the mirror.
# Mirror formula (real-is-positive convention, u positive = object
# distance in front of mirror): 1/v + 1/u = 1/f
#   f = 2.0, u = 1.2 (within F, u < f)  -- distinct values from any
#   prior mock's concave-mirror-within-F diagram, to avoid an
#   MD5-identical render.
#   1/v = 1/f - 1/u => v negative => virtual image, behind mirror.
#   m = -v/u (positive => upright, magnified when |m| > 1).
# ---------------------------------------------------------------
def concave_mirror_within_f():
    f = 2.0
    R = 2 * f
    u = 1.2
    obj_h = 0.9

    v = 1.0 / (1.0 / f - 1.0 / u)
    m = -v / u
    img_h = m * obj_h

    assert v < 0, "expected a virtual image for object within F"
    assert m > 1, "expected a magnified, upright image for object within F"

    obj_x = -u
    img_x = -v

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(-R - 0.8, img_x + 1.5)
    ax.set_ylim(-1.5, img_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave Mirror (Object Between F and the Mirror)",
                 fontsize=13.5, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # Concave mirror bulges TOWARD the object: x(y) = -k*y**2.
    yy = np.linspace(-2.6, 2.6, 100)
    xx = -0.09 * yy**2
    ax.plot(xx, yy, color="#2f6f9f", linewidth=3)

    for x, lbl in [(-R, "C"), (-f, "F"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green), between F and the mirror
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # virtual image (red, dashed, upright, magnified, BEHIND the mirror)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5, linestyle="dashed"))
    ax.text(img_x, img_h + 0.25, "Virtual Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis from object tip -> reflects through F;
    # backward extension (dashed) meets the other backward ray at the image.
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    slope1 = (obj_h - 0) / (0 - (-f))
    ax.plot([0, img_x], [obj_h, obj_h - slope1 * (img_x - 0)], color="#333", linewidth=1.2, linestyle="--")

    # ray 2: from object tip through the pole P, reflecting at the same
    # angle below the axis; its backward extension also passes through
    # the virtual image tip.
    ax.plot([obj_x, 0], [obj_h, 0], color="#555", linewidth=1.6)
    slope2 = obj_h / (0 - obj_x)
    reflect_y_at_imgx = -slope2 * (img_x - 0)
    ax.plot([0, img_x], [0, reflect_y_at_imgx], color="#555", linewidth=1.2, linestyle="--")
    ax.plot(img_x, img_h, "o", color="#a8332c", markersize=5, zorder=5)

    ax.text((obj_x + img_x) / 2, img_h + 0.9,
            f"u = {u}, f = {f}: virtual, upright, magnified (m = {m:.2f})",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_concave_mirror_object_between_f_and_mirror.png")


if __name__ == "__main__":
    vector_components_diagram()
    circuit_series_then_parallel()
    wire_in_magnetic_field_diagram()
    transformer_diagram()
    concave_mirror_within_f()

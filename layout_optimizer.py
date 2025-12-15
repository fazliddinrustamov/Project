# Students IDs: b250072, b250254, b251113, b251236, b251421, b250229, b250976, b250516
# Academic integrity statement: We affirm originality and proper attribution for this assignment.

import sympy as sp
import matplotlib.pyplot as plt

# Symbolic parameters
screen_width = sp.symbols('screen_width', positive=True)
screen_height = screen_width * 9 / 16  # 16:9 aspect ratio

camera_diameter = sp.symbols('camera_diameter', positive=True)
button_diameter = sp.symbols('button_diameter', positive=True)
padding = sp.symbols('padding', positive=True)          # equal padding all around
space_between = sp.symbols('space_between', positive=True)

# Parametric panel dimensions
panel_width = screen_width + 2 * padding
panel_height = (
    padding +               # top
    camera_diameter +
    space_between +
    screen_height +
    space_between +
    button_diameter +
    padding                 # bottom
)

# Areas and UI efficiency metric
panel_area = panel_width * panel_height
usable_area = screen_width * screen_height                  # UI usable = screen area
usable_ratio = usable_area / panel_area                     # how much of panel is useful UI


# Numerical configuration
values = {
    screen_width: 80,       # mm
    camera_diameter: 10,
    button_diameter: 18,
    padding: 15,
    space_between: 8
}

print("NUMERICAL EXAMPLE:")
print(f"Panel area: {panel_area.subs(values):.0f} mm²")
print(f"Usable screen area: {usable_area.subs(values):.0f} mm²")
print(f"UI Efficiency: {usable_ratio.subs(values)*100:.1f}%")

# Visualization 1 — Padding vs UI Efficiency
padding_vals = []
ratio_vals = []
for p in range(5, 31, 3):                    # padding from 5 to 30 mm
    subs = values.copy()
    subs[padding] = p
    ratio = usable_ratio.subs(subs)
    padding_vals.append(p)
    ratio_vals.append(float(ratio * 100))

plt.figure(figsize=(8,5))
plt.plot(padding_vals, ratio_vals, 'o-', color='blue')
plt.title("Padding vs Usable Area Efficiency")
plt.xlabel("Padding (mm)")
plt.ylabel("Usable Area (% of panel)")
plt.grid(True)
plt.savefig("padding_vs_efficiency.png")
plt.show()

# Visualization 2 — Screen Size vs UI Efficiency
width_vals = []
ratio_vals2 = []
for w in range(60, 121, 10):                 # screen width 60–120 mm
    subs = values.copy()
    subs[screen_width] = w
    ratio = usable_ratio.subs(subs)
    width_vals.append(w)
    ratio_vals2.append(float(ratio * 100))

plt.figure(figsize=(8,5))
plt.plot(width_vals, ratio_vals2, 's-', color='green')
plt.title("Screen Width vs Usable Area Efficiency")
plt.xlabel("Screen Width (mm)")
plt.ylabel("Usable Area (% of panel)")
plt.grid(True)
plt.savefig("screen_vs_efficiency.png")
plt.show()
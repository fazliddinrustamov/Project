# Students IDs: b250072, b250254, b251113, b251236, b251421, b******, b******, b******
# Academic integrity statement: We affirm originality and proper attribution for this assignment.

import math
import matplotlib.pyplot as plt

# Convert inches to millimeters
def inches_to_mm(inches):
    return inches * 25.4

# Convert screen diagonal to width and height using aspect ratio
def diagonal_to_wh_mm(diag_in, ar_w=16, ar_h=9):
    diag_mm = inches_to_mm(diag_in)
    w = diag_mm * ar_w / math.sqrt(ar_w**2 + ar_h**2)
    h = diag_mm * ar_h / math.sqrt(ar_w**2 + ar_h**2)
    return w, h

def simple_layout(panel_w, panel_h, screen_diag, n_buttons=3,
                  button_diameter=12, screen_ar=(16,9), v_gap=8):

    # --- Screen size ---
    scr_w, scr_h = diagonal_to_wh_mm(screen_diag, screen_ar[0], screen_ar[1])

    # --- Horizontal margin: center the screen ---
    m_x = (panel_w - scr_w) / 2

    # --- Vertical margin: simple symmetric formula ---
    m_y = (panel_h - scr_h - v_gap - button_diameter) / 2
    if m_y < 0:
        m_y = 0  # if screen is too large, just clamp

    # --- Button spacing (center to center) ---
    if n_buttons > 1:
        total_space = scr_w - n_buttons * button_diameter
        spacing = total_space / (n_buttons - 1)
    else:
        spacing = 0

    # --- Button coordinates ---
    group_left = (panel_w - scr_w) / 2
    button_centers = []
    for i in range(n_buttons):
        cx = group_left + button_diameter/2 + i * (button_diameter + spacing)
        cy = m_y + button_diameter/2
        button_centers.append((cx, cy))

    # --- Screen rectangle coordinates ---
    screen_bottom = m_y + button_diameter + v_gap
    screen_left = m_x
    screen_right = screen_left + scr_w
    screen_top = screen_bottom + scr_h

    # --- Area calculations (very simple) ---
    panel_area = panel_w * panel_h
    screen_area = scr_w * scr_h
    buttons_area = n_buttons * math.pi * (button_diameter/2)**2
    usable_area = screen_area + buttons_area
    usable_pct = usable_area / panel_area * 100

    return {
        'panel': (panel_w, panel_h),
        'screen': {
            'left': screen_left, 'right': screen_right,
            'bottom': screen_bottom, 'top': screen_top,
            'width': scr_w, 'height': scr_h
        },
        'buttons': {
            'centers': button_centers,
            'diameter': button_diameter,
            'spacing': spacing
        },
        'margins': {'m_x': m_x, 'm_y': m_y},
        'usable_pct': usable_pct
    }

def draw_layout(result, title='Demo Layout'):

    panel_w, panel_h = result['panel']
    scr = result['screen']
    btn = result['buttons']

    fig, ax = plt.subplots(figsize=(4, 7))

    # Panel
    ax.add_patch(plt.Rectangle((0, 0), panel_w, panel_h, fill=False, linewidth=1.5))

    # Screen
    ax.add_patch(plt.Rectangle((scr['left'], scr['bottom']),
                               scr['width'], scr['height'],
                               fill=False, linewidth=2))

    # Buttons
    for (cx, cy) in btn['centers']:
        ax.add_patch(plt.Circle((cx, cy), btn['diameter']/2, fill=False, linewidth=1.5))

    ax.set_xlim(-5, panel_w + 5)
    ax.set_ylim(-5, panel_h + 5)
    ax.set_aspect('equal')
    ax.set_title(title)

    plt.show()

def print_info(result):
    print("=== Layout Information ===")
    print(f"Panel: {result['panel'][0]} mm × {result['panel'][1]} mm")
    print(f"Screen size: {result['screen']['width']:.1f} × {result['screen']['height']:.1f} mm")
    print(f"Horizontal margin m_x: {result['margins']['m_x']:.1f} mm")
    print(f"Vertical margin m_y: {result['margins']['m_y']:.1f} mm")
    print(f"Usable area percent: {result['usable_pct']:.1f}%")
    print("Button centers:")
    for i, (cx, cy) in enumerate(result['buttons']['centers']):
        print(f"  Button {i+1}: x={cx:.1f}, y={cy:.1f}")

if __name__ == '__main__':
    # Example demo values
    panel_w = 85
    panel_h = 150
    screen_diag = 7.0  # inches
    n_buttons = 3

    result = simple_layout(panel_w, panel_h, screen_diag, n_buttons=n_buttons)
    print_info(result)
    draw_layout(result, title="Simple Demo Layout")

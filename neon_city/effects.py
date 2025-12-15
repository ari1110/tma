"""
Visual effects: power lines, distant lights, glows, etc.
"""

import pyray as rl
import random
import math

from .config import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, PALETTE_NEON


def draw_distant_city_lights():
    """Draw distant city lights in the far background."""
    random.seed(42)  # Fixed seed for consistent positions

    # Distant building lights - tiny dots representing far-off windows
    for _ in range(120):
        x = random.randint(0, VIRTUAL_WIDTH)
        y = random.randint(10, VIRTUAL_HEIGHT // 2 + 30)

        color_choice = random.random()
        if color_choice < 0.6:
            col = rl.Color(150 + random.randint(0, 50), 200 + random.randint(0, 55), 255,
                          random.randint(80, 180))
        elif color_choice < 0.8:
            brightness = random.randint(150, 220)
            col = rl.Color(brightness, brightness, brightness + 20, random.randint(100, 200))
        else:
            col = rl.Color(255, random.randint(150, 220), random.randint(100, 180),
                          random.randint(80, 160))

        size = 1
        rl.draw_rectangle(x, y, size, size, col)

    # Some slightly larger distant signs
    for _ in range(25):
        x = random.randint(0, VIRTUAL_WIDTH)
        y = random.randint(20, VIRTUAL_HEIGHT // 2)
        col = random.choice(PALETTE_NEON)
        faded_col = rl.Color(col.r, col.g, col.b, random.randint(40, 100))
        w = random.randint(2, 4)
        h = random.randint(1, 3)
        rl.draw_rectangle(x, y, w, h, faded_col)

    random.seed()  # Reset seed


def draw_power_lines(t):
    """Draw power lines/cables crossing the scene."""
    line_color = rl.Color(20, 15, 30, 200)

    cable_heights = [45, 55, 70, 90]
    for y in cable_heights:
        sag = 3 if y < 60 else 5
        segments = 8
        seg_w = VIRTUAL_WIDTH // segments
        for i in range(segments):
            x1 = i * seg_w
            x2 = (i + 1) * seg_w
            progress1 = abs(i - segments / 2) / (segments / 2)
            progress2 = abs(i + 1 - segments / 2) / (segments / 2)
            y1 = y + int((1 - progress1 * progress1) * sag)
            y2 = y + int((1 - progress2 * progress2) * sag)
            rl.draw_line(x1, y1, x2, y2, line_color)

    # Diagonal cables
    rl.draw_line(0, 30, VIRTUAL_WIDTH // 3, 80, line_color)
    rl.draw_line(VIRTUAL_WIDTH, 40, VIRTUAL_WIDTH * 2 // 3, 95, line_color)

    # Vertical poles on buildings
    pole_positions = [50, 150, 280, 380]
    for px in pole_positions:
        pole_h = random.Random(px).randint(60, 100)
        rl.draw_line(px, VIRTUAL_HEIGHT - pole_h, px, VIRTUAL_HEIGHT - pole_h - 20,
                     rl.Color(30, 25, 40, 255))


def draw_foreground_railings():
    """Draw railings and structural elements in the foreground."""
    rail_y = VIRTUAL_HEIGHT - 50
    rail_color = rl.Color(30, 20, 40, 255)
    highlight = rl.Color(60, 50, 80, 255)

    rl.draw_rectangle(110, rail_y, VIRTUAL_WIDTH - 110, 3, rail_color)
    rl.draw_rectangle(110, rail_y, VIRTUAL_WIDTH - 110, 1, highlight)
    rl.draw_rectangle(110, rail_y + 8, VIRTUAL_WIDTH - 110, 2, rail_color)

    for x in range(120, VIRTUAL_WIDTH + 40, 50):
        rl.draw_rectangle(x, rail_y - 15, 3, 25, rail_color)
        rl.draw_rectangle(x, rail_y - 15, 1, 25, highlight)

    rl.draw_line_ex(
        rl.Vector2(VIRTUAL_WIDTH - 80, rail_y + 10),
        rl.Vector2(VIRTUAL_WIDTH - 50, VIRTUAL_HEIGHT),
        2,
        rail_color
    )
    rl.draw_line_ex(
        rl.Vector2(VIRTUAL_WIDTH - 40, rail_y + 10),
        rl.Vector2(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT),
        2,
        rail_color
    )


def draw_bottom_neon_glow(t):
    """Draw large neon glow at bottom of screen."""
    glow_y = VIRTUAL_HEIGHT - 40
    glow_w = 140
    glow_h = 35
    glow_x = 20

    pulse = (math.sin(t * 1.5) + 1) * 0.5
    base_alpha = int(100 + pulse * 80)

    for i in range(8, 0, -1):
        expand = i * 6
        alpha = base_alpha // (i + 1)
        col = rl.Color(255, 80, 160, alpha)
        rl.draw_rectangle(
            glow_x - expand,
            glow_y - expand // 2,
            glow_w + expand * 2,
            glow_h + expand,
            col
        )

    rl.draw_rectangle(glow_x, glow_y, glow_w, glow_h, rl.Color(255, 120, 180, base_alpha))

    for i in range(10):
        lx = glow_x + 8 + i * 13
        ly = glow_y + glow_h - 10
        if int(t * 4 + i) % 3 != 0:
            rl.draw_circle(lx, ly, 3, rl.Color(255, 230, 255, 220))

    glow2_x = VIRTUAL_WIDTH // 2 - 80
    glow2_w = 50
    glow2_h = 18
    for i in range(4, 0, -1):
        expand = i * 3
        alpha = (base_alpha // 3) // (i + 1)
        col = rl.Color(0, 220, 255, alpha)
        rl.draw_rectangle(
            glow2_x - expand,
            glow_y + 8 - expand // 2,
            glow2_w + expand * 2,
            glow2_h + expand,
            col
        )
    rl.draw_rectangle(glow2_x, glow_y + 8, glow2_w, glow2_h, rl.Color(0, 240, 255, base_alpha // 3))


def draw_atmospheric_glow(t):
    """Draw pink/magenta atmospheric glow in the middle of the scene."""
    pulse = (math.sin(t * 0.8) + 1) * 0.5
    alpha = int(20 + pulse * 15)

    for i in range(3):
        y = VIRTUAL_HEIGHT // 2 + 20 + i * 30
        rl.draw_rectangle(0, y, VIRTUAL_WIDTH, 40, rl.Color(120, 40, 100, alpha - i * 5))

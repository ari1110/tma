"""
Flying vehicles (drones, hover cars, transports) for the cityscape.
"""

import pyray as rl
import random

from .config import VIRTUAL_WIDTH, PALETTE_NEON


class FlyingObject:
    def __init__(self):
        self.x = random.randint(-50, VIRTUAL_WIDTH + 50)
        self.y = random.randint(20, 120)
        self.direction = random.choice([-1, 1])
        self.light_color = random.choice(PALETTE_NEON)

        # Different vehicle types with varying sizes and speeds
        self.vehicle_type = random.choice(["drone", "drone", "hovercar", "hovercar", "hovercar", "transport"])

        if self.vehicle_type == "drone":
            # Small, fast drones
            self.size = random.randint(3, 5)
            self.speed = random.uniform(0.6, 1.2)
            self.trail_length = random.randint(5, 10)
            self.y = random.randint(15, 80)  # Higher up
        elif self.vehicle_type == "hovercar":
            # Medium hover cars
            self.size = random.randint(6, 10)
            self.speed = random.uniform(0.4, 0.8)
            self.trail_length = random.randint(10, 18)
            self.y = random.randint(40, 110)
        else:  # transport
            # Large, slow transports
            self.size = random.randint(12, 18)
            self.speed = random.uniform(0.2, 0.4)
            self.trail_length = random.randint(15, 25)
            self.y = random.randint(30, 70)

    def update(self):
        self.x += self.speed * self.direction
        # Wrap around
        if self.direction > 0 and self.x > VIRTUAL_WIDTH + 60:
            self.x = -50
            self._reset_altitude()
        elif self.direction < 0 and self.x < -60:
            self.x = VIRTUAL_WIDTH + 50
            self._reset_altitude()

    def _reset_altitude(self):
        if self.vehicle_type == "drone":
            self.y = random.randint(15, 80)
        elif self.vehicle_type == "hovercar":
            self.y = random.randint(40, 110)
        else:
            self.y = random.randint(30, 70)

    def draw(self, t):
        c = rl.Color(20, 15, 30, 220)  # Dark silhouette color
        x, y, s = int(self.x), int(self.y), self.size

        # Light trail behind
        for i in range(self.trail_length):
            alpha = int(60 * (1 - i / self.trail_length))
            trail_x = self.x - (i * 2 * self.direction)
            rl.draw_circle(int(trail_x + s // 2), int(y + s // 4),
                           1, rl.Color(self.light_color.r, self.light_color.g, self.light_color.b, alpha))

        if self.vehicle_type == "drone":
            # Small quadcopter shape
            rl.draw_rectangle(x + s // 4, y, s // 2, s // 3, c)  # Body
            rl.draw_rectangle(x, y + s // 6, s, 2, c)  # Arms
            # Rotor lights
            rl.draw_circle(x + 1, y + s // 6, 1, self.light_color)
            rl.draw_circle(x + s - 1, y + s // 6, 1, self.light_color)

        elif self.vehicle_type == "hovercar":
            # Sleek car shape
            rl.draw_rectangle(x, y + s // 4, s, s // 3, c)  # Main body
            rl.draw_rectangle(x + s // 5, y, int(s * 0.6), s // 4, c)  # Cabin/roof
            # Headlight/taillight
            light_x = x + s if self.direction > 0 else x - 2
            rl.draw_rectangle(light_x, y + s // 3, 2, s // 5, self.light_color)

        else:  # transport
            # Large boxy transport
            rl.draw_rectangle(x, y, s, s // 2, c)  # Main hull
            rl.draw_rectangle(x + s // 6, y - s // 6, int(s * 0.3), s // 6, c)  # Cockpit
            rl.draw_rectangle(x + s - s // 4, y + s // 2, s // 4, s // 6, c)  # Engine
            # Multiple lights
            rl.draw_circle(x + s // 4, y + s // 4, 1.5, self.light_color)
            rl.draw_circle(x + s * 3 // 4, y + s // 4, 1.5, self.light_color)
            # Red warning light on top
            rl.draw_circle(x + s // 2, y - 2, 1, rl.Color(255, 50, 50, 200))

"""
Configuration constants for neon city animation.
"""

import pyray as rl

# --- SCREEN ---
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
VIRTUAL_WIDTH = 480
VIRTUAL_HEIGHT = 270
TARGET_FPS = 60

# --- SKY COLORS ---
C_VOID = rl.Color(8, 2, 18, 255)  # Deep purple void
C_SKY_TOP = rl.Color(15, 8, 35, 255)
C_SKY_BOT = rl.Color(60, 20, 80, 255)  # More purple/pink at horizon

# --- NEON PALETTE ---
PALETTE_NEON = [
    rl.Color(0, 240, 255, 255),  # Cyan
    rl.Color(255, 0, 200, 255),  # Magenta
    rl.Color(180, 0, 255, 255),  # Purple
    rl.Color(255, 220, 50, 255),  # Warm Yellow
    rl.Color(255, 100, 150, 255),  # Pink
    rl.Color(0, 255, 180, 255),  # Teal
]

# --- ATMOSPHERIC HAZE ---
C_HAZE_BACK = rl.Color(80, 30, 100, 80)
C_HAZE_MID = rl.Color(60, 20, 80, 50)
C_HAZE_FRONT = rl.Color(100, 40, 120, 30)

# --- BUILDING GRADIENTS ---
C_BUILDING_BACK_TOP = rl.Color(40, 25, 70, 255)
C_BUILDING_BACK_BOT = rl.Color(25, 15, 45, 255)
C_BUILDING_MID_TOP = rl.Color(30, 18, 55, 255)
C_BUILDING_MID_BOT = rl.Color(18, 10, 35, 255)
C_BUILDING_FRONT_TOP = rl.Color(20, 12, 40, 255)
C_BUILDING_FRONT_BOT = rl.Color(10, 5, 20, 255)

# --- LEGACY FLAT COLORS ---
C_BUILDING_BACK = rl.Color(35, 20, 60, 255)
C_BUILDING_MID = rl.Color(22, 12, 40, 255)
C_BUILDING_FRONT = rl.Color(12, 6, 25, 255)

# --- HOLOGRAM CONFIG ---
PALETTE_HOLOGRAM = [
    rl.Color(0, 255, 255, 180),  # Cyan (classic hologram)
    rl.Color(255, 100, 200, 180),  # Hot pink (Blade Runner)
    rl.Color(200, 150, 255, 180),  # Soft purple
    rl.Color(255, 200, 100, 150),  # Warm amber/gold
]

# Position slots (x as fraction of VIRTUAL_WIDTH)
HOLOGRAM_SLOTS = [0.12, 0.35, 0.62, 0.88]
HOLOGRAM_COUNT_MIN = 1
HOLOGRAM_COUNT_MAX = 2
HOLOGRAM_HEIGHT_MIN = 60
HOLOGRAM_HEIGHT_MAX = 90

# Asset definitions (paths relative to project root)
# Types: "static", "animated" (GIF), "rotating" (3D rotation effect)
HOLOGRAM_ASSETS = [
    {"path": "neon_city/images/perfume_bottle_3d.gif", "type": "animated"},
    {"path": "neon_city/images/neon_cola_3d.gif", "type": "animated"},
    {"path": "neon_city/images/sam_altman.png", "type": "static"},
    {"path": "neon_city/images/elon-musk-dancing.gif", "type": "animated"},
]

# Glitch effect settings
GLITCH_CHANCE = 0.008  # 0.8% chance per frame (less frequent)
GLITCH_DURATION_MIN = 0.03  # seconds
GLITCH_DURATION_MAX = 0.12

# --- BILLBOARD IMAGE ADS ---
# Static images that can appear on building billboards
BILLBOARD_AD_IMAGES = [
    "neon_city/images/dior_perfume.png",
    "neon_city/images/en-card-cherry.png",
    "neon_city/images/sam_altman.png",
]
BILLBOARD_IMAGE_CHANCE = 0.3  # 30% of billboards use images instead of text

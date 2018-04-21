import ctypes
import random

user32 = ctypes.windll.user32


class Settings:
    """Stores all game settings"""

    def __init__(self):
        """Initialize the games settings"""

        self.screen_width = 1200  # user32.GetSystemMetrics(0)
        self.screen_height = 800  # user32.GetSystemMetrics(1)
        self.bkg_color = (random.random() * 255, random.random() * 255, random.random() * 255)

        self.max_ships = 2

        self.bullet_width = 2000
        self.bullet_height = 50
        self.bullet_color = (random.random() * 255, random.random() * 255, random.random() * 255)
        self.bullets_allowed = 3

        self.stars = 3

        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.level_up_multiplier = 1.1
        self.init_first_level()

    def init_first_level(self):
        """Set first level settings"""
        self.ship_speed_multiplier = 1.5
        self.bullet_speed_multiplier = 3
        self.alien_speed_multiplier = 1
        self.score_per_hit = 1

    def level_up(self):
        """Increase settings multipliers to next level"""

        self.ship_speed_multiplier *= self.level_up_multiplier
        self.bullet_speed_multiplier *= self.level_up_multiplier
        self.alien_speed_multiplier *= self.level_up_multiplier
        self.score_per_hit += self.score_per_hit

import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manages bullets fired from the ship"""

    def __init__(self, settings, screen, ship):
        """Create a bullet at the top of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_multiplier

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)

import pygame
from pygame.sprite import Sprite


class ShurikenStar(Sprite):
    """Represent a single shuriken star"""

    def __init__(self, setting, screen):
        """Initialize shuriken star"""
        super(ShurikenStar, self).__init__()

        self.screen = screen
        self.settings = setting

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw(self):
        """Draw shuriken stars at current location"""

        self.screen.blit(self.image, self.rect)

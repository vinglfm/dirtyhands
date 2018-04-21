import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents a single alien"""

    def __init__(self, setting, screen):
        """Initialize alien"""
        super(Alien, self).__init__()

        self.screen = screen
        self.settings = setting

        self.image = pygame.image.load('images/alians.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien"""
        self.x += self.settings.alien_speed_multiplier * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """True if alien is at edge of the screen"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def draw(self):
        """Draw the alien at its current location"""

        self.screen.blit(self.image, self.rect)

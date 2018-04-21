import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Represents ship"""

    def __init__(self, screen, setting):
        """Initialize the ship at starting position"""
        super(Ship, self).__init__()

        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx

        self.centerx = float(self.rect.centerx)
        self.centery = self.screen_rect.bottom - self.rect.width
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """Update the ships position based on the movement direction"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.ship_speed_multiplier
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.setting.ship_speed_multiplier
        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.centery -= self.setting.ship_speed_multiplier
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.setting.ship_speed_multiplier

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship at bottom of the screen"""
        self.centery = self.screen_rect.bottom - self.rect.width
        self.rect.centery = self.centery

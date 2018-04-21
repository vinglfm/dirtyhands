import pygame.sysfont
from pygame.sprite import Group

from katas.game.ship import Ship


class Scoreboard():
    """Represents game scoreboard"""

    def __init__(self, screen, settings, stats):
        """Initialize game scoreboard"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_scoreboard()

    def prep_scoreboard(self):
        """Prepare scoreboard images"""

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Prepare score image"""

        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bkg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Prepare high score image"""

        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bkg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """Prepare level image"""

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bkg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):
        """Prepare ships image"""

        self.ships = Group()

        for ship_number in range(self.stats.garrison):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def draw(self):
        """Prepare all images"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

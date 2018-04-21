from pygame.sprite import Group

from katas.game.functions import *
from katas.game.ship import Ship
from katas.game.settings import Settings
from katas.game.stats import Statistic
from katas.game.button import Button
from katas.game.scoreboard import Scoreboard


def run_game():
    pygame.init()
    pygame.display.set_caption('Alien sky')

    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))

    battle_ship = Ship(screen, setting)
    bullets = Group()
    aliens = Group()
    stars = Group()
    statistic = Statistic(setting)
    score_board = Scoreboard(screen, setting, statistic)

    create_alien_army(setting, screen, battle_ship, aliens)

    create_stars(setting, screen, stars)

    play_button = Button(screen, "Play")
    while True:
        check_events(setting, statistic, screen, battle_ship, bullets, aliens, play_button, score_board)

        if statistic.game_active:
            battle_ship.update()
            update_bullets(setting, screen, statistic, battle_ship, bullets, aliens, score_board)
            update_aliens(setting, statistic, screen, aliens, battle_ship, bullets, score_board)
        update_screen(setting, screen, statistic, score_board, stars, battle_ship, aliens, bullets, play_button)


run_game()

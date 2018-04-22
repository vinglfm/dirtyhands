import sys
from time import sleep

import pygame
import random

from katas.game.bullet import Bullet
from katas.game.alien import Alien
from katas.game.shurikenstar import ShurikenStar


def create_alien_army(setting, screen, ship, aliens):
    """Create an army of aliens"""
    alien = Alien(setting, screen)
    alien_ship_width = alien.rect.width

    max_aliens = calculate_aliens_in_row(setting.screen_width, alien_ship_width)
    rows = get_number_rows(setting, ship.rect.height, alien.rect.height)

    for row in range(rows):
        for alien_index in range(max_aliens):
            aliens.add(create_alien(setting, screen, alien_ship_width + 2 * alien_ship_width * alien_index, row))


def create_alien(setting, screen, alien_position, row_number):
    """Creates and position alien ship"""
    alien = Alien(setting, screen)
    alien.x = alien_position
    alien.rect.x = alien_position
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    return alien


def calculate_aliens_in_row(screen_width, alien_width):
    """Calculate max allowed aliens in row"""
    available_space_x = screen_width - 2 * alien_width
    max_aliens_in_row = int(available_space_x / (2 * alien_width))
    return max_aliens_in_row


def create_stars(setting, screen, stars):
    """Creates and position shuriken stars"""
    star_elems = []
    for star_number in range(setting.stars):
        star = create_star(setting, screen)
        stars.add(star)
        star_elems.append(star)

    return star_elems


def create_star(setting, screen):
    """Create shuriken star"""
    star = ShurikenStar(setting, screen)
    star.x = star.rect.width + random.random() * (setting.screen_width - star.rect.width)
    star.rect.x = star.x
    star.rect.y = star.rect.height + random.random() * star.rect.height
    return star


def check_events(setting, stats, screen, ship, bullets, aliens, play_button, scoreboard):
    """Respond to key pressed and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click(setting, stats, screen, ship, bullets, aliens, play_button, scoreboard)


def mouse_click(setting, stats, screen, ship, bullets, aliens, play_button, scoreboard):
    """Starts game on play button click"""
    if not stats.game_active:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            start_game(setting, stats, screen, ship, bullets, aliens, scoreboard)


def start_game(setting, stats, screen, ship, bullets, aliens, scoreboard):
    """Initialize game elements and start game"""
    pygame.mouse.set_visible(False)
    stats.init_first_level()
    setting.init_first_level()
    aliens.empty()
    bullets.empty()
    create_alien_army(setting, screen, ship, aliens)
    ship.center()
    scoreboard.prep_score()
    scoreboard.prep_level()
    scoreboard.prep_ships()
    stats.game_active = True


def keydown_events(event, setting, screen, ship, bullets):
    """Respond to kedown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def keyup_events(event, ship):
    """Respond to keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def update_screen(settings, screen, stats, scoreboard, stars, ship, aliens, bullets, shurikens, play_button):
    """Draw components to game screen"""
    screen.fill(settings.bkg_color)
    stars.draw(screen)
    ship.draw()

    aliens.draw(screen)

    for bullet in bullets:
        bullet.draw()

    for shuriken in shurikens:
        shuriken.draw()

    scoreboard.draw()

    if not stats.game_active:
        play_button.draw()

    pygame.display.flip()


def update_bullets(setting, screen, stats, ship, bullets, aliens, scoreboard):
    """Removes bullets that out of range, check hits aliens"""
    bullets.update(1)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_hit_aliens(setting, screen, stats, ship, bullets, aliens, scoreboard)


def fire_shurikens(setting, screen, stars, shurikens):
    """Fire shurikens if available"""

    if len(shurikens) == 0:
        shooting_star = random.randint(0, 2)
        new_bullet = Bullet(setting, screen, stars[shooting_star])
        shurikens.add(new_bullet)


def update_shurikens(settings, stats, screen, ship, ship_sprite, aliens, bullets, shurikens, scoreboard):
    """Removes shurikens that out of range, check hits ship"""
    shurikens.update(-1)

    for bullet in shurikens.copy():
        if bullet.rect.bottom >= settings.screen_width:
            shurikens.remove(bullet)

    hits = pygame.sprite.groupcollide(shurikens, ship_sprite, True, True)

    if hits:
        ship_hit(settings, stats, screen, ship, aliens, bullets, scoreboard)
        ship_sprite.add(ship)


def check_hit_aliens(setting, screen, stats, ship, bullets, aliens, scoreboard):
    """Checks hit aliens"""
    hits = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if hits:
        for hit_aliens in hits.values():
            stats.score += setting.score_per_hit * len(hit_aliens)
        check_high_score(stats, scoreboard)
        scoreboard.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        setting.level_up()
        stats.level += 1
        scoreboard.prep_level()
        create_alien_army(setting, screen, ship, aliens)


def fire_bullets(setting, screen, ship, bullets):
    """Fire bullets if available"""
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


def get_number_rows(setting, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(setting, stats, screen, aliens, ship, bullets, scoreboard):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(setting, aliens)
    aliens.update()

    check_aliens_invasion(setting, stats, screen, ship, aliens, bullets, scoreboard)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, screen, ship, aliens, bullets, scoreboard)


def change_fleet_direction(setting, aliens):
    """Drop the entire fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1


def check_fleet_edges(setting, aliens):
    """Changing direction on hitting edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break


def ship_hit(settings, stats, screen, ship, aliens, bullets, scoreboard):
    """Respond to ship being hit by alien"""
    if stats.garrison > 0:
        stats.garrison -= 1
        scoreboard.prep_ships()
        aliens.empty()
        bullets.empty()
        create_alien_army(settings, screen, ship, aliens)
        ship.center()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_invasion(settings, stats, screen, ship, aliens, bullets, scoreboard):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, scoreboard)
            break


def check_high_score(stats, scoreboard):
    """Set high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()

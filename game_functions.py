import sys
import pygame
from bullet import Bullet
from cat import Cat
from time import sleep

def check_keydown_events(event, ci_settings, screen, broccoli, bullets):
    if event.key == pygame.K_RIGHT:
        broccoli.moving_right = True
    elif event.key == pygame.K_LEFT:
        broccoli.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ci_settings, screen, broccoli, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ci_settings, screen, broccoli, bullets):
    """fire a bullet if the maximum number of bullets allowed on screen
    is not reached"""
    # create a bullet and add it to group
    if len(bullets) < ci_settings.bullets_allowed:
        new_bullet = Bullet(ci_settings, screen, broccoli)
        bullets.add(new_bullet)

def check_keyup_events(event, broccoli):
    if event.key == pygame.K_RIGHT:
        broccoli.moving_right = False
    elif event.key == pygame.K_LEFT:
        broccoli.moving_left = False

def check_events(ci_settings, screen, stats, start_button, broccoli, cats, bullets):
    """handles button and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ci_settings, screen, broccoli, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, broccoli)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(ci_settings, screen, stats, start_button,
                                broccoli, cats, bullets,  mouse_x, mouse_y)

def check_start_button(ci_settings, screen, stats, start_button, broccoli, cats, bullets, mouse_x, mouse_y):
    """start game when player hit start button
    """
    if start_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # reset game speed
        ci_settings.initialise_dynamic_settings()
        # hide mouse
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        
        cats.empty()
        bullets.empty()

        create_fleet(ci_settings, screen, broccoli, cats)
        broccoli.center_broccoli()
        
def update_screen(ci_settings, screen, stats, sb, broccoli, cats, bullets, start_button):
    """update the images on the screen, cut to new screen
    """
    screen.fill(ci_settings.bg_color)

    # draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    broccoli.blitme()
    cats.draw(screen) # paints every cat in cat group
    sb.show_score()

    if not stats.game_active:
        start_button.draw_button()

    # make the latest painted screen visible
    pygame.display.flip()

def update_bullets(ci_settings, screen, stats, sb, broccoli, cats, bullets):
    """update the position of bullets, delete bullets that have 
    disappeared from the screen."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_cat_collisions(ci_settings, screen, stats, sb, broccoli, cats, bullets)

def check_bullet_cat_collisions(ci_settings, screen, stats, sb, broccoli, cats, bullets):
    # check if bullet hit cat, if so, delete that bullet and the cat
    collisions = pygame.sprite.groupcollide(bullets, cats, True, True)

    if collisions:
        for cats in collisions.values():            
            stats.score += ci_settings.cat_points * len(cats)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(cats) == 0:
        bullets.empty()
        ci_settings.increase_speed()
        create_fleet(ci_settings, screen, broccoli, cats)

def get_number_cats_x(ci_settings, cat_width):
    """calculate the number of cats that could fit in one row
    """
    available_space_x = ci_settings.screen_width - 2*cat_width
    number_cats_x = int(available_space_x / (2 * cat_width))

    return number_cats_x


def get_number_rows(ci_settings, broccoli_height, cat_height):
    """how many rows of cats can fit in the screen
    """
    available_space_y = (ci_settings.screen_height - 
                            (3 * cat_height)- broccoli_height)
    number_rows = int(available_space_y /  (2 * cat_height))
    return number_rows


def create_cat(ci_settings, screen, cats, cat_n, row_number):
    """create a cat and place it in current row
    """
    cat = Cat(ci_settings, screen)
    cat_width = cat.rect.width
    cat.x = cat_width + 2 * cat_width * cat_n
    cat.rect.x = cat.x
    cat.rect.y = cat.rect.height + 2 * cat.rect.height * row_number
    cats.add(cat)

def create_fleet(ci_settings, screen, broccoli, cats):
    """create a group of cats
    """
    cat = Cat(ci_settings, screen)
    number_cats_x = get_number_cats_x(ci_settings, cat.rect.width)
    number_rows = get_number_rows(ci_settings, broccoli.rect.height,
                                    cat.rect.height)

    for row_number in range(number_rows):
        for cat_n in range(number_cats_x):
            create_cat(ci_settings, screen, cats, cat_n, row_number)
            
def check_fleet_edges(ci_settings, cats):
    """do something when cats reach the edges of screen
    """
    for cat in cats.sprites():
        if cat.check_edges():
            change_fleet_direction(ci_settings, cats)
            break

def change_fleet_direction(ci_settings, cats):
    """move the group of cats down and change their directions
    """
    for cat in cats.sprites():
        cat.rect.y += ci_settings.fleet_drop_speed
    ci_settings.fleet_direction *= -1 # alternate directions

def broccoli_hit(ci_settings, stats, screen, broccoli, cats, bullets):
    """respond when broccoli is hit by cat
    """
    if stats.broccoli_left > 0:
        stats.broccoli_left -= 1
    
        cats.empty()
        bullets.empty()

        create_fleet(ci_settings, screen, broccoli, cats)
        broccoli.center_broccoli()

        # pause
        sleep(0.7)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_cats_bottom(ci_settings, stats, screen, broccoli, cats, bullets):
    """check if any cat reaches the bottom of the screen
    """
    screen_rect = screen.get_rect()
    for cat in cats.sprites():
        if cat.rect.bottom >= screen_rect.bottom:
            broccoli_hit(ci_settings, stats, screen, broccoli, cats, bullets)
            break


def update_cats(ci_settings, stats, screen, broccoli, cats, bullets):
    """check if any cat reaches the edge of the screen
    update the position of all cats in group cats
    """
    check_fleet_edges(ci_settings, cats)
    cats.update()

    # check for cat-broccoli collisions
    if pygame.sprite.spritecollideany(broccoli, cats):
        broccoli_hit(ci_settings, stats, screen, broccoli, cats, bullets)
    # check if cat reaches bottom of screen
    check_cats_bottom(ci_settings, stats, screen, broccoli, cats, bullets)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

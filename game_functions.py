import sys
import pygame
from bullet import Bullet
from cat import Cat

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

def check_events(ci_settings, screen, broccoli, bullets):
    """handles button and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ci_settings, screen, broccoli, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, broccoli)
        
def update_screen(ci_settings, screen, broccoli, cats, bullets):
    """update the images on the screen, cut to new screen
    """
    screen.fill(ci_settings.bg_color)

    # draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    broccoli.blitme()
    cats.draw(screen) # paints every cat in cat group

    # make the latest painted screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """update the position of bullets, delete bullets that have 
    disappeared from the screen."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

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

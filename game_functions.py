import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ci_settings, screen, broccoli, bullets):
    if event.key == pygame.K_RIGHT:
        broccoli.moving_right = True
    elif event.key == pygame.K_LEFT:
        broccoli.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ci_settings, screen, broccoli, bullets)

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
        
def update_screen(ci_settings, screen, broccoli, bullets):
    """update the images on the screen, cut to new screen
    """
    screen.fill(ci_settings.bg_color)

    # draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    broccoli.blitme()

    # make the latest painted screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """update the position of bullets, delete bullets that have 
    disappeared from the screen."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

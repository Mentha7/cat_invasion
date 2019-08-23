import pygame
from settings import Settings
from broccoli import Broccoli
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialise game and create a screen
    pygame.init()
    ci_settings = Settings() 
    screen = pygame.display.set_mode(
            (ci_settings.screen_width, ci_settings.screen_height))
    pygame.display.set_caption('Cat Invasion!')

    # create a broccoli
    broc = Broccoli(ci_settings, screen)
    
    # create bullet group
    bullets = Group()

    # begin game
    while True:
        gf.check_events(ci_settings, screen, broc, bullets)
        broc.update()
        bullets.update()
        gf.update_screen(ci_settings, screen, broc, bullets)

run_game()

import pygame
from settings import Settings
from broccoli import Broccoli
from cat import Cat
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    # initialise game and create a screen
    pygame.init()
    ci_settings = Settings() 
    screen = pygame.display.set_mode(
            (ci_settings.screen_width, ci_settings.screen_height))
    pygame.display.set_caption('Cat Invasion!')

    # create start button
    start_button = Button(ci_settings, screen, 'Start')

    # create a broccoli
    broc = Broccoli(ci_settings, screen)
    
    # create bullet group
    bullets = Group()

    # create cat group
    cats = Group()

    # create a group of cats
    gf.create_fleet(ci_settings, screen, broc, cats)

    # create game stats
    stats = GameStats(ci_settings)

    # begin game
    while True:
        gf.check_events(ci_settings, screen, stats, start_button, broc, cats, bullets)
        if stats.game_active:
            broc.update()
            gf.update_bullets(ci_settings, screen, broc, cats, bullets)
            gf.update_cats(ci_settings, stats, screen, broc, cats, bullets)
        gf.update_screen(ci_settings, screen, stats, broc, cats, bullets, start_button)

run_game()

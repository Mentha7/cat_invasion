import sys
import pygame
from settings import Settings
from broccoli import Broccoli

def run_game():
    # initialise game and create a screen
    pygame.init()
    ci_settings = Settings() 
    screen = pygame.display.set_mode(
            (ci_settings.screen_width, ci_settings.screen_height))
    pygame.display.set_caption('Cat Invasion!')

    # create a broccoli
    broc = Broccoli(screen)

    # begin game
    while True:

        # monitor keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # paint screen
        screen.fill(ci_settings.bg_color)
        broc.blitme()

        # make screen visible
        pygame.display.flip()

run_game()

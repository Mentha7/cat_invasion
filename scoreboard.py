import pygame.font
from pygame.sprite import Group
from broccoli import Broccoli

class Scoreboard():
    """A class to display score
    """

    def __init__(self, ci_settings, screen, stats):
        """initialisation
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ci_settings = ci_settings
        self.stats = stats

        # font
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 88)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_broccoli()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.ci_settings.bg_color)

        # place score on upper right corner 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """show score on screen
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.broccoli.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                            self.text_color, self.ci_settings.bg_color)

        # place score on top middle of the screen  
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ci_settings.bg_color)

        # place score on upper right corner 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_broccoli(self):
        """display the remaining broccoli on upper left corner
        """
        self.broccoli = Group()
        for broc_n in range(self.stats.broccoli_left):
            broccoli = Broccoli(self.ci_settings, self.screen)
            broccoli.rect.x = 10 + broc_n * broccoli.rect.width
            broccoli.rect.y = 10
            self.broccoli.add(broccoli)


import pygame.font

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


    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                            self.text_color, self.ci_settings.bg_color)

        # place score on top middle of the screen  
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top



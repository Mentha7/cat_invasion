import pygame
from pygame.sprite import Sprite

class Broccoli(Sprite):

    def __init__(self, ci_settings, screen):
        """Initialises broccoli and set its initial position
        """
        super().__init__()
        self.screen = screen
        self.ci_settings = ci_settings

        # load broccoli image and get its rectangle
        tmp_image = pygame.image.load('images/broccoli.bmp')
        self.image = pygame.transform.rotozoom(tmp_image, 0, 0.09)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # place every new broccoli at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store floats in broccoli.center
        self.center = float(self.rect.centerx)

        # movement sign
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjusts broccoli position
        """
        # update the center of the broccoli rather than its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ci_settings.broccoli_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ci_settings.broccoli_speed_factor

        # update rectangle according to broccoli center
        self.rect.centerx = self.center

    def blitme(self):
        """paints broccoli at the designated position
        """
        self.screen.blit(self.image, self.rect)

    def center_broccoli(self):
        self.center = self.screen_rect.centerx

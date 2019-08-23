import pygame

class Broccoli():

    def __init__(self, screen):
        """Initialises broccoli and set its initial position
        """
        self.screen = screen

        # load broccoli image and get its rectangle
        tmp_image = pygame.image.load('images/broccoli.bmp')
        self.image = pygame.transform.rotozoom(tmp_image, 0, 0.1)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # place every new broccoli at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """paints broccoli at the designated position
        """
        self.screen.blit(self.image, self.rect)

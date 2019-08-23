import pygame
from pygame.sprite import Sprite

class Cat(Sprite):
    """A class tha represent a single cat
    """
    def __init__(self, ci_settings, screen):
        """initialise cat and its position on screen
        """
        super().__init__()
        self.screen = screen
        self.ci_settings = ci_settings

        # load cat image and set its rectangle
        tmp_image = pygame.image.load('images/cat1.bmp')
        self.image = pygame.transform.rotozoom(tmp_image, 0, 0.06)
        self.rect = self.image.get_rect()

        # every cat spawns from the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stores position of cat
        self.x = float(self.rect.x)

    def blitme(self):
        """paint cat at designated position
        """
        self.screen.blit(self.image, self.rect)


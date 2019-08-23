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
        self.image = pygame.transform.rotozoom(tmp_image, 0, 0.1)
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


    def check_edges(self):
        """return True if cat reaches edge of the screen
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move cat to the right/left
        """
        self.x += (self.ci_settings.cat_speed_factor 
                    * self.ci_settings.fleet_direction)
        self.rect.x = self.x



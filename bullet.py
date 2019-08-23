import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to organise the bullets fired from the broccoli.
    """

    def __init__(self, ci_settings, screen, broccoli):
        """creates a bullet object at the position of the broccoli
        """
        super().__init__()
        self.screen = screen

        # create a rectangular bullet at (0,0) then modify its position
        self.rect = pygame.Rect(0,0, ci_settings.bullet_width,
                ci_settings.bullet_height)
        self.rect.centerx = broccoli.rect.centerx
        self.rect.top = broccoli.rect.top

        # store float representation of bullet position
        self.y = float(self.rect.y)

        self.color = ci_settings.bullet_color
        self.speed_factor = ci_settings.bullet_speed_factor

    def update(self):
        """ moves bullet upwards
        """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

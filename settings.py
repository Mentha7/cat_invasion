class Settings():
    """A class to save all settings for the game cat_invasion.
    """
    def __init__(self):
        """initialises settings
        """
        # screen 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # broccoli
        self.broccoli_speed_factor = 1.5

        # bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 6

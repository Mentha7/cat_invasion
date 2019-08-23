class Settings():
    """A class to save all settings for the game cat_invasion.
    """
    def __init__(self):
        """initialises settings
        """
        # screen 
        self.screen_width = 2400
        self.screen_height = 1400
        self.bg_color = (230,230,230)

        # broccoli
        self.broccoli_speed_factor = 6

        # bullet
        self.bullet_speed_factor = 6
        self.bullet_width = 3 
        self.bullet_height = 30
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        # cat
        self.cat_speed_factor = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 for right, -1 for left





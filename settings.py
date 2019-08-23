class Settings():
    """A class to save all settings for the game cat_invasion.
    """
    def __init__(self):
        """initialises settings
        """
        # screen 
        self.screen_width = 2000
        self.screen_height = 1400
        self.bg_color = (230,230,230)

        # broccoli
        self.broccoli_speed_factor = 6
        self.broccoli_limit = 3

        # bullet
        self.bullet_speed_factor = 6
        self.bullet_width = 3 
        self.bullet_height = 30
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        # cat
        self.cat_speed_factor = 4
        self.fleet_drop_speed = 20
        self.fleet_direction = 1 # 1 for right, -1 for left

        # speed up the game if level up
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()


    def initialise_dynamic_settings(self):
        self.broccoli_speed_factor = 6
        self.bullet_speed_factor = 6
        self.cat_speed_factor = 4

        self.fleet_direction = 1


    def increase_speed(self):
        
        self.broccoli_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.cat_speed_factor *= self.speedup_scale




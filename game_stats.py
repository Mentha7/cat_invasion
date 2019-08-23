class GameStats():
    """game statistics
    """

    def __init__(self, ci_settings):
        """initialise game stats
        """
        self.ci_settings = ci_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        self.broccoli_left = self.ci_settings.broccoli_limit

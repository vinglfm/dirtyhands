class Statistic():
    """Tracks game statistics"""

    def __init__(self, settings):
        """Initialize the games statistics"""

        self.settings = settings
        self.game_active = False
        self.high_score = 0
        self.init_first_level()

    def init_first_level(self):
        """Reset statistics to initial level"""

        self.garrison = self.settings.max_ships
        self.score = 0
        self.level = 1

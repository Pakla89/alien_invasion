import os,json

os.chdir(os.path.dirname(__file__))

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score_file = 'high_score.json'
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        try:
            with open(self.high_score_file, 'r') as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return 0

    def save_high_score(self):
        """Save high score to a file."""
        with open(self.high_score_file, 'w') as file:
            json.dump(self.high_score, file)


#! /usr/bin/python3

import json

class GameStats:
    """Track statistics of Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an in active state.
        self.game_active = False

        # High score should never be reset.
        # Load high score from a json file
        filename = "data/high_score.json"
        with open(filename) as fn:
            self.high_score = json.load(fn)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

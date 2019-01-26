import pygame
import json

from level import Level
from player import Player

class Loader:
    def load(self, file):
        with open(file) as f:
            data = json.load(f)
        level = Level(data["level"])
        player = Player(data["player"])
        return [level, player]

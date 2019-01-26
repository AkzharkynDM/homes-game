import pygame
import json

from level import Level
from player import Player

class Loader:
    def __init__(self, res):
        self.res = res

    def load(self, file):
        with open(file) as f:
            data = json.load(f)
        data["level"].update({"res": self.res})
        level = Level(data["level"])
        player = Player(data["player"])
        return [level, player]

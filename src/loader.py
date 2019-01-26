import pygame
import json

from level import Level
from player import Player

class Loader:
    def __init__(self, res, file):
        self.res = res
        self.index = 0
        with open(file) as f:
            self.levels = json.load(f)

    def load(self):
        if self.index >= len(self.levels):
            self.index = 0
        data = self.levels[self.index]
        self.index = self.index + 1
        data["level"].update({"res": self.res})
        data["player"].update({"res": self.res})
        level = Level(data["level"])
        player = Player(data["player"])
        return [level, player]

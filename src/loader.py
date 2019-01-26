import pygame
import json
from level import Level

class Loader:
    def load(self, file):
        with open(file) as f:
            data = json.load(f)
        level = Level(data["level"])
        return level

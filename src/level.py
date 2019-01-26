import pygame

class Level:
    def __init__(self, info):
        self._backgroundImg = pygame.image.load(info["background"])

    def on_init(self):
        pass

    def on_render(self, display_surf):
        display_surf.blit(self._backgroundImg, (0,0))

    def on_loop(self):
        pass

    def on_event(self, event):
        pass

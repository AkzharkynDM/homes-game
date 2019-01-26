import pygame

class Level:
    def on_init(self):
        self._backgroundImg = pygame.image.load("sources/background.png")

    def on_render(self, display_surf):
        display_surf.blit(self._backgroundImg, (0,0))

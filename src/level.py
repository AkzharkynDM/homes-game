import pygame
import constants

class Level:
    def __init__(self, info):
        self._backgroundImg = pygame.image.load(info["background"])
        self._backgroundImg = pygame.transform.scale(self._backgroundImg, info["res"])
        pygame.font.init()
        self._myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self._textsurface = self._myfont.render('Reveal', False, (0, 0, 0))
        self._sqrt = pygame.rect.Rect(895, 650, 100, 50)

    def on_render(self, display_surf):
        display_surf.blit(self._backgroundImg, (0,0))
        pygame.draw.rect(display_surf, constants.WHITE, self._sqrt)
        display_surf.blit(self._textsurface,(900, 650))

    def on_loop(self):
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._sqrt.collidepoint(event.pos):
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT+2))

import pygame
import constants

class Player(object):
    def __init__(self, info):
        self._obj = [None]*info["squares"]
        for i in range(0, info["squares"]):
            self._obj[i] = pygame.rect.Rect(176, 134, constants.SIZE, constants.SIZE)

    def on_init(self):
        self.obj_draging = False
        self.offset_x = 0
        self.offset_y = 0

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(0, len(self._obj)):
                    if self._obj[i].collidepoint(event.pos):
                        self.obj_draging = True
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self._obj[i].x - mouse_x
                        self.offset_y = self._obj[i].y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.obj_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.obj_draging:
                mouse_x, mouse_y = event.pos
                for i in range(0, len(self._obj)):
                    self._obj[i].x = mouse_x + self.offset_x
                    self._obj[i].y = mouse_y + self.offset_y

    def on_loop(self):
        pass

    def on_render(self, surf):
        for i in range(0, len(self._obj)):
            pygame.draw.rect(surf, constants.WHITE, self._obj[i])

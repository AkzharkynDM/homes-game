import pygame
import constants

class Player(object):
    def __init__(self):
        self.obj = pygame.rect.Rect(176, 134, constants.SIZE, constants.SIZE)
        self.obj_draging = False
        self.offset_x = 0
        self.offset_y = 0

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if self.obj.collidepoint(event.pos):
                    self.obj_draging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.obj.x - mouse_x
                    self.offset_y = self.obj.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                self.obj_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.obj_draging:
                mouse_x, mouse_y = event.pos
                self.obj.x = mouse_x + self.offset_x
                self.obj.y = mouse_y + self.offset_y
            
    def on_loop(self):
        pass
    def on_render(self, surf):
        pygame.draw.rect(surf, constants.WHITE, self.obj) 
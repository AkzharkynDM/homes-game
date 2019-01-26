import pygame
import constants

class Player(object):
    def __init__(self, info):
        self.width, self.height = info["res"]
        self.sqrn,self.rectn,self.trin =info["sqrs"], info["rects"],info["tris"]
        self._obj = [None]*(info["sqrs"] + info["rects"] + info["tris"])
        i = 0
        print self.sqrn,self.rectn,self.trin 
        while i<len(self._obj):
            if(i<len(self._obj)-info["rects"] - info["tris"]):
                self._obj[i] = pygame.rect.Rect(self.width/10, self.height/25, constants.SIZE, constants.SIZE)
            elif(i < len(self._obj)-info["tris"]):
                self._obj[i] = pygame.rect.Rect(self.width/10,  2*self.height/25, constants.SIZE*3, constants.SIZE)
            elif (i<len(self._obj)):
                self._obj[i] = pygame.rect.Rect(self.width/10, 3*self.height/25, constants.SIZE, constants.SIZE)
            i = i+1
        self.obj_draging = False
        self.obj_draging_index = 0
        self.offset_x = 0
        self.offset_y = 0

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(0, len(self._obj)):
                    if self._obj[i].collidepoint(event.pos):
                        self.obj_draging = True
                        self.obj_draging_index = i
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self._obj[i].x - mouse_x
                        self.offset_y = self._obj[i].y - mouse_y
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.obj_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.obj_draging:
                mouse_x, mouse_y = event.pos
                self._obj[self.obj_draging_index].x = mouse_x + self.offset_x
                self._obj[self.obj_draging_index].y = mouse_y + self.offset_y

    def on_loop(self):
        pass

    def on_render(self, surf):
        print "render"
        for i in range(0, len(self._obj)-self.trin):
            pygame.draw.rect(surf, constants.BLACK, self._obj[i])
        for i in range(len(self._obj)-self.trin, len(self._obj)):
            print i
            p1 = [self._obj[i].x, self._obj[i].y +constants.SIZE]
            p2 = [p1[0]+constants.SIZE, p1[1]]
            p3 = [p1[0]+(constants.SIZE)/2, p1[1]-constants.SIZE]
            pygame.draw.polygon(surf, constants.BLACK, [p1,p2,p3])


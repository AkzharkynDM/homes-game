import pygame

class NextButton:

    def __init__(self, nextButton_x, nextButton_y, size):
        self.rect = pygame.rect.Rect(nextButton_x, nextButton_y, size, size)


    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1:
                   if self.rect.collidepoint(event.pos):
                       pygame.event.post(pygame.event.Event(pygame.USEREVENT+2))
                       #print "click"

    def on_loop(self):
        pass

    def on_render(self, DISPLAY):
        WHITE=(255,255,255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(DISPLAY,BLACK, self.rect)

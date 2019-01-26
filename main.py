import pygame
import src.constants as consts
from NextButton import NextButton

from src.level import Level
from src.loader import Loader
from src.player import Player

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        pygame.init()
        self.res = pygame.display.list_modes()[5]
        self._display_surf = pygame.display.set_mode(self.res,pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._loader = Loader(self.res, "resources/level0.json")
        self._level, self._player = self._loader.load()

    def on_event(self, event):
        self._player.on_event(event)
        self._level.on_event(event)
        if event.type == pygame.USEREVENT+2:
            self._level, self._player = self._loader.load()
        if event.type == pygame.QUIT:
			self._running = False
        if event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				self._running = False
			# elif keys[pygame.K_s]:
			# 	pygame.mixer.init()
			# 	pygame.mixer.music.load("/Users/Cutie/Movies/backgroundmusic.mp3")

    def on_render(self):
        self._display_surf.fill(consts.BLACK)
        self._level.on_render(self._display_surf)
        self._player.on_render(self._display_surf)
        pygame.display.flip()

    # def on_loop(self):
    #     self._player.on_loop()
    #     self._level.on_loop()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()

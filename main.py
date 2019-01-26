import pygame

from src.level import Level
from src.loader import Loader
from src.player import Player


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        pygame.init()
        self.res = self.weight, self.height = pygame.display.list_modes()[5]
        self._display_surf = pygame.display.set_mode(self.res,pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        self._running = True
        self._loader = Loader(self.res)
        self._level, self._player = self._loader.load("resources/level0.json")
        self._level.on_init()
        self._player.on_init()

    def on_event(self, event):
        self._player.on_event(event)
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
        self._display_surf.fill(BLACK)
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

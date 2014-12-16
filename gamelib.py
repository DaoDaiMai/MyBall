import pygame
from pygame.locals import *

class SimpleGame(object):

    def __init__(self, title, background_color, window_size=(800,500), fps=30):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.background_color = background_color

        self.is_terminated = False

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYUP and event.key == K_ESCAPE:
                self.terminate()
            elif event.type == KEYDOWN and event.key == K_r:
                self.restart()
                 

    def terminate(self):
        self.is_terminated = True

    def run(self):
        self.init()
        while not self.is_terminated:
            self.__handle_events()

            self.update()

            self.surface.fill(self.background_color)
            self.render(self.surface)
            pygame.display.update()

            self.clock.tick(self.fps)

    def key_pressed(self, key):
        keys_press = pygame.key.get_pressed()
        if key < 0 or key >= len(keys_press):
            return False
        return (keys_press[key])

    def init(self):
        self.__game_init()

    def update(self):
        pass

    def render(self, surface):
        pass

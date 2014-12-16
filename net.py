import pygame
from pygame.locals import *

class Net(object):

	def __init__(self):
		self.X = 400
		self.Y = 300
		self.Image = pygame.image.load("net.png")

	def update(self):
		pass

	def render(self,surface):
		surface.blit(self.Image, (self.X, self.Y))

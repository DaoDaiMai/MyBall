import pygame
from pygame.locals import *

class Player(object):

	def __init__(self,image,posX,posY):
		self.X = posX
		self.Y = posY
		self.G = 10
		self.Image = pygame.image.load(image)

	def update(self):
		self.Y += self.G
		self.G += 5
		if self.Y > 400 :
			self.Y = 400
			self.G = 0
		if self.Y < 0 :
			self.Y = 0

	def render(self,surface):
		surface.blit(self.Image, (self.X, self.Y))

	def jump(self):
		self.G -= 40
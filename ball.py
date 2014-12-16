import pygame
from pygame.locals import *
from random import randrange

class Ball(object):

	def __init__(self):
		self.Y = 250
		self.image = pygame.image.load("ball.png")
		self.G = 0
		if (randrange(1,10)%2) == 0 :
			self.X = 420
			self.VX = 5
		else :
			self.X = 380
			self.VX = -5

	def update (self):
		self.X += self.VX
		self.Y += self.G
		self.G += 3
		if(self.Y <= 0):
			self.Top()
		if(self.Y >= 460):
			self.Floor()
		if(self.X <= 0):
			self.LeftWall()
		if(self.X >= 760):
			self.RightWall()

	def render(self,surface):
		surface.blit(self.image, (self.X,self.Y))

	def Top(self):
		self.G = 5

	def Floor(self):
		self.G = -abs(self.G) + 5

	def LeftWall(self):
		self.VX = abs(self.VX)

	def RightWall(self):
		self.VX = -abs(self.VX)

	def hit(self):
		if (randrange(1,10)%2) == 0 :
			self.VX = randrange(10,20)
		else :
			self.VX = randrange(-20,-10)
		self.G = -35

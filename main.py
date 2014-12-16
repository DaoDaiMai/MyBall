import pygame
from pygame.locals import *
from gamelib import SimpleGame
from player import *
from ball import *
from net import *

class TakeMyBall(SimpleGame):
	GREY = pygame.Color('grey')
	BLACK = pygame.Color('black')
	Game_width = 800
	Game_height = 500
	global Key_P1, Key_P2, Game_over, time, p1win

	def __init__(self):
		super(TakeMyBall, self).__init__('TakeMyBall', TakeMyBall.BLACK)

	def init(self):
		super(TakeMyBall, self).init()
		self.init_Background()
		self.init_Players()
		self.init_Ball()
		self.init_Net()
		self.Key_P1 = 0
		self.Key_P2 = 0
		self.Game_over = False
		self.time = 600
		self.p1win = True

	def init_Background(self):
		self.bg = pygame.image.load("bg.png")

	def init_Players(self):
		self.P1 = Player("p1.png", 100, 400)
		self.P2 = Player("p2.png", 650, 400)

	def init_Ball(self):
		self.ball = Ball()

	def init_Net(self):
		self.net = Net()

	def update(self):
		if not self.Game_over :
			self.P1.update()
			self.P2.update()
			self.ball.update()
			self.collide_detector(self.ball, self.P1, self.P2, self.net)
			
			self.time -= 1
			if self.time == 0 :
				self.Game_over = True
			
			if self.key_pressed(K_LSHIFT) :
				self.Key_P1 += 1
			else :
				self.Key_P1 = 0
			if self.Key_P1 == 1 :
				self.P1.jump()
			if self.key_pressed(K_RSHIFT) :
				self.Key_P2 += 1
			else :
				self.Key_P2 = 0
			if self.Key_P2 == 1 :
				self.P2.jump()
		else :
			if self.ball.X > 400 :
				self.p1win = True
			else :
				self.p1win = False

	def render(self, surface):
		if not self.Game_over :
			self.surface.blit(self.bg, (0,0))
			time_image = self.font.render("TIME : %d" % (self.time/30), 0, self.GREY)
			self.surface.blit(time_image, (10,10))
			self.P1.render(surface)
			self.P2.render(surface)
			self.ball.render(surface)
			self.net.render(surface)
		else :
			if self.p1win :
				final = self.font.render("Player 1 WIN!!!" , 0, self.GREY)
			else :
				final = self.font.render("Player 2 WIN!!!", 0, self.GREY)
			self.surface.blit(final, (320,220))

	def collide_detector(self, ball, p1, p2, net):
		ballx = ball.X + 20
		bally = ball.Y + 20
		p1x = p1.X + 25
		p1y = p1.Y + 50
		p2x = p2.X + 25
		p2y = p2.Y + 50
		netX = net.X + 10
		netY = net.Y
		
		if (ballx+20 > netX and ballx-20 < netX) and (bally+20>=netY) :
			self.ball.VX = -self.ball.VX
		if ((ballx+20 > p1x-25 and ballx-20 < p1x+25) and (bally+20>p1y-50 and bally-20<p1y+50)) or ((ballx+20 > p2x-25 and ballx-20 < p2x+25) and (bally+20>p2y-50 and bally-20<p2y+50)) :
			self.ball.hit()
def main():
	Key_P1 = 0
	Key_P2 = 0
	game = TakeMyBall()
	game.run()

if __name__ == '__main__':
	main()

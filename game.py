import pygame
import math
from math import *
from map import *
from constants import *
from player import *
from finish import *
from enemy import *

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
		self.clock = pygame.time.Clock()

		self.build()

	def build(self):
		self.finish = Finish(self)
		self.map = Map(self)
		self.player = Player(self)
		self.enemy = Enemy(self)

	def update(self):
		self.player.update()
		self.enemy.update()
		pygame.display.flip()
		self.clock.tick(FPS)

	def draw(self):
		self.screen.fill(BLACK)
		self.map.draw()
		self.finish.draw()
		self.enemy.draw()
		self.player.draw()

	def is_finish(self):
		if self.player.rect.colliderect(self.finish.rect):
			return True	

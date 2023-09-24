import pygame
import math
from math import *
from map import *
from constants import *
from player import *

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
		self.clock = pygame.time.Clock()

		self.build()

	def build(self):
		self.map = Map(self)
		self.player = Player(self)

	def update(self):
		self.player.update()
		pygame.display.flip()
		self.clock.tick(FPS)

	def draw(self):
		self.screen.fill(BLACK)
		self.map.draw()
		self.player.draw()

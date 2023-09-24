import pygame
import math
from entity import *
from constants import *
from functions import *
from map import *

enemy_x = 1.5*CELL_SIZE
enemy_y = (len(str_map[0])-1.5)*CELL_SIZE

class Enemy(Entity):
	def __init__(self,game):
		super().__init__(enemy_x,enemy_y)
		self.game = game
	
	def draw(self):
		pygame.draw.circle(self.game.screen, RED, self.pos, 10)

	def update(self):
		self.move()

	def move(self):
		next_x, next_y = mapping(self.game.player.x,self.game.player.y)
		next_x += CELL_SIZE // 2
		next_y += CELL_SIZE // 2

		angle = math.atan2(next_y - self.y, next_x - self.x)

		self.x += math.cos(angle) * ENEMY_SPEED
		self.y += math.sin(angle) * ENEMY_SPEED
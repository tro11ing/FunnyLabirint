import pygame
import math
from entity import *
from constants import *
from functions import *
from map import *

class Enemy(Entity):
	def __init__(self,game,x,y,path,scale,shift):
		super().__init__(game,x,y,path,scale,shift)

	def update(self):
		self.move()

	def check_collision(self,dx,dy):
		if dx != 0:
			delta_x = (self.side // 2) * abs(dx) / dx
			if mapping(self.x + dx + delta_x, self.y + delta_x) in self.game.map.set_walls:
				dx = 0
			if mapping(self.x + dx + delta_x, self.y - delta_x) in self.game.map.set_walls:
				dx = 0

		if dy != 0:
			delta_y = (self.side // 2) * abs(dy) / dy
			if mapping(self.x + delta_y, self.y + dy + delta_y) in self.game.map.set_walls:
				dy = 0
			if mapping(self.x - delta_y, self.y + dy + delta_y) in self.game.map.set_walls:
				dy = 0

		self.x += dx
		self.y += dy

	def move(self):
		m_x, m_y = mapping(self.x,self.y)
		m_x //= CELL_SIZE
		m_y //= CELL_SIZE
		pl_x, pl_y = mapping(self.game.player.x,self.game.player.y)
		pl_x //= CELL_SIZE
		pl_y //= CELL_SIZE
		next_x, next_y = self.game.pathfinding.get_path((m_x,m_y),(pl_x,pl_y))
		next_x *= CELL_SIZE
		next_y *= CELL_SIZE
		next_x += CELL_SIZE // 2
		next_y += CELL_SIZE // 2

		angle = math.atan2(next_y - self.y, next_x - self.x)

		dx = math.cos(angle) * ENEMY_SPEED
		dy = math.sin(angle) * ENEMY_SPEED

		self.check_collision(dx,dy)

		self.rect.center = self.x, self.y
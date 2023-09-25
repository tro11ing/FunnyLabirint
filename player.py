import pygame
import math
from constants import *
from functions import *

class Player():
	def __init__(self,game):
		self.x = PLAYER_X
		self.y = PLAYER_Y
		self.side = 20
		self.rect = pygame.Rect(self.x,self.y, self.side, self.side)
		self.game = game
		self.angle = 0

	@property
	def pos(self):
		return (self.x,self.y)

	def move(self):
		dx = 0
		dy = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			dx = PLAYER_SPEED * math.cos(self.angle)
			dy = PLAYER_SPEED * math.sin(self.angle)
		if keys[pygame.K_s]:
			dx = -PLAYER_SPEED * math.cos(self.angle)
			dy = -PLAYER_SPEED * math.sin(self.angle)
		if keys[pygame.K_a]:
			self.angle -= 0.05
		if keys[pygame.K_d]:
			self.angle += 0.05

		self.check_collision(dx,dy)

		self.angle %= DOUBLE_PI

		self.rect.center = self.x, self.y

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

	def update(self):
		self.move()


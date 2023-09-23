import pygame
from entity import *
from constants import *
from map import walls,rect_walls
from raycast import mapping

class Player(Entity):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.angle = 0


	def check_collision(self, dx, dy):
		if dx != 0:
			delta_x = (self.side // 2) * abs(dx) / dx
			if mapping(self.x + dx + delta_x, self.y + delta_x) in walls:
				dx = 0
			if mapping(self.x + dx + delta_x, self.y - delta_x) in walls:
				dx = 0

		if dy != 0:
			delta_y = (self.side // 2) * abs(dy) / dy
			if mapping(self.x + delta_y, self.y + dy + delta_y) in walls:
				dy = 0
			if mapping(self.x - delta_y, self.y + dy + delta_y) in walls:
				dy = 0

		self.x += dx
		self.y += dy

	
	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			dx = PLAYER_SPEED * math.cos(self.angle)
			dy = PLAYER_SPEED * math.sin(self.angle)
			self.check_collision(dx, dy)
		if keys[pygame.K_s]:
			dx = -PLAYER_SPEED * math.cos(self.angle)
			dy = -PLAYER_SPEED * math.sin(self.angle)
			self.check_collision(dx, dy)
		if keys[pygame.K_a]:
			self.angle -= 0.05
		if keys[pygame.K_d]:
			self.angle += 0.05		

		self.rect.center = self.x, self.y
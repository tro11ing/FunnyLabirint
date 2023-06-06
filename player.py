import pygame
from constants import *
from map import walls,rect_walls
from raycast import mapping

class Player:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.angle = 0

		self.side = 20
		self.rect = pygame.Rect(self.x,self.y, self.side, self.side)

	@property
	def pos(self):
		return (self.x,self.y)

	# def check_collision(self, dx, dy):
	# 	next_rect = self.rect.copy()
	# 	next_rect.move_ip(dx, dy)
	# 	collisions = next_rect.collidelistall(rect_walls)

	# 	if len(collisions):
	# 		delta_x, delta_y = 0,0
	# 		for hit in collisions:
	# 			hit_rect = rect_walls[hit]
	# 			if dx > 0:
	# 				delta_x += next_rect.right - hit_rect.left
	# 			else:
	# 				delta_x += hit_rect.right - next_rect.left
	# 			if dy > 0:
	# 				delta_y += next_rect.bottom - hit_rect.top
	# 			else:
	# 				delta_y += hit_rect.bottom - next_rect.top
	# 		if abs(delta_x - delta_y) < 10:
	# 			dx, dy = 0, 0
	# 		elif delta_x > delta_y:
	# 			dy = 0
	# 		elif delta_y > delta_x:
	# 			dx = 0

	# 	self.x += dx
	# 	self.y += dy

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
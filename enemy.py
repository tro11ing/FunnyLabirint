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
		self.player = game.player
		self.image = pygame.image.load("./sprites/enemy.png").convert_alpha()
		self.IMAGE_WIDTH = self.image.get_width()
		self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
		self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
		self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
		self.sprite_half_width = 0
		self.SPRITE_SCALE = 50
		self.SPRITE_SHIFT = 0

	def get_sprite_projection(self):
		proj = DIST / self.norm_dist * self.SPRITE_SCALE
		proj_width, proj_height = proj * self.IMAGE_RATIO, proj

		image = pygame.transform.scale(self.image, (proj_width, proj_height))

		self.sprite_half_width = proj_width // 2
		height_shift = proj_height * self.SPRITE_SHIFT
		pos = self.screen_x - self.sprite_half_width, SCREEN_H//2 - proj_height // 2 + height_shift

		self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

	def get_sprite(self):
		dx = self.x - self.player.x
		dy = self.y - self.player.y
		self.dx, self.dy = dx, dy
		self.theta = math.atan2(dy, dx)

		delta = self.theta - self.player.angle
		if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
			delta += DOUBLE_PI

		delta_rays = delta / SPACE_ANGLE
		self.screen_x = (NUM_RAYS//2 + delta_rays) * SCALE

		self.dist = math.hypot(dx, dy)
		self.norm_dist = self.dist * math.cos(delta)
		if -self.IMAGE_HALF_WIDTH < self.screen_x < (SCREEN_W + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
			self.get_sprite_projection()

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
import pygame
import math
from map import *
from constants import *
from player import *
from enemy import *
from pathfinding import *
from raycast import *

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
		self.clock = pygame.time.Clock()

		self.build()

	def build(self):
		self.map = Map(self)
		self.player = Player(self)
		self.finish = Entity(self,FINISH_X,FINISH_Y,"./sprites/flag.png",50,0)
		self.enemy = Enemy(self,ENEMY_X,ENEMY_Y,"./sprites/enemy.png",50,0)
		self.pathfinding = PathFinding(self)
		self.raycasting = RayCasting(self)

	def update(self):
		self.player.update()
		self.enemy.update()
		self.raycasting.raycast()
		self.finish.get_sprite()
		self.enemy.get_sprite()
		pygame.display.flip()
		self.clock.tick(FPS)

	def draw(self):
		self.render_objects()

	def is_finish(self):
		if self.player.rect.colliderect(self.finish.rect):
			return True

	def is_enemy(self):
		if self.player.rect.colliderect(self.enemy.rect):
			return True

	def render_objects(self):
		list_objects = sorted(self.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
		for depth, image, pos in list_objects:
			if image == "":
				c1 = 201 / (1 + depth * depth * 0.00003)
				c2 = 133 / (1 + depth * depth * 0.00003)
				c3 = 104 / (1 + depth * depth * 0.00003)
				color = (c1,c2,c3)
				pygame.draw.rect(self.screen,color,pos)
			else:
				self.screen.blit(image, pos)
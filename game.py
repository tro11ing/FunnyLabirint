import pygame
import math
from map import *
from constants import *
from player import *
from finish import *
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
		self.finish = Finish(self)
		self.enemy = Enemy(self)
		self.pathfinding = PathFinding(self)
		self.raycasting = RayCasting(self)

	def update(self):
		self.player.update()
		self.enemy.update()
		self.raycasting.raycast()
		self.finish.get_sprite()
		pygame.display.flip()
		self.clock.tick(FPS)

	def draw(self):
		self.screen.fill(BLACK)
		self.render_game_objects()

	def is_finish(self):
		if self.player.rect.colliderect(self.finish.rect):
			return True	

	def render_game_objects(self):
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
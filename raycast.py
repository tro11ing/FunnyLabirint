import pygame
import math
from constants import *
from functions import *

class RayCasting:
	def __init__(self,game):
		self.game = game

	def raycast(self):
		x0,y0 = self.game.player.pos
		xm,ym = mapping(x0,y0)
		cur_angle = self.game.player.angle - FOV / 2
		for ray in range(NUM_RAYS):
			sin_a = math.sin(cur_angle)
			cos_a = math.cos(cur_angle)
			
			if cos_a >= 0:
				x = xm + CELL_SIZE
				dx = 1
			else:
				x = xm
				dx = -1

			for i in range(0,SCREEN_W,CELL_SIZE):
				depth_v = (x - x0) / cos_a
				y = y0 + depth_v * sin_a
				if mapping(x + dx, y) in self.game.map.set_walls:
					break
				x += dx*CELL_SIZE

			if sin_a >= 0:
				y = ym + CELL_SIZE
				dy = 1
			else:
				y = ym
				dy = -1

			for i in range(0,SCREEN_H,CELL_SIZE):
				depth_h = (y - y0) / sin_a
				x = x0 + depth_h * cos_a
				if mapping(x, y + dy) in self.game.map.set_walls:
					break
				y += dy*CELL_SIZE

			depth = min(depth_h,depth_v)


			depth *= math.cos(self.game.player.angle - cur_angle)
			depth = max(depth,0.00001)
			proj_height = min(int(PROJ_SCALE / depth), SCREEN_H)
			c1 = 201 / (1 + depth * depth * 0.00003)
			c2 = 133 / (1 + depth * depth * 0.00003)
			c3 = 104 / (1 + depth * depth * 0.00003)
			color = (c1,c2,c3)
			pygame.draw.rect(self.game.screen,color,(ray*SCALE, SCREEN_H // 2 - proj_height // 2, SCALE, proj_height))
			cur_angle += SPACE_ANGLE
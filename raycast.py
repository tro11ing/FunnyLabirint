import math
import pygame
from constants import *
from map import *

def mapping(x,y):
	return (x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE)

def raycast(screen, player_pos, player_angle, my_map):
	x0,y0 = player_pos
	xm,ym = mapping(x0,y0)
	cur_angle = player_angle - FOV / 2
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
			if mapping(x + dx, y) in my_map.walls:
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
			if mapping(x, y + dy) in my_map.walls:
				break
			y += dy*CELL_SIZE

		depth = depth_v if depth_v < depth_h else depth_h
		depth *= math.cos(player_angle - cur_angle) + 0.1
		depth = max(depth,0.00001)
		proj_height = min(int(PROJ_SCALE / depth), SCREEN_H)
		c = 255 / (1 + depth * depth * 0.00003)
		color = (c,c,c)
		pygame.draw.rect(screen,color,(ray*SCALE, SCREEN_H // 2 - proj_height // 2, SCALE, proj_height))
		cur_angle += SPACE_ANGLE
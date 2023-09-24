import pygame
import math
from math import *
from constants import *
from player import *

def mapping(x,y):
	return (x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE)

def check_collision(player, dx, dy, set_walls):
	if dx != 0:
		delta_x = (player.side // 2) * abs(dx) / dx
		if mapping(player.x + dx + delta_x, player.y + delta_x) in set_walls:
			dx = 0
		if mapping(player.x + dx + delta_x, player.y - delta_x) in set_walls:
			dx = 0

	if dy != 0:
		delta_y = (player.side // 2) * abs(dy) / dy
		if mapping(player.x + delta_y, player.y + dy + delta_y) in set_walls:
			dy = 0
		if mapping(player.x - delta_y, player.y + dy + delta_y) in set_walls:
			dy = 0

	return dx, dy


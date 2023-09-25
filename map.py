import pygame
from constants import *

class Map:
	def __init__(self, game):
		self.game = game
		self.str_map = STR_MAP
		self.set_walls=set()
		self.rect_walls = []
		self.build()

	def build(self):
		for line in range(len(self.str_map)):
			for col in range(len(self.str_map[0])):
				if self.str_map[line][col] == '1':
					self.set_walls.add((col*CELL_SIZE,line*CELL_SIZE))
					self.rect_walls.append(pygame.Rect(col*CELL_SIZE,line*CELL_SIZE,CELL_SIZE,CELL_SIZE))

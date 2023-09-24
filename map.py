import pygame
from constants import *
from finish import *

str_map=["11111111111111111111",
         "10000000000000010001",
         "10111101111110000001",
         "10010000000011110101",
         "10010111001001000101",
         "10010000001001000101",
         "10110011000000001101",
         "10010001111110001001",
         "10111111000000001101",
         "10000000011001000001",
         "11101110000001001001",
         "10000000000001011001",
         "10111101101011010001",
         "10001001001000000011",
         "10001001001011111111",
         "10001000000000000001",
         "10100001111110110001",
         "10101100101000000001",
         "10100100001000111001",
         "11111111111111111111"]

class Map:
	def __init__(self, game):
		self.game = game
		self.str_map = str_map
		self.set_walls=set()
		self.rect_walls = []
		self.build()

	def build(self):
		for line in range(len(self.str_map)):
			for col in range(len(self.str_map[0])):
				if self.str_map[line][col] == '1':
					self.set_walls.add((col*CELL_SIZE,line*CELL_SIZE))
					self.rect_walls.append(pygame.Rect(col*CELL_SIZE,line*CELL_SIZE,CELL_SIZE,CELL_SIZE))

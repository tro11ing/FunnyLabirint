import pygame
import math
from math import *
from constants import *
from player import *
from finish import *
from functions import *
from game import *

pygame.init()

game = Game()

finish_x=(len(str_map[0])-2)*CELL_SIZE
finish_y=(len(str_map)-2)*CELL_SIZE
running = True

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	game.update()
	game.draw()

	if game.is_finish():
		running = False
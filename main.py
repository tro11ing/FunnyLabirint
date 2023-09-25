import pygame
import math
from math import *
from constants import *
from player import *
from functions import *
from game import *

pygame.init()

game = Game()

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
		print("Победа!")

	if game.is_enemy():
		running = False
		print("Поражение...")
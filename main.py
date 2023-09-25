import pygame
import math
from math import *
from constants import *
from player import *
from functions import *
from game import *

inp = 0

while inp != 1 and inp != 2:
	print("Выберите время суток:\n1. День\n2. Ночь")
	inp = int(input())

pygame.init()

game = Game()

running = True

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False

	game.update()
	if inp == 1:
		floor_color = (210,131,102)
		sky_color = (153,255,255)
	else:
		floor_color = (30,17,13)
		sky_color = (0,0,102)
	pygame.draw.rect(game.screen,floor_color, (0,SCREEN_H//2,SCREEN_W,SCREEN_H//2))
	pygame.draw.rect(game.screen,sky_color, (0,0,SCREEN_W,SCREEN_H//2))
	game.draw()

	if game.is_finish():
		running = False
		print("Победа!")

	if game.is_enemy():
		running = False
		print("Поражение...")
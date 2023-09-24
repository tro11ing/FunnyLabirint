import pygame
import math
from math import *
from constants import *
from map import *
from player import *
from finish import *
from raycast import *


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

floor = pygame.image.load('sprites/floor1.png')

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

my_map = Map(str_map)
my_map.build()

player_x=CELL_SIZE*1.5
player_y=CELL_SIZE*1.5

finish_x=(len(str_map[0])-2)*CELL_SIZE
finish_y=(len(str_map)-2)*CELL_SIZE

player = Player(player_x,player_y)
finish = Finish(finish_x,finish_y)

running = True

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	player.move(my_map)
	
	screen.fill(BLACK)

	pygame.draw.rect(screen,SKY,(0,0,SCREEN_W,SCREEN_H//2))
	screen.blit(floor,(0,SCREEN_H//2,SCREEN_W,SCREEN_H//2))

	raycast(screen,player.pos,player.angle, my_map)

	pygame.display.flip()

	if player.rect.colliderect(finish.rect):
		exit()

	clock.tick(FPS)
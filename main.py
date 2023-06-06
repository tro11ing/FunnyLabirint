import pygame
import math
from math import *
from constants import *
from map import *
from player import *
from raycast import *


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

floor = pygame.image.load('sprites/floor1.png')

x=CELL_SIZE*1.5
y=CELL_SIZE*1.5

player = Player(x,y)

running = True

while running:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	player.move()
	
	screen.fill(BLACK)

	pygame.draw.rect(screen,SKY,(0,0,SCREEN_W,SCREEN_H//2))
	screen.blit(floor,(0,SCREEN_H//2,SCREEN_W,SCREEN_H//2))

	raycast(screen,player.pos,player.angle)

	pygame.display.flip()

	clock.tick(FPS)
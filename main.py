import pygame
import math
from settings import *


str_map=["1111111111",
          "1000000001",
          "1000110001",
          "1000000001",
          "1000000001",
          "1000011001",
          "1000011101",
          "1000000101",
          "1011100101",
          "1111111111",]

walls=set()

for line in range(len(str_map)):
	for col in range(len(str_map[0])):
		if str_map[line][col] == '1':
			walls.add((line*CELL_SIZE,col*CELL_SIZE))


pygame.init()

clock = pygame.time.Clock()

class Player:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.angle = 0

	@property
	def pos(self):
		return (self.x,self.y)
	

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.y -= PLAYER_SPEED
		elif keys[pygame.K_s]:
			self.y += PLAYER_SPEED
		elif keys[pygame.K_a]:
			self.x -= PLAYER_SPEED
		elif keys[pygame.K_d]:
			self.x += PLAYER_SPEED
		elif keys[pygame.K_l]:
			self.angle -= 0.02
		elif keys[pygame.K_h]:
			self.angle += 0.02

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

x=SCREEN_W/2
y=SCREEN_H/2

player = Player(x,y)

running = True

while running:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	player.move()
	
	screen.fill(BLACK)

	pygame.draw.circle(screen,GREEN,player.pos,12)
	pygame.draw.line(screen,RED,player.pos,(player.x + SCREEN_W * math.sin(player.angle),player.y + SCREEN_W * math.cos(player.angle)))

	for x,y in walls:
		pygame.draw.rect(screen,WHITE,(x,y,CELL_SIZE,CELL_SIZE),1)

	pygame.display.flip()

	clock.tick(FPS)
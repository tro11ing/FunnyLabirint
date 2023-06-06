import pygame
import math
from settings import *


str_map=["1111111111",
          "1000000001",
          "1000110001",
          "1000000001",
          "1000000001",
          "1000000001",
          "1000000101",
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

def raycasting(screen, player_pos, player_angle):
	cur_angle = player_angle - FOV / 2
	x0,y0=player_pos
	for ray in range(NUM_RAYS):
		sin_a = math.sin(cur_angle)
		cos_a = math.cos(cur_angle)
		for depth in range(DEPTH):
			x = x0 + depth * cos_a
			y = y0 + depth * sin_a
			if (x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE) in walls:
				depth *= math.cos(player_angle - cur_angle) + 0.1
				proj_height = PROJ_SCALE / depth
				c = 255 / (1 + depth * depth * 0.0001)
				color = (c,c,c)
				pygame.draw.rect(screen,color,(ray*SCALE, SCREEN_H // 2 - proj_height // 2, SCALE, proj_height))
				break
		cur_angle += SPACE_ANGLE

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
			self.x += PLAYER_SPEED * math.cos(self.angle)
			self.y += PLAYER_SPEED * math.sin(self.angle)
		elif keys[pygame.K_s]:
			self.x -= PLAYER_SPEED * math.cos(self.angle)
			self.y -= PLAYER_SPEED * math.sin(self.angle)
		elif keys[pygame.K_a]:
			self.x += PLAYER_SPEED * math.sin(self.angle)
			self.y -= PLAYER_SPEED * math.cos(self.angle)
		elif keys[pygame.K_d]:
			self.x -= PLAYER_SPEED * math.sin(self.angle)
			self.y += PLAYER_SPEED * math.cos(self.angle)
		elif keys[pygame.K_l]:
			self.angle += 0.02
		elif keys[pygame.K_h]:
			self.angle -= 0.02

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

	raycasting(screen,player.pos,player.angle)

	# pygame.draw.circle(screen,GREEN,player.pos,12)

	# for x,y in walls:
	# 	pygame.draw.rect(screen,WHITE,(x,y,CELL_SIZE,CELL_SIZE),1)

	pygame.display.flip()

	clock.tick(FPS)
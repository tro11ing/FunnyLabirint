import pygame
import math
from settings import *


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
         "11111111111111111111",]

walls=set()

for line in range(len(str_map)):
	for col in range(len(str_map[0])):
		if str_map[line][col] == '1':
			walls.add((line*CELL_SIZE,col*CELL_SIZE))


pygame.init()

clock = pygame.time.Clock()

def mapping(x,y):
	return (x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE)

def raycast(screen, player_pos, player_angle):
	x0,y0 = player_pos
	xm,ym = mapping(x0,y0)
	cur_angle = player_angle - FOV / 2
	for ray in range(NUM_RAYS):
		sin_a = math.sin(cur_angle)
		cos_a = math.cos(cur_angle)
		
		if cos_a >= 0:
			x = xm + CELL_SIZE
			dx = 1
		else:
			x = xm
			dx = -1

		for i in range(0,SCREEN_W,CELL_SIZE):
			depth_v = (x - x0) / cos_a
			y = y0 + depth_v * sin_a
			if mapping(x + dx, y) in walls:
				break
			x += dx*CELL_SIZE

		if sin_a >= 0:
			y = ym + CELL_SIZE
			dy = 1
		else:
			y = ym
			dy = -1

		for i in range(0,SCREEN_H,CELL_SIZE):
			depth_h = (y - y0) / sin_a
			x = x0 + depth_h * cos_a
			if mapping(x, y + dy) in walls:
				break
			y += dy*CELL_SIZE

		depth = depth_v if depth_v < depth_h else depth_h
		depth *= math.cos(player_angle - cur_angle) + 0.1
		depth = max(depth,0.00001)
		proj_height = min(int(PROJ_SCALE / depth), SCREEN_H)
		c = 255 / (1 + depth * depth * 0.00003)
		color = (c,c,c)
		pygame.draw.rect(screen,color,(ray*SCALE, SCREEN_H // 2 - proj_height // 2, SCALE, proj_height))
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
		if keys[pygame.K_s]:
			self.x -= PLAYER_SPEED * math.cos(self.angle)
			self.y -= PLAYER_SPEED * math.sin(self.angle)
		if keys[pygame.K_a]:
			self.angle -= 0.05
		if keys[pygame.K_d]:
			self.angle += 0.05

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

	# pygame.draw.circle(screen,GREEN,player.pos,12)

	# for x,y in walls:
	# 	pygame.draw.rect(screen,WHITE,(x,y,CELL_SIZE,CELL_SIZE),1)

	pygame.display.flip()

	clock.tick(FPS)
import pygame
from constants import *

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
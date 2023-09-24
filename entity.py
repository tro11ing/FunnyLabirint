import pygame

# Родительский класс игрока и врага
class Entity:
	def __init__(self,x,y,side=20):
		self.x = x
		self.y = y

		self.side = side
		self.rect = pygame.Rect(self.x,self.y, self.side, self.side)

	@property
	def pos(self):
		return (self.x,self.y)

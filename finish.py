import pygame
from constants import *
from entity import *

class Finish(Entity):
	def __init__(self,x,y):
		super().__init__(x,y,CELL_SIZE)
		
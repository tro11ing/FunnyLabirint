import pygame
import math
from entity import *
from constants import *
from map import *

finish_x = (len(str_map)-1.5)*CELL_SIZE
finish_y = (len(str_map[0])-1.5)*CELL_SIZE

class Finish(Entity):
	def __init__(self,game):
		super().__init__(finish_x,finish_y)
		self.game = game


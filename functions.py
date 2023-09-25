import pygame
import math
from math import *
from constants import *
from player import *

def mapping(x,y):
	return (x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE)
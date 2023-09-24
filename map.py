import pygame
from constants import *

class Map():
    def __init__(self,str_map):
        self.str_map = str_map
        self.walls=set()
        self.rect_walls = []


    def build(self):
        for line in range(len(self.str_map)):
            for col in range(len(self.str_map[0])):
                if self.str_map[line][col] == '1':
                    self.walls.add((line*CELL_SIZE,col*CELL_SIZE))
                    self.rect_walls.append(pygame.Rect(line*CELL_SIZE,col*CELL_SIZE,CELL_SIZE,CELL_SIZE))




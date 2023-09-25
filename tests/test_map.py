import pygame
from constants import *
from map import *
from game import *

game = Game()

def test_init_good():
	new_map = Map(game)
	assert isinstance(new_map, Map)

def test_init_bad():
	new_map = Player(game)
	assert not isinstance(new_map, Map)

def test_build():
	new_map = Map(game)
	new_map.set_walls=set()
	new_map.rect_walls = []
	new_map.build()
	assert len(new_map.set_walls) != 0
	assert len(new_map.rect_walls) != 0
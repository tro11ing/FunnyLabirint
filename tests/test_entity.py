import pygame
import math
from constants import *
from map import *
from game import *

game = Game()

def test_init_good():
	entity = Entity(game,0,0,"./sprites/test.png",0,0)
	assert isinstance(entity, Entity)

def test_init_bad():
	entity = Player(game)
	assert not isinstance(entity, Entity)

def test_pos_pos():
	entity = Entity(game,0,0,"./sprites/test.png",0,0)
	entity.x = 123
	entity.y = 123
	assert entity.pos == (entity.x,entity.y)

def test_pos_zero():
	entity = Entity(game,0,0,"./sprites/test.png",0,0)
	entity.x = 0
	entity.y = 0
	assert entity.pos == (entity.x,entity.y)

def test_pos_neg():
	entity = Entity(game,0,0,"./sprites/test.png",0,0)
	entity.x = -123
	entity.y = -123
	assert entity.pos == (entity.x,entity.y)


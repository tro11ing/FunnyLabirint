import pygame
import math
from constants import *
from functions import *
from entity import *
from game import *

game = Game()

def test_init_good():
	player = Player(game)
	assert isinstance(player, Player)

def test_init_bad():
	player = Map(game)
	assert not isinstance(player, Player)

def test_pos_pos():
	player = Player(game)
	player.x = 123
	player.y = 123
	assert player.pos == (player.x,player.y)

def test_pos_zero():
	player = Player(game)
	player.x = 0
	player.y = 0
	assert player.pos == (player.x,player.y)

def test_pos_neg():
	player = Player(game)
	player.x = -123
	player.y = -123
	assert player.pos == (player.x,player.y)

def test_check_collision_x_bad():
	player = Player(game)
	start_point = player.pos
	dx = -CELL_SIZE//2
	dy = 0
	player.check_collision(dx,dy)
	assert start_point == player.pos

def test_check_collision_x_good():
	player = Player(game)
	start_point = player.pos
	dx = CELL_SIZE//2
	dy = 0
	player.check_collision(dx,dy)
	assert start_point != player.pos

def test_check_collision_y_bad():
	player = Player(game)
	start_point = player.pos
	dx = 0
	dy = -CELL_SIZE//2
	player.check_collision(dx,dy)
	assert start_point == player.pos

def test_check_collision_y_good():
	player = Player(game)
	start_point = player.pos
	dx = 0
	dy = CELL_SIZE//2
	player.check_collision(dx,dy)
	assert start_point != player.pos

def test_check_collision_xy_bad():
	player = Player(game)
	start_point = player.pos
	dx = -CELL_SIZE
	dy = -CELL_SIZE
	player.check_collision(dx,dy)
	assert start_point == player.pos

def test_check_collision_xy_bad():
	player = Player(game)
	start_point = player.pos
	dx = 1
	dy = 1
	player.check_collision(dx,dy)
	assert start_point != player.pos
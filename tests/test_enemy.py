import pygame
import math
from game import *

game = Game()

def test_init_good():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	assert isinstance(enemy, Enemy)

def test_init_bad():
	enemy = Map(game)
	assert not isinstance(enemy, Enemy)

def test_check_collision_x_bad():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = -CELL_SIZE//2
	dy = 0
	enemy.check_collision(dx,dy)
	assert start_point == enemy.pos

def test_check_collision_x_good():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = 1
	dy = 0
	enemy.check_collision(dx,dy)
	assert start_point != enemy.pos

def test_check_collision_y_bad():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = 0
	dy = CELL_SIZE//2
	enemy.check_collision(dx,dy)
	assert start_point == enemy.pos

def test_check_collision_y_good():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = 0
	dy = -CELL_SIZE//2
	enemy.check_collision(dx,dy)
	assert start_point != enemy.pos

def test_check_collision_xy_bad():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = -CELL_SIZE
	dy = -CELL_SIZE
	enemy.check_collision(dx,dy)
	assert start_point == enemy.pos

def test_check_collision_xy_bad():
	enemy = Enemy(game,ENEMY_X,ENEMY_Y,"./sprites/test.png",0,0)
	start_point = enemy.pos
	dx = 1
	dy = 1
	enemy.check_collision(dx,dy)
	assert start_point != enemy.pos
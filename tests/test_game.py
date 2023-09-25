import pygame
import math
from game import *

game1 = Game()

def test_init_good():
	game = Game()
	assert isinstance(game, Game)

def test_init_bad():
	game = Player(game1)
	assert not isinstance(game, Game)

def test_init_objects():
	game = Game()
	assert isinstance(game.map, Map)
	assert isinstance(game.player, Player)
	assert isinstance(game.finish, Entity)
	assert isinstance(game.enemy, Enemy)
	assert isinstance(game.pathfinding, PathFinding)
	assert isinstance(game.raycasting, RayCasting)

def test_finish_good():
	game = Game()
	game.player.x = game.finish.x
	game.player.y = game.finish.y
	game.update()
	assert game.is_finish() == True

def test_finish_bad():
	game = Game()
	game.player.x = game.finish.x - CELL_SIZE
	game.player.y = game.finish.y - CELL_SIZE
	game.update()
	assert game.is_finish() != True

def test_enemy_good():
	game = Game()
	game.player.x = game.enemy.x
	game.player.y = game.enemy.y
	game.update()
	assert game.is_enemy() == True

def test_enemy_bad():
	game = Game()
	game.player.x = game.enemy.x - CELL_SIZE
	game.player.y = game.enemy.y - CELL_SIZE
	game.update()
	assert game.is_enemy() != True
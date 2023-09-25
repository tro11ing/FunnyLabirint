import pygame
import math
from constants import *
from pathfinding import *
from game import *

game = Game()

def test_init_good():
	pathfinding = PathFinding(game)
	assert isinstance(pathfinding, PathFinding)

def test_init_bad():
	pathfinding = Player(game)
	assert not isinstance(pathfinding, PathFinding)

def test_build():
	pathfinding = PathFinding(game)
	pathfinding.graph = {}
	pathfinding.build_graph()
	assert len(pathfinding.graph) != 0


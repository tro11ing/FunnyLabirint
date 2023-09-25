import pygame
import math
from constants import *
from functions import *
from game import *

game = Game()

def test_init_good():
	raycasting = RayCasting(game)
	assert isinstance(raycasting, RayCasting)

def test_init_bad():
	raycasting = Player(game)
	assert not isinstance(raycasting, RayCasting)

def test_build():
	raycasting = RayCasting(game)
	raycasting.objects_to_render = []
	raycasting.raycast()
	assert len(raycasting.objects_to_render) != 0
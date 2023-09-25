from functions import *
from constants import *

def test_mapping_1():
	x = 123
	y = 123
	xm, ym = mapping(x,y)
	assert xm == x // CELL_SIZE * CELL_SIZE
	assert ym == y // CELL_SIZE * CELL_SIZE

def test_mapping_2():
	xm, ym = mapping(0,0)
	assert xm == 0
	assert ym == 0

def test_mapping_3():
	x = -123
	y = -123
	xm, ym = mapping(x,y)
	assert xm == x // CELL_SIZE * CELL_SIZE
	assert ym == y // CELL_SIZE * CELL_SIZE

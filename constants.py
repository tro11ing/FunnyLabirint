import math

# Цвета
BLACK  = (0,   0,   0)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (0,  255,  0)
BLUE   = (0,  0,  255)
CYAN   = (0,  255,255)
YELLOW = (255, 255, 0)
MAGENTA= (255, 0, 255)
FLOOR  = (105, 67, 42)
SKY    = (244,216,213)

# Параметры экрана
SCREEN_W=1000
SCREEN_H=800
FPS=60

# Параметры поля
CELL_SIZE=40

# Параметры игрока
PLAYER_POS = PLAYER_X, PLAYER_Y = CELL_SIZE*1.5, CELL_SIZE*1.5
PLAYER_SPEED=3
PLAYER_ROT_SPEED=0.05
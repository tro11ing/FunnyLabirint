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
SCREEN_W=1200
SCREEN_H=800
FPS=60

# Параметры поля
CELL_SIZE=60

# Параметры рендеринга
FOV=int(math.pi/2.5)
NUM_RAYS=600
DEPTH=500
SPACE_ANGLE=FOV/NUM_RAYS
SCALE=SCREEN_W/NUM_RAYS
DIST=NUM_RAYS / math.tan(FOV/2)
PROJ_SCALE=DIST*CELL_SIZE * 3 // 5

# Параметры спрайтов
DOUBLE_PI = math.pi*2
CENTER_RAY = NUM_RAYS // 2 - 1

# Параметры игрока
PLAYER_POS = PLAYER_X, PLAYER_Y = CELL_SIZE*1.5, CELL_SIZE*1.5
PLAYER_SPEED=3
PLAYER_ROT_SPEED=0.05

#Параметры врага
ENEMY_SPEED=1
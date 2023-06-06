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
CELL_SIZE=60

# Параметры рендеринга
FOV=math.pi/3
NUM_RAYS=200
DEPTH=500
SPACE_ANGLE=FOV/NUM_RAYS
SCALE=SCREEN_W/NUM_RAYS
DIST=NUM_RAYS / (math.tan(FOV/2)*2)
PROJ_SCALE=DIST*CELL_SIZE * 3

# Параметры игрока
PLAYER_SPEED=3
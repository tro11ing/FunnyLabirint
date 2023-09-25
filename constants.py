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

STR_MAP=["11111111111111111111",
         "10000000000000010001",
         "10111101111110000001",
         "10010000000011110101",
         "10010111001001000101",
         "10010000001001000101",
         "10110011000000001101",
         "10010001111110001001",
         "10111111000000001101",
         "10000000011001000001",
         "11101110000001001001",
         "10000000000001011001",
         "10111101101011010001",
         "10001001001000000011",
         "10001001001011111111",
         "10001000000000000001",
         "10100001111110110001",
         "10101100101000000001",
         "10100100001000111001",
         "11111111111111111111"]

FINISH_X = (len(STR_MAP)-1.5)*CELL_SIZE
FINISH_Y = (len(STR_MAP[0])-1.5)*CELL_SIZE

ENEMY_X = 1.5*CELL_SIZE
ENEMY_Y = (len(STR_MAP[0])-1.5)*CELL_SIZE

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
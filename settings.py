# File created by Ben Pfaff

# screen color  
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255,255,255)
GREEN = (0,255,0)
# screen dimensions
WIDTH = 800
HEIGHT = 600

# game settings:
FPS = 30
RUNNING = True

# player attributes 
PLAYER_ACC = 2 
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .8
PLAYER_JUMP = 20

# mob attritubutes
MOB_ACC = 2
MOB_FRICTION = -0.12

PAUSED = False 
SCORE = 0

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (100, HEIGHT - 150, 100, 20, (200,100,50), "boost"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (600, HEIGHT - 450, 100, 20, (200,100,50), "fake"),
                 (200, HEIGHT - 350, 100, 20, (200,100,50), "fake2"),
                 (175, 100, 50, 20, (200,200,200), "normal")]
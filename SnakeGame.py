# PROJECT [Snake Game]  "Arda Sahin"


# LIBARIES
import pygame
import random
import time


pygame.init


# DEFINING COLORS
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)



#  SCREEN (WINDOW, FRAMERATE, PLAYER) [1, 2, 3]

# 1) WINDOW SIZE
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# 2) WINDOW SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_TITLE = pygame.display.set_caption("Snake Game")


# 3) FRAMERATE
CLOCK = pygame.time.Clock()
FRAMERATE = CLOCK.tick(10)




# SNAKE [STARTING DIRECTION]
CHANGE_TO = "RIGHT"
DIRECTION = CHANGE_TO



# DEFINING THE SNAKE [1, 2, 3]


# 1) SNAKE PLACEMENT IN SCREEN
SNAKE_X = 100
SNAKE_Y = 30

# 2) SNAKE SIZE
SNAKESIZE_1 = 20
SNAKESIZE_2 = 20

# 3) SNAKE
PLAYER = 1
PLAYER = pygame.draw.rect(SCREEN, GREEN, pygame.Rect(SNAKE_X, SNAKE_Y, SNAKESIZE_1, SNAKESIZE_2))



# FOOD SPAWN IN THE SCREEN
FOOD_X = round(random.randrange(0, SCREEN_WIDTH - SNAKE_X) / 10.0) * 10.0
FOOD_Y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_Y) / 10.0) * 10.0


# DEFINING FOOD
FOOD = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(FOOD_X, FOOD_Y, SNAKESIZE_1, SNAKESIZE_2))
FOOD_SPAWN = True


# SCORE 
SCORE = 0


# WHILE PROGRAM IS RUNNING
RUNNING = True

while RUNNING:

    # FILLING THE SCREEN [COLOR]
    SCREEN.fill(BLACK)

    # DRAWING THE SNAKE [PLAYER]
    PLAYER = pygame.draw.rect(SCREEN, GREEN, PLAYER)
    
    # DRAWING THE FOOD [WORK IN PROGRESS]
    FOOD = pygame.draw.rect(SCREEN, WHITE, FOOD)

  
    # MOVEMENT SYSTEM [1, 2] 

    # 1) KEYBINDS 
    KEYS = pygame.key.get_pressed()
    
    if KEYS[pygame.K_UP]:
      DIRECTION = "UP" 
    
    if KEYS[pygame.K_DOWN]:
      DIRECTION = "DOWN"
    
    if KEYS[pygame.K_LEFT]:
      DIRECTION = "LEFT"
    
    if KEYS[pygame.K_RIGHT]:
      DIRECTION = "RIGHT"
    
    
    # 2) PLAYER MOVING SIMULTANEOUSLY
      
    if DIRECTION == "RIGHT":
        CHANGE_TO = "RIGHT"
        PLAYER.x += 1
        time.sleep(0.001)
    
    if DIRECTION == "LEFT":
        CHANGE_TO = "LEFT"
        PLAYER.x -= 1
        time.sleep(0.001)
    
    if DIRECTION == "UP":
        CHANGE_TO = "UP"
        PLAYER.y -= 1
        time.sleep(0.001)
    
    if DIRECTION == "DOWN":
        CHANGE_TO = "DOWN"
        PLAYER.y += 1
        time.sleep(0.001)
    

    # BORDERS

    if PLAYER.x <= 1:
        time.sleep(1)
        RUNNING = False
    
    elif PLAYER.x >= 780: 
        time.sleep(1)
        RUNNING = False
    
    if PLAYER.y <= 1:
        time.sleep(1)
        RUNNING = False
    
    elif PLAYER.y >= 580:
        time.sleep(1)
        RUNNING = False
    


    # SPEEDING UP MECHANISM

    if PLAYER == FOOD.top:
        SCORE += 1
        FOOD = BLACK
    
    if PLAYER == FOOD.bottom:
        SCORE += 1
        FOOD = BLACK
    
    if PLAYER == FOOD.center:
        SCORE += 1
        FOOD = BLACK
    
    if PLAYER == FOOD.right:
        SCORE += 1
        FOOD = BLACK
    
    if PLAYER == FOOD.left:
        SCORE += 1
        FOOD = BLACK

    # PLAYER GETS FASTER EVERY + 1 SCORE   
    if SCORE + 1:
        PLAYER.y -= 1 * 0.02
        PLAYER.y += 1 * 0.02
        PLAYER.x -= 1 * 0.02
        PLAYER.x += 1 * 0.02
        
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
  
    
    pygame.display.update()
    DT = FRAMERATE / 60


pygame.display.update()

# PRINTS THE TOTAL SCORE
print("SCORE:", SCORE)

pygame.quit()
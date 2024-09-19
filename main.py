import pygame
from grid import Grid

#Initialize Pygame
pygame.init()

#Global varriables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR =(0,0,0)

#Colors 
RED = (255,0,0)
YELLOW = (255,255,51)
PURPLE = (127,0,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
COLORS = [RED,YELLOW,PURPLE,GREEN,BLUE,CYAN]

#Shapes/Tetromino (only has basic rotation scheme)
#I,O,T,S,Z,J and L
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]






#Setup window with the set variables and background color
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
game_grid = Grid()
game_grid.print_grid()



#Game loop
#Keep game running until quit event occurs
game_running = True
while game_running:
    
    #Close if user quits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    
    screen.fill(BACKGROUND_COLOR)
    game_grid.draw(screen)
    
    #Update the GUI game
    pygame.display.update() 
    clock.tick(60)
    

pygame.quit()

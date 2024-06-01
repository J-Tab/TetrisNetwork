import pygame
from grid import Grid

#Initialize Pygame
pygame.init()

#Global varriables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
BACKGROUND_COLOR =(255,255,255)


#Setup window with the set variables and background color
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()
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

    
    pygame.draw.rect(screen, ())
    
    #Update the GUI game
    pygame.display.update() 
    clock.tick(60)
    

pygame.quit()

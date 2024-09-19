import pygame
from colors import Colors
#Play area for the Tetris game

RED = (255,0,0)
YELLOW = (255,255,51)
PURPLE = (127,0,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
DARK_GREY = (12,12,12)

class Grid:
    #create a grid that is 10 by 20
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
            


#testing prints
Grid().print_grid()
from colors import Colors

class Tetromino:
    def __init__(self, id):
        self.id = 0
        self.cells = {}
        self.cell_size = 30
        self.color = Colors.get_cell_colors()
        self.rotation = 0
    def draw(self,screen):


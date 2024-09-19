from tetromino import Tetromino
from position import Position

#I,O,T,S,Z,J and L blocks are in this order
#Cyan, Blue, Orange, Yellow, Green, Purple and Red are the colors for these blocks respectively.
#Colors array give these colors from index 1-7

class IBlock(Tetromino):
    super().__init__(id =1)
    self.cells = {
        0: [Position(1,0), Position(1,1),Position(1,2), Position(1,3)],
        1: [Position(0,3), Position(1,3),Position(2,3), Position(3,3)],
        2: [Position(2,0), Position(2,1),Position(2,2), Position(2,3)],
        3: [Position(0,2), Position(1,2),Position(2,2), Position(3,2)]
    }

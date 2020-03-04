from random import randint
from Backtrack import is_valid



def check_vertical():
    return False
def check_horizontal():
    return False
def check_square():
    return False



def create_completed_sudoku():
    board = [['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],
            ['0','0','0', '0','0','0', '0','0','0'],]
    for x in range(9):
        
        for y in range(9):
            while(board[x][y]== '0'):
                num = str(randint(1,9))
                if is_valid(board, num, [x,y]):
                    board[x][y] = num
    
    return board



print(create_completed_sudoku())

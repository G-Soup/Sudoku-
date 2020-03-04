from random import choice
from Backtrack import is_valid
from Backtrack import guess_solve


def check_vertical():
    return False
def check_horizontal():
    return False
def check_square():
    return False



def create_completed_sudoku():
    board = [['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],]
    
    guess_solve(board)
    return board



print(create_completed_sudoku())

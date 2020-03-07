from random import choice
from Backtrack import is_valid
from Backtrack import guess_solve
from Backtrack import find_filled
from Backtrack import has_multiple_solutions
from Backtrack import print_board

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

def create_unsolved_sudoku(board):
    #create a solved board
    filled = find_filled(board)
    
    #if it has multiple solutions return False
    if has_multiple_solutions(board):

        return board
    temp_value = board[filled[0]][filled[1]] 
    board[filled[0]][filled[1]] = '.'
    
    create_unsolved_sudoku(board)


    if has_multiple_solutions(board):
        board[filled[0]][filled[1]] = temp_value
    return board






from random import shuffle
from copy import deepcopy

def print_board(board):
    """
    Simple print function
    """
    for x in range(9):
        print(board[x])
    print('\n')
        

def find_empty(board):
    """ Finds an empty location and returns its coords"""
    for x in range(9):
        for y in range(9):
            if board[x][y] == '.':
                return [x,y]
def find_filled(board):
    """Finds a random filled location and returns its coords"""
    x_coor = [0,1,2,3,4,5,6,7,8]
    y_coor = [0,1,2,3,4,5,6,7,8]
    shuffle(x_coor)
    shuffle(y_coor)

    for x in x_coor:
        for y in y_coor:
            if board[x][y] != '.':
                return[x,y]

def has_multiple_solutions(board):
    """Checks if a board has more than one solution"""
    tempboard1 = deepcopy(board)
    tempboard2 = deepcopy(board)

    #solve once
    guess_solve(tempboard1)
    
    #
    return guess_solve(tempboard2, tempboard1)
    



def guess_solve(board, not_this_board=0):
    """Solves the board using backtracking. Optional argument to remove a possible solution"""
    empty = find_empty(board)
    if not empty:

        #returns True if full
        if board != not_this_board:
            return True
        else:
            return False
    else:
        row = empty[0]
        column = empty[1]
    
    #Test numbers in a random order
    #Makes code reusable for createSudoku.py
    list_of_nums = [1,2,3,4,5,6,7,8,9]
    shuffle(list_of_nums)

    for x in list_of_nums:
        if is_valid(board, str(x), [row, column]):
            board[row][column] = str(x)

            if guess_solve(board, not_this_board):
                return True
            board[row][column] = '.'

    
    return False

def is_valid(board, number, location):
    """Checks against the basic rules of Sudoku(row, column, square)"""
    for x in range(len(board)):
        if board[location[0]][x] == number and location[1] != x:
            return False
    
    for x in range(len(board)):
        if board[x][location[1]] == number and location[0] != x:
            return False
    
    local_location = [int(location[0]/3)*3, int(location[1]/3)*3]

    for x in range(local_location[0], local_location[0]+3):
        for y in range(local_location[1], local_location[1]+3):
            if board[x][y] == number and [x,y] != location:
                return False
    
    return True


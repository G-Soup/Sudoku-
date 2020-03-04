from random import shuffle


def print_board(board):
    for x in range(9):
        print(board[x])
        print('\n')

def find_empty(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == '.':
                return [x,y]

def guess_solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row = empty[0]
        column = empty[1]
    
    list_of_nums = [1,2,3,4,5,6,7,8,9]
    shuffle(list_of_nums)

    for x in list_of_nums:
        if is_valid(board, str(x), [row, column]):
            board[row][column] = str(x)

            if guess_solve(board):
                return True
            board[row][column] = '.'
    return False

def is_valid(board, number, location):

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
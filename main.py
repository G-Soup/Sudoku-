#! python3

from Solution import *
from Backtrack import *
#test boards
board =[['5','3','.','.','7','.','.','.','.'], \
        ['6','.','.','1','9','5','.','.','.'], \
        ['.','9','8','.','.','.','.','6','.'], \
        ['8','.','.','.','6','.','.','.','.'], \
        ['4','.','.','8','.','3','.','.','1'], \
        ['7','.','.','.','2','.','.','.','6'], \
        ['.','6','.','.','.','.','2','8','.'], \
        ['.','.','.','4','1','9','.','.','5'], \
        ['.','.','.','.','8','.','.','7','9']]

board2 =   [[".",".","9","7","4","8",".",".","."],\
            ["7",".",".",".",".",".",".",".","."],\
            [".","2",".","1",".","9",".",".","."],\
            [".",".","7",".",".",".","2","4","."],\
            [".","6","4",".","1",".","5","9","."],\
            [".","9","8",".",".",".","3",".","."],\
            [".",".",".","8",".","3",".","2","."],\
            [".",".",".",".",".",".",".",".","6"],\
            [".",".",".","2","7","5","9",".","."]]


#main for Solution.py
def main(input):
    limit = 0
    board = input
    while(not is_solved(board)):
        possible_values = parse_possible(board)
        limit += 1
        #check if any cells are solved
        flag = is_cell_solved(possible_values)
        if flag:
            board[flag[0]][flag[1]] = possible_values[flag[0]][flag[1]][0]
            continue
        
        if limit > 1000:
            break
    
    print(board)
    return board



def main2(input):
    if guess_solve(input):
        print_board(input)
    else:
        print("Not able to be solved: \n")

        
main2(board)
#main(board)
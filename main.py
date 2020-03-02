#! python3

#from Solution import *

#test board
board =[['5','3','.','.','7','.','.','.','.'], \
        ['6','.','.','1','9','5','.','.','.'], \
        ['.','9','8','.','.','.','.','6','.'], \
        ['8','.','.','.','6','.','.','.','.'], \
        ['4','.','.','8','.','3','.','.','1'], \
        ['7','.','.','.','2','.','.','.','6'], \
        ['.','6','.','.','.','.','2','8','.'], \
        ['.','.','.','4','1','9','.','.','5'], \
        ['.','.','.','.','8','.','.','7','9']]

board2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]


def parse_possible(board):
    possible_values = []
    for x in range(9):
        array = []
        for y in range(9):
            if board[x][y] == '.':
                array.append(get_possible_values(board, x, y))
            else:
                #want to have a period for solved numbers
                array.append('.')
        possible_values.append(array)

    return possible_values

def get_possible_values(board, x, y):
    
    possible = remove_peers(board, x, y)
    
    return possible

#IMPORTANT: Replace try except with better DNE handling
#peers are the other locations on the board that directly affect a specific location
def remove_peers(board, x, y):
    possible_values = ['1','2','3','4','5','6','7','8','9']
    #check horizontal line
    for num in board[x]:
        if num != '.':
            try: 
                possible_values.remove(num)
            except: pass

    #check vertical line
    for i in range(9):
        
        if board[i][y] != '.':
            try: 
                possible_values.remove(board[i][y])
            except: pass
            
    #cheeky way to find which square you're in
    loc = [int(x/3)*3,int(y/3)*3]
    #check square
    for i in range(3):
        for j in range(3):
            if board[i+loc[0]][j+loc[1]] != '.':
                try: 
                    possible_values.remove(board[i+loc[0]][j+loc[1]])
                except: pass
    return possible_values


def is_cell_solved(possible_values):
    for x in range(9):
        for y in range(9):
            if possible_values[x][y] != '.' and len(possible_values[x][y]) == 1:
                return [x,y]
    return False

def is_solved(board):
    for line in board:
        for element in line:
            if element =='.':
                return False
    return True






def main():
    limit = 0

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
    for line in board:
        print(line)


main()
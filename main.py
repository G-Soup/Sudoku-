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






#print(parse_possible(board))
for line in parse_possible(board):
    print(line)
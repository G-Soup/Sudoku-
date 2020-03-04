
def parse_possible(board):
    possible_values = []
    for x in range(9):
        array = []
        for y in range(9):
            if board[x][y] == '.':
                array.append(remove_peers(board, x, y))
            else:
                #want to have a period for solved numbers
                array.append('.')
        possible_values.append(array)

    return possible_values

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


#returns a number if it is the only peer who can hold that number
def check_if_only_peer(possible_values, x, y):
    horiz_peer_possible_values = []
    vert_peer_possible_values = []
    square_peer_possible_values = []
    #check horizontal line
    for num in possible_values[x]:
        if num != '.':
            horiz_peer_possible_values.append(num)
            

    #check vertical line
    for i in range(9):
        if possible_values[i][y] != '.':
            vert_peer_possible_values.append(possible_values[i][y])
        
            
    #cheeky way to find which square you're in
    loc = [int(x/3)*3,int(y/3)*3]
    #check square
    for i in range(3):
        for j in range(3):
            if possible_values[i][y] != '.':
                square_peer_possible_values.append(possible_values[i+loc[0]][j+loc[1]])
    peer_possible_values = horiz_peer_possible_values + vert_peer_possible_values + square_peer_possible_values
    
    
    for num in possible_values[x][y]:
        count = 0
        for peer_nums in peer_possible_values:
            
            for peer_num in peer_nums:
                if peer_num == num:
                    count +=1
        
        if count < 4:
            print("This is the num: " + str(num))
            return num
    return False
"""
def check_for_lone_peer(possible_values):
    for x in range(9):
        for y in range(9):
            flag = check_if_only_peer(possible_values,x,y)
            if flag:
                return [x, y, flag]
    return False
"""
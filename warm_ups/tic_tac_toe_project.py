tic_map =[
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]

def get_winner():
    # checks for diagonals x and o
    px = 1 # negative slope
    po = 1

    nx = 1 # positive slope
    no = 1

    full = 1 # full board
    
    cx = 0 # column x
    co = 0 # column 0
    
    rx = 0 # column x
    ro = 0 # column 0
    
    #iterate over a single axis
    for x in range(3):
        
        # row logic
        if("-" not in tic_map[x]): # full row
            if("x" not in tic_map[x]):ro = 1 # all 0
            if("0" not in tic_map[x]):rx = 1 # all x
        else:full = 0 # not full yet
        
        
        # column logic
        column = [
            tic_map[0][x],
            tic_map[1][x],
            tic_map[2][x]
            ]
        if("-" not in column): # full column
            if("x" not in column):co = 1 # all 0
            if("0" not in column):cx = 1 # all x
            
        
        if(tic_map[x][x] != "x"): px = 0
        if(tic_map[x][x] != "0"): po = 0 
        
        if(tic_map[x][2-x] != "x"): nx = 0
        if(tic_map[x][2-x] != "0"): no = 0
    
    if full: return 3
    elif 1 in (no, po, ro, co): return 1
    elif 1 in (nx, px, rx, cx): return 2

    else: return 0
    
def get_pos(move):
    move = move.replace(" ","")
    move = move.replace(",","")
    if len(move) > 2:
        return -1,-1
    move = move.lower()
    x = move[0]
    try:y = int(move[1])-1
    except: return -1,-1

    x_map = ["a","b","c"]
    if(x not in x_map):
        return -1,-1
    else:x = x_map.index(x)
    return x,y


def possible_move(x,y):
    if ((0 <= x <= 2) and (0 <= y <= 2)):
        return (tic_map[y][x]) == "-"
    else: return False
    
def draw_map():
    print("  a b c")
    for y in range(3):
        line = ""
        for x in range(3):
            line += tic_map[y][x]+" " 
        print(y+1,line)

t = 0

        
        
print(
    """
    simple tic tac toe game,
    each turn give a position in the format: a1, c3, b2...
    
    """
    )
while True:
    
    move_value = "0"
    draw_map()
    t += 1
    if t%2 != 0:
        
        move = input("x move ")
        move_value = "x"
    else:
        move = input("0 move ")
        move_value = "0"
    
    x,y = get_pos(move) 
    
    while not possible_move(x,y):
        move = input("impossible move, try again ")
        x,y = get_pos(move)
    tic_map[y][x] = move_value
        
    
    diagonals = get_winner()
    if diagonals != 0:
        draw_map()
        if diagonals == 1:
            print(" 0 won!")
            draw_map()
            break
        elif diagonals == 2:
            print(" X won!")
            draw_map()
            break
        else:
            print("it's a tie")
            draw_map()
            break
            
            
            

        
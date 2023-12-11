'''Advent Of Code 2023 - Day 09'''

import sys

fname = 'dec10.data'
if len(sys.argv) > 1:
    fname = sys.argv[1]

print("Hello Advent Of Code 2023 - December 10")
print("Pipe Maze parts 1 and 2 - ", fname)

# destinations: Left, Up, Right, Down
# With each move, we decide on the character found
# how we calculate next pos (row/col offsets) and
# which direction we go to in the next move
#   { to_pos: [row, col, to], },
steps = {
    'L_L': [ -1,  0, 'U' ], # UpLeft
    'L_-': [  0, -1, 'L' ], # Left
    'L_F': [  1,  0, 'D' ], # DownLeft
    'R_J': [ -1,  0, 'U' ], # UpRight
    'R_-': [  0,  1, 'R' ], # Right
    'R_7': [  1,  0, 'D' ], # DownRight
    'U_7': [  0, -1, 'L' ], # UpLeft
    'U_|': [ -1,  0, 'U' ], # Up
    'U_F': [  0,  1, 'R' ], # UpRight
    'D_J': [  0, -1, 'L' ], # DownLeft
    'D_|': [  1,  0, 'D' ], # Down
    'D_L': [  0,  1, 'R' ], # DownRight
}  

# navigate worm 
def wormlen(data,row,col,rows,cols):
    pos = data[row][col]
    print("wormlen(pos, row, col, rows, cols) ", pos, row, col, rows, cols)
    # look for 1st step clockwise r d l u
    last = [row,col]
    to = '*'
    if '*' == to and col<cols-1: # try to move right
        if 'J'==data[row][col+1] or '-'==data[row][col+1] or '7'==data[row][col+1]:
            to = 'R'
            col +=1
    if '*' == to and row<rows-1: # try to move down
        if 'J'==data[row+1][col] or '|'==data[row+1][col] or 'L'==data[row+1][col]:
            to = 'D'
            row +=1
    if '*' == to and 0<col: # try to move left
        if 'L'==data[row][col-1] or '-'==data[row][col-1] or 'F'==data[row][col-1]:
            to = 'L'
            col -=1
    if '*' == to and 0<row: # try to move up
        if '7'==data[row-1][col] or '|'==data[row-1][col] or 'F'==data[row-1][col]:
            to = 'U'
            row +=1
    pos = data[row][col]
    turn = to + '_' + pos
    move = steps[turn]
    #print("start ", turn, row, col, steps[turn])
            
    if '*' == to:
        print("found no start")
        return 0

    turns = 1
    # while not back to 'S'tart
    while not 'S'==pos:
        turn = to + '_' + pos
        move = steps[turn]
        row += move[0]
        col += move[1]
        to  =  move[2]
        pos = data[row][col]
        #print("move ", turn, row, col, steps[turn])
        turns += 1

    return int(turns/2)

# main
datafile = open(fname, 'r')
lines = datafile.readlines()

result = 0
for row in range(len(lines)):
    col = lines[row].find('S')
    if not -1==col:
        result = wormlen(lines, row, col, len(lines), len(lines[0]))
        break

print("Puzzle result: ", result)

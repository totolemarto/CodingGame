import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.

def direction(elem : str):
    match elem:
        case 'TOP':
            return 2
        case 'LEFT':
            return 1
        case 'RIGHT':
            return 0
    return -1
w, h = [int(i) for i in input().split()]
liste_piece = []

corresp_piece = {
    "0": {1 :[0,0]},
    "1": {0 : [1,0], 1: [1,0], 2: [1,0] },
    "2": {0 : [0,-1], 1 : [0,1] }, 
    "3": {2 : [1,0]},
    "4": {2 : [0,-1], 0: [1,0] },
    "5": {2 : [0,1], 1 : [1,0] }, 
    "6": {0 : [0,-1], 1: [0,1] },
    "7": {2 : [1,0], 0 : [1,0] }, 
    "8": {1 : [1,0], 0: [1,0] },
    "9": {2 : [1,0], 1 : [1,0] }, 
    "10": {2 :[0,-1]},
    "11": {2 :[0,1]},
    "12": {0 :[1,0]},
    "13": {1 :[1,0]}
    }

for i in range(h):
    line = input() 
    liste_piece.append(line.split())
ex = int(input()) 
# game loop
for elem in liste_piece:
    print("Debug messages...",elem, file=sys.stderr, flush=True)

while True:
    inputs = input().split()
    print("Debug messages...",inputs, file=sys.stderr, flush=True)
    current_position = [int(inputs[0]),int(inputs[1])]
    pos = inputs[2]

    cur_piece = liste_piece[current_position[1]][current_position[0]]
    new = corresp_piece[cur_piece][direction(pos)]
    print("Debug messages...",new, cur_piece , file=sys.stderr, flush=True)

    print(current_position[0] + new[1], current_position[1] + new[0] )
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.


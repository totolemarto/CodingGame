import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
min_max_y = [0,h]
min_max_x = [0,w]

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir in ["U","D","UR","R","DR"]:
        min_max_x[0] = x0
    if bomb_dir in ["U","D","L","DL","UL"]:
        min_max_x[1] = x0
    if bomb_dir in ["U","UR","UL","R","L"]:
        min_max_y[1] = y0
    if bomb_dir in ["L","D","DL","R","DR"]:
        min_max_y[0] = y0

    y0= ( min_max_y[1] + min_max_y[0] ) // 2
    x0= ( min_max_x[1] + min_max_x[0] ) // 2
    print(x0,y0) 
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.

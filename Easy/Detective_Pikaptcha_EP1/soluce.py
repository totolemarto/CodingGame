import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def voisins(i,j):
    if mat[i][j] == '#':
        return '#'
    sum = 0
    if i  - 1 >= 0:
        if mat[i-1][j] != '#':
            sum+=1
    if i  + 1 < height:
        if mat[i+1][j] != '#':
            sum+=1
    if j  - 1 >= 0:
        if mat[i][j-1] != '#':
            sum+=1
    if j  + 1 < width:
        if mat[i][j + 1] != '#':
            sum+=1
    return str(sum)
mat =[]
width, height = [int(i) for i in input().split()]
for i in range(height):
    line = input()
    mat.append(list(line))
for i in range(height):
    for j in range(width):
        mat[i][j] = voisins(i,j)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(height):
    print("".join(mat[i]))

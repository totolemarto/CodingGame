import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lettre = {
    0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
    6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
    12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H",
    18: "I", 19: "J", 20: "K", 21: "L", 22: "M", 23: "N",
    24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T",
    30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"
}

entier = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
    "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17,
    "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23,
    "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
}

def reachable(pos):
    result = []
    i,j=pos
    if mat[(i + 1) % w][j] != "#":
        result.append([(i+1) %w,j])
    if mat[(i - 1) % w][j] != "#":
        result.append([(i-1) %w ,j])
    if mat[i][(j + 1) %h] != "#":
        result.append([i,(j + 1) % h])
    if mat[i][(j - 1) % h] != "#":
        result.append([i,(j - 1) % h])
    return result


def solve_maze(i,pos): 
    if i >35:return
    mat[pos[0]][pos[1]] = lettre[i]
    for elem in reachable(pos):
        if mat[elem[0]][elem[1]] in " ." or entier[mat[elem[0]][elem[1]]] >  i:
            solve_maze(i+1, elem)
    return



h, w = [int(i) for i in input().split()]
mat=[]
for i in range(w):
    row = input()
    if "S" in row:
        index=[i,row.index("S")]
    mat.append(list(row))
solve_maze(0,index)
for i in range(w):

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("".join(mat[i]))


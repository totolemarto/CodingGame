import sys
import math

def getGold(pos : list[int]) -> int:
    line = pos[0]
    column = pos[1]
    match mat[line][column]:
        case ' ':
            return 0
        case '#':
            return -1
        case 'X':
            return 0
        case _:
            return int(mat[line][column])

    return 0


def isValidCell(position : list[int]):
    return position[0] >= 0 and position[1] >= 0 and position[0] < h and position[1] < w


def parcours(illegalMoves : list[list[int]], actualPosition : list[int], actualGold : int) -> int:

    if (not isValidCell(actualPosition)):
        return actualGold

    if (getGold(actualPosition) == - 1 or actualPosition in illegalMoves):
        return actualGold
    actualGold += getGold(actualPosition)
    illegalMoves.append(actualPosition)
    maxi = -1
    for move in moves:
        newLine = actualPosition[0] + move[0]
        newCol = actualPosition[1] + move[1]
        newPos = [newLine, newCol]
        maxi = max(maxi, parcours(illegalMoves, newPos, actualGold))
    return maxi


moves = [[-1, 0],[0, 1],[1, 0], [0, -1]]

entryPoint = []
mat = []
h, w = [int(i) for i in input().split()]
for i in range(h):
    mat.append(list(input()))
    if ( "X" in mat[i]):
        entryPoint = [i, mat[i].index("X")]
print(parcours([], entryPoint, 0))

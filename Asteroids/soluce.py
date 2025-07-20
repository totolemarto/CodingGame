import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Asteroid:
    line_prev : int
    column_prev : int
    line: int
    column : int
    name: str
    def __init__(self, line, column, line_prev, column_prev, name):
        self.line = line
        self.line_prev = line_prev
        self.column = column
        self.column_prev = column_prev
        self.name = name
    
    def add_prev(self, line, column):
        self.line_prev = line
        self.column_prev = column
    
    def add_cur(self, line, column):
        self.line = line
        self.column = column

    def get_vector(self):
        result = [ self.line - self.line_prev, self.column - self.column_prev]
        return [min(self.line + result[0], h - 1), min(self.column + result[1], w - 1)]


w, h, t1, t2, t3 = [int(i) for i in input().split()]
picture_1 : list[str] = []
picture_2 : list[str] = []
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    picture_1.append(first_picture_row)
    picture_2.append(second_picture_row)


dico : dict[str, Asteroid] = {}


for i in range(len(picture_1)):
    for j in range(len(picture_1[i])):
        if picture_1[i][j] != ".":
            dico[picture_1[i][j]] = Asteroid(0, 0, i, j, picture_1[i][j])

for i in range(len(picture_1)):
    for j in range(len(picture_1[i])):
        if picture_2[i][j] != ".":
            dico[picture_2[i][j]].add_cur(i,j)

pos_asteroid : dict[str, str] = {} 
for key, value in dico.items():
    if str(value.get_vector()) in pos_asteroid.keys():
        pos_asteroid[str(value.get_vector())] = min(pos_asteroid[str(value.get_vector())], key)
    else:
        pos_asteroid[str(value.get_vector())] = key

for i in range(len(picture_1)):
    for j in range(len(picture_1[i])):
        if str([i,j]) in pos_asteroid.keys():
            print(pos_asteroid[str([i,j])], end="")
        else:
            print(".", end="")
    print()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)




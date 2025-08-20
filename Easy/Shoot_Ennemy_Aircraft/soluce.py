import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Plane:
    line : int
    column : int
    to_the_left : bool
    def __init__(self, line, column, left):
        self.line = line
        self.column = column
        self.to_the_left = left

    def __str__(self):
        sens= "gauche" if self.to_the_left else "droite"
        return f"vers la {sens} {self.line=} {self.column=}"

    def move(self):
        if self.to_the_left:
            self.column-=1
        else:
            self.column+= 1

class Missile:
    line : int
    column : int
    index : int

    def __init__(self, line, column, index):
        self.line = line
        self.column = column
        self.index = index

    def up(self) -> bool:
        self.line-=1
        if self.line < 0:
            return True
        return False

def get_plane(line : str, num : int):
    result : list[Plane] = []
    for i in range(len(line)):
        if line[i] == ">":
            result.append(Plane(num, i, False))
        if line[i] == "<":
            result.append(Plane(num, i, True))
    return result 
                



def simulate(mat : list[list[str]], planes : list[Plane], pos : list[int]):
    timing = 0
    good_timing : list[int] = []
    missiles : list[Missile] = []
    while len(good_timing) != len(planes): 
        missiles.append(Missile(pos[0],pos[1], timing))
        for plane in planes:
            plane.move()
        for missile in missiles:
            missile.up()
            for plane in planes:
                if missile.column == plane.column and missile.line == plane.line:
                    good_timing.append(missile.index)
        timing+= 1
    return good_timing


n = int(input())
right = []
left = []
mat =[]
pos = []
planes : list[Plane] = []
for i in range(n):
    line = input()

    mat.append(list(line))
    planes += get_plane(line, i)
    if "^" in line:
        pos = [i, line.index("^")]
shoot = simulate(mat, planes, pos)
for i in range(1, shoot[-1] + 1):
    if i in shoot:
        print("SHOOT")
    else:
        print("WAIT")
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



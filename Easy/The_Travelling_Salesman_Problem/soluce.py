import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def dist(elem,elem2):
    return math.sqrt(abs(elem[0] - elem2[0]) ** 2  + abs(elem[1] - elem2[1]) ** 2  ) 

n = int(input())
l = [[0,0]] * n
for i in range(n):
    x, y = [int(j) for j in input().split()]
    l[i] = [x,y]
already_see = [0] * n
current = l[0]
already_see[0] = 1
total_cost = 0
while 0 in already_see:
    maxi =  99999999
    for i, elem in enumerate(l):
        if already_see[i] == 1: 
            continue
        else:
            x = dist(current, elem)
            if x < maxi:
                maxi = x
                new = elem
                to_remove = i
    already_see[to_remove] = 1
    current= new
    total_cost += maxi
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(round(total_cost + dist(current, l[0])))


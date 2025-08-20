import sys
import math


def winner(a, b):
    c, d = players[a], players[b]
    if c == "R":
        if d == "R":
            return min(a, b)
        elif d == "P":
            return b
        elif d in ["C", "L"]:
            return a
        elif d == "S":
            return b
    elif c == "P":
        if d == "R":
            return a
        elif d == "P":
            return min(a, b)
        elif d in ["C", "L"]:
            return b
        elif d == "S":
            return a
    elif c == "C":
        if d == "C":
            return min(a, b)
        elif d in ["P", "L"]:
            return a
        elif d == "R":
            return b
        elif d == "S":
            return b
    elif c == "L":
        if d == "L":
            return min(a, b)
        elif d == "P":
            return a
        elif d in ["R", "C"]:
            return b
        elif d == "S":
            return a
    elif c == "S":
        if d == "S":
            return min(a, b)
        elif d == "P":
            return b
        elif d in ["R", "C"]:
            return a
        elif d == "L":
            return b



# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
players = {}
opponents = {}
order = []
n = int(input())
for i in range(n):
    inputs = input().split()
    num_player = int(inputs[0])
    signplayer = inputs[1]
    players[num_player] = signplayer
    opponents[num_player] = []
    order.append(num_player)
while len(order) != 1:
    for i,elem in enumerate(order):
        if i%2 == 0:
            opponents[elem].append(order[i+1])
        else:
            opponents[elem].append(order[i-1])
    to_remove = []
    for i,elem in enumerate(order):
        if i%2 == 0:
            x = winner(elem, order[i+1])
    #        print(elem, x, order[i+1])
            if x == elem:
                to_remove.append(order[i+1])
            else:
                to_remove.append(elem)
   # print(to_remove)
    for elem in to_remove:
        order.remove(elem)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(order[0])
for i,elem in enumerate(opponents[order[0]]):
    if i!=len(opponents[order[0]]) -1 :
        print(elem, end =" ")
    else:
        print(elem)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
card = []
n = int(input())
for i in input().split():
    x = int(i)
    card.append(x)

card.sort()
sumi = 0
while len(card) != 1:
    i = card[0]
    card.pop(0)
    j = card[0]
    card.pop(0)
    sumi += i + j
    card.append(i+j)
    card.sort()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(sumi)


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
level = []
n = int(input())
for i in input().split():
    level.append(int(i))

level.sort()
i = 0
flag = 1
while i < len(level) - 1:
    if i == len(level) - 1:
        break

    x = level[i]
    y = level[i+1]
    if x  == y :
        level.pop(i)
        level.pop(i)
        level.append(x+1)
        level.sort()
        i = 0
    else :
        i += 1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(len(level))


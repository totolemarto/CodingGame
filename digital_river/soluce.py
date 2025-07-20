import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r1 = int(input())
r2 = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
while r1 != r2:
    if r1 < r2:
        x = list(str(r1))
        sumi = sum(map(int, x))
        r1= r1 + sumi
    else:
        x = list(str(r2))
        sumi = sum(map(int, x))
        r2= r2 + sumi
print(r1)

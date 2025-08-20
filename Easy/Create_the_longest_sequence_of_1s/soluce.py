import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def brute_force(line):
    maxi = 0
    cur = 0
    for elem in line:
        if elem == "1":
            cur += 1
        else:
            cur =0
        if cur > maxi :
            maxi = cur
        
    return maxi

b = input()
maxi = 0
j = b
for i in range(len(j)):
    b = list(b)
    b[i] = "1"
    a = brute_force(b)
    if   a > maxi:
        maxi = a
    b = j
print(maxi)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



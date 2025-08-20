import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fast_enought(time : int) -> int:
    return math.floor(13 / time * 3600000)


fast_ones = []
all : dict[str, int] = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    plate = inputs[0]
    radarname = inputs[1]
    timestamp = int(inputs[2])
    if plate in all.keys():
        if fast_enought(timestamp - all[plate]) > 130:
            fast_ones.append(plate + " " + str(fast_enought(timestamp - all[plate])))
    else:
        all[plate] = timestamp

fast_ones.sort()
print("\n".join(fast_ones))




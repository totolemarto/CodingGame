import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fast_enought(time : int) -> int:
    goal = 130
    distance = 13
    minutes = 6
    return math.floor(distance / time * 3600000)


fast_ones = []
all : dict[str, int] = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    plate = inputs[0]
    radarname = inputs[1]
    timestamp = int(inputs[2])
    if plate in all.keys():
        #        print("fast_enought = ", fast_enought(timestamp - all[plate]), "time = ",timestamp - all[plate])
        if fast_enought(timestamp - all[plate]) > 130:
            fast_ones.append(plate + " " + str(fast_enought(timestamp - all[plate])))
    else:
        all[plate] = timestamp

fast_ones.sort()
print("\n".join(fast_ones))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



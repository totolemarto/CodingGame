import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = input()
b = input()
elem_1 = list(map(int, a.split(" ")))
elem_2 = list(map(int, b.split(" ")))
cur_1 : int  = 0
cur_2 : int = 0
index_1 : int = 0
index_2 : int = 0

result : int = 0

while(index_2 < len(elem_2)):
    if elem_1[index_1] >= elem_2[index_2] :
        result += elem_1[index_1 + 1] * elem_2[index_2 + 1] * elem_2[index_2]
        elem_1[index_1] -= elem_2[index_2]
        index_2 += 2
    else:
        result += elem_1[index_1 + 1] * elem_2[index_2 + 1] * elem_1[index_1]
        elem_2[index_2] -= elem_1[index_1]
        index_1 += 2
print(result)
        
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


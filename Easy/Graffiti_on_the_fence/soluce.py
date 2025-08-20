import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
t = []
n = int(input())
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    t.append([st,ed])
t.sort(key=lambda x: x[0])
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
maxi = max(x[1] for x in t)
cur_max = 0
flag = 0
if 0 != t[0][0]:
    flag = 1
    print("0", t[0][0])
for i in range(len(t) - 1):
    if t[i][1] > cur_max:
        cur_max = t[i][1]
    if t[i+1][0] > cur_max:
        flag = 1
        print(cur_max, t[i+1][0])
if l != maxi:
    flag = 1
    print(maxi, l)
if not flag:
    print("All painted")


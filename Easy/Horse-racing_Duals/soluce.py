import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
l=[]
n = int(input())
for i in range(n):
    l.append(int(input()))
l.sort()
difmax=10000000000000000000000000000
for i in range(1,len(l)):
    if l[i]-l[i-1]<difmax:
        difmax=l[i]-l[i-1]



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(difmax)


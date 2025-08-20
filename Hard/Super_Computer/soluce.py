import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def dedans(a,b,c,d):
    if a<=c and c<=b :
        return False
    if a<=d and d<=b:
        return False
    return True

n = int(input())
s=[(0,0)]*n
for i in range(n):
    j, d = [int(j) for j in input().split()]
    s[i]=(j,j+d)
s=sorted(s, key=lambda s:s[1])
lemax=0
ind_min=0
while ind_min != n:
    cur = s[ind_min]
    j = ind_min
    while  j < n and s[j][0] < cur[1] :
        j+=1
    ind_min=j
    lemax+=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lemax)


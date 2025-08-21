import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

n = int(input())
c = int(input())
l=[0] * n
for i in range(n):
    l[i] = int(input())

sumi = 0 
mean = c / n
l.sort()
if sum(l) < c:
    print("IMPOSSIBLE")
    exit(1)
j=[]
i = 0
tmp = n
while sumi != c and i < len(l):
    if l[i] >= mean:
        if mean * (len(l) - i) < c:
            mean = (c - sumi) / (len(l) - i)
        sumi += int(mean)
        j.append(int(mean))
    else:
        sumi += l[i]
        j.append(l[i])
        tmp -= 1
        mean = (c - sumi ) / max(1,tmp)
    i+=1
print("Debug messages...", sumi, c, file=sys.stderr, flush=True)
if int(sumi) +1 == c:
    if len(j) == 0:
        j[0] = 1
    else:
        j[-1] += 1
    sumi += 1
for e in j:
    print(round(e))

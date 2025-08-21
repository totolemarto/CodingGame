import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
liste=[]
n = int(input())
for i in input().split():
    v = int(i)
    liste.append(v)
maxi=(liste[0],0)
mini=(liste[0],0)
ladif=0
i=0
for elem in liste :
    if elem > maxi[0] : maxi=(elem,i)
    mini=(elem,i)
    if maxi[1]<mini[1] and maxi[0]-mini[0] > ladif : ladif=maxi[0]-mini[0]
    i+=1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(-ladif)


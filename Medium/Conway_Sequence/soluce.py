import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
nb = int(input())
l=[[str(r)]]
for j in range(nb-1):
    lenactu=len(l[j])
    liste=[]
    count=1
    for i in range(lenactu):
        if i==lenactu-1:
            liste.append(str(count))
            liste.append(l[j][i]) 
            l.append(liste)
            continue
        if l[j][i]==l[j][i+1]:
            count+=1
        else:
            liste.append(str(count))
            liste.append(l[j][i]) 
            count=1
print(" ".join(l[nb-1]))
        
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



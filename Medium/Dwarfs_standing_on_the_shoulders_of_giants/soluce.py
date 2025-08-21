import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def longueur(x,liste):
    max=0
    for (i,j) in liste:
        if i==x:
            k=longueur(j,liste)
            if max<k:
                max=k
    return 1+max   
n = int(input())  # the number of relationships of influence
liste=[]
personne=[]
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    liste.append((x,y))
    if x not in personne:
        personne.append(x)
    if y not in personne:
        personne.append(y)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
max=0
for elem in personne:
    x=longueur(elem,liste)
    if x>max:
        max=x

# The number of people involved in the longest succession of influences
print(max)


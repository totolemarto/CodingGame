import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
def plusproche(actu,sortie,liens):
    file=[actu];lebon=[]
    while file !=[]:
        actu=file[0]
        lebon.append(actu)
        file.remove(actu)
        for (a,b) in liens:
            if (a in sortie and b == actu ) or (a==actu and b in sortie):
                print("Debug messages... sortie ?",lebon,a,b, file=sys.stderr, flush=True)

                if a==actu:
                    lebon.append(b)
                    return lebon
                else:
                    lebon.append(a)
                    return lebon
            if actu==a:
                file.append(b)
                
            if actu==b:
                file.append(a)
                
    return lebon

n, l, e = [int(i) for i in input().split()]
link=[]
sortie=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    link.append([int(j) for j in input().split()])
for i in range(e):
    sortie.append(int(input()))  # the index of a gateway node
for i in range(n):
    flag=0
    for (k,j) in link:
        if j==i:
            flag=1
    if flag==0: lebon=i
print("Debug messages...",link,sortie, file=sys.stderr, flush=True)
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    chemin=plusproche(si,sortie,link)
    print("Debug messages... heyeh",link, file=sys.stderr, flush=True)
    print(chemin[-1],chemin[-2])
    if [chemin[-2],chemin[-1]] in link:
        link.remove([chemin[-2],chemin[-1]])
    else:
        link.remove([chemin[-1],chemin[-2]])
    print("Debug messages... yo",link, file=sys.stderr, flush=True)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    

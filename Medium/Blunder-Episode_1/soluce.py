import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# B = biere T = teleporteur S = Sud N = Nord E = Est W = ouest
# cassable obstacles = X obstacles = #
# but = $
# I = inverseur priorité
# @ = départ

# déplacement sur hauteur puis largeur 1 -> descendre ou droite
priorite = [[1,0],[0,1],[-1,0],[0,-1]]
biere=0
teleporteur=[]

l, c = [int(i) for i in input().split()]
mat = []
for i in range(l):    
    x=list(input())
    mat.append(x)
    if "T" in x:teleporteur.append([i,x.index("T")])
    if "@" in x: debut = [i, x.index("@")]
    if "$" in x: goal = [i, x.index("$")]
r=""

flag=0
cur_dir = priorite[0]
cur_word = "SOUTH"
for i in range(5000):
    if flag: break
#    print(cur_dir)
    if cur_dir == 0 : break
    #print(debut)
    tmp = [ debut[0]+cur_dir[0], debut[1]+cur_dir[1] ]
#    print(tmp)
    carac = mat[tmp[0]][tmp[1]]
    if carac == "$": flag =1
    if carac == "I":priorite.reverse()
    if carac == "B": biere = not biere
    if carac == "#": 
        cur_dir = 0
        for g in range(4):
#            print(mat[debut[0]+priorite[g][0]][debut[1]+priorite[g][1]])
            if mat[debut[0]+priorite[g][0]][debut[1]+priorite[g][1]] not in "X#" and cur_dir == 0:
                cur_dir = priorite[g]
        if cur_dir == 0 : break
        continue
    if cur_dir == 0: break
    if carac == "X" and not biere: 
        cur_dir = 0
        for g in range(4):
#            print(mat[debut[0]+priorite[g][0]][debut[1]+priorite[g][1]])

            if mat[debut[0]+priorite[g][0]][debut[1]+priorite[g][1]] not in "X#" and cur_dir == 0:
                cur_dir = priorite[g]
        if cur_dir == 0 : break
        continue
    if carac == "X" and biere: mat[tmp[0]][tmp[1]]= " "
    if carac == "T":
        #print(debut, teleporteur)
        debut = teleporteur[1] if tmp == teleporteur[0] else teleporteur[0]
        #print(debut)
    else:
        debut = tmp

    if cur_dir == [1,0]: cur_word = "SOUTH"
    if cur_dir == [-1,0]: cur_word = "NORTH"
    if cur_dir == [0,1]: cur_word = "EAST"
    if cur_dir == [0,-1]: cur_word = "WEST"
    r+=cur_word+'\n'
    if carac == "S" : cur_dir = [1,0]; cur_word = "SOUTH"
    if carac == "E" : cur_dir = [0,1]; cur_word = "EAST"
    if carac == "N" : cur_dir = [-1,0]; cur_word = "NORTH"
    if carac == "W" : cur_dir = [0,-1]; cur_word = "WEST"




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(r) if flag else print("LOOP")


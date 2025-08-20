import sys
import math
from copy import deepcopy
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
properties = []
people = []
p = int(input())
for i in range(p):
    properties.append(input())
n = int(input())
for i in range(n):
    people.append(input().split())
f = int(input())
for i in range(f):
    count = 0
    flag = 0
    formula = input()
    print("Debug messages iuci...",formula, file=sys.stderr, flush=True)
    good = deepcopy(people)
    for formul in formula.split(" AND "):
        formul = formul.split("=")
        print("Debug messages iuci...",formul, properties, file=sys.stderr, flush=True)
        try:
            utils= properties.index(formul[0])
        except:
            print(0)
            flag = 1
            break
        for elem in people:
            print("Debug messages...",elem, file=sys.stderr, flush=True)
            if elem not in good :continue
            if elem[1+utils] != formul[1]:
                good.remove(elem)
    if not flag : print(len(good))    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



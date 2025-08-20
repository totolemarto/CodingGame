import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def evaluate(line, dico):
    if not "[" in line:
        return int(line)
    name = line.split("[")[0]
    deb = line.index("[") + 1
    line = line[deb:-1]
    return dico[name][1][evaluate(line, dico) - dico[name][0]]

n = int(input())
dico = {}
for i in range(n):
    a = input()
    print(a, file=sys.stderr, flush=True)
    a = a.split(" = ")
    name = str(a[0]).split("[")[0]
    print(name, file=sys.stderr, flush=True)
    first = str(a[0]).split("[")[1]
    print(first, file=sys.stderr, flush=True)
    first = str(first).split(".")[0]
    first = int(first)
    l = []
    for k in str(a[1]).split():
        l.append(int(k))
    dico[name] = [first, l]
print(dico, file=sys.stderr, flush=True)
x = input()

print(evaluate(x, dico))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



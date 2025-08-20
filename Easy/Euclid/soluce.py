import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def euclide(a : int, b: int):
    r = a%b
    q = a // b
    print(f"{a}={b}*{q}+{r}")
    if r == 0:
        return b
    else:
        return euclide(b,r)

a, b = [int(i) for i in input().split()]
x = euclide(a,b)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(f"GCD({a},{b})={x}")


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def get_decimal(result : int) -> str:
    tmp = ""
    if result % 10 == 0:
        tmp = "A"
    else:
        return result
    if result % 100 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-2] + tmp
    if result % 1000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-3] + tmp
    if result % 10000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-4] + tmp
    if result % 100000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-5] + tmp
    if result % 1000000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-6] + tmp
    if result % 10000000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-7] + tmp
    if result % 100000000 == 0:
        tmp = "A" + tmp
    else:
        return str(result)[0:-8] + tmp
    return tmp

count = int(input())
result = 0
for decimary in input().split():
    leni = len(decimary) - 1
    current = 0
    for i, letter in enumerate(decimary):
        if letter == "A":
            current += 10 * ( 10 ** (leni - i) )
        else:
            current += int(letter) * ( 10 ** (leni - i) )
    print(current)
    result += current

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(get_decimal(result))


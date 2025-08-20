import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def compute_fibo(maxi):
    l=[1,1]
    last = 1
    while last < maxi:
        last = (l[-1] + l[-2])
        l.append(last)
    return l
n = int(input())
fibo = compute_fibo(n)
utile = []
for i in range(len(fibo) - 1 , -1 , -1):
    if n == 0:
        break
    while fibo[i] <= n:
        n-= fibo[i]
        utile.append(str(fibo[i]))

print("+".join(utile))


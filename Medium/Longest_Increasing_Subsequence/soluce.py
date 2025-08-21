import sys
import math
from functools import lru_cache
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
@lru_cache
def compute(cur, taille, last):
    global n
    print(f"{liste=}, {n=}, {cur=}, {taille=}, {last=}", file=sys.stderr, flush=True)
    global max_taille
    if cur ==  n :
        if max_taille < taille:
            max_taille = taille
        return taille
    if max_taille > taille + n - cur:
        return 0
    if last and liste[cur] <= last:
        return compute( cur +1, taille, last)
    else:
        return max (
            compute( cur +1, taille, last),
            compute( cur +1, taille + 1, liste[cur])
        )
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n  

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
max_taille = 0
n = int(input())
liste = []
dico = {}
for i in range(n):
    liste.append(int(input()))
print(longest_increasing_subsequence(liste))



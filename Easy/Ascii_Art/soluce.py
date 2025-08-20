import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
letter = []
for i in range(h):
    letter.append(input())
result =""
for i in range(h):
    for lettre in t:
        if (lettre.lower() >= 'a' and lettre.lower() <= 'z' ):
            pos= ord(lettre.lower()) - ord('a')
            for j in range(l):
                result+= letter[i][ j + l * (pos )  ]
        else:
            for j in range(l):
                result+= letter[i][ j + (len(result[0]) -l - 1 )]
    result+='\n' 


print(result)


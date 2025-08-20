import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
result = ""
flag = 0
flag2=0
n = int(input())
for i in range(n):
    fname = input()
    fname = fname.replace(";", ";_im_a_flag_")
    fnames = fname.split("_im_a_flag_")
    for i,fname in enumerate(fnames):
        if "begin" in fname.lower():
            flag2= 1
        if "end" in fname.lower():
            flag2=0
        if "INSERT INTO" in fname.upper() and not "--" in fname and not flag2:
            flag = 1
        if "--" in fname:
            result += "--" + fname.split("--")[1] 
        if not flag and not "--" in fname:
            result += fname 
        if ";" in fname and not "--" in fname :
            flag = 0 
    result+="\n"
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
z = len(result) -2

while "\n\x00" in result:
    result = result.replace("\n\x00","\x00")

while "\n\n" in result:
    result = result.replace("\n\n","\n")

print(result[0:-1])


import sys
import math

corresp= {
    111 : 0,
    110 : 1,
    101 : 2,
    100 : 3,
    11 : 4,
    10 : 5,
    1 : 6,
    000 : 7,
}

line_length = int(input())
max_iter = int(input())
rule_number = int(input())

cur_result = "." * (line_length // 2) + "1" + "." * (line_length // 2) 
automate = str(bin(rule_number))[2:].zfill(8)


print(automate,file=sys.stderr, flush=True)
print(cur_result, file=sys.stderr, flush=True)

dico = {}
dico[cur_result] = 1
for i in range(2, max_iter + 2):
    tmp = list(cur_result)
    cur_result = ""
    for j,elem in enumerate(tmp):
        state = 0
        if j == 0:
            carac = 1 if tmp[-1] == "1" else 0
        else:
            carac = 1 if tmp[ (j - 1) % line_length] == "1" else 0
        state += carac * 100
        carac = 1 if tmp[j] == "1" else 0
        state += carac * 10
        carac = 1 if tmp[ (j + 1) % line_length] == "1" else 0
        state += carac
        cur_result += "1" if automate[(corresp[state])] == "1" else "."
    
    print(cur_result, file=sys.stderr, flush=True)
    if cur_result in dico.keys():
        print((i ) - dico[cur_result])
        exit(1)
    else:
        dico[cur_result] = i
print("BIG")


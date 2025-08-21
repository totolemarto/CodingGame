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
rule_number = int(input())
max_iter = int(input())
cur_result = input()
automate = str(bin(rule_number))[2:].zfill(8)
line_length= len(cur_result)

print(automate,file=sys.stderr, flush=True)
print(cur_result)
for i in range(max_iter - 1):
    tmp = list(cur_result)
    cur_result = ""
    for j,elem in enumerate(tmp):
        state = 0
        if j == 0:
            carac = 1 if tmp[-1] == "@" else 0
        else:
            carac = 1 if tmp[ (j - 1) % line_length] == "@" else 0
        state += carac * 100
        carac = 1 if tmp[j] == "@" else 0
        state += carac * 10
        carac = 1 if tmp[ (j + 1) % line_length] == "@" else 0
        state += carac
        cur_result += "@" if automate[(corresp[state])] == "1" else "."
    
    print(cur_result)


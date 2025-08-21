import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
ingredients = {}
num_recipe, num_ingredients = [int(i) for i in input().split()]
is_liquid = []
for i in range(num_recipe):
    line = input().split()
    if line[0] == '-':
        if "kg" in line[1]:
            ingredients[" ".join(line[2:])] = float(line[1][0:-2]) * 1000
        elif "g" in line[1]:
            ingredients[" ".join(line[2:])] = float(line[1][0:-1])
        elif "cl" in line[1]:
            ingredients[" ".join(line[2:])] = float(line[1][0:-2])
            is_liquid.append(" ".join(line[2:]))
        else:
            ingredients[" ".join(line[2:])] = float(line[1][0:-1] * 100)
            is_liquid.append(" ".join(line[2:]))

#print(ingredients)    
dogs_buy = {}
for i in range(num_ingredients):
    line = input().split()
    if "kg" in line[-1]:
        dogs_buy[" ".join(line[:-1])] = float(line[-1][0:-2]) * 1000
    elif "g" in line[-1]:
        dogs_buy[" ".join(line[:-1])] = float(line[-1][0:-1])
    elif "cl" in line[-1]:
        dogs_buy[" ".join(line[:-1])] = float(line[-1][0:-2])
    else:
        dogs_buy[" ".join(line[:-1])] = float(line[-1][0:-1]) * 100

tot = 0
flag = 0
tmp = {}
while not flag:
    for key, value in ingredients.items():
        tmp[key] =  dogs_buy[key] - value
        if dogs_buy[key] < 0:
            failing = key
            flag = 1
        if dogs_buy[key] == 0:
            failing = key
            tot+=1
            flag = 1
    if not flag:
        tot+=1
        dogs_buy = tmp
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


print(failing)
print(tot)
list_final = []

for key, value in dogs_buy.items():
    if value > 0 :
        list_final.append([key,value])
list_final = sorted(list_final, key=lambda list_final : list_final[1])
for elem in list_final:
    if "".join(elem[:-1]) in is_liquid:
        continue 
    valeur = elem[1]
    if valeur >= 1000 :
        valeur = valeur / 1000
        print("".join(elem[:-1]), str(valeur)+"kg")
    else:
        print("".join(elem[:-1]), str(int(elem[-1]))+"g")
for elem in list_final:
    if "".join(elem[:-1]) not in is_liquid:
        continue 
    valeur = elem[1]
    if valeur >= 100 :
        valeur = valeur / 100
        print("".join(elem[:-1]), str(valeur)+"L")
    else:
        print("".join(elem[:-1]), str(int(elem[-1]))+"cl")


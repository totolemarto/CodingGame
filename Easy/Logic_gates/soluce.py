import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
input_names = []
input_signals = []
for i in range(n):
    input_name, input_signal = input().split()
    input_names.append(input_name)
    input_signals.append(input_signal)
lenght = len(input_signals[0])
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    if _type == "AND":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" and input_signals[input_names.index(input_name_2)][i] == "-":                 
                result += "-"
            else:
                result += "_"
        print(output_name, result)
    elif _type == "OR":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" or input_signals[input_names.index(input_name_2)][i] == "-":                 
                result += "-"
            else:
                result += "_"
        print(output_name, result)

    elif _type == "XOR":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" or input_signals[input_names.index(input_name_2)][i] == "-":                 
                if input_signals[input_names.index(input_name_1)][i] == "-" and input_signals[input_names.index(input_name_2)][i] == "-":                 
                    result += "_"
                else:
                    result += "-"
            else:
                result += "_"
        print(output_name, result)
           
    elif _type == "NAND":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" and input_signals[input_names.index(input_name_2)][i] == "-":                 
                result += "_"
            else:
                result += "-"
        print(output_name, result)
           
    elif _type == "NOR":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" or input_signals[input_names.index(input_name_2)][i] == "-":                 
                result += "_"
            else:
                result += "-"
        print(output_name, result)
           
    elif _type == "NXOR":
        result = ""
        for i in range(lenght):
            if input_signals[input_names.index(input_name_1)][i] == "-" or input_signals[input_names.index(input_name_2)][i] == "-":                 
                if input_signals[input_names.index(input_name_1)][i] == "-" and input_signals[input_names.index(input_name_2)][i] == "-":                 
                    result += "-"
                else:
                    result += "_"
            else:
                result += "-"
        print(output_name, result)
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


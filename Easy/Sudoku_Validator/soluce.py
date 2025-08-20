import sys
import math


def transpose(matrix):
    if matrix == None or len(matrix) == 0:
        return []

    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    return result

def check_line(line):
    for elem in range(1,10):
        if elem not in line:
            return True
    return False

def verifie(mat):
    for i in range(2):
        for l in mat:
            if check_line(l):
                print("false")
                return
        mat=transpose(mat)
    for i in range(0,9,3):
        for j in range(0,9,3):
            l = []
            for z in range(j,j+3):
                for k in range(i,i+3):
                    l.append(mat[k][z])
            if check_line(l):            
                print("false")
                return
    
    print("true")
    return    

mat=[]
for i in range(9):
    ligne=[]
    for j in input().split():
        n = int(j)
        ligne.append(n)
    mat.append(ligne)

verifie(mat)


import sys
import math

# Don't let the machines win. You are humanity's last hope...
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
mat=[]
for i in range(height):
    mat.append(list(input()))  # width characters, each either 0 or .
for i in range(height):
    for j in range(width):
        if mat[i][j]==".":continue
        if j+1<width and mat[i][j+1]!=".":
            right=(j+1,i)
        else: 
            tmp=j
            right=(-2,-2)
            while j<width:
                j+=1
                if j+1<width and mat[i][j+1]!=".":
                    right=(j+1,i)
                    break
                
            j=tmp
            if right==(-2,-2):
                right=(-1,-1)
        if i+1<height and mat[i+1][j]!=".":
            bottom=(j,i+1)
        else:
            bottom=(-2,-2)
            tmp=i
            i+=1
            while i<height:
                if i+1<height and mat[i+1][j]!=".":
                    bottom=(j,i+1)
                    break     
                i+=1       
            i=tmp
            if bottom==(-2,-2):
                bottom=(-1,-1)
    
        print(j,i,right[0],right[1],bottom[0],bottom[1])

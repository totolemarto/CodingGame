import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Queen:
    line : int
    column : int
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def get_all_cell(self, mat :list[str]) -> list[list[int]] :
        result : list[list[int]] = []
        for line in range(1,8):
            if self.line - line < 0:break
            piece = mat[self.line - line][self.column]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line - line , self.column])
                break
            result.append([self.line - line, self.column])
        for line in range(1,8):
            if self.line + line >= 8:break
            piece = mat[self.line + line][self.column]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line + line , self.column])
                break
            result.append([self.line + line, self.column])
        for column in range(1,8):
            if self.column + column >=8 :break
            piece = mat[self.line][self.column + column]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line, self.column + column])
                break
            result.append([self.line, self.column + column])
        for column in range(1,8):
            if self.column - column < 0:break
            piece = mat[self.line][self.column - column]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line, self.column - column])
                break
            result.append([self.line, self.column - column])
        
        for i in range(1,8):
            if self.line +i >= 8 or self.column + i >= 8:
                break
            piece = mat[self.line + i][self.column + i]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line+i, self.column - i])
                break
            result.append([self.line+i, self.column + i])
        
        for i in range(1, 8):
            if self.line - i < 0 or self.column + i >= 8:
                break
            piece = mat[self.line - i][self.column + i]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line+i, self.column - i])
                break
            result.append([self.line-i, self.column + i])
        
        for i in range(1, 8):
            if self.line +i >= 8 or self.column - i < 0:
                break
            piece = mat[self.line + i][self.column - i]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line+i, self.column - i])
                break
            result.append([self.line+i, self.column - i])

        for i in range(1, 8):
            if self.line - i < 0 or self.column - i < 0:
                break
            piece = mat[self.line - i][self.column - i]
            if piece != ".":
                if piece == "b" and color == "white" or piece == "w" and color == "black":
                    result.append([self.line+i, self.column - i])
                break
            result.append([self.line - i, self.column - i])
        return result



mat :list[str] = []
color = input()
queen : Queen  = None 
for i in range(8):
    mat.append(input())
    if "Q" in mat[i]:
        queen = Queen(i, mat[i].index("Q"))

result = 0
all_cell = queen.get_all_cell(mat)
print("\n".join(mat))
print()
print()
print()
for line in range(8):
    for column in range(8):
        if [line, column] in all_cell:
            print("Q", end="")
        else:
            print(".", end = "")
    print()
print(all_cell)
print(len(queen.get_all_cell(mat))) 

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



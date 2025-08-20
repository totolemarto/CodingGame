import sys
import math

def is_same_color(letter, letter2):
    if letter2 == "." : return False
    return letter.isupper() == letter2.isupper()


def tour(i, j, board):
    letter = board[i][j]
    result = []
    flag = True

    goal = i-1
    while goal!=-1 and flag:
        if board[goal][j] == ".":
            result.append((goal,j))
        else:
            flag= False
            result.append((goal,j))

            if not is_same_color(letter, board[goal][j]) and  board[goal][j] in "Kk":
                flag = True
        goal -= 1

    flag = True
    goal = i + 1
    while goal!= 8 and flag:
        if board[goal][j] == ".":
            result.append((goal,j))
        else:
            flag= False
            result.append((goal,j))

            if not is_same_color(letter, board[goal][j]) and board[goal][j] in "Kk":
                flag = True
        goal += 1

    flag = True
    goal = j-1
    while goal!=-1 and flag:
        if board[i][goal] == ".":
            result.append((i,goal))
        else:
            flag= False
            result.append((i,goal))

            if not is_same_color(letter, board[i][goal]) and board[i][goal] in "Kk":
                flag = True
        goal -= 1

    flag = True
    goal = j + 1
    while goal!= 8 and flag:
        if board[i][goal] == ".":
            result.append((i,goal))
        else:
            flag= False
            result.append((i,goal))
            if not is_same_color(letter, board[i][goal]) and board[i][goal] in "Kk":
                    flag = True
        goal += 1

    return result



def fou(i, j ,board):
    letter = board[i][j]
    result = []
    flag = True

    gap = -1
    while i + gap !=-1 and j + gap != -1 and flag:
        if board[i + gap][j + gap] == ".":
            result.append((i + gap, j + gap))
        else:
            flag= False
            result.append((i + gap, j + gap))
            if not is_same_color(letter, board[i + gap][j + gap]) and board[i + gap][j + gap] in "Kk":
                flag = True
        gap -= 1

    flag = True
    gap = 1
    while i + gap != 8 and j + gap != 8 and flag:
        if board[i + gap][j + gap] == ".":
            result.append((i + gap, j + gap))
        else:
            flag= False
            result.append((i + gap, j + gap))
            if not is_same_color(letter, board[i + gap][j + gap]) and board[i + gap][j + gap] in "Kk":
                    flag = True
        gap += 1

    flag = True
    gap = 1
    while i - gap !=-1 and j + gap != 8 and flag:
        if board[i - gap][j + gap] == ".":
            result.append((i - gap, j + gap))
        else:
            flag= False
            result.append((i - gap, j + gap))
            if not is_same_color(letter, board[i - gap][j + gap]) and board[i - gap][j + gap] in "Kk":
                flag = True
        gap += 1


    flag = True
    gap = - 1
    while i - gap != 8 and j + gap != -1 and flag:
        if board[i - gap][j + gap] == ".":
            result.append((i - gap, j + gap))
        else:
            flag= False
            result.append((i - gap, j + gap))
            if not is_same_color(letter, board[i - gap][j + gap]) and board[i - gap][j + gap] in "Kk":
                flag = True
        gap -= 1

    return result


def cavalier(i, j ,board):
    letter = board[i][j]
    result = []
    if i - 2 >= 0:
        if j - 1 >= 0:
            result.append((i-2, j-1)) 
        if j + 1 <= 7:
            result.append((i-2 , j+1))
    if i + 2 <= 7:
        if j - 1 >= 0:
            result.append((i+2, j-1)) 
        if j + 1 <= 7:
            result.append((i+2 , j+1))
    if j - 2 >= 0:
        if i - 1 >= 0:
            result.append((i-1, j-2)) 
        if i + 1 <= 7:
            result.append((i+1 , j-2))
    if j + 2 <= 7:
        if i - 1 >= 0:
            result.append((i - 1, j + 2)) 
        if i + 1 <= 7:
            result.append((i + 1 , j + 2))

    return result

def pion(i, j ,board):
    letter = board[i][j]
    result = []
    if letter.isupper():
        result.append((i-1, j-1))
        result.append((i-1, j+1))
    else:
        result.append((i+1, j-1))
        result.append((i+1, j+1))
    return result

def can_move(piece, board):
    name,i,j = piece
    result = []

    if name in "Rr":
        result += tour(i,j,board)
    
    if name in "Bb":
        result += fou(i,j,board)
    if name in "Nn":
        result += cavalier(i,j,board)
    
    if name in "Qq":
        result += tour(i,j,board)
        result += fou(i,j,board)
    
    if name in "Pp":
        result += pion(i,j, board)
    
    return result


def king_move(board, i,j):
    letter = board[i][j]
    result = [(i,j)]
    if i!=0  and not is_same_color(letter, board[i - 1][j]):
        result.append((i - 1, j))
    if i!=7 and not is_same_color(letter, board[i + 1][j]):
        result.append((i + 1, j))    
    if j!=0 and not is_same_color(letter, board[i][j - 1]):
        result.append((i, j - 1))
    if j != 0:
        if i != 0  and not is_same_color(letter, board[i - 1][j - 1]):
            result.append((i - 1, j - 1))    
        if i != 7  and not is_same_color(letter, board[i + 1][j - 1]):
            result.append((i + 1, j - 1))    
    if j!=7 and not is_same_color(letter, board[i][j + 1]):
        result.append((i, j + 1))    
    if j != 7:
        if i != 0 and not is_same_color(letter, board[i - 1][j + 1]):
            result.append((i - 1, j + 1))    
        if i != 7  and not is_same_color(letter, board[i + 1][j + 1]):
            result.append((i + 1, j + 1))    
    return result

def king_defend(board, i , j):
    letter = board[i][j]
    result = [(i,j)]
    if i!=0  :
        result.append((i - 1, j))
    if i!=7 :
        result.append((i + 1, j))    
    if j!=0 :
        result.append((i, j - 1))
    if j != 0:
        if i != 0  :
            result.append((i - 1, j - 1))    
        if i != 7  :
            result.append((i + 1, j - 1))    
    if j!=7 :
        result.append((i, j + 1))    
    if j != 7:
        if i != 0 :
            result.append((i - 1, j + 1))    
        if i != 7  :
            result.append((i + 1, j + 1))    
    return result


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
board = [[0 for _ in range(8)] for _ in range(8)]
black = []
white = []
for i in range(8):
    board_row = list(input())
    board[i] = board_row
for i in range(8):
    for j in range(8):
        if board[i][j] == "K":
            white_king = i,j
        if board[i][j] == "k":
            black_king = i,j
        if board[i][j] != ".":
            if board[i][j].isupper():
                white.append([board[i][j], i , j])
            else:
                black.append([board[i][j], i , j])

white_occup = []
for elem in white:
    white_occup += can_move(elem,board)

black_occup = []
for elem in black:
    black_occup += can_move(elem,board)


winne = "N"
flag = False
for case in king_move(board, black_king[0],black_king[1]):
    if case not in white_occup and case not in king_defend(board,white_king[0],white_king[1]):
        flag =True
if not flag:
    print("W")
else:
    flag = False
    for case in king_move(board, white_king[0],white_king[1]):
        if case not in black_occup and case not in king_defend(board, black_king[0],black_king[1]):
            flag =True
    if not flag:
        print("B")
    else:
        print("N")
#print(king_move(pos[0], pos[1]))



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)




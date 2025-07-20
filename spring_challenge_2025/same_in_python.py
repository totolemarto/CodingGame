#!/bin/python3
import cProfile
SIZE = 3
MAX_MEMO = 40000000

class Config:
    def __init__(self, hash_value, depth, result):
        self.hash = hash_value
        self.depth = depth
        self.result = result


class Point:
    def __init__(self, line, col):
        self.line = line
        self.col = col


class PointToRemove:
    def __init__(self):
        self.to_remove = []
        self.size = 0


class Capture:
    TOP_RIGHT = 0
    TOP_BOTTOM = 1
    TOP_LEFT = 2
    RIGHT_BOTTOM = 3
    RIGHT_LEFT = 4
    BOTTOM_LEFT = 5
    TOP_RIGHT_BOTTOM = 6
    TOP_RIGHT_LEFT = 7
    TOP_BOTTOM_LEFT = 8
    RIGHT_BOTTOM_LEFT = 9
    TOP_RIGHT_BOTTOM_LEFT = 10
    NOTHING = 11


# Dictionnaires de mémoïsation
memo_capture = {}
memo_hash = {}
memo_possibility = {}


def add_and_convert(current, total):
    total[0] = (current + total[0]) & 0x3FFFFFFF


def get_hash(mat):
    # Conversion de la matrice en hash
    mat_tuple = tuple(tuple(row) for row in mat)
    if mat_tuple in memo_hash:
        return memo_hash[mat_tuple]
    
    result = 0
    for i in range(SIZE):
        for j in range(SIZE):
            result = result * 10 + mat[i][j]
    
    memo_hash[mat_tuple] = result
    return result


def get_mat(hash_value):
    mat = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            mat[i][j] = hash_value % 10
            hash_value //= 10
    return mat


def reboot_mat(mat, tmp):
    for i in range(SIZE):
        for j in range(SIZE):
            tmp[i][j] = mat[i][j]


def get_value_cell(line, col, mat):
    if line < 0 or line >= SIZE or col < 0 or col >= SIZE:
        return 10
    if mat[line][col] == 0:
        return 10
    return mat[line][col]


def get_all_capture(mat, begin):
    mat_tuple = tuple(tuple(row) for row in mat)
    begin_tuple = (begin.line, begin.col)
    
    if (mat_tuple, begin_tuple) in memo_capture:
        return memo_capture[(mat_tuple, begin_tuple)]
    
    result = PointToRemove()
    value_top = get_value_cell(begin.line - 1, begin.col, mat)
    value_bottom = get_value_cell(begin.line + 1, begin.col, mat)
    value_right = get_value_cell(begin.line, begin.col + 1, mat)
    value_left = get_value_cell(begin.line, begin.col - 1, mat)

    if value_top + value_right <= 6:
        result.to_remove.append(Capture.TOP_RIGHT)
        result.size += 1
    if value_top + value_bottom <= 6:
        result.to_remove.append(Capture.TOP_BOTTOM)
        result.size += 1
    if value_top + value_left <= 6:
        result.to_remove.append(Capture.TOP_LEFT)
        result.size += 1
    if value_right + value_bottom <= 6:
        result.to_remove.append(Capture.RIGHT_BOTTOM)
        result.size += 1
    if value_right + value_left <= 6:
        result.to_remove.append(Capture.RIGHT_LEFT)
        result.size += 1
    if value_bottom + value_left <= 6:
        result.to_remove.append(Capture.BOTTOM_LEFT)
        result.size += 1
    if value_top + value_right + value_bottom <= 6:
        result.to_remove.append(Capture.TOP_RIGHT_BOTTOM)
        result.size += 1
    if value_top + value_right + value_left <= 6:
        result.to_remove.append(Capture.TOP_RIGHT_LEFT)
        result.size += 1
    if value_top + value_bottom + value_left <= 6:
        result.to_remove.append(Capture.TOP_BOTTOM_LEFT)
        result.size += 1
    if value_right + value_bottom + value_left <= 6:
        result.to_remove.append(Capture.RIGHT_BOTTOM_LEFT)
        result.size += 1
    if value_top + value_right + value_bottom + value_left <= 6:
        result.to_remove.append(Capture.TOP_RIGHT_BOTTOM_LEFT)
        result.size += 1
    if result.size == 0:
        result.to_remove.append(Capture.NOTHING)
        result.size = 1

    memo_capture[(mat_tuple, begin_tuple)] = result
    return result


def explore_all_possibility(mat, total, depth) -> int:
    mat_tuple = tuple(tuple(row) for row in mat)
    
    if (mat_tuple, depth) in memo_possibility:
        add_and_convert(memo_possibility[(mat_tuple, depth)], total)
        return memo_possibility[(mat_tuple, depth)]
    
    if depth == 0:
        add_and_convert(get_hash(mat), total)
        return get_hash(mat)

    to_call = [[[0 for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(81)]
    pass_once = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if mat[i][j] == 0:
                current = Point(i, j)
                todo = get_all_capture(mat, current)
                for indice in range(todo.size):
                    new_value = 0
                    reboot_mat(mat, to_call[pass_once])
                    capture_type = todo.to_remove[indice]
                    if capture_type == Capture.TOP_RIGHT:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i][j + 1]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i][j + 1] = 0
                    elif capture_type == Capture.TOP_BOTTOM:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i + 1][j]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i + 1][j] = 0
                    elif capture_type == Capture.TOP_LEFT:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.RIGHT_BOTTOM:
                        new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i + 1][j]
                        to_call[pass_once][i][j + 1] = 0
                        to_call[pass_once][i + 1][j] = 0
                    elif capture_type == Capture.RIGHT_LEFT:
                        new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i][j + 1] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.BOTTOM_LEFT:
                        new_value = to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i + 1][j] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.TOP_RIGHT_BOTTOM:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i][j + 1] + to_call[pass_once][i + 1][j]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i][j + 1] = 0
                        to_call[pass_once][i + 1][j] = 0
                    elif capture_type == Capture.TOP_RIGHT_LEFT:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i][j + 1] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i][j + 1] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.TOP_BOTTOM_LEFT:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i + 1][j] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.RIGHT_BOTTOM_LEFT:
                        new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1]
                        to_call[pass_once][i][j + 1] = 0
                        to_call[pass_once][i + 1][j] = 0
                        to_call[pass_once][i][j - 1] = 0
                    elif capture_type == Capture.TOP_RIGHT_BOTTOM_LEFT:
                        new_value = to_call[pass_once][i - 1][j] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1] + to_call[pass_once][i][j + 1]
                        to_call[pass_once][i - 1][j] = 0
                        to_call[pass_once][i + 1][j] = 0
                        to_call[pass_once][i][j - 1] = 0
                        to_call[pass_once][i][j + 1] = 0
                    elif capture_type == Capture.NOTHING:
                        new_value = 1
                    to_call[pass_once][i][j] = new_value
                    pass_once += 1
    result = 0
    if pass_once == 0:
        result = get_hash(mat)
        add_and_convert(result, total)
    else:
        for i in range(pass_once):
            result += explore_all_possibility(to_call[i], total, depth - 1)

    # Mémorisation du résultat pour les appels avec les mêmes paramètres
    memo_possibility[(mat_tuple, depth)] = result
    return result


def main():
    depth = int(input())
    total = [0]
    mat = []
    for i in range(SIZE):
        mat.append(list(map(int, input().split())))
    
    explore_all_possibility(mat, total, depth)
    print(total[0])


if __name__ == "__main__":
    # cProfile.run('main()')
    main()

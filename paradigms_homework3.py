import numpy as np


def read_matrix(reading_size, required_size):
    matrix = np.zeros((required_size, required_size), dtype=np.int)
    for k in range(reading_size):
        matrix[k][:reading_size] = list(map(int, input().split()))
    return matrix


def split(matrix):
    left, right = np.hsplit(matrix, 2)
    return np.vsplit(left, 2) + np.vsplit(right, 2)


def multi(matrix1, matrix2):
    if matrix1.size == 1:
        return matrix1 * matrix2
    else:
        a11, a21, a12, a22 = split(matrix1)
        b11, b21, b12, b22 = split(matrix2)
        p1 = multi(a11 + a22, b11 + b22)
        p2 = multi(a21 + a22, b11)
        p3 = multi(a11, b12 - b22)
        p4 = multi(a22, b21 - b11)
        p5 = multi(a11 + a12, b22)
        p6 = multi(a21 - a11, b11 + b12)
        p7 = multi(a12 - a22, b21 + b22)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        return np.vstack((np.hstack((c11, c12)),
                          np.hstack((c21, c22))))


base_size = int(input())
shape_size = 1
while shape_size < base_size:
    shape_size *= 2
a = read_matrix(base_size, shape_size)
b = read_matrix(base_size, shape_size)
result = multi(a, b)
for line in result[:base_size, :base_size]:
    print(' '.join(map(str, line)))

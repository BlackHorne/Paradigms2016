import numpy as np


def read_matrix():
    matrix = np.zeros((size, size), dtype=np.int)
    for i in range(base_size):
        matrix[i][:base_size] = list(map(int, input().split()))
    return matrix


def fragmentation(matrix):
    part1, part2 = np.vsplit(matrix, 2)
    up_and_left, up_and_right = np.hsplit(part1, 2)
    down_and_left, down_and_right = np.hsplit(part2, 2)
    return (up_and_left, down_and_left, up_and_right, down_and_right)


def multi(matrix1, matrix2):
    if matrix1.size == 1:
        return matrix1 * matrix2
    else:
        a11, a12, a21, a22 = fragmentation(matrix1)
        b11, b12, b21, b22 = fragmentation(matrix2)
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
size = 1
while size < base_size:
    size *= 2
a = read_matrix()
b = read_matrix()
rezult_matrix = multi(a, b)
for i in range(base_size):
    for j in range(base_size):
        print(rezult_matrix[i][j], end=' ')
    print()

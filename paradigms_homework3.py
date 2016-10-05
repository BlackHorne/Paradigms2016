import numpy as np


def multip(matrix1, matrix2, current_size):
    if current_size == 1:
        return matrix1 * matrix2
    else:
        s = current_size
        a_1_1 = matrix1[0:s//2, 0:s//2]
        a_1_2 = matrix1[0:s//2, s//2:s]
        a_2_1 = matrix1[s//2:s, 0:s//2]
        a_2_2 = matrix1[s//2:s, s//2:s]
        b_1_1 = matrix2[0:s//2, 0:s//2]
        b_1_2 = matrix2[0:s//2, s//2:s]
        b_2_1 = matrix2[s//2:s, 0:s//2]
        b_2_2 = matrix2[s//2:s, s//2:s]
        p_1 = multip(a_1_1 + a_2_2, b_1_1 + b_2_2, s//2)
        p_2 = multip(a_2_1 + a_2_2, b_1_1, s//2)
        p_3 = multip(a_1_1, b_1_2 - b_2_2, s//2)
        p_4 = multip(a_2_2, b_2_1 - b_1_1, s//2)
        p_5 = multip(a_1_1 + a_1_2, b_2_2, s//2)
        p_6 = multip(a_2_1 - a_1_1, b_1_1 + b_1_2, s//2)
        p_7 = multip(a_1_2 - a_2_2, b_2_1 + b_2_2, s//2)
        c_1_1 = p_1 + p_4 - p_5 + p_7
        c_1_2 = p_3 + p_5
        c_2_1 = p_2 + p_4
        c_2_2 = p_1 - p_2 + p_3 + p_6
        return np.vstack((np.hstack((c_1_1, c_1_2)),
                          np.hstack((c_2_1, c_2_2))))

size = input()
size = int(size)
a = np.array([[int(j) for j in input().split()] for i in range(size)])
b = np.array([[int(j) for j in input().split()] for i in range(size)])
new_size = 1
while new_size < size:
    new_size *= 2
add_right = np.zeros((size, new_size - size))
add_down = np.zeros((new_size - size, new_size))
new_b = np.vstack((np.hstack((b, add_right)), add_down))
new_a = np.vstack((np.hstack((a, add_right)), add_down))
print(multip(new_a, new_b, new_size)[0:size, 0:size])

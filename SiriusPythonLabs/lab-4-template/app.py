import time

import numpy as np
import sys
import math

SIZE_OF_FIELD = 100


def reader_xyw(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            x, y, w = line.split()
            field[int(x)][int(y)] += int(w)


'''
def reader_field(file_path):
    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            x_line = list(map(int, line.split()))
            field.append(x_line)
    return
'''
# reading args
path = sys.argv[1]
r = int(sys.argv[2])
#path = 'file.txt'
#r = 0.9
# reading field
# field = []

field = np.zeros((SIZE_OF_FIELD, SIZE_OF_FIELD), dtype=int)
reader_xyw(path)

# counting max weight
# SIZE_OF_FIELD = len(field)


# расстояние между точками
def dist_kv(x_1, y_1, x_2, y_2):
    return (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2


# урон ракеты
def weight_of_shot(x_roc, y_roc, r):
    w = 0
    for x_p in range(math.floor(x_roc - r), math.ceil(x_roc + r) + 1):
        for y_p in range(math.floor(y_roc - r), math.ceil(y_roc + r) + 1):
            if SIZE_OF_FIELD > x_p >= 0 and SIZE_OF_FIELD > y_p >= 0 and dist_kv(x_p, y_p, x_roc, y_roc) <= r ** 2:
                w += field[x_p][y_p]
    return w


# поиск двух центров окружностей, построенных на двух точках
def get_two_okr(x_1, y_1, x_2, y_2, r):
    x_c = (x_1 + x_2) / 2
    y_c = (y_1 + y_2) / 2
    len_ac_kv = dist_kv(x_1, y_1, x_c, y_c)
    len_co = math.sqrt(len_ac_kv + r ** 2)
    n_vec_x = y_2 - y_1
    n_vec_y = x_1 - x_2
    n_vec_len = math.sqrt(n_vec_x ** 2 + n_vec_y ** 2)
    n_vec_x = n_vec_x * len_co / n_vec_len
    n_vec_y = n_vec_y * len_co / n_vec_len
    x_o1 = x_c + n_vec_x
    y_o1 = y_c + n_vec_y
    x_o2 = x_c - n_vec_x
    y_o2 = y_c - n_vec_y
    return x_o1, y_o1, x_o2, y_o2


# перебор по точкам
def count_in_real():
    max_w = 0
    max_w_x = -1
    max_w_y = -1
    for i in range(0, SIZE_OF_FIELD):
        for j in range(0, SIZE_OF_FIELD):
            if r < 1:
                if field[i][j] > max_w:
                    max_w = field[i][j]
                    max_w_x = i
                    max_w_y = j
            else:
                for l in range(0, SIZE_OF_FIELD):
                    for m in range(j, SIZE_OF_FIELD):
                        if i != l or j != m:
                            if dist_kv(i, j, l, m) == (2 * r) ** 2:
                                x_rocket = (i + l) / 2
                                y_rocket = (j + m) / 2
                                local_w = weight_of_shot(x_rocket, y_rocket, r)
                                if local_w > max_w:
                                    max_w = local_w
                                    max_w_x = (i + l) / 2
                                    max_w_y = (l + m) / 2
                            elif dist_kv(i, j, l, m) < (2 * r) ** 2:
                                x_rocket1, y_rocket1, x_rocket2, y_rocket2 = get_two_okr(i, j, l, m, r)
                                w1 = weight_of_shot(x_rocket1, y_rocket1, r)
                                if w1 > max_w:
                                    max_w = w1
                                    max_w_x = x_rocket1
                                    max_w_y = y_rocket1
                                w2 = weight_of_shot(x_rocket2, y_rocket2, r)
                                if w2 > max_w:
                                    max_w = w2
                                    max_w_x = x_rocket2
                                    max_w_y = y_rocket2

    print(max_w_x, max_w_y, max_w)


def count_in_int():
    max_w = 0
    max_w_x = -1
    max_w_y = -1
    for i in range(0, SIZE_OF_FIELD):
        for j in range(0, SIZE_OF_FIELD):
            local_w = weight_of_shot(i, j, r)
            if local_w > max_w:
                max_w = local_w
                max_w_x = i
                max_w_y = j
    print(max_w_x, max_w_y, max_w)

count_in_int()


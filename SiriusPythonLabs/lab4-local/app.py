import time

import numpy as np
import sys

from Building import Building
from RacketShot import RacketShot

SIZE_OF_FIELD = 100


def reader_xyw(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            x, y, w = line.split()
            field[int(x)][int(y)] += int(w)
            new_build = Building(x, y, w)
            if new_build in builds:
                builds[builds.index(new_build)] = new_build.plus_w(builds[builds.index(new_build)].w)
            else:
                builds.append(new_build)
    builds.sort()
    return

'''
def reader_field(file_path):
    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            x_line = list(map(int, line.split()))
            field.append(x_line)
    return
'''

start_time = time.time()
# reading args
path = sys.argv[1]
r = int(sys.argv[2])
#path = 'resource/file.txt'
#r = 1
builds = []
# reading field
# field = []
field = np.zeros((SIZE_OF_FIELD, SIZE_OF_FIELD), dtype=int)
reader_xyw(path)
end_time = time.time()
elapsed_time = end_time - start_time
print('End of reading time: ', elapsed_time)

# counting max weight
#SIZE_OF_FIELD = len(field)
max_w = 0
max_w_x = -1
max_w_y = -1

#перебор по точкам

#add all points
builds_full = []

for i in range(0, SIZE_OF_FIELD):
    for j in range(0, SIZE_OF_FIELD):
        b = Building(i, j, 0)
        if b not in builds:
            builds.append(b)
        else:
            builds_full.append(builds[builds.index(b)])
builds.sort()
end2_time = time.time()
elapsed_time = end2_time - end_time
print('End of creating time: ', elapsed_time)

'''
def count_square(x1, y1, x2, y2):
    w = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            w += field[i][j]
    return w
'''

b1_best = Building(-1, -1, 0)
b2_best = Building(-2, -2, 0)


def new_w(w_prev, x_prev, y_prev, dot_new):
    if w_prev < dot_new.w:
        w_prev = dot_new.w
        x_prev = dot_new.x
        y_prev = dot_new.y
        p = True
    else:
        p = False
    return w_prev, x_prev, y_prev, p


for i in range(SIZE_OF_FIELD ** 2):
    for j in range(i + 1, SIZE_OF_FIELD ** 2):
        b1 = builds[i]
        b2 = builds[j]
        if b1.dot_dist_kv(b2) == (2*r) ** 2:
            rocket = RacketShot((b1.x + b2.x) / 2, (b1.y + b2.y) / 2, r)
            local_w = rocket.weight_of_shot(field)
            max_w, max_w_x, max_w_y, p = new_w(max_w, max_w_x, max_w_y, rocket)
        elif b1.dot_dist_kv(b2) < (2*r) ** 2:
            x1, y1, x2, y2 = b1.get_two_okr(b2, r)
            rocket1 = RacketShot(x1, y1, r)
            rocket2 = RacketShot(x2, y2, r)
            rocket1.weight_of_shot(field)
            rocket2.weight_of_shot(field)
            max_w, max_w_x, max_w_y, p = new_w(max_w, max_w_x, max_w_y, rocket1)
            max_w, max_w_x, max_w_y, p = new_w(max_w, max_w_x, max_w_y, rocket2)
end3_time = time.time()
elapsed_time = end3_time - end2_time
print('Elapsed time: ', elapsed_time)
# print("b1 best: ", end = '')
# b1_best.print_it()
# print("b2 best: ", end = '')
# b2_best.print_it()
'''

start_time = time.time()
for i in range(0, SIZE_OF_FIELD):
    for j in range(0, SIZE_OF_FIELD):
        for l in range(0, SIZE_OF_FIELD):
            for m in range(j, SIZE_OF_FIELD):
                if i != l or j != m:
                    b1 = Building(i, j, field[i][j])
                    b2 = Building(l, m, field[l][m])
                    if b1.dot_dist_kv(b2) == r ** 2:
                        rocket = RacketShot((i + l) / 2, (j + m) / 2, r)
                        local_w = rocket.weight_of_shot(field)
                        if local_w > max_w:
                            max_w = local_w
                            max_w_x = (i + l) / 2
                            max_w_y = (l + m) / 2
                    elif b1.dot_dist_kv(b2) < r ** 2:
                        x1, y1, x2, y2 = b1.get_two_okr(b2, r)
                        rocket1 = RacketShot(x1, y1, r)
                        rocket2 = RacketShot(x2, y2, r)
                        w1 = rocket1.weight_of_shot(field)
                        if w1 > max_w:
                            max_w = w1
                            max_w_x = x1
                            max_w_y = y1
                        w2 = rocket2.weight_of_shot(field)
                        if w2 > max_w:
                            max_w = w2
                            max_w_x = x2
                            max_w_y = y2
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
'''
print(max_w_x, max_w_y, max_w)

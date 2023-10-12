# Created by Hannah at 03.10.2023 17:23

import math


# for task with F

def get_F(a0):
    if isinstance(a0, int) and a0 > 0:
        length = 1
        while a0 > 1:
            if a0 % 2 == 0:
                a0 = a0 // 2
            else:
                a0 = 3 * a0 + 1
            length += 1
        print(math.log2(a0))
        return length - math.log2(a0)
    else:
        return None


def get_seq_len(a0):
    if isinstance(a0, int) and a0 > 0:
        length = 1
        while a0 > 1:
            if a0 % 2 == 0:
                a0 = a0 // 2
            else:
                a0 = 3 * a0 + 1
            length += 1
        return length
    else:
        return None


def get_longest_seq(L, U):
    if isinstance(L, int) and isinstance(U, int) and U > L > 0:
        length_max = 0
        a_max = -1
        for i in range(L, U + 1):
            length = get_seq_len(i)
            if length > length_max:
                length_max = length
                a_max = i
        return a_max, length_max
    else:
        return None


'''
l = (input("Input lower board:"))
u = int64(input("Input upper board:"))
l_ans, a_ans = get_longest_seq(l, u)
print("Max length: {}, meaning is a0: {}".format(a_ans, l_ans))
'''

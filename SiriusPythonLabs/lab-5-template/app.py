import sys
import re


def make_shablon(strs):
    type_list = []
    size_of = strs.count('%d') + strs.count('%s') + strs.count('%f')
    s_out = ''
    for ch in range(len(strs)):
        if strs[ch] in ('[', ']', '{', '}', '(', ')', '?', '^', '*', '+', '|', '$'):
            s_out += '\{}'.format(strs[ch])
        else:
            s_out += strs[ch]
        if strs[ch] == '%':
            type_list.append(strs[ch + 1])
    s_out = (s_out.replace('%d', '([\-\+]?\d+)').replace('%f', '([\+\-]?(\d+(\.\d*)?|\.\d+)([eE][\+\-]?\d+)?)')
             .replace("'%s'", "'(.*)'").replace('%s', '(.*)'))

    return s_out, size_of, type_list


if __name__ == '__main__':
    path = sys.argv[1]
    shablon_str = sys.argv[2]
    shablon, size, type_list = make_shablon(shablon_str)
    shablon = re.compile(shablon)
    res_lists = []

    for i in range(size):
        res_lists.append([])
    with open(path, 'r') as file:
        for line in file:
            match_res = shablon.match(line)
            if match_res:
                j = 0
                for i in range(size):
                    res_lists[i].append(match_res.groups()[j])
                    if type_list[i] == 'f':  # если был float
                        j += 3
                    j += 1
    for i in res_lists:
        print(i)

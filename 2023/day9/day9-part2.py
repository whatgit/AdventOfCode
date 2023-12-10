import re
import numpy as np


def is_all_same(s):
    a = np.asarray(s)
    return (a[0] == a).all()


def is_all_zero(s):
    a = np.asarray(s)
    return (0 == a).all()


def get_adjacent_diff(a):
    d = []
    for i in range(0, len(a)):
        if i != 0:
            d.append(a[i] - a[i-1])
    return d


def extrapolate(diff_array, num):
    accumulated_diff = 0
    while diff_array:
        diff = diff_array[-1][0]
        accumulated_diff = diff - accumulated_diff
        diff_array.pop()
    return num - accumulated_diff


recorded_diff = []
new_value = []
with open('input.txt') as input_file:
    for line in input_file:
        diff = []
        all_num = re.findall(r'[a-zA-Z0-9-]+', line)   # add '-' to regex to match negative number
        all_num = [int(n) for n in all_num]
        diff = get_adjacent_diff(all_num)
        recorded_diff.append(diff)
        while not is_all_zero(diff):
            diff = get_adjacent_diff(diff)
            if not is_all_zero(diff):
                recorded_diff.append(diff)
        next_num = extrapolate(recorded_diff, all_num[0])
        new_value.append(next_num)
input_file.close()    
print(sum(new_value))
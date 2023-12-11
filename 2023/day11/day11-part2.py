import itertools
import math
import numpy as np
import re
from scipy import interpolate


def galaxy_dist(p1, p2):
    x1 = float(p1[0])
    x2 = float(p2[0])
    y1 = float(p1[1])
    y2 = float(p2[1])
    return np.abs(x1 - x2) + np.abs(y1 - y2)

initial_galaxy = []
col_check = []
with open('example.txt') as input_file:
    # Check where to expand but not expanding it
    row = 0
    for line in input_file:
        col = 0
        if row == 0:
            col_check = [True for x in range(0, len(line))]
        for h in re.finditer(r'[^a-zA-z0-9.]', line):
            col_check[h.start(0)] = False
        line = re.findall(r'[^a-zA-z0-9\n]', line)
        initial_galaxy.append(line)
        row += 1
    inserted_count = 0
    row = 0
    row_to_append = []
    for r in initial_galaxy:
        if not re.findall(r'#', "".join(r)):
            the_dots = "".join(r)
            row_to_append.append(row)
        row += 1
    # Finish checking for expansion 
    # --------------------------------------
    galaxies = {}
    num_galaxy = 1
    row = 0
    add_row = 0
    expansion = 1   # extra row and col
    # Now find number of galaxy and location
    col_to_append = [i for i, n in enumerate(col_check) if n]
    for line in initial_galaxy:
        add_col = 0
        line = ''.join(line)
        if row in row_to_append:
            add_row += expansion
        for galaxy in re.finditer('#', line):
            if any(x < galaxy.start(0) for x in col_to_append):
                for c in col_to_append:
                    if galaxy.start(0) > c:
                        add_col += expansion
            col = galaxy.start(0) + add_col
            galaxies[num_galaxy] = (row + add_row, col)
            num_galaxy += 1
        row += 1
    # print(galaxies)
    galaxy_pairs = list(itertools.combinations(galaxies, 2))
    sum_dist = 0
    for pair in galaxy_pairs:
        # print("Distance between ", pair[0], " and ", pair[1], " is ", galaxy_dist(galaxies[pair[0]], galaxies[pair[1]]))
        sum_dist += galaxy_dist(galaxies[pair[0]], galaxies[pair[1]])
    print(sum_dist)
x = np.array([1, 2, 10])
y = np.array([292, 374, 1030])
f = interpolate.interp1d(x, y, fill_value='extrapolate')
print("WHAT")
print(f(100))
import itertools
import math
import numpy as np
import re


def galaxy_dist(pa, pb):
    return np.abs(pa[0] - pb[0]) + np.abs(pa[1] - pb[1])

initial_galaxy = []
col_check = []
with open('input.txt') as input_file:
    # Expanding the galaxy
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
    for c in col_check:
        if c:
            initial_galaxy = np.insert(initial_galaxy, col+inserted_count, ['.'], axis=1)
            inserted_count +=1
        col += 1
    initial_galaxy = initial_galaxy.tolist()
    row = 0
    row_to_append = []
    for r in initial_galaxy:
        if not re.findall(r'#', "".join(r)):
            the_dots = "".join(r)
            row_to_append.append(row)
        row += 1
    inserted_count = 0
    for i in row_to_append:
        initial_galaxy = np.insert(initial_galaxy, i+inserted_count, ['.'], axis=0)
        inserted_count += 1
    initial_galaxy = initial_galaxy.tolist()
    # Finish expanding the galaxy
    # --------------------------------------
    galaxies = {}
    num_galaxy = 1
    row = 0
    # Now find number of galaxy and location
    for line in initial_galaxy:
        line = ''.join(line)
        for galaxy in re.finditer('#', line):
            galaxies[num_galaxy] = (row, galaxy.start(0))
            num_galaxy += 1
        row += 1
    print(galaxies)
    galaxy_pairs = list(itertools.combinations(galaxies, 2))
    sum_dist = 0
    for pair in galaxy_pairs:
        print("Distance between ", pair[0], " and ", pair[1], " is ", galaxy_dist(galaxies[pair[0]], galaxies[pair[1]]))
        sum_dist += galaxy_dist(galaxies[pair[0]], galaxies[pair[1]])
    print(sum_dist)
    # space = re.findall(r'[^a-zA-z0-9#\n]', line)
    # galaxy = re.findall(r'#', line)
    # print(space)
    # print(galaxy)
import re


def shift_rock_north(arr):
    for c, col in enumerate(arr[0]):
        for r, row in enumerate(arr):
            if r - 1 >= 0:
                 if row[c] == 'O':   
                    # found the rock
                    empty_space_count = 0
                    for i in range(r - 1, -1, -1):
                        if arr[i][c] != '#' and arr[i][c] != 'O':
                            empty_space_count += 1
                        else:
                            break
                    new_pos = r - empty_space_count
                    arr[new_pos][c], arr[r][c] = arr[r][c], arr[new_pos][c]
    return arr


def calculate_load(arr):
    total_load = 0
    for r, row in enumerate(arr):
        for thing in row:
            if thing == 'O':
                total_load += len(arr) - r
    return total_load

rock_array = []
with open('input.txt') as input_file:
    for line in input_file:
        rocks = re.findall(r'[O.#]', line)
        rock_array.append(rocks)
    shift_rock_north(rock_array)
    print(calculate_load(rock_array))
    
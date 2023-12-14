import re

def guess_seq_len(seq, verbose=False):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess


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


def shift_rock_south(arr):
    for c, col in enumerate(arr[0]):
        for r, row in enumerate(reversed(arr)):
            real_index = len(arr) - 1 - r
            if r - 1 >= 0:
                 if row[c] == 'O':   
                    # found the rock
                    empty_space_count = 0
                    for i in range(real_index + 1, len(arr)):
                        if arr[i][c] != '#' and arr[i][c] != 'O':
                            empty_space_count += 1
                        else:
                            break
                    new_pos = real_index + empty_space_count
                    arr[new_pos][c], arr[real_index][c] = arr[real_index][c], arr[new_pos][c]
    return arr


def shift_rock_west(arr):
    for r, row in enumerate(arr):
        for c in range(0, len(arr[0])):
            if c - 1 >= 0:
                if row[c] == 'O':
                    # found the rock
                    empty_space_count = 0
                    for i in range(c - 1, -1, -1):
                        if arr[r][i] != '#' and arr[r][i] != 'O':
                            empty_space_count += 1
                        else:
                            break
                    new_pos = c - empty_space_count
                    arr[r][new_pos], arr[r][c] = arr[r][c], arr[r][new_pos]
    return arr

def shift_rock_east(arr):
    for r, row in enumerate(arr):
        for c in range(len(arr[0]) - 1, -1, -1):
            if c + 1 <= len(arr[0]):
                if row[c] == 'O':
                    # found the rock
                    empty_space_count = 0
                    for i in range(c + 1, len(row)):
                        if arr[r][i] != '#' and arr[r][i] != 'O':
                            empty_space_count += 1
                        else:
                            break
                    new_pos = c + empty_space_count
                    arr[r][new_pos], arr[r][c] = arr[r][c], arr[r][new_pos]
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
input_file.close()
previous_load = 0
# Manual work here
target = 1000000000
answers = []
for i in range(0, 1000):
    rock_array = shift_rock_north(rock_array)
    rock_array = shift_rock_west(rock_array)
    rock_array = shift_rock_south(rock_array)
    rock_array = shift_rock_east(rock_array)
    load = calculate_load(rock_array) 
    if i >= 134:
        answers.append(load)
    # after a certain cycles (e.g., 134 here)
    # loads are repeating with only 42 numbers (use guess_seq_len function below)
rep = print(guess_seq_len(answers))
index = (target - 134) % rep # see where target = 1000000000 would end up
print(index)
potential_answers = []
for i in range(0, guess_seq_len(answers)):
    potential_answers.append(answers[i])
print('----')
print(potential_answers[index - 1])
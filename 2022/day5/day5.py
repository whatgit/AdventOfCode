import pandas as pd
import numpy as np


def move_multiple(array, n, origin, destination):
    crate = []
    for j in range(0, n):
        row_org = 0
        while array[row_org][origin] == '' and row_org < len(array)-1:
            row_org += 1
        crate.insert(0, array[row_org][origin])  # take the crate
        array[row_org][origin] = ''

    for jj in range(0, n):
        row_dest = 0
        if crate[jj] == '':
            continue
        if array[0][destination] != '':
            # the top row is occupied
            new_top = ["" for x in range(9)]
            new_top[destination] = crate[jj]
            array = np.vstack([new_top, array])
            continue
        else:
            while array[row_dest][destination] == '' and row_dest < len(array) - 1:
                row_dest += 1
            if row_dest == len(array):
                array[row_dest][destination] = crate[jj]
            else:
                array[row_dest - 1][destination] = crate[jj]
    return array


def move(array, n, origin, destination):
    for j in range(0, n):
        crate = ''
        row_org = 0
        row_dest = 0
        while array[row_org][origin] == '' and row_org < len(array)-1:
            row_org += 1
        crate = array[row_org][origin]  # take the crate
        array[row_org][origin] = ''

        if array[0][destination] != '':
            # the top row is occupied
            new_top = ["" for x in range(9)]
            new_top[destination] = crate
            array = np.vstack([new_top, array])
            continue
        else:
            while array[row_dest][destination] == '' and row_dest < len(array) - 1:
                row_dest += 1
            if row_dest == len(array):
                array[row_dest][destination] = crate
            else:
                array[row_dest - 1][destination] = crate
    return array


def get_top_row(array):
    text = ""
    for ncol in range(0, len(array[0])):
        for nrow in range(0, len(array)):
            if array[nrow][ncol] != '':
                text = text + array[nrow][ncol]
                break
    return text


parcels = []
inputs = pd.read_table('input_array.txt', header=None, delimiter=' ', keep_default_na=False)
for index, row in inputs.iterrows():
    row = row.tolist()
    for i in range(0, len(row)-4):
        if all(element == '' for element in row[i:i+4]):
            row[i:i+4] = [''.join(row[i:i+4])]
    parcels.append(row[0:9])
# now columns are stack number and rows are height
part1_parcel = parcels
instructions = pd.read_table('input_instruction.txt', header=None, delimiter=' ', names=['move',
                                                                                         'n_move',
                                                                                         'from',
                                                                                         'origin',
                                                                                         'to',
                                                                                         'destination'])
for index, row in instructions.iterrows():
    part1_parcel = move(part1_parcel, int(row['n_move']), int(row['origin']) - 1, int(row['destination']) - 1)
for i in range(0, len(part1_parcel)):
    print(part1_parcel[i])
print(get_top_row(part1_parcel))

# Part 2
parcels = []
inputs = pd.read_table('input_array.txt', header=None, delimiter=' ', keep_default_na=False)
for index, row in inputs.iterrows():
    row = row.tolist()
    for i in range(0, len(row)-4):
        if all(element == '' for element in row[i:i+4]):
            row[i:i+4] = [''.join(row[i:i+4])]
    parcels.append(row[0:9])
# now columns are stack number and rows are height

part2_parcel = parcels
instructions = pd.read_table('input_instruction.txt', header=None, delimiter=' ', names=['move',
                                                                                         'n_move',
                                                                                         'from',
                                                                                         'origin',
                                                                                         'to',
                                                                                         'destination'])
for index, row in instructions.iterrows():
    part2_parcel = move_multiple(part2_parcel, int(row['n_move']), int(row['origin']) - 1, int(row['destination']) - 1)
for i in range(0, len(part2_parcel)):
    print(part2_parcel[i])
print(get_top_row(part2_parcel))

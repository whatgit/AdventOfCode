import pandas as pd
import numpy as np

contained_count = 0
# Part 1
inputs = pd.read_csv('input.txt', header=None, delimiter=',', names=['elf1', 'elf2'])
for index, row in inputs.iterrows():
    elf1_range = row['elf1'].split("-")
    elf2_range = row['elf2'].split("-")
    elf1_task = np.arange(int(elf1_range[0]), int(elf1_range[1]) + 1)
    elf2_task = np.arange(int(elf2_range[0]), int(elf2_range[1]) + 1)
    if set(elf1_task).issubset(elf2_task):
        contained_count = contained_count + 1
    elif set(elf2_task).issubset(elf1_task):
        contained_count = contained_count + 1
print(contained_count)

# Part 2
overlap_count = 0
for index, row in inputs.iterrows():
    elf1_range = row['elf1'].split("-")
    elf2_range = row['elf2'].split("-")
    elf1_task = np.arange(int(elf1_range[0]), int(elf1_range[1]) + 1)
    elf2_task = np.arange(int(elf2_range[0]), int(elf2_range[1]) + 1)
    if set(elf1_task).intersection(elf2_task) != set():
        overlap_count = overlap_count + 1
    elif set(elf2_task).intersection(elf1_task) != set():
        overlap_count = overlap_count + 1
print(overlap_count)

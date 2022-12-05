import pandas as pd
import numpy as np
# 'a' is 97 but we want 1
offset_small = 96
# 'A' is 65 but we want 27
offset_big = 38
sum_value = 0
# Part 1
inputs = pd.read_csv('input.txt', header=None, delimiter=' ', names=['stuff'])
for index, row in inputs.iterrows():
    length = len(row['stuff'])
    split_point = length//2
    bags = [row['stuff'][i: i + split_point] for i in range(0, len(row['stuff']), split_point)]
    for thing in bags[0]:
        if thing in bags[1]:
            value = ord(thing)
            if value > 90:
                # small letter
                value = value - offset_small
            else:
                value = value - offset_big
            sum_value = sum_value + value
            break
print(sum_value)

# Part 2
sum_value = 0
inputs = pd.read_csv('input.txt', header=None, delimiter=' ', names=['stuff'])
for i in range(0, len(inputs), 3):
    elf1 = inputs.iloc[i]['stuff']
    elf2 = inputs.iloc[i+1]['stuff']
    elf3 = inputs.iloc[i+2]['stuff']
    for thing in elf1:
        if thing in elf2 and thing in elf3:
            value = ord(thing)
            if value > 90:
                # small letter
                value = value - offset_small
            else:
                value = value - offset_big
            sum_value = sum_value + value
            break
print(sum_value)

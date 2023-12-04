import pandas as pd
import re


current_row = 0
gear_position = []
all_number_positions = []
actual_part_number = 0
sum_gear_ratios = 0
with open('input.txt') as input:
    for line in input:
        for symbol in re.finditer(r'[^a-zA-z0-9.\n]', line):  # find symbols excluding . and \n
            if symbol.group(0) == '*':  # if it is a gear
                gear_position.append((current_row, symbol.start(0))) # save symbol position
        for number in re.finditer(r'\d+', line):  # find numbers
            number_data = [int(number.group(0)),current_row, number.start(0), number.end(0)]
            all_number_positions.append(number_data)
        current_row += 1
input.close()
gear_number_count = {}
for gear in gear_position:
    gear_number_count[gear] = []
for number, row, start_column, end_column in all_number_positions:
    neighbors = []
    neighbors.append((row, start_column-1))
    neighbors.append((row, end_column))
    neighbors.append(((row-1, start_column-1)))
    neighbors.append(((row-1, end_column)))
    neighbors.append(((row+1, start_column-1)))
    neighbors.append(((row+1, end_column)))
    for c in range(start_column, end_column):
        neighbors.append((row-1, c))
        neighbors.append((row+1, c))
    for gear_pos in list(set(neighbors).intersection(gear_position)):
        gear_number_count[gear_pos].append(number)
for g, n in gear_number_count.items():
    gear_ratio = 1
    if len(n) == 2:
        for g in n:
            gear_ratio *= g
        sum_gear_ratios += gear_ratio
print(sum_gear_ratios)


import re


current_row = 0
symbol_position = []
all_number_positions = []
actual_part_number = 0
sum_all = 0
with open('input.txt') as input:
    for line in input:
        for symbol in re.finditer(r'[^a-zA-z0-9.\n]', line):  # find symbols excluding . and \n
            print(symbol.group(0))
            symbol_position.append((current_row, symbol.start(0))) # save symbol position
        for number in re.finditer(r'\d+', line):  # find numbers
            number_data = [int(number.group(0)),current_row, number.start(0), number.end(0)]
            all_number_positions.append(number_data)
        current_row += 1
input.close()
# all_number_positions_df = pd.DataFrame(all_number_positions, columns=['number', 'row', 'start_column', 'end_column'])
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
    if list(set(neighbors).intersection(symbol_position)):
        actual_part_number += number
print(actual_part_number)

import pandas as pd
import re


current_line = 0
part_number_positions = []
all_number_positions = []
actual_part_number = 0
sum_all = 0
with open('input.txt') as input:
    for line in input:
        symbols = re.findall(r'[^a-zA-z0-9.\n]', line) # find symbols excluding . and \n
        numbers = re.findall(r'\d+', line)  # find numbers
        # create a mask around it for each symbol
        start_search_symbol = -1
        start_search_number = -1
        # print(symbols)
        for symbol in symbols:  # for each symbol
            symbol_index = line.index(symbol, start_search_symbol+1)    # get its index
            # print("symbol ", symbol, " found at index ", symbol_index)
            part_number_positions.append([current_line-1, symbol_index-1])
            part_number_positions.append([current_line-1, symbol_index])
            part_number_positions.append([current_line-1, symbol_index+1])
            part_number_positions.append([current_line, symbol_index-1])
            part_number_positions.append([current_line, symbol_index+1])
            part_number_positions.append([current_line+1, symbol_index-1])
            part_number_positions.append([current_line+1, symbol_index])
            part_number_positions.append([current_line+1, symbol_index+1])
            start_search_symbol = symbol_index  # shift the start searching index to handle repetitive symbols
        # print(numbers)
        for number in numbers:
            number_indices = []
            number_index = line.index(number, start_search_number+1)
            # print("number ", number, " found at index ", number_index)
            for i in range(len(number)):
                number_indices.append(number_index+i)
            all_number_positions.append([number, current_line, number_indices])
            start_search_number = number_index  # shift the start searching index to handle repetitive numbers
        current_line += 1
input.close()
part_number_positions_df = pd.DataFrame(part_number_positions, columns=['line', 'column']).drop_duplicates().sort_values('line')
# print(part_number_positions_df)
all_number_positions_df = pd.DataFrame(all_number_positions, columns=['number', 'line', 'number_indices'])
# print(all_number_positions_df)
for index,row in all_number_positions_df.iterrows():
    df_line = part_number_positions_df.loc[part_number_positions_df['line'] == row['line']]
    for i in row['number_indices']:
        if i in df_line['column'].values:
            actual_part_number += int(row['number'])
            break
print(actual_part_number)

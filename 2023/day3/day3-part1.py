import pandas as pd
import re



current_line = 0
pd_columns = ['line', 'column']
part_number_positions = []
all_number_positions = []
actual_part_number = 0
with open('input_day3.txt') as input:
    for line in input:
        symbols = re.findall(r'[^a-zA-z0-9.\n]', line) # find symbols excluding . and \n
        numbers = re.findall(r'\d+', line)  # find numbers
        # create a mask around it for each symbol
        start_search_symbol = -1
        start_search_number = -1
        for symbol in symbols:  # for each symbol
            symbol_index = line.index(symbol, start_search_symbol+1)    # get its index
            part_number_positions.append([current_line-1, symbol_index-1])
            part_number_positions.append([current_line-1, symbol_index])
            part_number_positions.append([current_line-1, symbol_index+1])
            part_number_positions.append([current_line, symbol_index-1])
            part_number_positions.append([current_line, symbol_index+1])
            part_number_positions.append([current_line+1, symbol_index-1])
            part_number_positions.append([current_line+1, symbol_index])
            part_number_positions.append([current_line+1, symbol_index+1])
            start_search_symbol = symbol_index
        for number in numbers:
            number_index = line.index(number, start_search_number+1)
            number_start_index = number_index
            number_end_index = number_index + len(number)
            all_number_positions.append([number, current_line, number_start_index, number_end_index])
            start_search_number = number_index
        current_line += 1
input.close()
part_number_positions_df = pd.DataFrame(part_number_positions, columns=['line', 'column'])
print(part_number_positions_df)
all_number_positions_df = pd.DataFrame(all_number_positions, columns=['number', 'line', 'start_index', 'end_index'])
print(all_number_positions_df)
for index,row in all_number_positions_df.iterrows():
    df_line = part_number_positions_df.loc[part_number_positions_df['line'] == row['line']]
    number_indices = range(row['start_index'], row['end_index'])
    for i in number_indices:
        print(i)
        if i in df_line['column'].values:
            actual_part_number += int(row['number'])
            break
print(actual_part_number)

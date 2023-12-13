import re
import itertools


with open('input.txt') as input_file:
    arrangement_count = 0
    for line in input_file:
        possible_symbols = ['#', '.']
        condition_records = re.findall(r'\d+', line)
        condition_records = [int(c) for c in condition_records]
        # find all unknowns
        unknowns = re.findall(r'\?+', line)
        num_unknowns = 0
        for u in unknowns:
            num_unknowns += len(u)
        # create a possible combination for all unknowns
        possible_combinations = itertools.product(possible_symbols, repeat=num_unknowns)
        for combination in possible_combinations:
            # create a line
            new_line = line.replace('?', '{}', len(combination)).format(*combination)
            # find damaged springs
            dmg_groups = re.findall(r'#+', new_line)   # get groups of damaged spring(s)
            dmg_dist = []
            if len(dmg_groups) == len(condition_records):   # possible match
                for dmg in dmg_groups:
                    dmg_dist.append(len(dmg))
                if dmg_dist == condition_records:
                    arrangement_count += 1
print(arrangement_count)
input_file.close()     
        
import re


my_scratchcards = 0
max_card_number = 193
dict_card_ncopies = {x: int(1) for x in range(1,max_card_number+1)}
with open('input.txt') as input:
    for line in input:
        [card_number, content] = line.split(':')
        my_card_number = re.findall(r'\d+', card_number)
        my_card_number = int(my_card_number[0])
        [winning_side, my_side] = content.split('|')
        winning_numbers = re.findall(r'\d+', winning_side)
        my_numbers = re.findall(r'\d+', my_side)
        matching_numbers = list(set(my_numbers).intersection(winning_numbers))
        number_of_matches = len(matching_numbers)
        number_of_copies = dict_card_ncopies[my_card_number]
        for n in range(0, number_of_copies):    # for each copy
            my_scratchcards += 1
            for w in range(1,number_of_matches+1):
                if w <= max_card_number:
                    dict_card_ncopies[my_card_number+w] += 1        # win more
print(my_scratchcards)    
            

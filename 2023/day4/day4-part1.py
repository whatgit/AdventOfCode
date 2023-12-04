import re


my_point = 0
with open('input.txt') as input:
    for line in input:
        [card_number, content] = line.split(':')
        [winning_side, my_side] = content.split('|')
        winning_numbers = re.findall(r'\d+', winning_side)
        my_numbers = re.findall(r'\d+', my_side)
        matching_numbers = list(set(my_numbers).intersection(winning_numbers))
        card_point = 0
        if matching_numbers:
            for n in matching_numbers:
                if card_point == 0:
                    card_point = 1
                else:
                    card_point += card_point
        my_point += card_point
print(my_point)    
            

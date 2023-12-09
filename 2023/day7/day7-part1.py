import re
import pandas as pd
from enum import Enum
import math


# Five of a kind = 600
# Four of a kind = 500
# Fullhouse = 400
# Three of a kind = 300
# Two pairs = 200
# One pair = 100
# High card = 0
class Hands(Enum):
    FIVE_OF_A_KIND = 600
    FOUR_OF_A_KIND = 500
    FULL_HOUSE = 400
    THREE_OF_A_KIND = 300
    TWO_PAIRS = 200
    ONE_PAIR = 100
    HIGH_CARD = 0

# A = 14 -> 2 = 2
card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2 
}

col_names = ['c1', 'c2', 'c3', 'c4', 'c5']


def evaluate_hand(hand):
    hand_val = 0
    sets = set((hand.count(c), c) for c in hand)
    for s in sets:
        if s[0] == 5:
            hand_val += Hands.FIVE_OF_A_KIND.value
        elif s[0] == 4:
            hand_val += Hands.FOUR_OF_A_KIND.value
        elif s[0] == 3:
            hand_val += Hands.THREE_OF_A_KIND.value
        elif s[0] == 2:
            hand_val += Hands.ONE_PAIR.value
        else:
            hand_val += Hands.HIGH_CARD.value
    return hand_val


def tiebreak(df, dup, rank, col_name):
    grouped = dup.groupby(col_name)
    broken = True
    i = 0
    for name, group in grouped:
        if len(group) == 1:
            ind = group.index.values[0]
            df.at[ind, 'set_rank'] = rank + float(i)
            i += 1
        else:
            group.set_rank =  rank + float(i)
            i += 1
            broken = False
    return broken


def tiebreaker(data_frame):
    duplicated_data = data_frame[data_frame.duplicated(subset=['set_rank'], keep=False)]
    if duplicated_data.empty:
        # no duplicate
        return False
    duplicated_rank = duplicated_data[duplicated_data.duplicated(subset=['set_rank'])]['set_rank'].values
    # print(duplicated_data)
    for r in duplicated_rank:
        # get all df with this rank
        duplicate = duplicated_data.loc[duplicated_data['set_rank'] == r]
        i = 0
        grouped_c1 = duplicate.groupby('c1')
        for name, group in grouped_c1:
            if len(group) == 1:
                ind = group.index.values[0]
                df.at[ind, 'set_rank'] = r + float(i)
                i += 1
            else:
                grouped_c2 = group.groupby('c2')
                for name, group in grouped_c2:
                    if len(group) == 1:
                        ind = group.index.values[0]
                        df.at[ind, 'set_rank'] = r + float(i)
                        i += 1
                    else:
                        grouped_c3 = group.groupby('c3')
                        for name, group in grouped_c3:
                            if len(group) == 1:
                                ind = group.index.values[0]
                                df.at[ind, 'set_rank'] = r + float(i)
                                i += 1
                            else:
                                grouped_c4 = group.groupby('c4')
                                for name, group in grouped_c4:
                                    if len(group) == 1:
                                        ind = group.index.values[0]
                                        df.at[ind, 'set_rank'] = r + float(i)
                                        i += 1
                                    else:
                                        grouped_c5 = group.groupby('c5')
                                        for name, group in grouped_c5:
                                            if len(group) == 1:
                                                ind = group.index.values[0]
                                                df.at[ind, 'set_rank'] = r + float(i)
                                                i += 1
                                            else:
                                                print("cannot tie break!")


df = pd.DataFrame(columns=['hand', 'bet', 'value', 'c1', 'c2', 'c3', 'c4', 'c5'])
with open('input.txt') as input_file:
    for line in input_file:
        [hand, bet] = re.findall(r'\w+', line)
        c = []
        for card in hand:
            c.append(int(card_values[card]))
        bet = int(bet)
        df.loc[len(df.index)] = [hand, bet, evaluate_hand(hand), c[0], c[1], c[2], c[3], c[4]]
input_file.close()
df['set_rank'] = df['value'].rank(method='min')
# Tiebreakerssss
tiebreaker(df)
df['winning'] = df.bet * df.set_rank
print(df.winning.sum(axis=0))

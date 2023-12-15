import re


def reindeer_hash(word):
    value = 0
    for letter in word:
        value = value + (ord(letter))
        value = value * 17
        value = value % 256
    return value


final_value = 0
with open('input.txt') as input_file:
    line = input_file.readline()
    for h in re.finditer(r'[^,\n]+', line): # find anything except comma and new line
        final_value += reindeer_hash(h.group(0))
input_file.close()
print(final_value)
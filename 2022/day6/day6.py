text = ""
comparison_block = 14
# Part 1 comparison block = 4
# Part 2 comparison block = 14

with open('input.txt') as inputs:
    for line in inputs:
        text += line
for index, c in enumerate(text):
    block = text[index:index+comparison_block]
    if len(block) == len(set(block)):
        print(index+comparison_block)
        break

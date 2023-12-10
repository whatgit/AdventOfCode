import re


map = {}
step_count = 0
my_pos = 'AAA'
destination = 'ZZZ'
with open('input.txt') as input_file:
    first_line = input_file.readline()
    my_steps = re.findall(r'\w', first_line)
    for line in input_file:
        row = re.findall(r'\w+', line)
        if row:
            map[row[0]] = (row[1], row[2])
input_file.close()
while my_pos != destination:
    for step in my_steps:
        if step == 'L':
            my_pos = map[my_pos][0]
        if step == 'R':
            my_pos = map[my_pos][1]
        step_count += 1
        if my_pos == destination:
            break
print(step_count)
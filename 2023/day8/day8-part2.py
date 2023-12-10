import re
import math


map = {}
step_count = 0
my_pos = []
step_counts = []
destination_reached = False
with open('input.txt') as input_file:
    first_line = input_file.readline()
    my_steps = re.findall(r'\w', first_line)
    for line in input_file:
        row = re.findall(r'\w+', line)
        if row:
            map[row[0]] = (row[1], row[2])
            if row[0][-1] == 'A':
                my_pos.append(row[0])
                print("Starting at ", row[0])
input_file.close()
for pos in my_pos:
    step_count = 0
    while(not destination_reached):
        for step in my_steps:
            z = 0
            if step_count == 0:
                new_pos = pos
            if step == 'L':
                # print("Moving from ", my_pos[my_pos.index(pos)], " to ", map[pos][0])
                my_pos[my_pos.index(new_pos)] = map[new_pos][0]
                new_pos = map[new_pos][0]
            if step == 'R':
                # print("Moving from ", my_pos[my_pos.index(pos)], " to ", map[pos][1])
                my_pos[my_pos.index(new_pos)] = map[new_pos][1]
                new_pos = map[new_pos][1]
            if my_pos[my_pos.index(new_pos)][-1] == 'Z':
                # print("My destination ends with Z")
                z += 1
            step_count += 1
            if z == 1:
                destination_reached = True
                break
    step_counts.append(step_count)
    destination_reached = False
print('---------')
print(step_counts)
print("Step required ", math.lcm(*step_counts))
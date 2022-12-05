current_sum = 0
largest_sum = 0
with open('input.txt') as input:
    for line in input:
        if line.strip():
            current_sum = current_sum + int(line)
        else:
            if current_sum > largest_sum:
                largest_sum = current_sum
            current_sum = 0
print(largest_sum)

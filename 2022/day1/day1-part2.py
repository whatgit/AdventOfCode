current_sum = 0
all_sums = []


def get_sum_top_i(array, i):
    array_sum = 0
    if i <= len(array):
        for j in range(i):
            array_sum = array_sum + array[j]
        return array_sum
    else:
        print('i is larger than array size')
        return None


with open('input.txt') as input:
    for line in input:
        if line.strip():
            current_sum = current_sum + int(line)
        else:
            all_sums.append(current_sum)
            current_sum = 0
all_sums.sort(reverse=True)
print(get_sum_top_i(all_sums, 3))

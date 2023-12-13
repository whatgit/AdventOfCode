import re


def is_reflect_row(arr):
    row = []
    reflections = []
    for r, a in enumerate(arr):
        if not row:
            row = a
        else:
            if a == row:
                reflections.append(r)
            row = a
    reflect_row = False
    reflection_row = 0
    for ref in reflections:
        # check other rows
        # print("Potential a reflection at row ", reflection_row)
        reflect_row = True
        up = ref - 1
        down = ref
        for i in range(len(arr)):
            a = up - i
            b = down + i
            if a >= 0 and b < len(arr):
                if arr[a] != arr[b]:
                    reflect_row = False
        if reflect_row:
            reflection_row = ref
    if reflection_row:
        return True, reflection_row
    else:
        return False, 0
    

def is_reflect_row_greedy(arr, original):
    row = []
    reflections = []
    for r, a in enumerate(arr):
        if not row:
            row = a
        else:
            if a == row:
                reflections.append(r)
            row = a
    reflect_row = False
    reflection_row = 0
    for ref in reflections:
        # check other rows
        # print("Potential a reflection at row ", reflection_row)
        reflect_row = True
        up = ref - 1
        down = ref
        for i in range(len(arr)):
            a = up - i
            b = down + i
            if a >= 0 and b < len(arr):
                if arr[a] != arr[b]:
                    reflect_row = False
        if reflect_row and ref != original:
            reflection_row = ref
    if reflection_row:
        return True, reflection_row
    else:
        return False, 0


def is_reflect_column(arr):
    # transpose it and check for rows
    transpose = list(map(list, zip(*arr)))
    return is_reflect_row(transpose)


def is_reflect_column_greedy(arr, original):
    # transpose it and check for rows
    transpose = list(map(list, zip(*arr)))
    return is_reflect_row_greedy(transpose, original)


def flip(letter):
    if letter == '#':
        return '.'
    elif letter == '.':
        return '#'
    else:
        print("what is this letter?")


def find_reflection(arr):
    original_reflection_on_row, original_r = is_reflect_row(arr)
    original_reflection_on_column, original_c = is_reflect_column(arr)
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            arr[i][j] = flip(col)
            reflection_on_row, r = is_reflect_row_greedy(arr, original_r)
            if reflection_on_row:
                return r * 100
            reflection_on_column, c = is_reflect_column_greedy(arr, original_c)
            if reflection_on_column:
                return c
            arr[i][j] = col
    print("DID NOT FIND REFLECTION")
    if original_reflection_on_row:
        print("Original row is ", original_r)
    elif original_reflection_on_column:
        print("Original column is ", original_c)
    for a in arr:
        print(a)
    return 0
    

summary = 0
with open('input.txt') as input_file:
    chunk = []
    for line in input_file:
        symbols = re.findall(r'[^a-zA-z0-9\n]', line)
        if not symbols:
            # end of chunk; find reflections
            summary += find_reflection(chunk)
            chunk = []
        else:
            chunk.append(symbols)
input_file.close()
# end of chunk; find reflection for last chunk
summary += find_reflection(chunk)
print(summary)
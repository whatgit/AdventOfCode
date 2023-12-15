import re


def reindeer_hash(word):
    value = 0
    for letter in word:
        value = value + (ord(letter))
        value = value * 17
        value = value % 256
    return value


def get_focusing_power(b):
    value = 0
    for key in b:
        box_no = key + 1
        for slot, l in enumerate(b[key]):
            value += box_no * (slot + 1) * l[1]
    return value


final_value = 0
boxes = {x: [] for x in range(0, 256)}
with open('input.txt') as input_file:
    line = input_file.readline()
    for h in re.finditer(r'[^,\n]+', line): # find anything except comma and new line
        str = h.group(0)
        label = re.match(r'[a-zA-Z]+', str)
        box_no = reindeer_hash(label.group(0))
        label = label.group(0)
        opt = re.search(r'[^a-zA-Z0-9]+', str)
        if opt.group(0) == '=':
            focal_length = re.search(r'\d+', str)
            focal_length = int(focal_length.group(0))
            match_result = [item for item in boxes[box_no] if label in item]
            if match_result:
                # just update focal length
                for l in boxes[box_no]:
                    if l[0] == label:
                        l[1] = focal_length
            else:
                boxes[box_no].append([label, focal_length])
        else:
            match_result = [item for item in boxes[box_no] if label in item]
            if match_result:
                # remove the old lens
                for l in boxes[box_no]:
                    if l[0] == label:
                        boxes[box_no].remove(l)
input_file.close()
print(get_focusing_power(boxes))
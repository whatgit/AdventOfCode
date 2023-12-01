import re


def transform_letters_to_digit(digit):
    if digit == 'one':
        return '1'
    elif digit == 'two':
        return '2'
    elif digit == 'three':
        return '3'
    elif digit == 'four':
        return '4'
    elif digit == 'five':
        return '5'
    elif digit == 'six':
        return '6'
    elif digit == 'seven':
        return '7'
    elif digit == 'eight':
        return '8'
    elif digit == 'nine':
        return '9'
    else:
        return digit


calibration_value = 0
with open('input.txt') as input:
    for line in input:
        x = re.findall((r'\d|one|two|three|four|five|six|seven|eight|nine'), line)
        first_digit = transform_letters_to_digit(x[0])
        last_digit = transform_letters_to_digit(x[-1])
        calibration_value += int(first_digit + last_digit)
input.close()
print(calibration_value)

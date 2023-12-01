import re


calibration_value = 0
with open('input.txt') as input:
    for line in input:
        x = re.findall(r'\d', line)
        first_digit = x[0]
        last_digit = x[-1]
        calibration_value += int(first_digit + last_digit)
input.close()
print(calibration_value)

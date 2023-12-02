import re


min_red = 0
min_green = 0
min_blue = 0
sum_power_games = 0
with open('input.txt') as input:
    for line in input:
        [x, data] = line.split(':')
        games = data.split(';')
        for game in games:
            shows = game.split(',')
            for show in shows:
                [number, color] = re.findall(r'\w+', show)
                number = int(number)
                if color == 'red':
                    min_red = max(number, min_red)
                if color == 'green':
                    min_green = max(number, min_green)
                if color == 'blue':
                    min_blue = max(number, min_blue)
        power = min_red * min_green * min_blue
        min_red = min_blue = min_green = 0
        sum_power_games += power
input.close()
print(sum_power_games)

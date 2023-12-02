import re

max_red = 12
max_green = 13
max_blue = 14
sum_possible_games = 0
with open('input.txt') as input:
    for line in input:
        [x, data] = line.split(':')
        id = re.search(r'\d+', line)
        game_id = int(id[0])
        games = data.split(';')
        for game in games:
            shows = game.split(',')
            for show in shows:
                [number, color] = re.findall(r'\w+', show)
                if int(number) > max_red and color == 'red':
                    game_id = 0
                if int(number) > max_green and color == 'green':
                    game_id = 0
                if int(number) > max_blue and color == 'blue':
                    game_id = 0
        sum_possible_games += game_id
input.close()
print(sum_possible_games)

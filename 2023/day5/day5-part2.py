import re
import pandas as pd
import itertools


def update_map(df, origin, destination, the_map):
    destination_range_start = int(the_map[0])
    source_range_start = int(the_map[1])
    n = int(the_map[2])
    source_range_stop = source_range_start + n
    destination_range_stop = destination_range_start + n
    source_range = range(source_range_start, source_range_stop)
    destination_range = range(destination_range_start, destination_range_stop)
    if list(set(df[origin].values).intersection(source_range)):
        common_values = list(set(df[origin].values).intersection(source_range))
        for value in common_values:
            index = df.loc[df[origin] == value].index.values[0]
            df.at[index, destination] = destination_range[source_range.index(value)]
    return df

result = 0
origin = ""
destination = ""
seed_map = pd.DataFrame(columns=['seed'])
with open('input.txt') as input:
    min_location_array = []
    first_line = input.readline()
    [x, seed_number] = first_line.split(':')
    my_actual_seed = []
    my_seed_number = re.findall(r'\d+', seed_number)
    # by default it is the same destination
    my_seed_number = [int(i) for i in my_seed_number]
    actual_seed = itertools.batched(my_seed_number, 2)
    i = 0
    for start_seed, n in actual_seed:
        print("Constructing seed set # ", i)
        i+=1
        sn = range(start_seed, start_seed + n)
        df_sn = pd.DataFrame({'seed': sn})
        seed_map = pd.concat([seed_map, df_sn], ignore_index=True)
        print("Finish constructing seed")
    for line in input:
        if "to" in line:
            #update origin and destination
            map_desc = re.findall(r'\w+', line)
            origin = map_desc[0]
            destination = map_desc[2]
            if destination == 'soil':
                print("seed-to-soil ")
                seed_map = seed_map.assign(soil=lambda x: x.seed)
            elif destination == 'fertilizer':
                print("soil-to-fertilizer")
                seed_map = seed_map.assign(fertilizer=lambda x: x.soil)
            elif destination == 'water':
                print("fertilizer-to-water")
                seed_map = seed_map.assign(water=lambda x: x.fertilizer)
            elif destination == 'light':
                print("water-to-light")
                seed_map = seed_map.assign(light=lambda x: x.water)
            elif destination == 'temperature':
                print("light-to-temperature")
                seed_map = seed_map.assign(temperature=lambda x: x.light)
            elif destination == 'humidity':
                print("temperature-to-humidity")
                seed_map = seed_map.assign(humidity=lambda x: x.temperature)
            elif destination == 'location':
                print("humidity-to-location")
                seed_map = seed_map.assign(location=lambda x: x.humidity)
        else:
            new_map = re.findall(r'\d+', line)
            if new_map:
                seed_map = update_map(seed_map, origin, destination, new_map)
    print(seed_map)
    print(min(seed_map['location'].values))
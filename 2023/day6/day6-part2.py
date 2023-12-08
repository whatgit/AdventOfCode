import re


def ways_of_winning(time, record):
    time_array = range(1,time)
    wow = 0
    for acc in time_array:
        s = acc * (time - acc)
        if s > record:
            wow += 1
    return wow


with open('input.txt') as input:
    timeline = input.readline()
    times = re.findall(r'\d+', timeline)
    longtime = ""
    for time in times:
        longtime += time
    longtime = int(longtime)
    longdistance = ""
    distanceline = input.readline()
    distances = re.findall(r'\d+', distanceline)
    for distance in distances:
        longdistance += distance
    longdistance = int(longdistance)
    print("Time is ", longtime, " with record ", longdistance)
    print(ways_of_winning(longtime, longdistance))
input.close()
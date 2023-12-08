import re


def ways_of_winning(time, record):
    time_array = range(1,int(time))
    wow = 0
    for acc in time_array:
        s = acc * (int(time) - acc)
        if s > int(record):
            wow += 1
    return wow



total_way = 1
with open('input.txt') as input:
    timeline = input.readline()
    time = re.findall(r'\d+', timeline)
    distanceline = input.readline()
    distance = re.findall(r'\d+', distanceline)
    for t, d in zip(time, distance):
        print("Time is ", t, " with record ", d)
        print(ways_of_winning(t, d))
        total_way *= ways_of_winning(t,d)
input.close()    
print(total_way)
import re
from enum import Enum
import numpy as np
import shapely


class MapSign(Enum):
    VPIPE = ('N', 'S')
    HPIPE = ('E', 'W')
    LPIPE = ('N', 'E')
    JPIPE = ('N', 'W')
    ZPIPE = ('S', 'W') # Z = 7 because Python
    FPIPE = ('S', 'E')
    DOT = ('X', 'X')
    START = []
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


def available_directions(i, j):
    # assuming pos is a 2D-array
    my_connection = function_map[i][j]
    direction = []
    if i != 0:
        if 'S' in function_map[i - 1][j] and 'N' in my_connection:   # is the one above me connected to South?
            direction.append('N')   # then we can go North
    if i + 1 != len(map):
        if 'N' in function_map[i + 1][j] and 'S' in my_connection:   # is the one below me connected to North?
            direction.append('S')   # then we can go South
    if j != 0:
        if 'E' in function_map[i][j - 1] and 'W' in my_connection:   # is the one on my left connected to East?
            direction.append('W')   # then we can go West
    if j + 1 != len(map[0]):
        if 'W' in function_map[i][j + 1] and 'E' in my_connection:   # is the one on my right connected to West?
            direction.append('E')   # then we can go East
    return direction


def first_available_directions(i, j):
    # assuming pos is a 2D-array
    direction = []
    if 'S' in function_map[i - 1][j]:   # is the one above me connected to South?
        direction.append('N')   # then we can go North
    if 'N' in function_map[i + 1][j]:   # is the one below me connected to North?
        direction.append('S')   # then we can go South
    if 'E' in function_map[i][j - 1]:   # is the one on my left connected to East?
        direction.append('W')   # then we can go West
    if 'W' in function_map[i][j + 1]:   # is the one on my right connected to West?
        direction.append('E')   # then we can go East
    return direction


def move_in_pipe(pos, previous_steps):
    choice = available_directions(pos[0], pos[1])
    for c in choice:
        newpos1 = move_pos(pos, c, previous_steps)
        if newpos1 is not None:
            break
    return newpos1


def move_pos(origin, direction, previous_steps):
    if direction == 'S':
        destination = [origin[0] + 1, origin[1]]
    elif direction == 'W':
        destination = [origin[0], origin[1] - 1]
    elif direction == 'N':
        destination = [origin[0] - 1, origin[1]]
    elif direction == 'E':
        destination = [origin[0], origin[1] + 1]
    if destination not in previous_steps:
        return destination
    else:
        return None
    

def get_starting_shape(choice):
    if tuple(choice) == MapSign.VPIPE.value:
        return MapSign.VPIPE.value
    elif tuple(choice) == MapSign.HPIPE.value:
        return MapSign.HPIPE.value
    elif tuple(choice) == MapSign.LPIPE.value:
        return MapSign.LPIPE.value
    elif tuple(choice) == MapSign.JPIPE.value:  
         return MapSign.JPIPE.value
    elif tuple(choice) == MapSign.ZPIPE.value:
         return MapSign.ZPIPE.value
    elif tuple(choice) == MapSign.FPIPE.value:
        return MapSign.FPIPE.value
    else:
        print("Cannot determine start pos")


def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))


map = []
function_map = []
starting_pos = None
my_pos = None
with open('p2_ex1.txt') as input_file:
    row = 0
    for line in input_file:
        function_array = []
        symbols = re.findall(r'[-LJ7F.S\|]', line)
        for s in symbols:
            if s == '|':
                function_array.append(MapSign.VPIPE.value)
            elif s == '-':
                function_array.append(MapSign.HPIPE.value)
            elif s == 'L':
                function_array.append(MapSign.LPIPE.value)
            elif s == 'J':
                function_array.append(MapSign.JPIPE.value)
            elif s == '7':
                function_array.append(MapSign.ZPIPE.value)
            elif s == 'F':
                function_array.append(MapSign.FPIPE.value)
            elif s == '.':
                function_array.append(MapSign.DOT.value)
            elif s == 'S':
                function_array.append(MapSign.START.value)
            else:
                print(s, "IS NOT A SYMBOL?")
        if 'S' in symbols:
            starting_pos = (row, symbols.index('S'))
            print("Found a starting point at (", row, ", ", symbols.index('S'), ")")
        map.append(symbols)
        function_map.append(function_array)
        row += 1
    # for line in map:
    #   print(line)
    if starting_pos:
        my_pos = [starting_pos[0], starting_pos[1]]
        choices = first_available_directions(my_pos[0], my_pos[1])
        function_map[my_pos[0]][my_pos[1]] = get_starting_shape(choices)
    else:
        print("No starting position (S)")
    same_pos = False
    newpos = move_pos(my_pos, choices[0], my_pos)
    last_pos = move_pos(my_pos, choices[1], my_pos)
    my_pos = [my_pos]
    my_pos.append(newpos)
    while not same_pos:
        newpos = move_in_pipe(newpos, my_pos)
        my_pos.append(newpos)
        if newpos == last_pos:
            same_pos = True
input_file.close()
print(my_pos)
my_pos = [[5, 1], [6, 1], [7, 1], [7, 2], [7, 3], [7, 4], [6, 4], [5, 4], [5, 3], [5, 2]]
my_pos = [[5, 1], [6, 1], [7, 1], [7, 2], [7, 3], [7, 4], [6, 4], [5, 4], [5, 3], [5, 2]]
the_x = [item[0] for item in my_pos]
the_y = [item[1] for item in my_pos]
print(the_x)
print(the_y)
print(PolyArea(the_x, the_y))
pgon = shapely.Polygon(zip(the_x, the_y)) # Assuming the OP's x,y coordinates
print('------')
print(pgon.area)
print(shapely.minimum_clearance(pgon))
for c in pgon.interiors:
    print(c)
from pprint import pprint
from itertools import product as prod
import numpy as np
test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

data = test.split('\n')

# with open('./data/day_11.txt') as fd:
#     data = fd.read().split('\n')

Nx = len(data[0])
Ny = len(data)

def adjacents(state, place):
    x, y = place
    adj = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
           (x + 1, y), (x - 1, y),
           (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    adj = [p for p in adj if p[0] >= 0 and p[0] < len(state)]
    adj = [p for p in adj if p[1] >= 0 and p[1] < len(state[0])]
    adj = [state[r][s] for r, s in adj if state[r][s] != '.']
    return adj


def check_line(state, place, increment):
    x0, y0 = place
    inc_x, inc_y = increment
    if inc_x == 0:
        for col in state[x0][y0::inc_x]:
            if col in ['L', '#']:
                return col
    elif inc_y == 0:
        for row in state[x0::inc_x][y0]:
            if row in ['L', '#']:
                return row
    else:
        for elem in [state[x0+(inc_x)*i][y0+(inc_y)*i] for i in range(max(Nx-x0, Ny-y0))]:
            if elem in ['L', '#']:
                return elem


def adjacents1(state, place):
    x, y = place
    max_x, max_y = len(state), len(state[0])
    sides = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]
    adj = [check_line(state, place, side) for side in sides]
    return adj


def is_empty(state, place):
    if state[place[0]][place[1]] == 'L' and set(adjacents1(state, place)).intersection({'L'}) == {'L'}:
        return True
    else:
        return False


def is_occupied(state, place):
    if state[place[0]][place[1]] == '#' and adjacents1(state, place).count('#') >= 5:
        return True
    else:
        return False


def round(state):
    new_state = ['' for _ in range(len(state))]
    for i, row in enumerate(state):
        for j, seat in enumerate(row):
            if is_empty(state, (i, j)):
                new_state[i] += '#'
            elif is_occupied(state, (i, j)):
                new_state[i] += 'L'
            else:
                new_state[i] += seat

    return new_state


for i in range(200):
    print(f"Round {i}")
    new_data = round(data)
    if new_data == data:
        print(f"Round {i}")
        print('Break!')
        print(''.join(data).count('#'))
        break
    data = new_data[:]

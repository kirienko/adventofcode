with open('./data/data_12.txt') as fd:
    data = fd.read().split('\n')

dirs = ('E', 'S', 'W', 'N')

# logs for both tasks:
log1 = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
log2 = {'E': 0, 'S': 0, 'W': 0, 'N': 0}

course = 0  # used in the Task 1
waypoint = {'E': 10, 'S': 0, 'W': 0, 'N': 1}    # used in the Task 2

turns = {'R': 1, 'L': -1}

for command in data:
    c, num = command[0], int(command[1:])
    if c in turns:
        # all numbers are in fact multiples of 90
        turn = (turns[c] * int(num/90)) % 4
        course = (course + turn) % 4    # new course
        # rotate waypoint
        k, v = list(waypoint.keys()), waypoint.values()
        k = k[turn:] + k[:turn]
        waypoint = dict(zip(k, v))
    elif c == 'F':
        log1[dirs[course]] += num
        for k, v in waypoint.items():
            log2[k] += v * num
    else:
        log1[c] += num
        waypoint[c] += num


def dist(l):
    return abs(l['E'] - l['W']) + abs(l['N'] - l['S'])


print(f"Answer 1: {dist(log1)}")
print(f"Answer 2: {dist(log2)}")

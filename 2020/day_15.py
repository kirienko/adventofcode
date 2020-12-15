from collections import deque, OrderedDict

puzzle = [0, 3, 6]  # Answer 1: 436, answer 2: 175594
puzzle = [7, 12, 1, 0, 16, 2]  # Answer 1: 410, Answer 2: 238


class OrderedDefaultdict(OrderedDict):
    def __missing__(self, key):
        ret = self[key] = deque([], maxlen=2)
        return ret


puzzle = [-1] + puzzle  # to start counting from ONE

for i, max_turn in enumerate((2020, 30000000)):
    data = OrderedDefaultdict(zip(puzzle, (deque([i], maxlen=2) for i in range(len(puzzle)))))
    for turn in range(len(data), max_turn + 1):
        last, dq = data.popitem()
        if len(dq) == 1:
            data[last] = dq
            data[0].append(turn)
            data.move_to_end(0)
        else:
            data[last] = dq
            spoken = dq[1] - dq[0]
            data[spoken].append(turn)
            data.move_to_end(spoken)

    print(f"Answer {i+1}: {data.popitem()[0]}")

with open('./data/day_04.txt') as fd:
    raw = fd.read().strip().split('\n\n')

calls = list(map(int, raw[0].split(',')))
boards = []

for board in raw[1:]:
    board = [list(map(int, x.split())) for x in board.split('\n')]
    for line in board:
        boards += [frozenset(line)]
    for col in range(len(line)):
        boards += [frozenset(line[col] for line in board)]

called = set(calls[:5])     # the first 5 numbers are called already
win_five, win_boards, win_nums = None, [], []

for i in range(5, len(calls)):
    called.add(calls[i])
    for j, b in enumerate(boards):
        board_number = j // 10
        if board_number in win_boards:  # don't recheck boards that won already
            continue
        if called.intersection(b) == b:
            win_five = b
            win_num = calls[i]
            print(f"Eureka: {b}, winning number: {win_num}")
            print(f"Board number: {board_number}")
            if board_number not in win_boards:
                win_boards += [board_number]
                win_nums += [win_num]

print(f"All winning boards: {list(zip(win_boards, win_nums))}")
for j, b in enumerate([win_boards[0], win_boards[-1]]):
    win_board = set().union(*[set(map(int, x.split())) for x in raw[b + 1].split('\n')])
    print(f"\n\nWinning board: \n{raw[b + 1]}")
    i = calls.index(win_nums[-j])
    print(f"Marked numbers: {win_board.intersection(set(calls[:i + 1]))}, {len(win_board.intersection(set(calls[:i + 1])))}")
    print(f"Unmarked numbers: {win_board.difference(set(calls[:i + 1]))}, {len(win_board.difference(set(calls[:i + 1])))}")
    score = sum(win_board.difference(set(calls[:i + 1])))
    print(f"Answer : {score * win_nums[-j]}")

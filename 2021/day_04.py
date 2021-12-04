with open('./data/day_04.txt') as fd:
    raw = fd.read().strip().split('\n\n')
test = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

# raw = test.strip().split('\n\n')
input = list(map(int, raw[0].split(',')))
boards = []

for board in raw[1:]:
    board = [list(map(int, x.split())) for x in board.split('\n')]
    for line in board:
        boards += [frozenset(line)]
    for col in range(len(line)):
        boards += [frozenset(line[col] for line in board)]

called = set(input[:5])
win_five, win_boards, win_nums = None, [], []

for i in range(5, len(input)):
    called.add(input[i])
    for b in boards:
        if called.intersection(b) == b:
            win_five = b
            win_num = input[i]
            print(f"Eureka: {b}, winning number: {win_num}")
            break
    if win_five:
        board_number = boards.index(win_five) // 10
        print(f"Board number: {board_number}")
        if board_number not in win_boards:
            win_boards += [board_number]
            win_nums += [win_num]
        break
        # continue

print(f"win boards: {win_boards}")
print(f"win nums: {win_nums}")
win_board = set().union(*[set(map(int, x.split())) for x in raw[win_boards[0] + 1].split('\n')])
print(f"Winning board: \n{raw[win_boards[0] + 1]}")
print(win_board)
print(f"Winning numbers: ")
print(set(input[:i+1]))
print(f"Marked numbers: {win_board.intersection(set(input[:i+1]))}, {len(win_board.intersection(set(input[:i+1])))}")
print(f"Unmarked numbers: {win_board.difference(set(input[:i+1]))}, {len(win_board.difference(set(input[:i+1])))}")
score = sum(win_board.difference(set(input[:i+1])))
print(f"Answer 1: {score * win_num}")

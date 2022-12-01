with open('./data/day_10.txt') as fd:
    data = fd.read().split()

score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
match = {'(': ')', '[': ']', '{': '}', '<': '>'}
score = 0
incomplete = []
for line in data:
    """ https://codereview.stackexchange.com/a/180569 """
    chunk = []
    for s in line:
        if s in match:
            chunk += [match[s]]
        else:
            if s not in chunk or s != chunk.pop():
                score += score_table[s]
                chunk = None
                break
    if chunk:
        incomplete += [''.join(chunk[::-1])]

print(f"Answer 1: {score}")

score_table = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in incomplete:
    score = 0
    for s in line:
        score *= 5
        score += score_table[s]
    scores += [score]

print(f"Answer 2: {sorted(scores)[len(scores) // 2]}")

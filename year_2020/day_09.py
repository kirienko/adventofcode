from itertools import combinations as comb

with open('./data/day_09.txt') as fd:
    inp = fd.read()

data = list(map(int, inp.split('\n')))

offset = 25

for i, n in enumerate(data[offset:]):
    if n not in {x + y for x, y in comb(data[i:i+offset], 2)}:
        clue = n
        print(f"Answer 1: {clue}")
        break

ans = None
for j in range(2, 20):
    if ans: break
    for i, n in enumerate(data):
        test = sum(data[i:i+j])
        if test == clue:
            ans = sorted(data[i:i+j])
            print(f"Answer 2: {ans[0] + ans[-1]}")
            break

def place_id(code):
    row = int(code[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(code[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col


assert place_id('BFFFBBFRRR') == 567
assert place_id('FFFBBBFRRR') == 119
assert place_id('BBFFBBFRLL') == 820

with open('./data/day_05.txt') as fd:
    data = fd.read().split('\n')

print(f"Answer 1: {max(map(place_id, data))}")

passengers = sorted(map(place_id, data))
first = passengers[0]
for i, l in enumerate(passengers):
    if l != i + first:
        print(f"Answer 2: {i + first}")
        break

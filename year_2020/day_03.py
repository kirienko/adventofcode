from numpy import prod

with open('data/day_03.txt') as fd:
    tile = fd.readlines()

counters = [0, 0, 0, 0, 0]
slopes = [1, 3, 5, 7]

width, height = len(tile[0]), len(tile)
n = int(height * max(slopes) / width) * 2
for i in range(height):
    tile[i] = tile[i].strip() * n

for s, slope in enumerate(slopes):
    for i, line in enumerate(tile):
        loc = i * slope
        if line[loc] == '#':
            counters[s] += 1

for i, line in enumerate(tile[::2]):
    loc = i
    if line[loc] == '#':
        counters[-1] += 1

print(f"1) answer = {counters[1]}")
print(f"2) answer = {' × '.join(map(str, counters))} = {prod(counters)}")

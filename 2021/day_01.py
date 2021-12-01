with open('./data/day_01.txt') as fd:
    data = list(map(int, fd.readlines()))

# Part 1:
res1, res2 = 0, 0
for i in range(1, len(data)):
    if data[i] - data[i - 1] > 0:
        res1 += 1
print(f"Answer 1: {res1}")

# Part 2:
for i in range(3, len(data)):
    if sum(data[i - 2:i + 1]) - sum(data[i - 3: i]) > 0:
        res2 += 1
print(f"Answer 2: {res2}")

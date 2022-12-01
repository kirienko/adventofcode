with open('./data/day_02.txt') as fd:
    raw = fd.read()

data = raw.strip().split('\n')
pos, depth1, depth2, aim = 0, 0, 0, 0

for line in data:
    comm, value = line.split()
    value = int(value)
    if comm == "down":
        depth1 += value
        aim += value
    elif comm == "up":
        depth1 -= value
        aim -= value
    else:
        pos += value
        depth2 += aim * value

print(f"Answer 1: {pos * depth1}")
print(f"Answer 2: {pos * depth2}")

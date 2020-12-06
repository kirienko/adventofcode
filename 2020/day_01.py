with open('./data/day_01.txt') as fd:
    l = list(map(int, fd.readlines()))

for i, x in enumerate(sorted(l)):
    for j, y in enumerate(l[i:]):
        if x + y == 2020:
            print(x * y)
            break

with open('./data/day_18.txt') as fd:
    data = [eval(f.strip()) for f in fd.readlines()]

print(len(data))
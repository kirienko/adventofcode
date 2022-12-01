with open('./data/day_06.txt') as fd:
    data = fd.read().split('\n\n')

print(sum([len(set(x.replace('\n', ''))) for x in data]))
# looks a bit creepy, I admit :(
print(sum([len(set.intersection(*map(set, x.split('\n')))) for x in data]))

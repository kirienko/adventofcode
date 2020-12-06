with open('./data/day_06.txt') as fd:
    test_data = fd.read().split('\n\n')

print(sum([len(set(x.replace('\n', ''))) for x in test_data]))
# looks a bit creepy, I admit :(
print(sum([len(set.intersection(*map(set, x.split('\n')))) for x in test_data]))

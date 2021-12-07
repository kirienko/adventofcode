from collections import Counter

with open('./data/day_07.txt') as fd:
    mass = Counter(list(map(int, fd.read().split(','))))

print(f"Answer 1: {min([sum([abs(k - r) * v for k, v in mass.items()]) for r in range(0, max(mass))])}")
print(f"Answer 2: {min([sum([sum(range(abs(k - r)+1)) * v for k, v in mass.items()]) for r in range(0, max(mass))])}")

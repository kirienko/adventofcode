from collections import Counter
with open('./data/day_14.txt') as fd:
    pattern, elements = fd.read().split('\n\n')

pairs = Counter()   # all pairs in the input
for k in range(len(pattern) - 1):
    pairs[pattern[k:k+2]] += 1
elements = dict(e.split(' -> ') for e in elements.split('\n'))


def polymerize(elems: Counter, n: int):
    for _ in range(n):
        new_elements = Counter()
        for p, v in elems.items():  # every input pair produces two output pairs
            new_elements[p[0] + elements[p]] += v
            new_elements[elements[p]+p[1]] += v
        elems = new_elements

    counter = Counter()
    for k, v in elems.items():
        counter[k[0]] += v
        counter[k[1]] += v
    counter[pattern[0]] += 1    # we count all elements twice, apart from the first and the last ones, here we fix it
    counter[pattern[-1]] += 1   # we count all elements twice, apart from the first and the last ones, here we fix it
    counter = {k: int(v/2) for k, v in counter.items()}     # fix double counts
    counter = dict(sorted(counter.items(), key=lambda items: items[1]))
    least, most = [v for k, v in enumerate(counter.values()) if k in (0, len(counter) - 1)]
    return most - least


print(f"Answer 1: {polymerize(pairs, 10)}")
print(f"Answer 2: {polymerize(pairs, 40)}")

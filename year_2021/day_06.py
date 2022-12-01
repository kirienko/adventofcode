from collections import Counter

with open('./data/day_06.txt') as fd:
    data = list(map(int, fd.read().strip().split(',')))


def fib(inp, n: int) -> int:
    init = Counter(inp)
    elems = [init[i] for i in range(9)]
    for _ in range(n):
        zeros, elems = elems[0], elems[1:]
        elems[6] += zeros
        elems.append(zeros)
    return sum(elems)


print(f"Answer 1: {fib(data, 80)}")
print(f"Answer 2: {fib(data, 256)}")

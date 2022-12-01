with open('./data/day_08.txt') as fd:
    raw = fd.read().split('\n')

# Part 1
known_numbers = {2: 1, 4: 4, 3: 7, 7: 8}  # {<number of digits>: <the number itself>}

ans1 = 0
for line in raw:
    res = line.split('|')[1].split()
    ans1 += len([known_numbers[x] for x in map(len, res) if x in known_numbers])
print(f"Answer 1: {ans1}")


# Part 2
def get_num(line: str) -> dict:
    ciphers = line.split()
    known_numbers = {2: 1, 4: 4, 3: 7, 7: 8}    # {<number of digits>: <the number itself>}
    output = {frozenset(elem): known_numbers[len(elem)] for elem in ciphers if len(elem) in known_numbers}
    numbers = {v: k for k, v in output.items()}     # reverse to the `output`: {<the number itself>: <set of letters>}
    for elem in ciphers:
        se = set(elem)
        if len(elem) == 5:
            if len(se.intersection(numbers[4])) == 2:
                output[frozenset(elem)] = 2
            elif se.intersection(numbers[1]) == numbers[1]:
                output[frozenset(elem)] = 3
            else:
                output[frozenset(elem)] = 5
        elif len(elem) == 6:
            if len(se.intersection(numbers[1])) == 1:
                output[frozenset(elem)] = 6
            elif se.intersection(numbers[4]) == numbers[4]:
                output[frozenset(elem)] = 9
            else:
                output[frozenset(elem)] = 0
    return output


ans2 = 0
for line in raw:
    first, second = line.split('|')
    d = get_num(first)
    ans2 += int(''.join([str(d[frozenset(elem)]) for elem in second.split()]))
print(f"Answer 2: {ans2}")

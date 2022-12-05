def parse_input(text: str):
    part1, part2 = text.split('\n\n')
    # reverse:
    part1 = part1.split('\n')[::-1]
    num_crates = max(map(int, part1[0].split()))
    crates = ['' for _ in range(num_crates)]
    for line in part1[1:]:
        for n in range(num_crates):
            crates[n] += line[4 * n + 1]
    crates = [c.replace(' ', '') for c in crates]

    # take every odd element of each string line this:
    # `move 2 from 2 to 1`
    actions = tuple(tuple(map(int, x.split()[1::2])) for x in part2.strip().split('\n'))
    return crates, actions


def move_crates(crates, actions, model):
    """ the `model` is either "9000" (Part 1) or "9001" (Part 2) """
    if model == "9000":
        order = -1
    elif model == "9001":
        order = 1
    else:
        return

    for action in actions:
        # move NUM from C1 to C2
        num, c1, c2 = action
        c1, c2 = c1 - 1, c2 - 1
        crates[c2] += crates[c1][-num:][::order]
        crates[c1] = crates[c1][:-num]
    return ''.join([x[-1] for x in crates])


def task1(text: str) -> str:
    crates, actions = parse_input(text)
    return move_crates(crates, actions, "9000")


def task2(text: str) -> str:
    crates, actions = parse_input(text)
    return move_crates(crates, actions, "9001")


if __name__ == "__main__":
    with open('data/day_05.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

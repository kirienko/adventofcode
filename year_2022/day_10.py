def read(text: str) -> list:
    """ Reads the instruction and returns a list of values to add

    at the end of every cycle: [0, 0, 15, 0, -11, ...]
    """
    cycles = []
    for line in text.strip().split('\n'):
        if line.startswith('noop'):
            cycles += [0]
        else:
            cycles += [0, int(line.split()[1])]
    return cycles


def show(screen: str):
    assert len(screen) == 240
    print()
    for i in range(6):
        print(f"Cycle {40 * i + 1:> 4} ->", end=' ')
        for j in range(40):
            pos = i * 40 + j
            print(screen[pos], end='')
        print(f" <- Cycle {40 * (i + 1)}")


def task1(text: str) -> int:
    x, result = 1, 0
    cycles = read(text)
    for cycle, val in enumerate(cycles):
        if (cycle + 20 + 1) % 40 == 0:
            result += (cycle + 1) * x
        x += val
    return result


def task2(text: str) -> str:
    x, cycle = 1, 1
    sprite = [x-1, x, x+1]
    result = ''
    cycles = read(text)
    for i, val in enumerate(cycles):
        result += '#' if i % 40 in sprite else '.'
        x += val
        sprite = [x-1, x, x+1]
    show(result)
    return result


if __name__ == "__main__":
    with open('data/day_10.txt') as fd:
        data = fd.read()

    print(task1(data))
    task2(data)

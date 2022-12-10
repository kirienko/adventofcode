def read(text: str) -> list:
    program = []
    for line in text.strip().split('\n'):
        if line.startswith('noop'):
            program += [(1, 0)]
        else:
            program += [(2, int(line.split()[1]))]
    return program


def task1(text: str) -> int:
    x, cycle, result = 1, 1, 0
    program = read(text)
    # print()
    for i, line in enumerate(program):
        if (cycle + 20) % 40 == 0:
            # print(f"{i} (+20), {cycle=}: {line}: {x=}")
            result += cycle * x
        elif (cycle + 20) % 40 == 1 and program[i-1][0] == 2:
            # print(f"{i} (+19), cycle={cycle-1}: x={x - program[i-1][1]}")
            result += (cycle-1) * (x - program[i-1][1])

        cycle += line[0]
        x += line[1]

    return result


def task2(text: str) -> int:
    return 1


if __name__ == "__main__":
    with open('data/day_10.txt') as fd:
        data = fd.read()

    print(task1(data))
    # print(task2(data))

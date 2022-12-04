def get_ranges(text: str):
    for line in text.strip().split("\n"):
        s1, s2 = line.split(',')
        r11, r12 = map(int, s1.split('-'))
        r21, r22 = map(int, s2.split('-'))
        yield set(range(r11, r12 + 1)), set(range(r21, r22 + 1))


def task1(text: str) -> int:
    return sum(
            int(len(s1.intersection(s2)) == min(len(s1), len(s2)))
            for s1, s2 in get_ranges(text)
    )


def task2(text: str) -> int:
    return sum(1 for s1, s2 in get_ranges(text) if len(s1.intersection(s2)))


if __name__ == "__main__":
    with open('data/day_04.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

from string import ascii_letters as abc


def task1(text: str) -> int:
    result = 0
    for line in text.strip().split("\n"):
        l = int(len(line)/2)
        s1, s2 = set(line[:l]), set(line[l:])
        shared = s1.intersection(s2)
        result += abc.index(shared.pop()) + 1
    return result


def task2(text: str) -> int:
    result = 0
    elves = text.strip().split("\n")
    for g in range(int(len(elves)/3)):
        s1, s2, s3 = set(elves[3*g]), set(elves[3*g + 1]), set(elves[3*g + 2])
        shared = s1.intersection(s2).intersection(s3)
        result += abc.index(shared.pop()) + 1
    return result


if __name__ == "__main__":
    with open('data/day_03.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

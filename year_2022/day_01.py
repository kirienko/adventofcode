def get_calories_list(inp: str) -> list:
    elves = inp.strip().split('\n\n')
    return [sum([int(x) for x in e.split('\n')]) for i, e in enumerate(elves)]


def task1(calories: list) -> int:
    return max(calories)


def task2(calories: list) -> int:
    return sum(sorted(calories, reverse=True)[:3])


if __name__ == "__main__":
    with open('data/day_01.txt') as fd:
        data = fd.read()

    cals = get_calories_list(data)

    print(task1(cals))
    print(task2(cals))

def task_1(data: str):
    res = 0
    for line in data.strip().splitlines():
        winning, yours = line.split(': ')[1].split(' | ')
        winning = set(map(int, winning.split()))
        yours = set(map(int, yours.split()))
        res += 1 << (len(winning & yours) - 1) if winning & yours else 0
    return res


def task_2(data: str) -> int:
    cards = [1 for _ in range(len(data.strip().splitlines()))]
    for i, line in enumerate(data.strip().splitlines()):
        winning, yours = line.split(': ')[1].split(' | ')
        winning = set(map(int, winning.split()))
        yours = set(map(int, yours.split()))
        for j in range(len(winning & yours)):
            cards[i+j+1] += cards[i]
    return sum(cards)


if __name__ == '__main__':
    with open('data/data_04.txt') as fd:
        data = fd.read()
    print(task_1(data=data))    # 17803
    print(task_2(data=data))    # 5554894

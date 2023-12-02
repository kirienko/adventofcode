def parser(text: str) -> list[list[dict[str, int]]]:
    data = []
    for line in text.strip().splitlines():
        games = []
        for game in line.split(':')[1].strip().split(';'):
            d = {'red': 0, 'green': 0, 'blue': 0}
            for round in game.split(','):
                num, color = round.split()
                d[color.strip()] = int(num)
            games.append(d)
        data.append(games)

    return data


def task_1(test_data: str) -> int:
    score = set()
    valid_game = {'red': 12, 'green': 13, 'blue': 14}
    data = parser(test_data)
    for i, games in enumerate(data):
        okay = True
        for game in games:
            for color, value in game.items():
                if value > valid_game[color] :
                    okay = False
                    break
        if not okay: continue
        score.add(i+1)

    return sum(score)


def task_2(test_data: str) -> int:
    data = parser(test_data)
    score = 0
    for i, games in enumerate(data):
        minimum = {'blue': [], 'red': [], 'green': []}
        for game in games:
            for color, value in game.items():
                minimum[color] += [value]
        score += max(minimum['red']) * max(minimum['green']) * max(minimum['blue'])
    return score


if __name__ == '__main__':
    with open('./data/data_02.txt') as fd:
        data = fd.read()

    print(task_1(data))     # 2416
    print(task_2(data))     # 63307

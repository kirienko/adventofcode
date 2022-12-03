score = {'A': 1, 'B': 2, 'C': 3}

games = {'A A': 3, 'A B': 6, 'A C': 0,
         'B A': 0, 'B B': 3, 'B C': 6,
         'C A': 6, 'C B': 0, 'C C': 3,
         }


def process(scenario: str, mapping) -> int:
    """ Process all the games in a scenario

    according to the mapping of X, Y, and Z.
    """
    result = 0
    for game in scenario.strip().split('\n'):
        a, b = game.split()
        b = mapping(game)
        result += games[f"{a} {b}"]
        result += score[b]
    return result


def task1(scenario: str) -> int:
    def mapping_xyz(x: str) -> str:
        """ The result does not depend on what the opponent has chosen """
        return {'X': 'A', 'Y': 'B', 'Z': 'C'}[x.split()[1]]

    return process(scenario, mapping_xyz)


def task2(scenario: str) -> int:
    def mapping_xyz(x: str) -> str:
        """ X -> lose, Y -> draw, Z -> win """
        mapping = {'A X': 'C', 'B X': 'A', 'C X': 'B',
                   'A Y': 'A', 'B Y': 'B', 'C Y': 'C',
                   'A Z': 'B', 'B Z': 'C', 'C Z': 'A',
                   }

        return mapping[x]

    return process(scenario, mapping_xyz)


if __name__ == "__main__":
    with open('data/day_02.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

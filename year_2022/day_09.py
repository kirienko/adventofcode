import numpy as np


def parse_route(text: str) -> list:
    route = [line.split() for line in text.strip().split('\n')]
    return [(a, int(b)) for a, b in route]


def go(route: list, n: int = 2):
    """ Move the rope according to the route """
    move = {'R': np.array([1, 0]),
            'L': np.array([-1, 0]),
            'U': np.array([0, 1]),
            'D': np.array([0, -1])}

    tail = np.array([0, 0])
    rope = [np.array([0, 0]) for _ in range(n)]

    visited = set()
    for step in route:
        for _ in range(step[1]):
            # cycle for the number of repeats of the same move (like 'R 4')
            rope[0] += move[step[0]]

            for i in range(1, n):
                head = rope[i-1]
                tail = rope[i]
                if np.linalg.norm(head - tail) > 2:
                    # if "head" and "tail" are not adjacent, move strictly diagonal
                    tail[0] += 1 if tail[0] < head[0] else -1
                    tail[1] += 1 if tail[1] < head[1] else -1
                elif abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    if tail[0] != head[0]:
                        tail[0] += np.sign(head[0] - tail[0])
                    else:
                        tail[1] += np.sign(head[1] - tail[1])
            visited.add(tuple(tail))
    return len(visited)


def task1(text: str) -> int:
    return go(parse_route(text))


def task2(text: str) -> int:
    return go(parse_route(text), n=10)


if __name__ == "__main__":
    with open('data/day_09.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

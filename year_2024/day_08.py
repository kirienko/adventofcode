from collections import defaultdict

import numpy as np


def parse_input(text: str) -> tuple[int, defaultdict]:
    result = defaultdict(list)
    lines = text.strip().split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                result[char].append(np.array((x, y)))
    return len(lines), result

def antinodes_number(size: int, nodes: defaultdict) -> int:
    antinodes = set()
    is_in_bounds = lambda point: 0 <= point[0] < size and 0 <= point[1] < size

    for key, points in nodes.items():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]

                vector = p2 - p1

                antinode1, antinode2 = p1 - vector, p2 + vector

                if is_in_bounds(antinode1):
                    antinodes.add(tuple(antinode1))
                if is_in_bounds(antinode2):
                    antinodes.add(tuple(antinode2))

    return len(antinodes)


def resonant_antinodes(size: int, nodes: defaultdict) -> int:
    antinodes = set()
    is_in_bounds = lambda point: 0 <= point[0] < size and 0 <= point[1] < size

    for key, points in nodes.items():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]

                vector = p2 - p1

                antinode1, antinode2 = p1.copy(), p2.copy()
                antinodes.add(tuple(antinode1))
                antinodes.add(tuple(antinode2))

                while is_in_bounds(antinode1 - vector):
                    antinode1 -= vector
                    if is_in_bounds(antinode1):
                        antinodes.add(tuple(antinode1))

                while is_in_bounds(antinode2 + vector):
                    antinode2 += vector
                    if is_in_bounds(antinode2):
                        antinodes.add(tuple(antinode2))

    return len(antinodes)

if __name__ == '__main__':
    with open('data/data_08.txt') as f:
        data = f.read()

    size, nodes = parse_input(data)
    print(antinodes_number(size, nodes))
    print(resonant_antinodes(size, nodes))
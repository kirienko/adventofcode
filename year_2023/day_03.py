import re


punctuation = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'


def find_symbols(test_data:str, symbols=punctuation) -> set[(int, int)]:
    coordinates = []
    for i,line in enumerate(test_data.strip().splitlines()):
        for j, char in enumerate(line):
            if char in symbols:
                coordinates.append((i,j))

    return set(coordinates)


def find_numbers_positions(input_string: str) -> list[(int, int)]:
    """ '467..114..' -> [(0,2), (5,7)] """
    pattern = r'\d+'  # This pattern matches sequences of digits
    matches = re.finditer(pattern, input_string)
    positions = [(match.start(), match.end()) for match in matches]
    return positions


def task_1(test_data:str) -> int:
    symbols = find_symbols(test_data)
    new_string = ''
    # make a new string with right numbers, comma-separated
    for i, line in enumerate(test_data.strip().splitlines()):
        numbers = find_numbers_positions(line)
        for number in numbers:
            # check if there is an adjacent symbol
            start, end = number
            for j in range(start, end):
                if point_area(i, j).intersection(symbols):
                    new_string += line[start: end] + ','
                    break
    return sum(map(int, new_string[:-1].split(',')))


def point_area(i: int, j: int) -> set[(int, int)]:
    """ Return a set with all points adjacent to the input one """
    return {(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)}


def number_set(i: int, start: int, end: int) -> set[(int, int)]:
    """ Returns a set with all point adjacent to a sting """
    return {(i, j) for j in range(start, end)}


def find_intersecting_pairs(symbol: tuple[int, int], numbers: list[list[set], str]):
    score = 0

    symbol_set = point_area(*symbol)
    # Find all sets in 'numbers' that intersect with `symbols`
    intersecting_sets = [(number_set, str_num) for number_set, str_num in numbers if symbol_set & number_set]

    # If there are exactly two intersecting sets, add calculate the score as the product of the two numbers
    if intersecting_sets and len(intersecting_sets) == 2:
        score = int(intersecting_sets[0][1])*int(intersecting_sets[1][1])

    return score


def task_2(test_data: str) -> int:
    symbols = find_symbols(test_data, symbols='*')
    number_sets = []
    res = 0
    for i, line in enumerate(test_data.strip().splitlines()):
        numbers = find_numbers_positions(line)
        number_sets += [(number_set(i, start, end), line[start: end]) for start, end in numbers]
    for s in symbols:
        res += find_intersecting_pairs(symbol=s, numbers=number_sets)
    return res


if __name__ == '__main__':
    with open('data/data_03.txt') as fd:
        data = fd.read()

    print(task_1(test_data=data))   # 531561
    print(task_2(test_data=data))   # 83279367
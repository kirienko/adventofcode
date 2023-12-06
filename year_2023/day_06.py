import re
from math import prod


def calculate_ways_to_win(time: int, record: int) -> int:
    ways_to_win = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        distance = hold_time * travel_time
        if distance > record:
            ways_to_win += 1
    return ways_to_win


def parse(data: str):
    data = data.strip().split('\n')
    times = [int(time) for time in re.findall(r'\d+', data[0])]
    records = [int(distance) for distance in re.findall(r'\d+', data[1])]
    return zip(times, records)


def parse_task2(data: str) -> tuple[int, int]:
    data = data.strip().split('\n')
    time = int(''.join(filter(str.isdigit, data[0])))
    distance = int(''.join(filter(str.isdigit, data[1])))
    return time, distance


def task_1(data: str) -> int:
    races = parse(data)
    res = [calculate_ways_to_win(*race) for i, race in enumerate(races)]
    return prod(res)


def task_2(data: str) -> int:
    time, distance = parse_task2(data)
    return calculate_ways_to_win(time, distance)


if __name__ == '__main__':
    with open('data/data_06.txt') as fd:
        data = fd.read()
    print(task_1(data))     # 741000
    print(task_2(data))     # 38220708

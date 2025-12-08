from typing import Tuple

def is_invalid_id(value: int) -> bool:
    """Return True if the ID consists of a digit sequence repeated twice."""
    str_id = str(value)
    if len(str_id) % 2 != 0:
        return False
    half_len = len(str_id) // 2
    return str_id[0:half_len] == str_id[half_len:]


def sum_invalid_ids(text: str) -> Tuple[int, int]:
    """Return the sum of all invalid IDs present in the given ranges."""
    part_1 = 0
    part_2 = 0

    for r in text.split(','):
        start, end = r.split('-')
        for i in range(int(start), int(end) + 1):
            if is_invalid_id(i):
                part_1 += i
            if is_invalid_id_part2(i):
                part_2 += i

    return part_1, part_2


def is_invalid_id_part2(value: int) -> bool:
    """Return True if the ID is some digit sequence repeated at least twice."""
    str_id = str(value)
    for k in range(1, len(str_id) // 2 + 1):
        if len(set([str_id[i:i+k] for i in range(0,len(str_id),k)])) == 1:
            return True
    return False



if __name__ == "__main__":
    with open("./data/data_02.txt") as f:
        puzzle_input = f.read()
    print(sum_invalid_ids(puzzle_input))

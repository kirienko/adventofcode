def is_safe(levels: list[int]) -> bool:
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels ) - 1)]
    for diff in diffs:
        if abs(diff) < 1 or abs(diff) > 3 or diff == 0:
            return False

    # Check that all diffs are positive or all diffs are negative
    if all(diff > 0 for diff in diffs):
        return True
    elif all(diff < 0 for diff in diffs):
        return True
    else:
        return False


def count_safe(lvl_list:list[list[int]]) -> int:
    return sum(int(is_safe(l)) for l in lvl_list)


def is_safe_singe_bad(levels: list[int]) -> bool:
    for i in range(len(levels)):
        if is_safe(levels[:i]+levels[i+1:]):
            return True
    return False


def count_safe_singe_bad(levels: list[list[int]]) -> int:
    count = 0
    for lvl in levels:
        if is_safe(lvl):
            count += 1
        else:
            if is_safe_singe_bad(lvl):
                count += 1
    return count


if __name__ == "__main__":
    with open('./data/data_02.txt') as f:
        data = f.read()
    lvl_lists = [list(map(int, line.split())) for line in data.strip().splitlines()]
    print(count_safe(lvl_lists))
    print(count_safe_singe_bad(lvl_lists))

def parser(input_data: str) -> tuple[list, list]:
    sections = input_data.strip().split("\n\n")
    seeds, parsed_data = None, []

    for section in sections:
        lines = section.split('\n')
        header = lines[0].strip()  # First line is the header

        if header.startswith('seeds:'):
            # For seeds, just split the line and convert to integers
            seeds = list(map(int, lines[0].split(':')[1].split()))
        else:
            # For maps, create a list of tuples
            map_data = []
            for line in lines[1:]:
                map_data.append(tuple(map(int, line.split())))
            parsed_data += [map_data]

    return seeds, parsed_data


def F(param_list, x: int):
    # big F for functor
    for a, b, c in param_list:
        if x in range(b, b + c):
            return x + a - b
    return x


def task_1(data: str) -> int:
    print("Task 1:")
    seeds, parsed_data = parser(data)
    print(f"{len(seeds)=}")
    # print(f"{parsed_data=}")
    res = []
    for s in seeds:
        for line in parsed_data:
            s = F(line, s)
        res += [s]
    # print(f"{res=}")
    return min(res)


# ===== TASK 2 =====
def get_seed_ranges(arr):
    print("Get seeds:")
    return sorted([(arr[i], arr[i]+arr[i+1]) for i in range(0, len(arr), 2)])


def get_map_ranges(arr):
    print("Get maps:")
    return arr


def task_2(data: str) -> int:
    seeds, parsed_data = parser(data)
    seeds = get_seed_ranges(seeds)
    print(f"{seeds=}")
    print(f"{len(seeds)=}")
    res = []
    r = []
    for b, e in seeds:
        r += [b]
        r += [e]
    for s in r:
        for line in parsed_data:
            s = F(line, s)
        res += [s]
    # print(f"{res=}")
    return min(res)



if __name__ == '__main__':
    with open('data/data_05.txt') as fd:
        data = fd.read()
    print(task_1(data=data))    # 309796150
    print(task_2(data=data))
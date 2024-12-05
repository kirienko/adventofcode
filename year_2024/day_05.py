from graphlib import TopologicalSorter

def parse_input(input_str: str) -> (list[tuple],list[list]):
    before_part, after_part = input_str.strip().split('\n\n', 1)

    pairs = []
    for line in before_part.strip().split('\n'):
        left, right = line.strip().split('|')
        pairs.append((int(left), int(right)))
    pairs = tuple(pairs)

    lists = []
    for line in after_part.strip().split('\n'):
        lists += [[int(x.strip()) for x in line.split(',')]]

    return pairs, lists


def is_correct(rules: list[tuple], update: tuple) -> bool:
    """ A simple pythonic solution without graph theory """
    index_map = {value: i for i, value in enumerate(update)}

    for a, b in rules:
        if a in index_map and b in index_map and index_map[a] >= index_map[b]:
                return False
    return True

def fix_incorrect(rules: list[tuple], update: tuple) -> tuple:
    """ Since topological sorting assumes multiple solutions,
        the resulting tuples might differ from the AoC examples.
        But the middle element is always the same.
    """
    related_rules = [(r1, r2) for r1, r2 in rules if r1 in update and r2 in update]
    ts = TopologicalSorter()
    for r1, r2 in related_rules:
        ts.add(r1, r2)

    return tuple(ts.static_order())

middle = lambda lst: lst[len(lst) // 2]


if __name__ == '__main__':
    with open('./data/data_05.txt', 'r') as f:
        data = f.read()
    rules, updates = parse_input(data)

    # Part 1
    print(sum(middle(update) for update in updates if is_correct(rules, update)))

    # Part 2
    print(sum(middle(fix_incorrect(rules, update))
                           for update in updates if not is_correct(rules, update)))

def parse_input(input_str: str) -> (list[tuple],list[list]):
    # Split into two parts using the first '\n\n'
    before_part, after_part = input_str.strip().split('\n\n', 1)

    # Parse the pairs (lines separated by '\n', each contains "number|number")
    pairs = []
    for line in before_part.strip().split('\n'):
        left, right = line.strip().split('|')
        pairs.append((int(left), int(right)))
    pairs = tuple(pairs)

    # Parse the lists (lines separated by '\n', each contains "number,number,...")
    lists = []
    for line in after_part.strip().split('\n'):
        elements = [int(x.strip()) for x in line.split(',')]
        lists.append(elements)

    return pairs, lists




# print("Pairs:", pairs)
# print("Lists:", lists)

def is_correct(rules: list[tuple], update: tuple) -> bool:
    index_map = {value: i for i, value in enumerate(update)}

    for a, b in rules:
        # Check if both numbers are present in update
        if a in index_map and b in index_map:
            # Ensure that 'a' comes before 'b'
            if index_map[a] >= index_map[b]:
                # 'a' does not appear to the left of 'b', return False
                return False
        # If one of them doesn't appear, skip this rule

    return True

def fix_incorrect(rules: list[tuple], update: tuple) -> tuple:
    # Convert update to a dictionary mapping the number to its index for quick lookups
    # correct_update = list(update)
    index_map = {value: i for i, value in enumerate(update)}
    for a, b in rules:
        if a in index_map and b in index_map:
            # Ensure that 'a' comes before 'b'
            i_a, i_b = index_map[a], index_map[b]
            if i_a >= i_b:
                # correct_update[i_a], correct_update[i_b] = correct_update[i_b], correct_update[i_a]
                index_map[a], index_map[b] = i_b, i_a

    # print()
    # print(tuple(dict(sorted(index_map.items(), key=lambda item: item[1])).keys()))
    # return tuple(correct_update)
    # return tuple(index_map[v] for v in index_map.values())
    return tuple(dict(sorted(index_map.items(), key=lambda item: item[1])).keys())


get_middle = lambda lst: lst[len(lst)//2]



if __name__ == '__main__':
    with open('./data/data_05.txt', 'r') as f:
        data = f.read()
    rules, updates = parse_input(data)
    result_correct = 0
    result_corrected = 0

    for update in updates:
        if is_correct(rules, update):
            result_correct += get_middle(update)
        else:
            result_corrected += get_middle(fix_incorrect(rules, update))

    # result = get_middle(updates)
    print(result_correct)

    result_corrected = sum(get_middle(fix_incorrect(rules, update))
                for update in updates if not is_correct(rules, update))
    print(result_corrected)


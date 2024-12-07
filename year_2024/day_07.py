from itertools import product


def parse_input(input_str: str) -> list[tuple[int, list[int]]]:
    """Parse the input data into a list of (target, numbers) tuples."""
    parsed_data = []
    for line in input_str.strip().split('\n'):
        left, right = line.split(':')
        target = int(left.strip())
        numbers = list(map(int, right.strip().split()))
        parsed_data.append((target, numbers))
    return parsed_data


def evaluate_part_1(numbers: list, ops: tuple[str]) -> int:
    """Evaluate the numbers with the given operators (ops) strictly left-to-right."""
    # ops is a list of '+' or '*' of length len(numbers) - 1
    result = numbers[0]
    for i, op in enumerate(ops, 1):
        if op == '+':
            result += numbers[i]
        else:
            result *= numbers[i]
    return result


def evaluate_part_2(numbers: list, ops: tuple[str]) -> int:
    """ The same but with concat operator """
    result = numbers[0]
    for i, op in enumerate(ops, 1):
        if op == '+':
            result += numbers[i]
        elif op == '*':
            result *= numbers[i]
        else:
            result = int(str(result) + str(numbers[i]))
    return result


def main(parsed_data: list, evaluator = evaluate_part_1) -> int:
    if evaluator is evaluate_part_1:
        ops_list = ('+', '*')
    else:
        ops_list = ('*', '+', '|')
    result = 0
    for target, numbers in parsed_data:
        # all combinations of operations
        for ops in product(ops_list, repeat=len(numbers) - 1):
            if evaluator(numbers, ops) == target:
                result += target
                break
    return result

if __name__ == "__main__":
    with open("./data/data_07.txt") as f:
        parsed_data = parse_input(f.read())

    print(main(parsed_data))
    print(main(parsed_data, evaluate_part_2))

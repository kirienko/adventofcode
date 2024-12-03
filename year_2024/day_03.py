import re


def mul(text: str) -> int:
    # Regex magic, output's like [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)

    return sum(int(n) * int(m) for n, m in matches)


def cond_mul(text: str, debug: bool = False) -> int:
    # Finds "do()", "don't()", and 'mul(n,m)'
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

    # Find all matches along with their _positions_
    matches = list(re.finditer(pattern, text))
    if debug:
        print(f"\n{matches=}")

    state = 'do'
    total_sum = 0

    # Process each match in order
    # Each match (token) is one of the three: "do", "dont", or "mul(n,m)"
    for match in matches:
        token = match.group()
        if debug:
            print(f"\n{token=}, current state: {state}")
        if token == 'do()':
            state = 'do'
        elif token == "don't()":
            state = "don't"
        elif token.startswith('mul'):
            if state == 'do':
                nums = re.findall(r'\d{1,3}', token)
                n, m = int(nums[0]), int(nums[1])
                total_sum += n * m

    return total_sum


if __name__ == '__main__':
    with open("./data/data_03.txt") as input_file:
        input_string = input_file.read()

    print(mul(input_string))
    print(cond_mul(input_string))
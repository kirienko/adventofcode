import re


def sum_of_numbers(text):
    sum_of_nums = 0
    for line in text.splitlines():
        numbers = [int(n) for n in line if n.isdigit()]
        if numbers:
            first_last_num = int(f'{numbers[0]}{numbers[-1]}')
            sum_of_nums += first_last_num
    return sum_of_nums


# Part two
digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
f_pattern = r'(.*?)(\d.*)'              # finds the first number
l_pattern = r'(.*?)(\d+(?!.*\d).*)'     # finds the last number


def replace_first_number(match):
    first, last = match.groups()
    # search the indices of all keys in `first` and take the smallest
    indices = get_indices(first)
    if indices:
        _, number = min(indices)
        first = first.replace(number, digits[number])
    return first + last


def replace_last_number(match):
    first, last = match.groups()
    # search the indices of all keys in `last` and take the largest
    indices = get_indices(last)
    if indices:
        _, number = max(indices)
        last = last.replace(number, digits[number])
    return first + last


def get_indices(text):
    # search the indices of all keys in `text` and take the largest
    return [(i, key) for key in digits.keys() for i in range(len(text)) if text.startswith(key, i)]


def sum_with_words(text):
    sum_of_nums = 0
    for line in text.splitlines():
        line = line.strip()
        first_number, last_number = None, None
        if line[0].isdigit() and line[-1].isdigit():
            sum_of_nums += int(f'{line[0]}{line[-1]}')
            continue
        # check if there are digits in the `line`
        if line[0].isdigit():
            first_number = int(line[0])
        elif any(n.isdigit() for n in line):
            # find the number before the very first digit in a line
            line = re.sub(f_pattern, replace_first_number, line)
        else:
            indices = get_indices(line)
            _, number = min(indices)
            first_number = digits[number]
        # only if the last character is not a digit
        if line[-1].isdigit():
            last_number = line[-1]
        # find the number after the very last digit in a line
        elif any(n.isdigit() for n in line):
            line = re.sub(l_pattern, replace_last_number, line)
        else:
            indices = get_indices(line)
            _, number = max(indices)
            line = line.replace(number, digits[number])
        numbers = [int(n) for n in line if n.isdigit()]
        first_last_num = int(f'{first_number or numbers[0]}{last_number or numbers[-1]}')
        sum_of_nums += first_last_num
    return sum_of_nums


if __name__ == "__main__":
    with open('data/day_01.txt') as fd:
        data = fd.read()

    print(f"Part one: {sum_of_numbers(data)}")      # 55834
    print(f"Part two: {sum_with_words(data)}")      # 53221

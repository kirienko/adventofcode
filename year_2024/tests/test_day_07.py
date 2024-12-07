from year_2024.day_07 import parse_input, main, evaluate_part_2

text = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

parsed = parse_input(text)

def test_part_1():
    assert main(parsed) == 3749


def test_part_2():
    assert main(parsed, evaluate_part_2) == 11387

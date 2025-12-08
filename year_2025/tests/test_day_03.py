from year_2025.day_03 import (
    max_two_banks_joltage,
    total_output_part_1,
    max_twelve_banks_joltage,
    total_output_part_2,
)


example_text = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_max_bank_joltage_per_bank():
    assert max_two_banks_joltage("987654321111111") == 98
    assert max_two_banks_joltage("811111111111119") == 89
    assert max_two_banks_joltage("234234234234278") == 78
    assert max_two_banks_joltage("818181911112111") == 92


def test_total_output_example():
    assert total_output_part_1(example_text) == 357


def test_max_bank_joltage_per_bank_12():
    assert max_twelve_banks_joltage("987654321111111") == 987654321111
    assert max_twelve_banks_joltage("811111111111119") == 811111111119
    assert max_twelve_banks_joltage("234234234234278") == 434234234278
    assert max_twelve_banks_joltage("818181911112111") == 888911112111


def test_total_output_example_part2():
    assert total_output_part_2(example_text) == 3121910778619

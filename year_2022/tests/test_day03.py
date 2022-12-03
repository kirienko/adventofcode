from year_2022.day_03 import task1, task2

test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_task1(sc=test_data):
    expected = 157
    assert task1(sc) == expected


def test_task2(sc=test_data):
    expected = 70
    assert task2(sc) == expected


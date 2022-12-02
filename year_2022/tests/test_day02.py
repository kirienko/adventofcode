from year_2022.day_02 import task1, task2

test_scenario = """
A Y
B X
C Z
"""


def test_task1(sc=test_scenario):
    expected = 15
    assert task1(sc) == expected


def test_task2(sc=test_scenario):
    expected = 12
    assert task2(sc) == expected


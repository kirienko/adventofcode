from year_2022.day_09 import task1, task2

test_data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

larger_example = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def test_task1(data=test_data):
    expected = 13
    assert task1(data) == expected


def test_task2(data=test_data):
    expected = 1
    assert task2(data) == expected


def test_task2_larger(data=larger_example):
    expected = 36
    assert task2(data) == expected

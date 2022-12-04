from year_2022.day_04 import task1, task2

test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_task1(sc=test_data):
    expected = 2
    assert task1(sc) == expected


def test_task2(sc=test_data):
    expected = 4
    assert task2(sc) == expected


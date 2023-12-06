from year_2023.day_06 import task_1, task_2

test_data = """Time:      7  15   30
Distance:  9  40  200"""


def test_task_1():
    assert task_1(test_data) == 288


def test_task_2():
    assert task_2(test_data) == 71503
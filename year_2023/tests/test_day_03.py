from year_2023.day_03 import task_1, task_2


test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_task_1():
    assert task_1(test_data=test_data) == 4361


def test_task_2():
    assert task_2(test_data=test_data) == 467835
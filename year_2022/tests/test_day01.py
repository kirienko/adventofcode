from year_2022.day_01 import get_calories_list, task1, task2

with open('tests/example_day01.txt') as td:
    data = td.read()
calories = get_calories_list(data)


def test_task1(inp=calories):
    expected = 24000
    assert task1(inp) == expected


def test_task2(inp=calories):
    expected = 45000
    assert task2(inp) == expected


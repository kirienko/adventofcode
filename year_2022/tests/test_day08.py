from year_2022.day_08 import get_array, get_score, is_visible, task1, task2

test_data = """
30373
25512
65332
33549
35390
"""

arr = get_array(test_data)


def test_is_visible():
    assert is_visible(1, 1, arr) == True
    assert is_visible(2, 2, arr) == False


def test_get_score():
    assert get_score(1, 2, arr) == 4
    assert get_score(3, 2, arr) == 8


def test_task1(data=test_data):
    expected = 21
    assert task1(data) == expected


def test_task2(data=test_data):
    expected = 8
    assert task2(data) == expected

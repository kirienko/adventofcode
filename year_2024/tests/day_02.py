from year_2024.day_02 import (count_safe, is_safe,
                              is_safe_singe_bad, count_safe_singe_bad)

text = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

lvl_lists = [list(map(int, line.split())) for line in text.strip().splitlines()]

def test_is_safe():
    expected = (True, False, False, False, False, True)
    for levels, e in zip(lvl_lists, expected):
        assert is_safe(levels) == e

def test_count_safe():
    assert count_safe(lvl_lists) == 2

def test_is_safe_singe_bad():
    expected2 = (True, False, False, True, True, True)
    for levels, e in zip(lvl_lists, expected2):
        if not is_safe(levels):
            assert is_safe_singe_bad(levels) == e

def test_count_safe_singe_bad():
    assert count_safe_singe_bad(lvl_lists) == 4
import re
from year_2023.day_01 import (sum_of_numbers, sum_with_words,
                              replace_first_number, replace_last_number,
                              f_pattern, l_pattern)


def test_sum_of_numbers():
    text = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    assert sum_of_numbers(text) == 142


def test_sum_with_words():
    text = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
    assert sum_with_words(text.strip()) == 281


def test_complex_string():
    text_init = "onelxsixbmznqnfqtmdscjthree5dltxeightwox"
    text = re.sub(f_pattern, replace_first_number, text_init)
    assert text == '1lxsixbmznqnfqtmdscjthree5dltxeightwox'
    text = re.sub(l_pattern, replace_last_number, text)
    assert text == '1lxsixbmznqnfqtmdscjthree5dltxeigh2x'
    assert sum_with_words(text_init) == 12
    assert sum_with_words('six92one') == 61
    assert sum_with_words('three2fiveonexrllxsvfive') == 35


def test_no_digits():
    assert sum_with_words("eightwothree") == 83
    assert sum_with_words("eighthree") == 83
    assert sum_with_words("sevenine") == 79
    assert sum_with_words("oneight") == 18


def test_one_digit():
    assert sum_with_words("2bb") == 22
    assert sum_with_words("q9") == 99
    assert sum_with_words("1") == 11
    assert sum_with_words("one") == 11
    assert sum_with_words("tgppgp9") == 99

import pytest

from year_2022.day_06 import decode

test_array = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23,),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)
]


@pytest.mark.parametrize("test_data, e1, e2", test_array)
def test_decode_1(test_data, e1, e2):
    assert decode(test_data, 4) == e1


@pytest.mark.parametrize("test_data, e1, e2", test_array)
def test_decode_2(test_data, e1, e2):
    assert decode(test_data, 14) == e2


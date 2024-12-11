from year_2024.day_11 import blink, count_stones, parse

text = "125 17"

def test_blink():
    assert blink(parse("125 17"), 6) == 22
    assert blink(parse("125 17"), 25) == 55312

def test_count_stones():
    assert sum(count_stones(s, 25) for s in (125, 17)) == 55312
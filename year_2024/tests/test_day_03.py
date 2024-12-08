from year_2024.day_03 import cond_mul, mul

text_1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
expected_1 = 161

def test_mul():
    assert mul(text_1) == expected_1

text_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"""
expected_2 = 48

def test_cond_mul():
    assert cond_mul(text_2, debug=True) == expected_2

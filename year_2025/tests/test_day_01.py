from year_2025.day_01 import password


example_text = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

another_text = """L12
R101"""

def test_password_example():
    assert password(example_text) == (3, 6)

def test_another_example():
    assert password(another_text) == (0, 1)

def test_L250():
    assert password("L250") == (1, 3)

def test_L251():
    assert password("L251") == (0, 3)

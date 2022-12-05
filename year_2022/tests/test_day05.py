from year_2022.day_05 import parse_input, task1, task2

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

crates, actions = parse_input(test_data)


def test_crates(cr=crates):
    assert cr == ['ZN', 'MCD', 'P']


def test_actions(ac=actions):
    assert ac == ((1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2))


def test_task1(sc=test_data):
    expected = 'CMZ'
    assert task1(sc) == expected


def test_task2(sc=test_data):
    expected = 'MCD'
    assert task2(sc) == expected


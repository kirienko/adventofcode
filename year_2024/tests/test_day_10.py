from year_2024.day_10 import parse_map, part_1, part_2, visualise

text = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

def test_parse_map():
    G, matrix, start, end = parse_map(text)
    visualise(G, matrix)
    assert True

G, _, start, end = parse_map(text)

def test_part_1():
    assert part_1(G, start, end) == 36

def test_part_2():
    assert part_2(G, start, end) == 81

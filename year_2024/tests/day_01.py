from year_2024.day_01 import get_lists, distance, similarity

text = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def test_distances():
    assert distance(get_lists(text)) == 11

def test_similarity():
    assert similarity(get_lists(text)) == 31
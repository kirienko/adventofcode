from year_2024.day_04 import count_xmas, count_x_mas, data_matrix

word = "XMAS"

text = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

m = data_matrix(text)

def test_count_word_occurrences():
    assert count_xmas(word, m) == 18


def test_count_x_mas():
    assert count_x_mas(m) == 9
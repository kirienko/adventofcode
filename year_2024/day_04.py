import re
import numpy as np


def data_matrix(text: str) -> np.ndarray:
    return np.array([list(line) for line in text.strip().split('\n')])


def count_xmas(word: str, matrix: np.ndarray) -> int:
    # regex patterns for the word in forward and backward directions
    pattern = re.compile(f"(?=({word}|{word[::-1]}))")

    occurrences = 0

    # Stack the matrix on top of its transpose for vertical search in the same loop
    for row in np.vstack((matrix, matrix.T)):
        occurrences += len(pattern.findall(''.join(row)))

    # Diagonals: https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
    # For all ↘ diagonals
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
    # For all ↙ diagonals
    diags += [matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1)]

    for diag in diags:
        occurrences += len(pattern.findall(''.join(diag)))

    return occurrences


def all_3x3_submatrices(matrix):
    n = matrix.shape[0]
    return [matrix[i:i+3, j:j+3] for i in range(n - 2) for j in range(n - 2)]


def is_mas(A: np.ndarray) -> bool:
    if A[1,1] != 'A':
        return False

    corners = [A[0,0], A[0,2], A[2,0], A[2,2]]
    if ''.join(sorted(corners)) != 'MMSS':
        return False

    # Check that top-left != bottom-right
    if A[0,0] == A[2,2]:
        return False

    return True


def count_x_mas(matrix: np.ndarray) -> int:
    return sum([is_mas(m) for m in all_3x3_submatrices(matrix)])


if __name__ == "__main__":
    with open("./data/data_04.txt") as input_file:
        data = input_file.read()

    print("Total XMAS:", count_xmas("XMAS", data_matrix(data)))
    print("Total X-MAS:", count_x_mas(data_matrix(data)))
import numpy as np


def get_array(text: str) -> np.array:
    array = np.array([[int(x) for x in row] for row in text.strip().split('\n')])
    return array


def is_visible(row: int, col: int, arr: np.array) -> bool:
    elem = arr[row][col]

    left = max(arr[row, :col]) < elem
    right = max(arr[row, col + 1:]) < elem
    top = max(arr[:row, col]) < elem
    bottom = max(arr[row + 1:, col]) < elem
    return left or right or top or bottom


def get_score(row: int, col: int, arr: np.array) -> int:
    elem = arr[row][col]

    def view_length(li):
        for i, x in enumerate(li):
            if x >= elem:
                return i + 1
        return len(li)

    left = view_length(arr[row, :col][::-1])
    right = view_length(arr[row, col + 1:])
    top = view_length(arr[:row, col][::-1])
    bottom = view_length(arr[row + 1:, col])
    return left * right * top * bottom


def task1(text: str) -> int:
    array = get_array(text)
    result = 0
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[0]) - 1):
            if is_visible(i, j, array):
                result += 1
    return result + 4 * len(array) - 4


def task2(text: str) -> int:
    array = get_array(text)
    scores = []
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[0]) - 1):
            scores += [get_score(i, j, array)]
    return max(scores)


if __name__ == "__main__":
    with open('data/day_08.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

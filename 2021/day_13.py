with open('./data/day_13.txt') as fd:
    point_data, fold_data = fd.read().split('\n\n')

initial_points = []
for p in point_data.split():
    x, y = p.split(',')
    initial_points += [(int(x), int(y))]

instructions = [x.split()[-1].split('=') for x in fold_data.split('\n')]
instructions = [(x, int(n)) for x, n in instructions]


def fold(points: list, folds: list, fold_num: int = None):
    """ This is a school math: if we mirror the array (i.e. "fold the paper")
    along the y-axis at the coordinate f_y, then essentially we do the following:
    (x_i, y_i) --> (x_i, y_i - 2 * (y_i - f_y)) = (x_i, 2 * f_y - y_i)
    and this affects only the points which are lower than the folding line.
    Similarly, for the x-axis reflection:
    (x_i, y_i) --> (2 * f_x - x_i, y_i)
    and this affects only the points which are on the right of the folding line.
    """
    fold_x, fold_y = 10000, 10000     # some rather big number
    for coord, num in folds[:fold_num]:
        if coord == 'x':
            fold_x = num
            for i, (x, y) in enumerate(points):
                if x > num:
                    points[i] = (2 * num - x, y)
        else:
            fold_y = num
            for i, (x, y) in enumerate(points):
                if y > num:
                    points[i] = (x, 2 * num - y)
    return set(points), fold_x, fold_y


one_fold, max_x, max_y = fold(initial_points, instructions, 1)
s = [(x, y) for (x, y) in one_fold if x < max_x and y < max_y]
print(f"Answer 1: {len(s)}")

all_folds, max_x, max_y = fold(initial_points, instructions)
print("Answer 2:")
for y in range(max_y):
    for x in range(max_x):
        if (x, y) in all_folds:
            print('#', end='')
        else:
            print(' ', end='')
    print()

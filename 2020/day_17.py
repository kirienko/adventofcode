import numpy as np

test = """.#.
..#
###"""

# test = """###..#..
# .#######
# #####...
# #..##.#.
# ###..##.
# ##...#..
# ..#...#.
# .#....##"""

data = np.array(test.split("\n"))
data = np.array(test.replace('#', '1').replace('.', '0').split("\n"))
data = np.array([list(map(int, x)) for x in data])
print(np.hstack((data, np.zeros(data.shape, dtype=int))))

# print(data)
# print(np.zeros(data.shape, dtype=int))
# for c in range(6):
#     print(f"shape: {data.shape}")

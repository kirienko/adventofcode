import pandas as pd

raw = """
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

# with open('./data/day_03.txt') as fd:
#     raw = fd.read()

# Create a 2D Pandas DataFrame with zeros and ones
df = pd.DataFrame((pd.to_numeric(list(x)) for x in raw.strip().split('\n')), dtype=int)
# `mode()` returns the value that appears most often. Then we concatenate in one string all zeros and ones
gamma = df.mode().to_string(header=False, index=False).replace(' ', '')
# We simply do bitwise NOT
eps = gamma.translate(str.maketrans("01", "10"))

print(f"Answer 1: {int(gamma, 2) * int(eps, 2)}")
print(f"Answer 2: ")

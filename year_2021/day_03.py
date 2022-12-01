import pandas as pd

with open('./data/day_03.txt') as fd:
    raw = fd.read()


def df2str(data: pd.DataFrame) -> str:
    return data.to_string(header=False, index=False).replace(' ', '')


# Create a 2D Pandas DataFrame with zeros and ones
df = pd.DataFrame((pd.to_numeric(list(x)) for x in raw.strip().split('\n')), dtype=int)
# `mode()` returns the value that appears most often. Then we concatenate in one string all zeros and ones
gamma = df2str(df.mode())
# We simply do bitwise NOT
eps = gamma.translate(str.maketrans("01", "10"))

print(f"Answer 1: {int(gamma, 2) * int(eps, 2)}")


# Part 2:
def msb(bits: pd.DataFrame, pos) -> int:
    """ Find the most significant bit of a data frame `bits` at the position `pos`"""
    if bits[pos].mode().shape == (2,):
        return 1
    return int(bits[pos].mode())


def lsb(bits: pd.DataFrame, pos) -> int:
    """ Find the least significant bit of a data frame `bits` at the position `pos`"""
    return int(not(msb(bits, pos)))


def filter_rows(bits: pd.DataFrame, array: list, func):
    if len(bits) == 1:
        return bits
    i = bits.shape[1] - len(array)
    return filter_rows(bits[bits[i] == func(bits, i)], array[1:], func=func)


ogr = filter_rows(df, list(gamma), msb)
co2 = filter_rows(df, list(eps), lsb)
print(f"Answer 2: {int(df2str(ogr), 2) * int(df2str(co2), 2)}")

import pandas as pd

with open('./test/day_09.txt') as fd:
    raw = fd.read()

data = pd.DataFrame((pd.to_numeric(list(x)) for x in raw.split('\n')), dtype=int)

# print(data)
# print(data.shape)


def adj(df: pd.DataFrame, i: int, j: int) -> tuple:
    """ Returns a list of values of elements adjacent to elem[i][j] in the array df """
    sx, sy = df.shape
    sx -= 1
    sy -= 1
    if 0 < i < sx and 0 < j < sy:
        return df.loc[i-1, j], df.loc[i+1, j], df.loc[i, j-1], df.loc[i, j+1]
    elif i in (0, sx) and 0 < j < sy:
        return df.loc[i, j-1], df.loc[i, j+1], df.loc[abs(i-1), j]
    elif 0 < i < sx and j in (0, sy):
        return df.loc[i-1, j], df.loc[i+1, j], df.loc[i, abs(j-1)]
    else:
        return df.loc[i, abs(j-1)], df.loc[abs(i-1), j]


def min_adj(elem: int, arr: tuple) -> bool:
    """ True if the point is lower than all its adjacent """
    return elem < min(arr)


risk_level = 0
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        # print(f"{i}, {j} ({data.loc[i, j]})", end=': ')
        # print(adj(data, i, j), end=' ')
        if min_adj(data.loc[i,j], adj(data, i, j)):
            print(f"*{data.loc[i,j]}*", end='')
            risk_level += 1 + data.loc[i, j]
        else:
            print(f" {data.loc[i,j]} ", end='')
    print()

print(f"Answer 1: {risk_level}")

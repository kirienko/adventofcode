import numpy as np
from collections import deque


def parse_and_defragment_files(text: str):
    files = list(map(int, text.strip()[::2]))
    spaces = list(map(int, text.strip()[1::2]))

    d = []
    for i, f in enumerate(files):
        d.extend([i] * f)
    de = deque(d)

    disk = np.array([], dtype=int)
    for j in range(len(spaces)):
        for _ in range(files[j]):
            disk = np.concatenate((disk, np.array([de.popleft()])))
            if len(de) == 0:
                return disk
        for _ in range(spaces[j]):
            disk = np.concatenate((disk, np.array([de.pop()])))
            if len(de) == 0:
                return disk
    return disk

def checksum(disk: np.array) -> int:
    cs  = 0
    for i, f in enumerate(disk):
        if f >= 0:
            cs += i * f
    return cs

if __name__ == '__main__':
    with open('./data/data_09.txt') as fd:
        text = fd.read()
    disk = parse_and_defragment_files(text)
    print(f"Answer 1: {checksum(disk)}")

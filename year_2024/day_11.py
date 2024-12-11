from collections import Counter
from datetime import datetime as dt
from functools import lru_cache

def parse(text: str):
    zeros = 0
    evens = Counter()
    other = Counter()

    for elem in text.strip().split():
        if elem == '0':
            zeros += 1
        elif len(elem) % 2 == 0:
            evens.update([elem])
        else:
            other.update([int(elem)])
    return zeros, evens, other

def blink(data, N: int) -> int:
    """
    This function is usable for the Part 1 only.
    Memoization is not enough for the Part 2.
    """

    zeros, evens, other = data
    for i in range(N):
        print(f"Blink {i}, {dt.now().time()}")
        _zeros, _evens, _other = 0, Counter(), Counter()
        # all zeroes become ones and go to the 'other'
        _other.update([1]*zeros)
        # every even number split into two
        for k,v in evens.items():
            n = len(k) // 2
            e1, e2 = k[:n], int(k[n:])
            # the left strings cannot contract due to zeros
            if len(e1) % 2 == 0:
                # still even number of digits
                _evens.update([e1] * v)
            else:
                _other.update([int(e1)] * v)
            # the right string can become zero
            if e2 == 0:
                _zeros += v
            elif len(se2:=str(e2)) % 2 == 0:
                # still even number of digits
                _evens.update([se2] * v)
            else:
                 _other.update([e2] * v)
        # every other number is multiplied by 2024
        for k,v in other.items():
            ik = int(k) * 2024
            sk = str(ik)
            if len(sk) % 2 == 0:
                # still even number of digits
                _evens.update([sk] * v)
            else:
                _other.update([ik] * v)
        zeros, evens, other = _zeros, _evens, _other

    result = zeros + sum(v for v in evens.values()) + sum(v for v in other.values())
    return result


@lru_cache(None)
def count_stones(n, steps):
    """
    Return how many stones result from starting with a single stone n (integer)
    after 'steps' transformations.
    """
    if steps == 0:
        return 1

    if n == 0:
        # Rule 1: 0 -> 1
        return count_stones(1, steps - 1)
    else:
        s = str(n)
        length = len(s)

        if length % 2 == 0:
            n = length // 2
            left_str, right_str = s[:n], s[n:]

            left_num = int(left_str)
            right_num = int(right_str)

            return (count_stones(left_num, steps - 1) +
                    count_stones(right_num, steps - 1))
        else:
            new_num = n * 2024
            return count_stones(new_num, steps - 1)


if __name__ == "__main__":
    with open('data/data_11.txt') as f:
        data = f.read()

    # part 1, although one can use the lru_cached version instead
    print(parse(data))
    print(blink(parse(data), 25))

    # part 2
    stones = list(map(int, data.strip().split()))
    print(sum(count_stones(stone, 75) for stone in stones))
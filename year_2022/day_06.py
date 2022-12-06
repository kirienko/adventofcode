def decode(text: str, n: int) -> int:
    for i in range(len(text) - n):
        if len(set(text[i:i+n])) == n:
            return i + n


if __name__ == "__main__":
    with open('data/day_06.txt') as fd:
        data = fd.read()

    print(decode(data, 4))
    print(decode(data, 14))

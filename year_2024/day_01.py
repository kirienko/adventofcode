def get_lists(text: str) -> (list, list):
    text = text.strip()
    list_of_pairs = [x.split('   ') for x in text.split("\n")]

    l1, l2 = [], []
    for a,b in list_of_pairs:
        l1.append(int(a))
        l2.append(int(b))
    return sorted(l1), sorted(l2)


def distance(lists) -> int:
    result = sum(abs(int(a) - int(b)) for a, b in zip(*lists))
    return result


def similarity(lists) -> int:
    l1, l2 = lists
    result = 0
    for a in l1:
        result += a * l2.count(a)
    return result


if __name__ == "__main__":
    with open("./data/data_01.txt") as f:
        data = f.read()

    lists = get_lists(data)
    print(distance(lists))
    print(similarity(lists))
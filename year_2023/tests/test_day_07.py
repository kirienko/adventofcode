from year_2023.day_07 import Hand, Hand2, parse, task_1, task_2

test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

parsed_test_data = parse(test_data)

hands = [Hand(*d) for d in parsed_test_data]
h1 = Hand("T55J5", 684)  # Three of a kind
h2 = Hand("32T3K", 765)  # one pair
h3 = Hand("KK677", 28)  # two pair
h4 = Hand("KTJJT", 220)  # two pair
h5 = Hand("2AAAA", 23)  # 4 of a kind
h6 = Hand("AAAAA", 220)  # 5 of a kind


def test_hand_comparisons():
    assert h1 > h2
    assert h2 < h1
    assert h3 > h4
    assert h6 > h5


def test_sorting():
    assert sorted([h1, h2, h3, h4]) == [h2, h4, h3, h1]


def test_task_1():
    print(hands)
    assert task_1(test_data) == 6440


h2_1 = Hand2("T55J5", 684)  # 4 of a kind
h2_2 = Hand2("32T3K", 765)  # one pair
h2_3 = Hand2("KK677", 28)   # two pair
h2_4 = Hand2("KTJJT", 220)  # 4 of a kind
h2_5 = Hand2("2JJJJ", 23)    # 5 of a kind
h2_6 = Hand2("JJJJJ", 220)   # 5 of a kind


def test_hand2_comparisons():

    assert h2_1 > h2_2
    assert h2_2 < h2_1
    assert h2_3 < h2_4
    assert h2_5 > h2_6


def test_task_2():
    assert task_2(test_data) == 5905

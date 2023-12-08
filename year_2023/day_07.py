from collections import Counter


class Hand:
    value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                  '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                  '4': 4, '3': 3, '2': 2, }

    def __init__(self, cards: str, bid: int):
        self.hand = cards
        self.bid: int = int(bid)
        counts = Counter(cards)
        self.counts = counts
        # Classify the hand
        if 5 in counts.values():
            self.rank, self.type = 7, "Five of a kind"
        elif 4 in counts.values():
            self.rank, self.type = 6, "Four of a kind"
        elif 3 in counts.values() and 2 in counts.values():
            self.rank, self.type = 5, "Full house"
        elif 3 in counts.values():
            self.rank, self.type = 4, "Three of a kind"
        elif list(counts.values()).count(2) == 2:
            self.rank, self.type = 3, "Two pair"
        elif 2 in counts.values():
            self.rank, self.type = 2, "One pair"
        else:
            self.rank, self.type = 1, "High card"

    def __repr__(self):
        return f"{self.hand} ({self.rank}: {self.type})"

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank == other.rank:
            for i in range(5):
                if self.__class__.value[self.hand[i]] > self.__class__.value[other.hand[i]]:
                    return True
                elif self.__class__.value[self.hand[i]] < self.__class__.value[other.hand[i]]:
                    return False


def parse(text):
    hands = []
    for line in text.strip().splitlines():
        hand, bid = line.strip().split()
        hands.append((hand, bid))
    return hands


def task_1(text: str) -> int:
    parsed_data = parse(text)
    hands = [Hand(*d) for d in parsed_data]
    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), start=1))


# === Task 2 ===
class Hand2(Hand):
    value = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10,
             '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
             '4': 4, '3': 3, '2': 2, }

    def __init__(self, cards: str, bid: int):
        super().__init__(cards, bid)
        # check Jokers
        if self.rank == 1 and self.counts['J'] == 1:
            self.rank, self.type = 2, "One pair"
        elif self.rank == 2 and self.counts['J'] in [1, 2]:
            self.rank, self.type = 4, "3 of a kind"
        elif self.rank == 3 and self.counts['J'] == 1:
            self.rank, self.type = 5, "Full house"
        elif self.rank == 3 and self.counts['J'] == 2:
            self.rank, self.type = 6, "4 of a kind"
        elif self.rank == 4 and self.counts['J'] in [1, 3]:
            self.rank, self.type = 6, "4 of a kind"
        elif self.rank == 5 and self.counts['J'] in [2, 3]:
            self.rank, self.type = 7, "5 of a kind"
        elif self.rank == 6 and self.counts['J'] in [1, 4]:
            self.rank, self.type = 7, "5 of a kind"


def task_2(text: str) -> int:
    parsed_data = parse(text)
    hands = [Hand2(*d) for d in parsed_data]
    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), start=1))


if __name__ == "__main__":
    with open("./data/data_07.txt") as f:
        data = f.read()
    print("Task 1:", task_1(data))      # 250370104
    print("Task 2:", task_2(data))      # 251735672


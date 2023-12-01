class Monkey:
    counter = 0

    def __init__(self, text: str):
        lines = text.strip().split('\n')
        self.number = int(lines[0].split()[1][:-1])
        self.items = list(map(int, lines[1].split(': ')[1].split(', ')))
        self.operation = lambda old: eval(lines[2].split(' = ')[1])
        self.action = lines[2].split()[4]
        self.divisor = int(lines[3].split('divisible by')[1])
        self.pass_true = int(lines[4].split()[-1])
        self.pass_false = int(lines[5].split()[-1])

    def __repr__(self):
        return f"Monkey {self.number} ({self.counter}) has items {[i for i in self.items]}"

    def test_1(self, monkeys: list):
        self.counter += 1
        worry_level = self.items.pop(0)
        worry_level = self.operation(worry_level) // 3
        if worry_level % self.divisor == 0:
            pass_to(worry_level, self.pass_true, monkeys)
            # print(f"Monkey {self.number}: '{worry_level}' -> {self.pass_true}")
        else:
            pass_to(worry_level, self.pass_false, monkeys)
            # print(f"Monkey {self.number}: '{worry_level}' -> {self.pass_false}")

    def test_2(self, monkeys: list):

        self.counter += 1
        item = self.items.pop(0)
        worry_level = self.operation(item)
        # worry_level = self.operation(self.items.pop(0))
        if worry_level % self.divisor == 0:
            # if self.action == '*':
                pass_to(worry_level // self.divisor, self.pass_true, monkeys)
            # else:
            #     pass_to(worry_level, self.pass_true, monkeys)
            # print(f"Monkey {self.number} ({self.divisor}): {item} -> {worry_level} -> to M{self.pass_true}")
        else:
            # if self.action == '*':
                pass_to(worry_level % self.divisor, self.pass_false, monkeys)
            # else:
            #     pass_to(worry_level, self.pass_false, monkeys)
            # print(f"Monkey {self.number} ({self.divisor}): {item} -> {worry_level} -> to M{self.pass_false}")


def read(text: str) -> list:
    return [Monkey(monkey_def) for monkey_def in text.strip().split('\n\n')]


def pass_to(it: int, monkey_num: int, monkey_list: list):
    monkey_list[monkey_num].items += [it]


def task1(text: str) -> int:
    monkey_list = read(text)
    # for m in monkey_list:
    #     print(m)

    for r in range(20):
        for m in monkey_list:
            while m.items:
                m.test_1(monkey_list)
        # print(f"== After round {r + 1} ==")
        # for m in monkey_list:
        #     print(m)
    inspects = sorted([m.counter for m in monkey_list], reverse=True)
    return inspects[0] * inspects[1]


def task2(text: str) -> int:
    monkey_list = read(text)

    for r in range(1000):
        for m in monkey_list:
            while m.items:
                m.test_2(monkey_list)
        if (r+1) % 1000 == 0:
            print(f"== After round {r + 1} ==")
            for m in monkey_list:
                print(m)
    inspects = sorted([m.counter for m in monkey_list], reverse=True)
    print(f"{inspects=}")
    return inspects[0] * inspects[1]


if __name__ == "__main__":
    with open('data/day_11.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))

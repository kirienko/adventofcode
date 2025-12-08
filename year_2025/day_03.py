def max_two_banks_joltage(bank: str) -> int:
    """Return the maximum joltage producible from a single bank (two batteries)."""
    first_digit = max(j for j in bank[:-1])
    first_digit_idx = bank.index(str(first_digit))
    if first_digit_idx == len(bank) - 1:
        second_digit = bank[-1]
    else:
        second_digit = max(b for b in bank[first_digit_idx + 1:])
    return int(first_digit + second_digit)


def total_output_part_1(text: str) -> int:
    """Return the sum of maximum joltages from all banks in the input."""

    return sum(max_two_banks_joltage(b) for b in text.splitlines())


def max_twelve_banks_joltage(bank: str) -> int:
    """Return the maximum joltage producible from a single bank (twelve batteries)."""
    result = []
    start = 0
    picks_remaining = 12

    for _ in range(picks_remaining):
        # We can look ahead only so far to still have enough digits left to fill remaining picks.
        max_search_end = len(bank) - (picks_remaining - 1)
        window = bank[start:max_search_end]
        best_digit = max(window)
        best_idx = window.index(best_digit) + start

        result.append(best_digit)
        start = best_idx + 1
        picks_remaining -= 1

    return int("".join(result))


def total_output_part_2(text: str) -> int:
    """Return the sum of maximum joltages (twelve batteries per bank) from the input."""
    return sum(max_twelve_banks_joltage(b) for b in text.splitlines())


if __name__ == "__main__":
    with open("./data/data_03.txt") as f:
        puzzle_input = f.read()
    print(total_output_part_1(puzzle_input))
    print(total_output_part_2(puzzle_input))

from typing import Tuple

def _zero_hits_during_rotation(position: int, direction: str, distance: int) -> int:
    """Count how many clicks in this rotation leave the dial pointing at 0."""
    if distance == 0:
        return 0

    if direction == "R":
        distance_to_zero = (100 - position) % 100
    else:
        distance_to_zero = position % 100

    # If we're already at 0, the first time we'll see it again is after one full loop.
    if distance_to_zero == 0:
        distance_to_zero = 100

    if distance < distance_to_zero:
        return 0

    remaining = distance - distance_to_zero
    return 1 + remaining // 100


def password(text: str) -> Tuple[int, int]:
    """
    Returns a tuple with:
    - times the dial ends a rotation pointing at 0 (part 1)
    - total times the dial points at 0 during all rotations (part 2)
    """
    position = 50
    zeros_at_rest = 0
    zeros_while_rotating = 0

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        zeros_while_rotating += _zero_hits_during_rotation(position, direction, distance)

        if direction == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

        if position == 0:
            zeros_at_rest += 1

    return zeros_at_rest, zeros_while_rotating


if __name__ == "__main__":
    with open("./data/data_01.txt") as f:
        data = f.read()

    part_1, part_2 = password(data)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

from year_2025.day_02 import (
    is_invalid_id,
    is_invalid_id_part2,
    sum_invalid_ids,
)


example_ranges = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def test_example_sum():
    part1, part2 = sum_invalid_ids(example_ranges)
    assert part1 == 1227775554
    assert part2 == 4174379265


def test_invalid_id_detection():
    invalid_ids = [55, 6464, 123123, 1010]
    valid_ids = [101, 1234, 38593858, 1698523]

    for value in invalid_ids:
        assert is_invalid_id(value)

    for value in valid_ids:
        assert not is_invalid_id(value)


def test_range_with_no_invalids():
    assert sum_invalid_ids("1698522-1698528") == (0, 0)


def test_invalid_id_detection_part2():
    invalid_ids = [111, 12341234, 123123123, 1212121212, 565656]
    valid_ids = [101, 1234, 1698523, 123451234]  # last one is not a clean repeat

    for value in invalid_ids:
        assert is_invalid_id_part2(value)

    for value in valid_ids:
        assert not is_invalid_id_part2(value)


def test_part2_ranges_match_example():
    cases = [
        ("11-22", [11, 22]),
        ("95-115", [99, 111]),
        ("998-1012", [999, 1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", [565656]),
        ("824824821-824824827", [824824824]),
        ("2121212118-2121212124", [2121212121]),
    ]

    for range_text, expected_ids in cases:
        # Sum of invalids should match the sample description exactly.
        _, part2 = sum_invalid_ids(range_text)
        assert part2 == sum(expected_ids)

        start, end = [int(x) for x in range_text.split("-")]
        expected_set = set(expected_ids)

        # For these small ranges, validate every value matches the expected membership.
        for value in range(start, end + 1):
            assert is_invalid_id_part2(value) == (value in expected_set)

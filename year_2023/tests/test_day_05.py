from year_2023.day_05 import F, task_1, get_seed_ranges, task_2


test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def test_F():
    assert F([(50, 98, 2), (52, 50, 48)], 0) == 0
    assert F([(50, 98, 2), (52, 50, 48)], 49) == 49
    assert F([(50, 98, 2), (52, 50, 48)], 50) == 52
    assert F([(50, 98, 2), (52, 50, 48)], 79) == 81
    assert F([(50, 98, 2), (52, 50, 48)], 99) == 51
    assert F([(50, 98, 2), (52, 50, 48)], 199) == 199

def test_task_1():
    assert task_1(test_data) == 35


def test_get_seeds():
    assert get_seed_ranges([79, 14, 55, 13]) == sorted(list(range(79, 79 + 14)) + list(range(55, 55 + 13)))

def test_task_2():
    assert task_2(test_data) == 46
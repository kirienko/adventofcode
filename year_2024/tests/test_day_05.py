from year_2024.day_05 import fix_incorrect, middle, is_correct, parse_input

input_str = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

rules, updates = parse_input(input_str)

def test_middle():
    assert middle([75, 47, 61, 53, 29]) == 61

def test_is_correct():
    assert is_correct(rules, (75,47,61,53,29))
    assert is_correct(rules, (97,13,75,29,47)) == False

def test_fix_incorrect():
    assert middle(fix_incorrect(rules, (75, 97, 47, 61, 53))) == middle((97, 75, 47, 61, 53))
    assert middle(fix_incorrect(rules, (61, 13, 29))) == middle((61, 29, 13))
    assert middle(fix_incorrect(rules, (97, 13, 75, 29, 47))) == middle((97, 75, 47, 29, 13))

def test_sum_correct():
    assert sum(middle(update) for update in updates if is_correct(rules, update)) == 143

def test_sum_corrected():
    assert  sum(middle(fix_incorrect(rules, update))
                for update in updates if not is_correct(rules, update)) == 123


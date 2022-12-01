import numpy as np

with open('./data/day_16.txt') as fd:
    test = fd.read()

rules, mine, nearby = test.split('\n\n')
rule_set = set()
rules_d = dict()

for line in rules.split('\n'):
    field, line = line.split(': ')
    line = line.split(' or ')
    rules_d[field] = set()
    for r in line:
        a, b = r.split('-')
        rule_set.update([i for i in range(int(a), int(b)+1)])
        rules_d[field].update([i for i in range(int(a), int(b)+1)])


mine = list(map(int, mine.split('\n')[1].split(',')))
nearby = [list(map(int, x.split(','))) for x in nearby.split('\n')[1:]]

error_rate = 0
invalid_tickets = []
for i, ticket in enumerate(nearby):
    invalid_field = set(ticket).difference(rule_set)
    if invalid_field:
        invalid_tickets += [i]
        error_rate += invalid_field.pop()

print(f"Answer 1: {error_rate}")
print(f"Invalid tickets: {len(invalid_tickets)} of {len(nearby)}")
nearby = [nearby[i] for i in range(len(nearby)) if i not in invalid_tickets]

nearby = np.array(nearby)
sorted_by_fields = nearby.T
candidates = [[] for _ in range(len(rules_d))]
for _ in range(len(candidates)):
    for i, f in enumerate(sorted_by_fields):
        for k, v in rules_d.items():
            if v.issuperset(f):
                candidates[i] += [k]
    for i, f in enumerate(candidates):
        if len(f) == 1:
            if f[0] in rules_d:
                rules_d.pop(f[0])
        else:
            candidates[i] = []

ans = np.prod([mine[i] for i in range(len(mine)) if candidates[i][0].startswith('departure')])
print(f"Answer 2: {ans}")

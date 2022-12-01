import re

with open('./data/day_04.txt') as fd:
    data = fd.read().split('\n\n')

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

rules = {'byr': lambda x: re.match('^\d{4}$', x) and 1920 <= int(x) <= 2002,
         'iyr': lambda x: re.match('^\d{4}$', x) and 2010 <= int(x) <= 2020,
         'eyr': lambda x: re.match('^\d{4}$', x) and 2020 <= int(x) <= 2030,
         'hgt': lambda x: (re.match('^\d{3}cm$', x) and 150 <= int(x[:3]) <= 193) or
                          (re.match('^\d{2}in$', x) and 59 <= int(x[:2]) <= 76),
         'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
         'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(' '),
         'pid': lambda x: re.match('^\d{9}$', x)}

counter_1, counter_2 = 0, 0
for passport in data:
    parsed = dict(map(lambda x: x.split(':'), passport.replace('\n', ' ').split(' ')))
    if required.issubset(parsed.keys()):
        counter_1 += 1
        if all([rules[k](v) for k, v in parsed.items() if k in required]):
            counter_2 += 1

print(f"Answer 1: {counter_1}")
print(f"Answer 2: {counter_2}")

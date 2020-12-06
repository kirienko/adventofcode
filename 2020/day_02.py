with open('data/day_02.txt') as fd:
    data = fd.readlines()

count_1, count_2 = 0, 0
for j, line in enumerate(data):
    policy, pwd = line.strip().split(': ')
    num, symbol = policy.split()
    r1, r2 = tuple(map(int, num.split('-')))

    if r1 <= pwd.count(symbol) <= r2:
        count_1 += 1
    if (pwd[r1 - 1] + pwd[r2 - 1]).count(symbol) == 1:
        count_2 += 1

print(count_1, count_2)

test = """939
7,13,x,x,59,x,31,19"""

test = """1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"""


time, schedule_src = test.split('\n')
time = int(time)
schedule_src = schedule_src.split(',')
schedule = [int(x) for x in schedule_src if x != 'x']
N = len(schedule)
n_schedule = tuple(schedule_src.index(str(x)) for x in schedule)

# shift number to zero the biggest value os `schedule`
t_max = (max(schedule), schedule_src.index(str(max(schedule))))
z_schedule = tuple(x - t_max[1] for x in n_schedule)

assert len(schedule) == len(n_schedule)


for i in range(max(schedule)):
    next_bus = list(map(lambda x: (time + i) % x, schedule))
    if 0 in next_bus:
        print(f"Answer 1: {i * schedule[next_bus.index(0)]}")
        break

# there is a hint that the number is bigger than 100000000000000, therefor
# we start from the next
hint_start = 100000000000000
hinted_value = hint_start // t_max[0] * t_max[0]
for t in range(hinted_value, hint_start * 10, t_max[0]):
    if sum([(t + z_schedule[i]) % x for i, x in enumerate(schedule)]) == 0:
        print(f"Answer 2: {t-t_max[1]}")
        break

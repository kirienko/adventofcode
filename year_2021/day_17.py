from math import floor, sqrt

with open('./data/day_17.txt') as fd:
    data = fd.read().strip()

data = data.split('=')[1:]
ta = []
ta += [[int(x) for x in data[0].replace(', y', '').split('..')]]   # x coordinate
ta += [[int(x) for x in data[1].split('..')]]                      # y coordinate
target_area = ((ta[0][0], ta[0][1]), (ta[1][0], ta[1][1]))


def simulate(v: tuple):
    """ Simulate the trajectory of the probe """
    x, y = (0, 0)
    v_x, v_y = v
    while True:
        x += v_x
        y += v_y
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        yield x, y


def check(coord, area):
    """ True if the coordinate falls into the `area`"""
    (x1, x2), (y1, y2) = area[0], area[1]
    return coord[0] in range(x1, x2 + 1) and coord[1] in range(y1, y2 + 1)


def find_vx(area):
    vx_min = floor((sqrt(1 + 8 * area[0][0]) - 1) / 2)  # just kinematics
    vx_max = area[0][1] + 1         # just the right border of the `area`
    return vx_min, vx_max


def find_vy(area):
    vy_min = area[1][0] - 1     # the bottom of the area
    vy_max = 100                # some bit number
    return vy_min, vy_max


def max_trajectory(traj_func):
    h = 0
    while True:
        h1 = next(traj_func)[1]
        if h1 < h:
            break
        h = h1
    return h


def draw(v, area):
    c = (0, 0)
    points = []
    traj = simulate(v)
    while not check(c, area) and c[1] >= area[1][0]:
        points += [next(traj)]
        c = points[-1]
    print(points)
    for yi in range(max(p[1] for p in points), area[1][0] - 1, -1):
        print(f"{yi}".zfill(3), end=' ')
        for xi in range(0, area[0][1] + 1):
            if (xi, yi) == (0, 0):
                print('S', end='')
            elif (xi, yi) in points:
                print('#', end='')
            elif yi == 0:
                print('_', end='')
            elif check((xi, yi), area):
                print('T', end='')
            else:
                print('.', end='')
        print()


vx = find_vx(target_area)
vy = find_vy(target_area)
print(f"v_x should be in {vx}")
print(f"v_y should be in {vy}")


res, vels = [], []
for i in range(vx[0],target_area[0][1] + 1):
    for j in range(*vy):
        velocity = (i, j)
        fire = simulate(velocity)
        x, y = 0, 0
        while y > target_area[1][0]:
            x, y = next(fire)
            if check((x, y), target_area):
                res += [max_trajectory(simulate(velocity))]
                vels += [velocity]
                break

print(f"Answer 1: {max(res)}\nAnswer 2: {len(vels)}")

# Just for debugging:
# draw((17, -4), target_area)
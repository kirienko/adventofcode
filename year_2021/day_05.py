from sympy import Line, Point, Segment
from collections import Counter
with open('./data/day_05.txt') as fd:
    raw = fd.readlines()

hline = Line(Point(0, 0), Point(1, 0))
vline = Line(Point(0, 0), Point(0, 1))
diag1 = Line(Point(0, 0), Point(1, 1))
diag2 = Line(Point(0, 0), Point(1, -1))

pt = lambda s: tuple(map(int, s.split(',')))    # '0,9' -> (0, 9)
points = [tuple(map(pt, x.strip().split(' -> '))) for x in raw]
points = [(Point(p1), Point(p2)) for p1, p2 in points]

hv_lines = [Segment(*p) for p in points if 0 in Line(*p).coefficients[:2]]
d1_lines = [Segment(*p) for p in points if Line(*p).is_parallel(diag1)]
d2_lines = [Segment(*p) for p in points if Line(*p).is_parallel(diag2)]

hv_dots = []
for line in hv_lines:
    if line.is_parallel(hline):
        for i in range(min(line.p1[0], line.p2[0]), max(line.p1[0], line.p2[0]) + 1):
            hv_dots += [(i, line.p1[1])]
    else:
        for i in range(min(line.p1[1], line.p2[1]), max(line.p1[1], line.p2[1]) + 1):
            hv_dots += [(line.p1[0], i)]

d_dots = []
for line in d1_lines:
    p1, p2 = sorted([line.p1, line.p2], key=lambda x: x[0])
    for i in range(p2[0] - p1[0] + 1):
        d_dots += [(p1[0]+i, p1[1]+i)]
for line in d2_lines:
    p1, p2 = sorted([line.p1, line.p2], key=lambda x: x[0])
    for i in range(p2[0] - p1[0] + 1):
        d_dots += [(p1[0]+i, p1[1]-i)]

print(f"Answer 1: {len([x for x in Counter(hv_dots).values() if x > 1])}")
print(f"Answer 2: {len([x for x in Counter(hv_dots+d_dots).values() if x > 1])}")

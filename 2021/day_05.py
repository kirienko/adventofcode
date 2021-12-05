from sympy import Line, Point
from sympy.plotting import plot, plot_implicit
with open('./test/day_05.txt') as fd:
    raw = fd.readlines()

print(raw)
pt = lambda s: tuple(map(int, s.split(',')))    # '0,9' -> (0, 9)
points = [tuple(map(pt, x.strip().split(' -> '))) for x in raw]
points = [(Point(p1), Point(p2)) for p1, p2 in points]
print(points)
lines = [Line(*p) for p in points]
print(lines[0].s)


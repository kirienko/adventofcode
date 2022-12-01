test = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

test1 = """16
10
15
5
1
11
7
19
6
12 1

# with open('./data/day_10.txt') as fd:
#     test = fd.read()

from math import factorial as f


def diff(arr, deg=1):
    """ n-th difference of the row"""
    _r = arr[:]
    for i in range(deg):
        _r = list(map(lambda x: x[0] - x[1], (zip(_r[1:], _r))))
    return _r

data = sorted(map(int, test.split('\n')))
data = [0] + data + [max(data)+3]

print(data)

res = list(map(lambda x: x[0]-x[1], (zip(data[1:], data))))
rr = res[1:-1]
res1 = list(map(lambda x: str(abs(x[0]-x[1])), (zip(rr[1:], rr))))
print(res)
print(res1, res1.count(0), 2**17)
print(f"Answer 1: {res.count(1) * res.count(3)}")

res2 = ''.join(res1)
print(res2, res2.count('000'))


print(diff(data,3))

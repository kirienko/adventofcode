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

test = """16
10
15
5
1
11
7
19
6
12
4"""

with open('./data/day_10.txt') as fd:
    test = fd.read()

data = sorted(map(int, test.split('\n')))
data = [0] + data + [max(data)+3]

print(data)

res = list(map(lambda x: x[0]-x[1], (zip(data[1:], data))))
print(f"Answer 1: {res.count(1) * res.count(3)}")






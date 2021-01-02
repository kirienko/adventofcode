import re
test = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))"""

data = test.split('\n')

def evaluate(s):
    """ evaluate a string without parentheses"""
    # operators = filter(lambda x: x in ('+', '*'), s)
    r = re.finditer('\+|\*', s)
    for ac in r:
        a,b = ac.span()
        print(f"{s[:a]} = {eval(s[:a])}")
        print()

print(evaluate(test))
# def find_parens(s):
#     # toret = {}
#     rep = s
#     d = {}
#     pstack = []
#
#     for i, c in enumerate(s):
#         if c == '(':
#             pstack.append(i)
#         elif c == ')':
#             start = pstack.pop()
#             # toret[start] = i
#             d[start] = s[start:i+1]
#             if s[start:i].count('(') == 0
#                 s.replace(s[start:i+1], )
#     return d
#
# print(find_parens(data[1]))
# for k, v in find_parens(data[1]):
#     if v.count('(') == 0:
#         data.
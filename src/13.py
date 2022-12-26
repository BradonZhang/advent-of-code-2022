import numpy as np
from itertools import zip_longest

with open('./in/13.txt') as f:
    chunks = f.read().strip().split('\n\n')
    pairs = [tuple(map(eval, chunk.splitlines())) for chunk in chunks]

def compare(left, right):
    if type(left) == int and type(right) == int:
        return np.sign(right - left)
    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]
    
    for x, y in zip_longest(left, right):
        if x is None:
            return 1
        if y is None:
            return -1
        if c := compare(x, y):
            return c
    return 0

total = 0
for i, (x, y) in enumerate(pairs):
    if compare(x, y) >= 0:
        total += i + 1
print(total)

lower, upper = 1, 2
for x, y in pairs:
    lower += compare(x, [[2]]) >= 0
    lower += compare(y, [[2]]) >= 0
    upper += compare(x, [[6]]) >= 0
    upper += compare(y, [[6]]) >= 0
print(lower * upper)

import numpy as np
from collections import deque

with open('./in/18.txt') as f:
    points = [np.array(list(int(x) for x in line.split(','))) for line in f.read().strip().splitlines()]

point_set = set(map(tuple, points))

I = np.identity(3, dtype=int)
D = [I[i] for i in range(3)] + [-I[i] for i in range(3)]


total = 0
for p in points:
    for dp in D:
        total += tuple(p + dp) not in point_set
print(total)


S = np.array([min(point[i] for point in points) - 1 for i in range(3)])
E = np.array([max(point[i] for point in points) + 1 for i in range(3)])

open_set = {tuple(S)}
bfs = deque(open_set)
total = 0
while bfs:
    p0 = bfs.popleft()
    for dp in D:
        p1 = p0 + dp
        if np.min(p1 - S) < 0 or np.min(E - p1) < 0:
            continue
        pt = tuple(p1)
        if pt in open_set:
            continue
        if pt in point_set:
            total += 1
            continue
        open_set.add(pt)
        bfs.append(p1)
print(total)

import numpy as np

with open('./in/14.txt') as f:
    lines = f.read().strip().splitlines()

walls = set()

for line in lines:
    points = [np.array(tuple(map(int, point_str.split(',')))) for point_str in line.split(' -> ')]
    curr = points[0]
    walls.add(tuple(curr))
    for point in points[1:]:
        step = np.sign(point - curr)
        while tuple(curr) != tuple(point):
            curr += step
            walls.add(tuple(curr))

Y = max(point[1] for point in walls)

D = [np.array((0, 1)), np.array((-1, 1)), np.array((1, 1))]
sands = set()
part1 = True

while True:
    s = np.array((500, 0))
    while s[1] < Y + 1:
        if part1 and s[1] == Y:
            part1 = False
            print(len(sands))
        for d in D:
            if tuple(s + d) not in sands and tuple(s + d) not in walls:
                s += d
                break
        else:
            sands.add(tuple(s))
            break
    sands.add(tuple(s))
    if tuple(s) == (500, 0):
        break

print(len(sands))

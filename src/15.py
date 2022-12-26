import re

with open('./in/15.txt') as f:
    data = [tuple(map(int, re.findall(r'\d+', line))) for line in f.read().strip().splitlines()]

def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

forbidden = []
Y = 10 if len(data) == 14 else 2000000

beacons = set()
for sx, sy, bx, by in data:
    d1 = manhattan(sx, sy, bx, by)
    d2 = manhattan(sx, sy, sx, Y)
    beacons.add((bx, by))
    dd = d1 - d2
    if dd < 0:
        continue
    forbidden.append((sx - dd, sx + dd))

forbidden.sort(key=lambda x: (x[0], -x[1]))
largest = -float('inf')
total = -sum(beacon[1] == Y for beacon in beacons)
for start, end in forbidden:
    if start > largest:
        total += end - start + 1
        largest = end
    elif end > largest:
        total += end - largest
        largest = end
print(total)


points = set()
steps = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
for sx, sy, bx, by in data:
    d = manhattan(sx, sy, bx, by)
    curr = (sx + d, sy)
    for step in steps:
        dx, dy = step
        for _ in range(d):
            x, y = curr
            if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                points.add(curr)
            curr = (x + dx, y + dy)
for i, point in enumerate(points):
    x, y = point
    if (x + 1, y) not in points and (x + 2, y) in points and (x + 1, y - 1) in points and (x + 1, y + 1) in points:
        for sx, sy, bx, by in data:
            d = manhattan(sx, sy, bx, by)
            if manhattan(x + 1, y, sx, sy) <= d:
                break
        else:
            print((x + 1) * 4000000 + y)
            break

from collections import deque

with open('./in/12.txt') as f:
    grid = f.read().strip().splitlines()

M = len(grid)
N = len(grid[0])
D = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i, line in enumerate(grid):
    j = line.find('S')
    if j != -1:
        S = (i, j)
    j = line.find('E')
    if j != -1:
        E = (i, j)

bfs = deque([(*S, 0)])
visited = {S}
while bfs:
    x, y, s = bfs.popleft()
    s2 = s + 1
    for dx, dy in D:
        x2, y2 = x + dx, y + dy
        if not 0 <= x2 < M or not 0 <= y2 < N:
            continue
        if (x2, y2) in visited:
            continue
        a, b = grid[x][y], grid[x2][y2]
        if b == 'S':
            continue
        if b == 'E':
            if a == 'z':
                print(s2)
                bfs.clear()
                break
            continue
        if a == 'S' and b != 'a':
            continue
        if a != 'S' and ord(b) - ord(a) > 1:
            continue
        bfs.append((x2, y2, s2))
        visited.add((x2, y2))

bfs = deque([(*E, 0)])
visited = {E}
while bfs:
    x, y, s = bfs.popleft()
    s2 = s + 1
    for dx, dy in D:
        x2, y2 = x + dx, y + dy
        if not 0 <= x2 < M or not 0 <= y2 < N:
            continue
        if (x2, y2) in visited:
            continue
        a, b = grid[x][y], grid[x2][y2].replace('S', 'a')
        if b in 'SE':
            continue
        if a == 'E' and b != 'z':
            continue
        if a != 'E' and ord(a) - ord(b) > 1:
            continue
        if b == 'a':
            print(s2)
            bfs.clear()
            break
        bfs.append((x2, y2, s2))
        visited.add((x2, y2))

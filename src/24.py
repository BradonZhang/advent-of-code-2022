import sys
import math
from functools import lru_cache
from collections import defaultdict

sys.setrecursionlimit(100000)

with open('./in/24.txt') as f:
    grid = [line[1:-1] for line in f.read().strip().splitlines()[1:-1]]

H = len(grid)
W = len(grid[0])
C = H * W // math.gcd(H, W)

blizzards = defaultdict(list)
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        blizzards[i, j].append(c)
blizzards_over_time = [blizzards]
for t in range(1, C):
    new_blizzards = defaultdict(list)
    for (i, j), blizlist in blizzards.items():
        for c in blizlist:
            if c == '>':
                new_blizzards[i, (j + 1) % W].append(c)
            elif c == '<':
                new_blizzards[i, (j - 1) % W].append(c)
            elif c == '^':
                new_blizzards[(i - 1) % H, j].append(c)
            elif c == 'v':
                new_blizzards[(i + 1) % H, j].append(c)
            else:
                assert c == '.'
    blizzards = new_blizzards
    blizzards_over_time.append(blizzards)

# print(blizzards_over_time[3])

S = (-1, 0)
E = (H, W - 1)
D = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = set()
@lru_cache(maxsize=None)
def dfs(r=S[0], c=S[1], t=0, reverse=False):
    # print(r, c, t)
    if (r, c) in blizzards_over_time[t]:
        return math.inf
    if reverse and r == c == 0:
        return 1
    if not reverse and r == H - 1 and c == W - 1:
        return 1
    visited.add((r, c, t))
    t1 = (t + 1) % C
    best = math.inf
    if (r, c, t1) not in visited:
        best = min(best, dfs(r, c, t1, reverse))
    for dr, dc in D:
        r1, c1 = r + dr, c + dc
        if not 0 <= r1 < H or not 0 <= c1 < W:
            continue
        if (r1, c1, t1) in visited:
            continue
        best = min(best, dfs(r1, c1, t1, reverse))
    visited.discard((r, c, t))
    return 1 + best

t1 = dfs()
print(t1)
dfs.cache_clear()

t2 = t1 + dfs(*E, t1 % C, reverse=True)
dfs.cache_clear()

t3 = t2 + dfs(t=t2 % C)
print(t3)

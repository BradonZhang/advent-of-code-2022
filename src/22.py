import re
from collections import deque
from itertools import zip_longest

with open('./in/22.txt') as f:
    A, B = f.read().split('\n\n')
    grid = A.splitlines()
    directions = B.strip()

R, C = len(grid), max(len(row) for row in grid)
for r in range(R):
    grid[r] += ' ' * (C - len(grid[r]))
increment = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def score():
    r, c = pos
    return (r + 1) * 1000 + (c + 1) * 4 + facing


assert grid[0].strip()
START = (0, grid[0].find('.'))
pos = START
facing = 0

steps_list = [int(x) for x in re.findall(r'\d+', directions)]
rotations = re.findall(r'[RL]', directions)

assert len(steps_list) - len(rotations) in (0, 1)
for num_steps, rotation in zip_longest(steps_list, rotations):
    start = pos
    dr, dc = increment[facing]
    for i in range(num_steps):
        r0, c0 = pos
        r1, c1 = r0 + dr, c0 + dc
        if not 0 <= r1 < R or not 0 <= c1 < C or grid[r1][c1] == ' ':
            r1, c1 = pos
            while 0 <= r1 < R and 0 <= c1 < C and grid[r1][c1] != ' ':
                r1 -= dr
                c1 -= dc
            r1 += dr
            c1 += dc
        if grid[r1][c1] == '#':
            break
        assert grid[r1][c1] == '.'
        pos = (r1, c1)
    if rotation == 'R':
        facing += 1
    elif rotation == 'L':
        facing -= 1
    facing %= 4

print(score())


G = round(((A.count('#') + A.count('.')) // 6) ** 0.5)
def get_face(r, c):
    return (r // G, c // G)
def get_local_pos(pos, face):
    fr, fc = face
    r0, c0 = fr * G, fc * G
    r1, c1 = pos
    return (r1 - r0, c1 - c0)
def get_global_pos(pos, face):
    fr, fc = face
    r0, c0 = fr * G, fc * G
    r1, c1 = pos
    return (r1 + r0, c1 + c0)

adj_list = {}
for r in range(0, R, G):
    for c in range(0, C, G):
        if grid[r][c] != ' ':
            adj_list[get_face(r, c)] = [None] * 4

faces_to_join = deque()
edges = set()
for face, neighbors in adj_list.items():
    r0, c0 = face
    for i, (dr, dc) in enumerate(increment):
        r1, c1 = r0 + dr, c0 + dc
        if (r1, c1) in adj_list:
            face1 = (r1, c1)
            neighbors[i] = face1
            edges.add((face, face1))
            edges.add((face1, face))
    for i in range(4):
        j = (i + 1) % 4
        if neighbors[i] and neighbors[j]:
            faces_to_join.append((face, i, j))

while faces_to_join:
    f, fg, fh = faces_to_join.popleft()
    g = adj_list[f][fg]
    h = adj_list[f][fh]
    if (g, h) in edges:
        continue
    gf = adj_list[g].index(f)
    hf = adj_list[h].index(f)
    gh = (fh + gf - fg - 2) % 4
    hg = (fg + hf - fh - 2) % 4
    adj_list[g][gh] = h
    adj_list[h][hg] = g
    edges.add((g, h))
    edges.add((h, g))
    if adj_list[g][(gh + 1) % 4]:
        faces_to_join.append((g, gh, (gh + 1) % 4))
    if adj_list[g][(gh - 1) % 4]:
        faces_to_join.append((g, gh, (gh - 1) % 4))
    if adj_list[h][(hg + 1) % 4]:
        faces_to_join.append((h, hg, (hg + 1) % 4))
    if adj_list[h][(hg - 1) % 4]:
        faces_to_join.append((h, hg, (hg - 1) % 4))

def move(pos, facing):
    r0, c0 = pos
    dr, dc = increment[facing]
    final_facing = facing
    r1, c1 = r0 + dr, c0 + dc
    if not 0 <= r1 < R or not 0 <= c1 < C or grid[r1][c1] == ' ':
        g = get_face(r0, c0)
        h = adj_list[g][facing]
        hg = adj_list[h].index(g)
        final_facing = (hg + 2) % 4
        i = [r0, -1 - c0, -1 - r0, c0][facing] % G
        local_pos = [(i, 0), (0, G - 1 - i), (G - 1 - i, G - 1), (G - 1, i)][final_facing]
        r1, c1 = get_global_pos(local_pos, h)
    if grid[r1][c1] == '#':
        return pos, facing
    assert grid[r1][c1] == '.'
    return (r1, c1), final_facing

pos = START
facing = 0
for num_steps, rotation in zip_longest(steps_list, rotations):
    for i in range(num_steps):
        next_pos, facing = move(pos, facing)
        if next_pos == pos:
            break
        pos = next_pos
    if rotation == 'R':
        facing += 1
    elif rotation == 'L':
        facing -= 1
    facing %= 4

print(score())

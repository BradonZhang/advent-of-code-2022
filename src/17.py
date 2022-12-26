from itertools import cycle

with open('./in/17.txt') as f:
    jets_text = f.read().strip()

rocks = [
    [(2, 3), (3, 3), (4, 3), (5, 3)],
    [(3, 3), (2, 4), (3, 4), (4, 4), (3, 5)],
    [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)],
    [(2, 3), (2, 4), (2, 5), (2, 6)],
    [(2, 4), (3, 4), (2, 3), (3, 3)],
]

def get_new_rock(rock, delta):
    dx, dy = delta
    new_rock = [(x + dx, y + dy) for x, y in rock]
    if all(0 <= x <= 6 and y >= 0 and (x, y) not in rock_set for x, y in new_rock):
        return new_rock
    return None


height = 0
rock_set = set()

jets = cycle(-1 if jet == '<' else 1 for jet in jets_text)
for i in range(2022):
    rock = [(x, y + height) for x, y in rocks[i % 5]]
    for dx in jets:
        rock = get_new_rock(rock, (dx, 0)) or rock
        down_rock = get_new_rock(rock, (0, -1))
        if not down_rock:
            break
        rock = down_rock
    for x, y in rock:
        rock_set.add((x, y))
        height = max(height, y + 1)

print(height)


heights = [0] * 7
rock_set = set()
cache = {}
last_sprint = False
jets = cycle(enumerate(-1 if jet == '<' else 1 for jet in jets_text))
t = 0
T = 1000000000000
extra_height = 0
for i in cycle(range(5)):
    rock = [(x, y + max(heights)) for x, y in rocks[i % 5]]
    for j, dx in jets:
        rock = get_new_rock(rock, (dx, 0)) or rock
        down_rock = get_new_rock(rock, (0, -1))
        if not down_rock:
            break
        rock = down_rock
    for x, y in rock:
        rock_set.add((x, y))
        heights[x] = max(heights[x], y + 1)
    t += 1
    if t == T:
        break
    diffs = tuple(heights[i + 1] - heights[i] for i in range(6))
    if not last_sprint and max(diffs) <= 2 and min(diffs) >= -2:
        key = (*diffs, i, j)
        h  = max(heights)
        if key in cache:
            last_sprint = True
            t0, h0 = cache[key]
            dt = t - t0
            dh = h - h0
            num_cycles = (T - t) // dt
            extra_height = dh * num_cycles
            t += num_cycles * dt
        cache[key] = (t, h)

print(max(heights) + extra_height)

with open('./in/23.txt') as f:
    grid = f.read().strip().splitlines()

elves = set()
for y, line in enumerate(reversed(grid)):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x, y))

proposals = [(0, 1), (0, -1), (-1, 0), (1, 0)]
sides = [(1, 0), (1, 0), (0, 1), (0, 1)]

t = 0
while True:
    proposed = {}
    for elf in elves:
        ex, ey = elf

        alone = True
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                if (ex + dx, ey + dy) in elves:
                    alone = False
        if alone:
            continue

        for i in range(4):
            j = (t + i) % 4
            dx, dy = proposals[j]
            ddx, ddy = sides[j]
            target = tx, ty = ex + dx, ey + dy
            if all((tx + ddx * m, ty + ddy * m) not in elves for m in (-1, 0, 1)):
                proposed[target] = None if target in proposed else elf
                break

    moved = False
    for target, elf in proposed.items():
        if elf is None:
            continue
        assert target not in elves
        elves.remove(elf)
        elves.add(target)
        moved = True

    t += 1
    if t == 10:
        x0 = min(x for x, _ in elves)
        x1 = max(x for x, _ in elves)
        y0 = min(y for _, y in elves)
        y1 = max(y for _, y in elves)
        print((x1 - x0 + 1) * (y1 - y0 + 1) - len(elves))
    if not moved:
        print(t)
        break

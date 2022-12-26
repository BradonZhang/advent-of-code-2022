import numpy as np

with open('./in/9.txt') as f:
    def parse_line(line):
        d, m = line.split()
        return (d, int(m))
    moves = [parse_line(line) for line in f.read().splitlines()]

D = {
    'U': np.array((0, 1)),
    'D': np.array((0, -1)),
    'R': np.array((1, 0)),
    'L': np.array((-1, 0)),
}

visited = {(0, 0)}
H, T = np.array((0, 0)), np.array((0, 0))
for dn, m in moves:
    d = D[dn]
    for _ in range(m):
        H += d
        if abs(H[0] - T[0]) > 1:
            T += d
            T[1] = H[1]
        elif abs(H[1] - T[1]) > 1:
            T += d
            T[0] = H[0]
        else:
            continue
        visited.add(tuple(T))

print(len(visited))


visited = {(0, 0)}
knots = [np.array((0, 0)) for _ in range(10)]
for dn, m in moves:
    d = D[dn]
    for _ in range(m):
        knots[0] += d
        H = knots[0]
        for T in knots[1:]:
            if np.max(np.abs(H - T)) > 1:
                T += np.sign(H - T)
            H = T
        visited.add(tuple(T))

print(len(visited))

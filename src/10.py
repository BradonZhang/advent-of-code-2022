with open('./in/10.txt') as f:
    ops = [line.split() for line in f.read().strip().splitlines()]

X = 1
t = 0

part1 = 0
part2 = ''

def draw():
    global part2
    part2 += '#' if (t % 40) in range(X - 1, X + 2) else '.'
    if t % 40 == 39:
        part2 += '\n'

def increment_t():
    global t, part1
    draw()
    t += 1
    if t in range(20, 221, 40):
        part1 += t * X

for op in ops:
    increment_t()
    if len(op) == 2:
        increment_t()
        X += int(op[1])

print(part1)
print(part2)

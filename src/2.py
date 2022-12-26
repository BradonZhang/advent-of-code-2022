with open('./in/2.txt') as f:
    lines = f.read().strip().splitlines()

total = 0
for line in lines:
    x1, x2 = line.split()
    p1 = ord(x1) - ord('A') + 1
    p2 = ord(x2) - ord('X') + 1
    res = (p2 - p1) % 3
    total += p2
    if res == 0:
        total += 3
    if res == 1:
        total += 6

print(total)

total = 0
for line in lines:
    opp, res = line.split()
    if res == 'Y':
        total += 3
    if res == 'Z':
        total += 6
    total += (ord(opp) - ord('A') + ord(res) - ord('Y')) % 3 + 1

print(total)

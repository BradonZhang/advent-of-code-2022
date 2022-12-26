with open('./in/3.txt') as f:
    lines = f.read().strip().splitlines()

total = 0
for line in lines:
    k = len(line)
    m = k // 2
    c = next(iter(set(line[:k // 2]) & set(line[k // 2:])))
    if c <= 'Z':
        total += ord(c) - ord('A') + 27
    else:
        total += ord(c) - ord('a') + 1
print(total)

total = 0

for a, b, c in zip(lines[0::3], lines[1::3], lines[2::3]):
    c = next(iter(set(a) & set(b) & set(c)))
    if c <= 'Z':
        total += ord(c) - ord('A') + 27
    else:
        total += ord(c) - ord('a') + 1

print(total)


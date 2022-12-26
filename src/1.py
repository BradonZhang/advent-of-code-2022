with open('./in/1.txt') as f:
    chunks = [[int(line) for line in chunk.splitlines()] for chunk in f.read().strip().split('\n\n')]

sums = list(map(sum, chunks))
print(max(sums))

print(sum(sorted(sums)[-3:]))

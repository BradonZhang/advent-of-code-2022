with open('./in/20.txt') as f:
    nums = list(map(int, f.read().strip().splitlines()))

N = len(nums)
O = nums.index(0)

def mix():
    for i in range(N):
        k = nums[i] % (N - 1)
        if k == 0:
            continue
        j = i
        nxt[prv[i]] = nxt[i]
        prv[nxt[i]] = prv[i]
        for _ in range(k):
            j = nxt[j]
        nxt[i] = nxt[j]
        prv[i] = j
        prv[nxt[j]] = i
        nxt[j] = i

def score():
    j = O
    total = 0
    for i in range(1, 3001):
        j = nxt[j]
        if i % 1000 == 0:
            total += nums[j]
    return total


nxt = {i: (i + 1) % N for i in range(N)}
prv = {i: (i - 1) % N for i in range(N)}

mix()
print(score())


nxt = {i: (i + 1) % N for i in range(N)}
prv = {i: (i - 1) % N for i in range(N)}

for i in range(N):
    nums[i] *= 811589153

for _ in range(10):
    mix()
print(score())

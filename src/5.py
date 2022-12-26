import re
from collections import deque

with open('./in/5.txt') as f:
    stacks_text, moves_text = f.read().split('\n\n')
    moves_text = moves_text.strip()

def init_stacks():
    stacks = [deque() for _ in stacks_text.splitlines()[-1].split()]
    for line in reversed(stacks_text.splitlines()[:-1]):
        for i, stack in enumerate(stacks):
            c = line[i * 4 + 1]
            if c != ' ':
                stacks[i].append(line[i * 4 + 1])
    return stacks

moves = [tuple(int(x) for x in re.findall(r'\d+', line)) for line in moves_text.splitlines()]

stacks = init_stacks()
for count, i, j in moves:
    for _ in range(count):
        stacks[j - 1].append(stacks[i - 1].pop())

print(''.join(stack[-1] for stack in stacks))

stacks = init_stacks()
for count, i, j in moves:
    temp = deque()
    for _ in range(count):
        temp.append(stacks[i - 1].pop())
    while temp:
        stacks[j - 1].append(temp.pop())

print(''.join(stack[-1] for stack in stacks))

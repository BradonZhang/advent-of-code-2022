import re
import math

with open('./in/11.txt') as f:
    chunks = f.read().split('\n\n')

class Monkey:
    def __init__(self, chunk):
        lines = chunk.splitlines()
        self.id = int(lines[0].split()[-1][:-1])
        self.items = [int(x) for x in re.findall('\d+', lines[1])]
        self.op = eval(f"""lambda old: {lines[2].split('= ')[-1]}""")
        self.factor = int(lines[3].split()[-1])
        self.tmonkey = int(lines[4].split()[-1])
        self.fmonkey = int(lines[5].split()[-1])
        self.num_inspections = 0
    def inspect(self, monkeys, generate_new_item):
        self.num_inspections += len(self.items)
        for item in self.items:
            new_item = generate_new_item(item)
            next_monkey = monkeys[self.tmonkey if new_item % self.factor == 0 else self.fmonkey]
            next_monkey.items.append(new_item)
        self.items.clear()
    def inspect1(self, monkeys):
        generate_new_item = lambda old: self.op(old) // 3
        self.inspect(monkeys, generate_new_item)
    def inspect2(self, monkeys, mod):
        generate_new_item = lambda old: self.op(old) % mod
        self.inspect(monkeys, generate_new_item)

monkeys = [Monkey(chunk) for chunk in chunks]

for _ in range(20):
    for monkey in monkeys:
        monkey.inspect1(monkeys)
print(math.prod(sorted(monkey.num_inspections for monkey in monkeys)[-2:]))

monkeys = [Monkey(chunk) for chunk in chunks]
mod = math.prod(monkey.factor for monkey in monkeys)

for _ in range(10000):
    for monkey in monkeys:
        monkey.inspect2(monkeys, mod)
print(math.prod(sorted(monkey.num_inspections for monkey in monkeys)[-2:]))

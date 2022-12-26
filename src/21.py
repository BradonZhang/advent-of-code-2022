import re
from fractions import Fraction
from collections import deque


with open('./in/21.txt') as f:
    lines = f.read().strip().splitlines()

OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
nodes = {}

class Node:
    def __init__(self, line):
        self.name, expr = line.split(': ')
        tokens = expr.split()
        if len(tokens) == 1:
            self.value = int(tokens[0])
        else:
            assert len(tokens) == 3
            assert len(tokens[0]) == len(tokens[2]) == 4
            self.a, self.op, self.b = tokens
            self.value = None
    def eval(self):
        if self.value is not None:
            return self.value
        self.value = OPS[self.op](nodes[self.a].eval(), nodes[self.b].eval())
        return self.value

for line in lines:
    node = Node(line)
    nodes[node.name] = node

print(nodes['root'].eval())

class Line:
    def __init__(self, line):
        self.name, expr = line.split(': ')
        self.slope = Fraction(0)
        self.has_humn = False
        self.intercept = Fraction(0)
        self.eq = None
        tokens = expr.split()

        if self.name == 'humn':
            self.has_humn = True
            self.slope = Fraction(1)
            # breakpoint()
            return

        if len(tokens) == 1:
            self.intercept = Fraction(tokens[0])
            return

        a, op, b = tokens
        A, B = nodes[a], nodes[b]

        self.has_humn = A.has_humn or B.has_humn

        if self.name == 'root':
            self.eq = (A, B)
            return

        if op == '+':
            self.slope = A.slope + B.slope
            self.intercept = A.intercept + B.intercept
        elif op == '-':
            self.slope = A.slope - B.slope
            self.intercept = A.intercept - B.intercept
        elif op == '*':
            assert not A.has_humn or not B.has_humn, (A.has_humn, B.has_humn)
            self.intercept = A.intercept * B.intercept
            if A.has_humn:
                self.slope = A.slope * B.intercept
            elif B.has_humn:
                self.slope = B.slope * A.intercept
        elif op == '/':
            assert not B.has_humn, (A.has_humn, B.has_humn)
            self.intercept = A.intercept / B.intercept
            if A.has_humn:
                self.slope = A.slope / B.intercept
        else:
            raise
        if self.slope == 0:
            self.has_humn = False
    def __repr__(self):
        if self.has_humn:
            return f'{self.slope}x+{self.intercept}'
        return str(self.intercept)

nodes = {}
q = deque(lines)
while q:
    line = q.popleft()
    name, *ops = re.findall(r'[a-z]{4}', line)
    if ops:
        a, b = ops
        if a in nodes and b in nodes:
            nodes[name] = Line(line)
        else:
            q.append(line)
    else:
        nodes[name] = Line(line)

A, B = nodes['root'].eq
lhs = A.slope - B.slope
rhs = B.intercept - A.intercept
print(rhs / lhs)

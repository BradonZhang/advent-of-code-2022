import math

with open('./in/7.txt') as f:
    stdout = f.read().strip().splitlines()

class FileNode:
    def __init__(self, name, parent=None, size=None, is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {}
        self.size = size
    @property
    def size(self):
        if self._size is not None:
            return self._size
        self._size = sum(child.size for child in self.children.values())
        return self._size
    @size.setter
    def size(self, value):
        self._size = value
    def __repr__(self):
        if self.is_dir:
            return f'{self.name} (dir)'
        return f'{self.name} (file, size={self.size})'
    def part1(self):
        if not self.is_dir:
            return 0
        total = self.size
        if total > 100000:
            total = 0
        return total + sum(child.part1() for child in self.children.values())
    def part2(self, minimum):
        if not self.is_dir or self.size < minimum:
            return math.inf
        return min(self.size, min(child.part2(minimum) for child in self.children.values()))
        

root = FileNode('', is_dir=True)
curr = root
for line in stdout:
    if line.startswith('$ cd'):
        dirname = line[5:]
        if dirname == '..':
            curr = curr.parent
            continue
        if dirname == '/':
            curr = root
            continue
        if dirname not in curr.children:
            curr.children[dirname] = FileNode(dirname, curr, is_dir=True)
        curr = curr.children[dirname]
    elif line.startswith('$ ls'):
        pass
    else:
        size, name = line.split()
        node = FileNode(name, curr, is_dir=True) if size == 'dir' else FileNode(name, curr, size=int(size))
        curr.children[name] = node

print(root.part1())
print(root.part2(root.size - (70000000 - 30000000)))

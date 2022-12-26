import numpy as np

with open('./in/8.txt') as f:
    grid = np.array([[int(x) for x in line] for line in f.read().strip().splitlines()])

R = len(grid)
C = len(grid[0])

visibility = np.array([[0] * len(row) for row in grid])

for r in range(R):
    height = -1
    for c in range(C):
        h = grid[r][c]
        if h > height:
            visibility[r][c] |= 1
            height = h
for c in range(C):
    height = -1
    for r in range(R):
        h = grid[r][c]
        if h > height:
            visibility[r][c] |= 2
            height = h
for r in range(R):
    height = -1
    for c in range(C - 1, -1, -1):
        h = grid[r][c]
        if h > height:
            visibility[r][c] |= 4
            height = h
for c in range(C):
    height = -1
    for r in range(R - 1, -1, -1):
        h = grid[r][c]
        if h > height:
            visibility[r][c] |= 8
            height = h

print(np.count_nonzero(visibility))


max_scenic = 0

for r in range(R):
    for c in range(C):
        height = grid[r][c]
        scenic = 1
        
        num_trees = 0
        for r2 in range(r - 1, -1, -1):
            num_trees += 1
            if grid[r2][c] >= height:
                break
        scenic *= num_trees
        
        num_trees = 0
        for c2 in range(c - 1, -1, -1):
            num_trees += 1
            if grid[r][c2] >= height:
                break
        scenic *= num_trees
        
        num_trees = 0
        for r2 in range(r + 1, R):
            num_trees += 1
            if grid[r2][c] >= height:
                break
        scenic *= num_trees
        
        num_trees = 0
        for c2 in range(c + 1, C):
            num_trees += 1
            if grid[r][c2] >= height:
                break
        scenic *= num_trees
        
        max_scenic = max(max_scenic, scenic)

print(max_scenic)

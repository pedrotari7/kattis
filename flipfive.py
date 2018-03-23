import sys
import copy

def isempty(grid): return all(all(_) for _ in grid)

def update_grid(grid, i, j):
    grid[i][j] = not grid[i][j]

    if j - 1 >= 0: grid[i][j-1] = not grid[i][j-1]
    if j + 1 <  3: grid[i][j+1] = not grid[i][j+1]
    if i - 1 >= 0: grid[i-1][j] = not grid[i-1][j]
    if i + 1 <  3: grid[i+1][j] = not grid[i+1][j]

    return grid

n = int(next(sys.stdin))

for game in xrange(n):

    queue = [([[line=='.' for line in next(sys.stdin).strip()] for _ in  xrange(3)], 0, None, None)]

    while queue:
        grid, step, i, j = queue.pop(0)

        if isempty(grid):
            print step
            break

        for i in xrange(3):
            for j in xrange(3):
                # print grid, update_grid(grid, i, j), i,j
                g = update_grid(copy.deepcopy(grid), i, j)
                queue.append((g, step + 1, i, j))







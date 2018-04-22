import sys
from math import sin, cos, radians

def find_start(grid):
    for r, row in enumerate(grid):
        if '*' in row:
            x,y = r, row.index('*')
            print x,y
            if x == 0:
                angle = 270
            elif x == len(grid)-1:
                angle = 90
            elif y == 0:
                angle = 0
            elif y == len(grid[0])-1:
                angle = 180
            return (x, y), angle

def move(grid, p, angle):
    
    if grid[p[0]][p[1]] == '\\':
        if angle in [270,90]:
            angle = (angle + 90) % 360
        elif angle in [0,180]:
            angle = (angle - 90 + 360) % 360
    elif grid[p[0]][p[1]] == '/':
        if angle in [270,90]:
            angle = (angle - 90 + 360) % 360
        elif angle in [0,180]:
            angle = (angle + 90) % 360

    p = [p[0] - int(sin(radians(angle))), p[1] + int(cos(radians(angle)))]

    return p, angle

def calculate_exit(grid):
    start, angle = find_start(grid)

    p, angle = move(grid, start, angle)

    while grid[p[0]][p[1]] not in ['#', 'x']:
        p, angle = move(grid, p, angle)

    grid[p[0]][p[1]] = '&'

    return grid

i = 0

while 1:
    W, L = map(int, next(sys.stdin).strip().split())
    if (W, L) == (0, 0): break
    i += 1
    grid = []
    for l in xrange(L):
        grid.append(list(next(sys.stdin).strip()))
    grid = calculate_exit(grid)
    print 'HOUSE', i
    for row in grid:
        print ''.join(row)
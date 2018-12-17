import sys

R, C, N = map(int,next(sys.stdin).strip().split())

cells = {tuple(map(int, line.split())) for line in map(str.strip,sys.stdin)}

days = 1
while len(cells) < R*C:
    for cell in list(cells)[::]:
        for u in [(cell[0]+1,cell[1]),(cell[0]-1,cell[1]),(cell[0],cell[1]+1),(cell[0],cell[1]-1)]:
            if 1 <= u[0] <= R and 1 <= u[1] <= C:
                cells.add(u)
    days += 1

print days
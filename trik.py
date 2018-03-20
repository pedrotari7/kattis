import sys

c = [1,0,0]

for move in next(sys.stdin):
    if move == 'A':
        c[1],c[0] = c[0],c[1]
    elif move == 'B':
        c[1],c[2] = c[2],c[1]
    elif move == 'C':
        c[2],c[0] = c[0],c[2]
print c.index(1) + 1
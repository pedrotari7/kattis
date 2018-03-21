import sys

R, C, ZR, ZC = map(int, next(sys.stdin).split())

final = [[''] * C * ZC for i in xrange(R*ZR)]

M = [list(line.strip()) for line in sys.stdin]

for r in xrange(R):
    for c in xrange(C):
        for zr in xrange(ZR):
            final[r*ZR+zr][c*ZC:c*ZC+ZC+1] = [M[r][c]]*ZC

for row in final:
    print ''.join(row)
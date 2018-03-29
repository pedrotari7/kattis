import sys

R, C = map(int, next(sys.stdin).strip().split())


g = [_.strip() for _ in sys.stdin]

result = [0, 0, 0 ,0, 0]

for r in xrange(R-1):
    for c in xrange(C-1):
        spot = g[r][c:c+2] + g[r+1][c:c+2]
        if '#' not in spot:
            result[spot.count('X')] += 1

print '\n'.join(map(str,result))

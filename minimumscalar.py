import sys

T = int(next(sys.stdin).strip())

for  _ in xrange(T):
    n = next(sys.stdin)

    v1 = sorted(map(int, next(sys.stdin).strip().split()))
    v2 = sorted(map(int, next(sys.stdin).strip().split()),reverse=True)

    print 'Case #{0}: {1}'.format(_+1, sum(x*y for x,y in zip(v1, v2)))


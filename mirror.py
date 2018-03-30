import sys, math

for _ in xrange(int(next(sys.stdin).strip())):
    print 'Test', _+1

    R, C = map(int, next(sys.stdin).strip().split())

    g = [list(next(sys.stdin).strip()) for r in xrange(R)]

    for r in g[::-1]:
        print ''.join(r[::-1])
import sys

n = int(next(sys.stdin).strip())

for _ in xrange(n):
    k = int(next(sys.stdin).strip())
    print 2**k - 1
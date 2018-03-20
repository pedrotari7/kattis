import sys
X = int(next(sys.stdin))
N = int(next(sys.stdin))

print sum([X-int(next(sys.stdin)) for _ in xrange(N)]) + X
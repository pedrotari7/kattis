import sys
N = int(next(sys.stdin))

for _ in xrange(N):
    s = next(sys.stdin)
    if '+' in s:
        print eval(s)
    else:
        print 'skipped'
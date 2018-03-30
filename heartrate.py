import sys, math

for _ in xrange(int(next(sys.stdin).strip())):
    b, p = map(float, next(sys.stdin).strip().split())
    print (b-1)*60/p, b*60/p, (b+1)*60/p
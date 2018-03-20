import sys
n = int(next(sys.stdin))

for _ in xrange(n):
    c = int(next(sys.stdin))
    cities = set()
    for _ in xrange(c):
        cities.add(next(sys.stdin).strip())
    print len(cities)
import sys
N, M = map(int, next(sys.stdin).split())

extra = 0
collection = set()

for _ in xrange(N+M):
    c = int(next(sys.stdin))
    if c in collection:
        extra += 1
    else:
        collection.add(c)
print extra
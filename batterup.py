import sys
n = int(next(sys.stdin))

b = [_ for _ in map(int, next(sys.stdin).split()) if _ >= 0]

print sum(b) / float(len(b))
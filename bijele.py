import sys
n = int(next(sys.stdin))

print sum([_<0 for _ in map(int, next(sys.stdin).split())])
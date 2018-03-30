import sys

r = [len(_.strip()) for _ in  sys.stdin]

print sum((max(r) - _)**2 for _ in r[:-1])
import sys

A,B,C,D = map(int, next(sys.stdin).split())

a = sorted([A,B,C,D])

print a[0]*a[2]
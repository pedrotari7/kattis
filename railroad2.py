import sys

X, Y = map(int, next(sys.stdin).strip().split())

if Y % 2 != 0:
    print('impossible')
else:
    print('possible')
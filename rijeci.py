import sys

K = int(next(sys.stdin))

A , B = 1, 0

for k in xrange(K):
    A, B = B, A+B

print A,B
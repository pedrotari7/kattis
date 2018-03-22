import sys

N, M = map(int, next(sys.stdin).split())

s = 's' if abs(N-M) != 1 else ''

if N > M:
    print 'Dr. Chaz needs {0} more piece{1} of chicken!'.format(N-M, s)
else:
    print 'Dr. Chaz will have {0} piece{1} of chicken left over!'.format(M-N, s)
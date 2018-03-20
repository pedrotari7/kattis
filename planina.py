import sys
N = int(next(sys.stdin))
A1 = 3

if N == 1:
    print A1**2
else:
    s = (2**(N-1))*A1 - (2**(N-1)-1)
    print s**2
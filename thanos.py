import sys
from math import log10

n = next(sys.stdin)

for line in sys.stdin:
    P, R, F = map(int, line.strip().split())

    i = 0
    while P <= F:
        P *= R
        i +=1
    print i
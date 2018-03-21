import sys
from itertools import product
from collections import Counter
N, M = map(int, next(sys.stdin).split())

prev = 0

for c in Counter(map(sum,list(product(range(1,M+1),range(1,N+1))))).most_common():
    
    if c[1] >= prev:
        print c[0]
        prev = c[1]
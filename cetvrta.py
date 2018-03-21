import sys
from itertools import product

p1 = tuple(map(int, next(sys.stdin).split()))
p2 = tuple(map(int, next(sys.stdin).split()))
p3 = tuple(map(int, next(sys.stdin).split()))

x = set([p1[0],p2[0],p3[0]])
y = set([p1[1],p2[1],p3[1]])

d = set(product(x,y)) - {p1,p2,p3}

print list(d)[0][0], list(d)[0][1]
import sys
from itertools import combinations

W, _ = map(int, next(sys.stdin).strip().split())

P = [0] +  map(int, next(sys.stdin).strip().split()) + [W]

sizes = set([p[1]-p[0] for p in combinations(P,2)])

print ' '.join(map(str,(sorted(sizes))))

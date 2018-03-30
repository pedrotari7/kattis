import sys

targets = []

def number_of_hits(x, y, targets):
    hits = 0
    for t, p in targets:
        if t == 'circle' and (x-p[0])**2 + (y-p[1])**2 <= p[2]**2:
            hits += 1
        if t == 'rectangle' and x>=p[0] and x<=p[2] and y>=p[1] and y<=p[3]:
            hits += 1
    return hits

for m in xrange(int(next(sys.stdin).strip())):
    line = next(sys.stdin).strip().split()
    targets.append((line[0], map(int, line[1:])))

for n in xrange(int(next(sys.stdin).strip())):
    x, y = map(int, next(sys.stdin).strip().split())
    print number_of_hits(x,y, targets)
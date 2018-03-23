import sys

T = next(sys.stdin)

def noneg(n): return n if n > 0 else 0

for line in sys.stdin:
    turtles = map(int, line.strip().split())
    print sum(noneg(turtles[t+1] - 2*turtles[t]) for t in xrange(len(turtles)-2))

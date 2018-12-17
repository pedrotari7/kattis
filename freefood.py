import sys
import operator

N = next(sys.stdin)

print len(set(reduce(operator.add, [range(l,h+1) for l,h in [map(int,line.strip().split()) for line in sys.stdin]])))
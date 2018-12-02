import sys
from collections import defaultdict
from itertools import combinations

while 1:

    n = int(next(sys.stdin).strip())
    
    if n == -1 : break

    net = defaultdict(list)

    for i in xrange(n):
        net[i] = [j for j,a in enumerate(next(sys.stdin).strip()) if a == '1']

    print net

    weak = []

    for v in net:
        print 'v', v
        print 'net[v]', net[v] 
        print 'net[v]', net[v] 
        
        for p in combinations(net[v], 2):
            if p[1] in net[p[0]] and p[0] in net[p[1]]:
                print p
                # weak.append(p[0])
                # weak.append(p[1])
                # if v not in weak: weak.append(v)
        print weak
            
                

    print net

print sorted(weak)
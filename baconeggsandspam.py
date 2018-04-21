import sys
from collections import defaultdict

while 1:
    n = int(next(sys.stdin).strip())
    if n == 0: break
    items = defaultdict(list)
    for _ in xrange(n):
        info = next(sys.stdin).strip().split()
        client = info[0]
        for i in info[1:]:
           items[i].append(client)
    for p in sorted(items.keys()):
        print p, ' '.join(sorted(items[p]))
    print


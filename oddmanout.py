import sys
from collections import Counter

N = int(next(sys.stdin))

for n in xrange(N):
    G = int(next(sys.stdin))
    print 'Case #'+str(n+1)+':',Counter(next(sys.stdin).split()).most_common()[-1][0]
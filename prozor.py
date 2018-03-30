from __future__ import print_function
import sys

R, S, K = map(int, next(sys.stdin).strip().split())

W = [list(_.strip()) for _ in sys.stdin]

best = (0, ())

for r in xrange(R-K+1):
    for s in xrange(S-K+1):
        w = [W[r+i][s+1:s+K-1] for i in xrange(1,K-1)]
        killed = sum(w, []).count('*')
        if killed > best[0]: best = (killed, (r,s))

_, (a,b) = best
print(_)

for r in xrange(R):
    for s in xrange(S):

        if (r==a and s==b) or (r==a and s==b+K-1) or (r==a+K-1 and s==b) or (r==a+K-1 and s==b+K-1):
            print('+', end='')
        elif (s==b or s==b+K-1) and a<r<a+K:
            print('|', end='')
        elif (r==a or r==a+K-1) and b<s<b+K:
            print('-', end='')
        else:
            print(W[r][s], end='')
    print()
import sys

n = int(next(sys.stdin).strip())

diff = [a==b for a,b in zip(next(sys.stdin).strip(), next(sys.stdin).strip())]

if (n%2!=0 and sum(diff)==0) or (n%2==0 and all(diff)):
    print 'Deletion succeeded'
else:
    print 'Deletion failed'
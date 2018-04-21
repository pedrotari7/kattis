import sys

T = int(next(sys.stdin).strip())

for _ in xrange(T):
    n = int(next(sys.stdin).strip())
    votes = [(int(next(sys.stdin).strip()),v+1) for v in xrange(n)]
    majority = [i for v, i in votes if v > sum([j for j,k in votes])/2]
    if majority:
        print 'majority winner', majority[0]
    else:
        s = sorted(votes, reverse=True)
        if s[0][0] != s[1][0]:
            print 'minority winner', s[0][1]
        else:
            print 'no winner'

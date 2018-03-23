import sys

n = -1

c = 1

while 1:
    n = int(next(sys.stdin).strip())
    if n == 0: break

    print 'SET', c
    l1, l2 = [], []

    for j, _ in enumerate([next(sys.stdin).strip() for i in xrange(n)]):
        if j % 2 == 0:
            l1.append(_)
        else:
            l2.append(_)
    print '\n'.join(l1 + l2[::-1])

    c += 1


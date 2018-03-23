import sys

n = -1

while n != 0:
    n = int(next(sys.stdin).strip())
    if n != 0:
        l1 = [int(next(sys.stdin).strip()) for i in xrange(n)]
        l2 = [int(next(sys.stdin).strip()) for i in xrange(n)]

        sorted_l1, sorted_l2 = sorted(l1), sorted(l2)

        order = [sorted_l1.index(_) for _ in l1]

        for num in [sorted_l2[_] for _ in order]:
            print num

        print
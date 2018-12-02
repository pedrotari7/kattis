import sys
from itertools import combinations

def closest(nums, n):
    prev = (-1, 0)
    for num in nums:
        if prev[0] >= 0 and prev[0] < abs(num-n):
            break
        prev = (abs(num-n), num)
    return prev[1]
i = 0

while 1:
    try:
        n = int(next(sys.stdin).strip())
        i += 1
    except:
        break
    nums = [int(next(sys.stdin).strip()) for _ in xrange(n)]

    m = int(next(sys.stdin).strip())

    targets = [int(next(sys.stdin).strip()) for _ in xrange(m)]

    sums = map(sum, combinations(nums,2))

    print 'Case {0}:'.format(i)

    for t in targets:
        print 'Closest sum to {0} is {1}.'.format(t, closest(sorted(sums), t))
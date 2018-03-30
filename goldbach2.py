import sys
from itertools import combinations_with_replacement
from collections import defaultdict


def primes(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

n = next(sys.stdin)

nums = [int(_.strip()) for _ in sys.stdin]

p = primes(max(nums))

represent = defaultdict(list) 

for s in combinations_with_replacement(p,2):
    if sum(s) in nums:
        represent[sum(s)].append(s)

for num in nums:
    if len(represent[num]):
        print num, 'has', len(represent[num]), 'representation(s)'
        for r in represent[num]:
            print '+'.join(map(str,r))
        print
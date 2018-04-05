import sys

import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor



for num in map(str.strip, sys.stdin):
    num = int(num)
    s = sum(divisorGenerator(num))+1

    text = 'perfect'
    extra = ''

    print num,

    if s != num:
        if num-2 <= s <= num+2: print 'almost perfect'
        else: print 'not perfect'
    else: print 'perfect'
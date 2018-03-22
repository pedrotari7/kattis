import sys
from itertools import chain

n = next(sys.stdin)

def split(arr):
    count = int(len(arr)**(1/2.))
    return [arr[i*count:i*count + count] for i in range(count)]

for m in sys.stdin:
    print ''.join(chain.from_iterable(zip(*zip(*zip(*split(list(m.strip())))))[::-1]))
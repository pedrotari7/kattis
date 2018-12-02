import sys
from functools import reduce

T = next(sys.stdin)

for line in sys.stdin:
    n = int(line.strip())
    print(reduce(lambda x, y: x*y, range(1,n+1)) % 10)
import sys

P = next(sys.stdin)

for line in sys.stdin:
    K, N = map(int, line.split())
    print(K,sum(range(N+1))+N)
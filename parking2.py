import sys

t = int(next(sys.stdin).strip())

for _ in range(t):
    n = next(sys.stdin)
    p = list(map(int, next(sys.stdin).strip().split()))
    print(2*(max(p)-min(p)))
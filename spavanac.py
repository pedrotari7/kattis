import sys

H, M = map(int, next(sys.stdin).split())

m = (M - 45) % 60

if m > M:
    H = (H - 1) % 24

print H,m
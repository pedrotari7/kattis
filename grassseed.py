import sys

C = float(next(sys.stdin))
L = int(next(sys.stdin))

cost = 0

for line in sys.stdin:
    w, l = map(float, line.split())
    cost += w * l * C

print cost
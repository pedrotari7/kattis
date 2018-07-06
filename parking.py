import sys

cost = [0] + [int(_) for _ in next(sys.stdin).strip().split()]

total = 0

trucks = [tuple(map(int, _)) for _ in  map(str.split, sys.stdin)]

for t in range(1, 101):
    count = sum(_[0] <= t < _[1] for _ in trucks)

    total += count*cost[count]

print(total)
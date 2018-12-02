import sys

N, Q = next(sys.stdin).strip().split()

pos = list(map(int, next(sys.stdin).strip().split()))

for line in sys.stdin:
    mode, n1, n2 =map(int, line.strip().split())

    if mode  == 1:
        pos[n1-1] = n2
    elif mode == 2:
        print(max(pos[n1-1], pos[n2-1]) - min(pos[n1-1], pos[n2-1]))

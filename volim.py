import sys

K = int(next(sys.stdin).strip()) - 1 
N = int(next(sys.stdin).strip())

players = [1, 2, 3, 4, 5, 6, 7, 8]

total = 0
limit = 3 * 60 + 30

for line in sys.stdin:
    time, Z = line.strip().split() 
    time = int(time)
    if Z == 'T':
        if total + time > limit:
            break
        total += time
        K = (K + 1) % 7
    elif Z in ['N','P']:
        if total + time > limit:
            break
        total += time

print players[K]
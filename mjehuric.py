import sys

target = [1, 2, 3, 4, 5]

current = [int(_) for _ in next(sys.stdin).split()]

i = -1

while current != target:
    i = (i + 1) % 4

    if current[i] > current[i+1]:
        current[i], current[i+1] = current[i+1], current[i]
        print(' '.join(map(str, current)))






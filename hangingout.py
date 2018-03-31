import sys

L, x = map(int, next(sys.stdin).strip().split())

roof = 0
reject = 0

for line in sys.stdin:
    line = line.strip().split()

    if line[0] == 'enter':
        if roof + int(line[1]) > L:
            reject += 1
        else:
            roof += int(line[1])
    elif line[0] == 'leave':
        roof -= int(line[1])

print reject
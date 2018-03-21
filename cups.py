import sys

n = next(sys.stdin)

cups = []

for A,B in map(str.split,sys.stdin):

    if A.isdigit():
        cups.append((int(A)/2, B))
    else:
        cups.append((int(B), A))

for _ in [c[1] for c in sorted(cups, reverse=False)]:
    print _
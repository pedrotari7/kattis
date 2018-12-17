import sys

next(sys.stdin)

print max([i+_+1 for i,_ in enumerate(sorted([int(line) for line in next(sys.stdin).strip().split()], reverse=True))]) + 1

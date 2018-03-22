import sys

n = next(sys.stdin)

for line in sys.stdin:
    print len(line.strip())
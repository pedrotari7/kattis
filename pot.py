import sys

n = int(next(sys.stdin))

print sum(int(num.strip()[:-1])**int(num.strip()[-1]) for num in sys.stdin)
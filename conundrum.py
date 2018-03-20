import sys

n = 'PER'

pwd = list(next(sys.stdin).upper())

day = 0

for i,p in enumerate(pwd):
    if p != n[i%len(n)]:
        day += 1
print day
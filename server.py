import sys

n, T = map(int,next(sys.stdin).split())

times = map(int,next(sys.stdin).split())

total = 0
s = 0

for i in times:
    total += i
    if total > T:
        break
    s+=1
print s
    
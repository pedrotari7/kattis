import sys

n = int(next(sys.stdin))

i = 1

while n!=1:
    i+=1
    n /= i
print i
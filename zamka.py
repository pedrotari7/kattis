import sys

def sum_digits(n):
   return sum(map(int, list(str(n))))

L = int(next(sys.stdin))
D = int(next(sys.stdin))
X = int(next(sys.stdin))

upper, lower = D, L
N, M = 0, 0

while not M or not N:
    if not N:
        if sum_digits(lower) == X:
            N = lower
        else:
            lower += 1
    if not M:
        if sum_digits(upper) == X:
            M = upper
        else:
            upper -= 1

print N
print M


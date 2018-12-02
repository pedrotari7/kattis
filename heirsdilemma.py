import sys

L, H = map(int, next(sys.stdin).split())

count = 0

for n in range(L, H+1):
    s = str(n)
    count += '0' not in s and len(set(s)) == len(s) and all(n % int(_) == 0 for _ in s)

print(count)
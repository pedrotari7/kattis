import sys

for n in sys.stdin:
    n = int(n)
    if n != 0:
        s = sum(map(int, list(str(n))))
        i = 11
        while s != sum(map(int, list(str(n*i)))):
            i += 1
        print i
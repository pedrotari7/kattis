import sys

for line in sys.stdin:
    n, m = map(int, line.split())

    if n != 0 and m != 0:
        print str(n/m) + ' ' + str(n%m) + ' / ' + str(m)

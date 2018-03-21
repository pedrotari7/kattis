import sys

N = int(next(sys.stdin))

for line in sys.stdin:
    a, b, c = map(int, line.split())

    if c in [a/float(b), a+b, a-b, a*b, b/float(a), b+a, b-a, b*a]:
        print 'Possible'
    else:
        print 'Impossible'

import sys
n = int(next(sys.stdin))

names = [_.strip() for _ in sys.stdin]

if names == sorted(names):
    print 'INCREASING'
elif names == sorted(names, reverse=True):
    print 'DECREASING'
else:
    print 'NEITHER'


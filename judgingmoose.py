import sys

l, r = map(int, next(sys.stdin).split())

if l == r: 
    if l == 0:
        print 'Not a moose'
    else:
        print 'Even', l+r
else:
    print 'Odd', 2*max([l, r])
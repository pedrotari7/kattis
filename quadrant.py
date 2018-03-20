import sys
x = int(next(sys.stdin))
y = int(next(sys.stdin))

if x > 0 and y > 0:
    print 1
elif x > 0 and y < 0:
    print 4
elif x < 0 and y > 0:
    print 2
elif x < 0 and y < 0:
    print 3
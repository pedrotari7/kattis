import sys

n = int(next(sys.stdin))

for line in sys.stdin:
    r, e, c = map(int, line.split())
    if r < e - c:
        print 'advertise'
    elif r > e - c:
        print 'do not advertise'
    else:
        print 'does not matter'

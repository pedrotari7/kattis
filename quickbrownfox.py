import sys

n = next(sys.stdin)

abc = set([chr(i) for i in xrange(ord('a'), ord('z')+1)])

for line in sys.stdin:
    s = set([_ for _ in line.strip().lower() if _.isalpha()])

    missing = ''.join(abc - s)

    if missing:
        print 'missing', missing
    else:
        print 'pangram'
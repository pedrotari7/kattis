import sys
line = next(sys.stdin)
i = 1
while line:
    a,b = map(int, line.strip().split())
    line = next(sys.stdin)
    c,d = map(int, line.strip().split())
    print 'Case {0}:'.format(i)
    det = a*d - b*c
    print d/det, -1*b/det
    print -1*c/det, a/det
    try:
        line = next(sys.stdin)
        line = next(sys.stdin)
    except:
        line = ''
    i += 1
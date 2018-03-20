import sys
t = int(next(sys.stdin))


for _ in xrange(t):
    n = int(next(sys.stdin))
    fl = []
    for _ in xrange(n):
        fl.append(next(sys.stdin).strip())

    valid = True
    for i,a in enumerate(fl):
        if not valid:
            break
        for j,b in enumerate(fl):
            if i != j:
                if a.startswith(b) or b.startswith(a):
                    valid = False
                    break

    if valid:
        print 'Yes'
    else:
        print 'No'

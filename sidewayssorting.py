import sys

while 1:
    r,c = map(int, next(sys.stdin).strip().split())

    if (r,c) == (0,0): break

    data = [next(sys.stdin).strip() for i in xrange(r)] 

    print data

    data = [(d.lower(), d) for d in data]

    print data

    

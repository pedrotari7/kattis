import sys

n = int(next(sys.stdin))

for _ in xrange(n):

    s1 = next(sys.stdin).strip()
    s2 = next(sys.stdin).strip()

    print s1
    print s2

    print ''.join(['*' if (ord(a)-ord(b)) != 0 else '.' for a,b in zip(s1,s2)])
    print
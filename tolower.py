import sys

P, T = map(int,next(sys.stdin).split())

tests = [(line[0].lower() + line[1:]) == line.lower() for line in map(str.strip,sys.stdin)]

print sum(all(tests[T*p:T*p+T]) for p in xrange(P))


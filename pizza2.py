import sys

R, C = map(int,next(sys.stdin).split())

print 100*(R-C)**2/float(R**2)
import sys

b = next(sys.stdin).strip()

if len(b) % 3 != 0:
    b = '0'*(3 - (len(b) % 3)) + b

print ''.join([str(int(b[i*3:i*3 + 3],2)) for i in xrange(len(b)/3)])
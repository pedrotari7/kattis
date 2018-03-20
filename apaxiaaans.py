import sys

s = next(sys.stdin)
print ''.join([c for i,c in enumerate(s) if i == 0 or c != s[i-1]])
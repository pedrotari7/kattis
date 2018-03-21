import sys

words = next(sys.stdin).split()

print 'yes' if len(set(words)) == len(words) else 'no'
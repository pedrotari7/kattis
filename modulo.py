import sys

print len(set([ int(_)%42 for _ in sys.stdin]))
    
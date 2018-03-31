import sys

line = next(sys.stdin).strip()

d = dict()

while line:
    value, key = line.split()
    d[key] = value
    line = next(sys.stdin).strip()

for line in map(str.strip, sys.stdin):
    if line in d:
        print d[line]
    else:
        print 'eh'

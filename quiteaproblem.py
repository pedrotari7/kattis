import sys

for line in map(str.strip, sys.stdin):
    if 'problem' in line.lower():
        print 'yes'
    else:
        print 'no'

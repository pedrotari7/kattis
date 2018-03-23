import sys

d = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')

for line in sys.stdin:
    if line != '0':
        N = int(line.strip().split()[0])
        s = line.strip().split()[1].upper()
        print ''.join(d[(d.index(c) + N) % len(d)] for c in s[::-1])
exit(0)
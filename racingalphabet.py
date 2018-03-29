import sys, math

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ \''

D = 60

d = 2 * math.pi * (D / 2.) / 28
s = 15

N = next(sys.stdin)

for line in sys.stdin:
    line = list(line.strip())
    total = len(line)
    for i in xrange(len(line) - 1):
        p = (abc.index(line[i]), abc.index(line[i+1]))
        l = min(p)
        r = max(p)

        total += min(abs(l-r), l + len(abc) - r) * d / s

    print total
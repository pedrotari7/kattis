import sys

for i, stats in enumerate(sys.stdin):
    samples = map(int, stats.strip().split()[1:])
    print 'Case {}: {} {} {}'.format(i+1 ,min(samples), max(samples), max(samples)-min(samples))
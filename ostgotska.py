import sys

line = next(sys.stdin).strip().split()

total = len(line)

ae = sum('ae' in _ for _ in line)

if ae / float(total) >= 0.4:
    print 'dae ae ju traeligt va'
else:
    print 'haer talar vi rikssvenska'
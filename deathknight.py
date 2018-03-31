import sys

n = int(next(sys.stdin).strip())
losses = 0
for line in map(str.strip, sys.stdin):
    losses += sum((line[i],line[i+1]) == ('C','D') for i in xrange(len(line)-1))        

print n-losses
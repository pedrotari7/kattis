import sys 
data = next(sys.stdin)

hiss = False

for i in xrange(1,len(data)):
    if data[i] == data[i-1] and data[i] == 's':
        hiss = True
        break

if hiss:
    print 'hiss'
else:
    print 'no hiss'
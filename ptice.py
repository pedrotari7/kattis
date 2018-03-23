import sys

N = int(next(sys.stdin))
A = next(sys.stdin).strip()

Adrian = str('ABC'*(N/3+1))[:N]
Bruno = str('BABC'*(N/4+1))[:N]
Goran = str('CCAABB'*(N/6+1))[:N]

results = [
            sum(Adrian[i]==A[i] for i in xrange(N)),
            sum(Bruno[i]==A[i] for i in xrange(N)),
            sum(Goran[i]==A[i] for i in xrange(N))
]

print max(results)

for i,_ in enumerate(results):
    if _  == max(results):
        if i == 0:
            print 'Adrian'
        if i == 1:
            print 'Bruno'
        if i == 2:
            print 'Goran'

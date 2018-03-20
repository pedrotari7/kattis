import sys, math

n = next(sys.stdin)

for message in sys.stdin:
    L = len(message.strip())
    K = int(math.ceil(math.sqrt(L)))

    message = message.strip().ljust(K*K,'*')

    m = [['']*K for _ in xrange(K)]

    for i in xrange(K):
        for j in xrange(K):
            m[i][j] = message[K*i + j]

    print ''.join([''.join(reversed(_)).replace('*','') for _ in map(list, zip(*m))])
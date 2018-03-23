import sys

g = []

N = 4

def move(a):
    j = 0
    k = 0
    while j < N-1 and k < N-1:
        k += 1
        if a[j] == 0:
            del(a[j])
            a.append(0)
        else:
            j += 1

    for j in xrange(N-1):
        if a[j] == a[j+1]:
            a[j] *= 2
            del(a[j+1])
            a.append(0)
    return a

for _ in xrange(N):
    g.append(map(int, next(sys.stdin).split()))

d = int(next(sys.stdin))

for i in xrange(N):
    if d == 0: # left
        g[i] = move(g[i])
    elif d == 1: # up
        temp = [g[j][i] for j in xrange(N)]
        temp = move(temp)
        for j in xrange(N):
            g[j][i] = temp[j]
    elif d == 2: # right
        g[i] = move(g[i][::-1])[::-1]
    elif d == 3: # down
        temp = [g[j][i] for j in xrange(N-1,-1,-1)]
        temp = move(temp)
        for j in xrange(N):
            g[j][i] = temp[N-1-j]

for r in g:
    print ' '.join(map(str,r))

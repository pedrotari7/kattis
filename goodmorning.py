import sys

T = int(next(sys.stdin).strip())

a = [('1','2','3'), ('4','5','6'), ('7','8','9'), (' ','0',' ')]

final = []

curr = [[(j,i)] for j in xrange(4) for i in xrange(3)]

while curr:
    n = curr.pop(0)

    new_num = ''.join([a[i][j] for i,j in n if a[i][j] != ' '])
    if new_num and int(new_num) <= 200:
        final.append(int(new_num))

    if len(n) < 3:
        for istep in xrange(4):
            if i + istep < 4:
                curr.append(n+[(n[-1][0]+istep, n[-1][1])])
                for jstep in xrange(3):
                    if j + jstep < 3:
                        curr.append(n+[(n[-1][0]+istep, n[-1][1]+jstep)])        

final = set(final)

for t in xrange(T):
    num = int(next(sys.stdin).strip())
    print sorted(final, key=lambda x:abs(x-num))[0]
    
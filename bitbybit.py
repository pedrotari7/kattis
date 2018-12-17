import sys

for N in sys.stdin:
    N = int(N.strip())

    if N == 0: break

    bits = ['?'] * 32

    for n in xrange(N):

        inst = next(sys.stdin).strip().split()
        if inst[0] == 'SET':
            bits[int(inst[1])] = 1
        elif inst[0] == 'CLEAR':
            bits[int(inst[1])] = 0
        elif inst[0] == 'AND':
            i,j = map(int, (inst[1],inst[2]))
            if bits[i] == 0 or bits[j] == 0:
                bits[i] = 0
            elif bits[i] != '?' and bits[j] != '?':
                bits[i] = bits[i] & bits[j]
            else:
                bits[i] = '?'
        elif inst[0] == 'OR':
            i,j = map(int, (inst[1],inst[2]))
            if bits[i] == 1 or bits[j] == 1:
                bits[i] = 1
            elif bits[i] != '?' and bits[j] != '?':
                bits[i] = bits[i] | bits[j]
            else:
                bits[i] = '?'
    print ''.join(map(str,bits))[::-1]
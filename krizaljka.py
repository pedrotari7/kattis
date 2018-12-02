import sys

w1, w2 = next(sys.stdin).strip().split()

for i,d in enumerate(w1):
    if d in w2:
        idy = w2.index(d)
        idx = i
        break

for i, l in enumerate(w2):

    if i == idy:
        print(w1)
    else:
        r = list('.' * len(w1))
        r[idx] = l
        print(''.join(r))

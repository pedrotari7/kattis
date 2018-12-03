import sys

pieces,black,white = [],[],[]
order = ['K','Q','R','B','N','P']
c = 'abcdefgh'

for j, line in enumerate(range(8)):
    next(sys.stdin)

    try:
        line = next(sys.stdin).strip()
    except:
        break

    pieces += [(line[i], (int((i-2)/4)+1,8-j)) for i in range(2,len(line), 4) if line[i].isalpha()]

for p in pieces:
    if p[0].islower():
        black += [[p[0].upper(), c[p[1][0]-1], str(p[1][1])]]
    else:
        white += [[p[0], c[p[1][0]-1], str(p[1][1])]]


white = sorted(white, key=lambda x: (order.index(x[0]), int(x[2]), x[1]))
black = sorted(black, key=lambda x: (order.index(x[0]), 8-int(x[2]), x[1]))


print('White:', ','.join([''.join(_) for _ in white]).replace('P',''))
print('Black:', ','.join([''.join(_) for _ in black]).replace('P',''))
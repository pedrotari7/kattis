import sys

rows = 'abcdefgh'

def piece(p):
    if len(p) == 3:
        a = p[0]
        x,y = rows.index(p[1]), 8-int(p[2])+1
    else:
        a = 'P'
        x,y = rows.index(p[0]), 8-int(p[1])+1

    return (a, (x,y))

white = next(sys.stdin).strip().split(' ')
white = list(map(piece, [] if len(white) == 1 else white[1].split(',')))

black = next(sys.stdin).strip().split(' ')
black = list(map(piece, [] if len(black) == 1 else black[1].split(',')))

def get_row(i):
    if i % 2 == 0:
        row = ''.join([''.join(_) for _ in zip(['|...']*4,['|:::']*4)])
    else:
        row = ''.join([''.join(_) for _ in zip(['|:::']*4,['|...']*4)])

    row = list(row)

    for p in white:
        if i+1 == p[1][1]:
            # print(p)
            row[4*(p[1][0])+2] = p[0]
    for p in black:
        if i+1 == p[1][1]:
            # print(p)
            row[4*(p[1][0])+2] = p[0].lower()
    return ''.join(row)

for i in range(8):
    print('+---'*8+'+')
    print(get_row(i) + '|')
print('+---'*8+'+')

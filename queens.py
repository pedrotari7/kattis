import sys

N = next(sys.stdin)

queens = [(x, y)for x, y in map(lambda a: map(int,a.strip().split()), sys.stdin)]

def is_correct():
    rows, collumns, ldiag, rdiag = [], [], [], []
    for i in range(len(queens)):
        if queens[i][0] in rows or queens[i][1] in collumns or sum(queens[i]) in rdiag or queens[i][0]-queens[i][1] in ldiag:
            return True
        rows.append(queens[i][0])
        collumns.append(queens[i][1])
        rdiag.append(sum(queens[i]))
        ldiag.append(queens[i][0]-queens[i][1])
    return False

if is_correct():
    print('INCORRECT')
else:
    print('CORRECT')
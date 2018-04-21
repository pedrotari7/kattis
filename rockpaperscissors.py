import sys

winners = {('rock','paper'):'paper',('rock','scissors'):'rock',('paper','rock'):'paper',('paper',
           'scissors'):'scissors',('scissors','rock'):'rock',('scissors','paper'):'scissors'}

while 1:
    line = next(sys.stdin).strip()

    if line == '0': break

    n, k = map(int, line.split())

    results = {str(_+1):{'w':0, 'l':0} for _ in xrange(n)}

    total = k*n*(n-1)/2

    for _ in xrange(total):
        line = next(sys.stdin).strip().split()

        p1, m1, p2, m2 = line

        if m1 == m2: continue

        g, p = (m1, m2), (p1, p2)

        winner = p[g.index(winners[g])]
        loser = p[(p.index(winner)+1)%2]

        results[winner]['w'] += 1
        results[loser]['l'] += 1

    for player in results:
        if results[player]['w'] + results[player]['l'] == 0:
            print '%.3f' % 0
        else:
            print '%.3f' % round(results[player]['w'] / float(results[player]['w'] + results[player]['l']),3)

    print

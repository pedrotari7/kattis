import sys
from collections import defaultdict

price = 0.1

day = 1
for line in map(str.strip, sys.stdin):
    if line == 'OPEN':
        if day > 1: print
        print 'Day', day
        clients = defaultdict(dict)
    elif 'ENTER' in line:
        _, name, entry = line.split()
        if 'total' not in clients[name]: clients[name]['total'] = 0
        clients[name]['entry'] = int(entry)
    elif 'EXIT' in line:
        _, name, exit_time = line.split()
        clients[name]['total'] += int(exit_time) - clients[name]['entry']
    elif line == 'CLOSE':
        for name in sorted(clients.keys()):
            print name, '$%.2f' % (clients[name]['total']*price)
        day += 1

import sys
from collections import defaultdict

price = 0.1

day = 1
for line in map(str.strip, sys.stdin):
    if line == 'OPEN':
        print 'Day', day
        clients = defaultdict(dict)
    elif 'ENTER' in line:
        _, name, entry = line.split()
        clients[name]['entry'] = int(entry)
    elif 'EXIT' in line:
        _, name, exit_time = line.split()
        clients[name]['exit'] = int(exit_time)
    elif line == 'CLOSE':
        for c in sorted(clients.keys()):
            print c, '%.2f' % ((clients[c]['exit']-clients[c]['entry'])*price)
        day += 1
        print


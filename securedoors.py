import sys

n = next(sys.stdin)

entries = []

for m in sys.stdin:
    action, name = m.strip().split()

    if action == 'entry':
        print name, 'entered',
        if name in entries:
            print '(ANOMALY)',
        else:
            entries.append(name)
        print

    elif action == 'exit':
        print name, 'exited',
        if name not in entries:
            print '(ANOMALY)',
        else:
            entries.remove(name)
        print
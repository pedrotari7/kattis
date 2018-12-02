import sys

from collections import defaultdict

family = defaultdict(dict)

for line in sys.stdin:
    command = line.split(' ')[0]
    info = map(str.strip, ' '.join(line.split(' ')[1:]).strip().split(':'))

    if command == 'BIRTH':
        child, birth, mother, father = info
        family[child] = {'birth':birth, 'mother':mother, 'father':father}
        if 'children' not in family[mother]: family[mother]['children'] = []
        family[mother]['children'].append(child)
        if 'children' not in family[father]: family[father]['children'] = []
        family[father]['children'].append(child)
    elif command == 'DEATH':
        person, date = info
        family[person]['death'] = date  
    elif command == 'ANCESTORS':
        person = info[0]
        print 'ANCESTORS of', person
        for parent in sorted([family[person]['mother'],family[person]['father']]):
            print ' ',parent,family[parent]['birth'], '-',
            if 'death' in family[parent]:
                print family[parent]['death'],
            print
            for p in sorted([family[parent]['mother'],family[parent]['father']]):
                print '   ', p
        print
    elif command == 'DESCENDANTS':
        person = info[0]
        print 'DESCENDANTS of', person
        for child in sorted(family[person]['children']):
            print ' ',child,family[child]['birth'], '-',
            if 'death' in family[child]:
                print family[child]['death'],
            print
        print
    elif command == 'QUIT':
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
import sys

problems = dict()

for line in map(str.strip, sys.stdin):
    if line != '-1':
        time, letter, result = line.split()

        if letter not in problems:
            problems[letter] = {'solved':False, 'time':0}

        if result == 'wrong' and not problems[letter]['solved']:
            problems[letter]['time'] += 20            
        elif result == 'right' and not problems[letter]['solved']:
            problems[letter]['solved'] = True
            problems[letter]['time'] += int(time)

solved = [problems[p]['time'] for p in problems if problems[p]['solved']]
            
print len(solved), sum(solved)
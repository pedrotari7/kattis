import sys

n = next(sys.stdin)

for line in sys.stdin:
    name, study, birth, courses = line.strip().split()
    courses = int(courses)
    study = map(int, study.split('/'))
    birth = map(int, birth.split('/'))

    state = 'coach petitions'

    if study[0] >= 2010 or birth[0] >= 1991:
        state = 'eligible' 
    elif courses >= 41:
        state = 'ineligible'
    print name, state
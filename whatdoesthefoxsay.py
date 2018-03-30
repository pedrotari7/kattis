import sys

n = int(next(sys.stdin).strip())

for _ in xrange(n):
    phrase = next(sys.stdin).strip().split()
    animal = next(sys.stdin).strip()
    sounds = []

    while animal != 'what does the fox say?':
        sounds.append(animal.split()[-1])
        animal = next(sys.stdin).strip()

    phrase = filter(lambda a: a not in sounds, phrase)
    print ' '.join(phrase)
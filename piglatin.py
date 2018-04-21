import sys

vowels = 'aeiouy'

for line in map(str.strip, sys.stdin):
    for word in line.split():
        if word[0] in vowels:
            print word + 'yay',
        else:
            first = min([word.index(v) for v in vowels if v in word])
            print word[first:] + word[:first] + 'ay',
    print
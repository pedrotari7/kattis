from __future__ import print_function
import sys

words = set()

for line in sys.stdin:
    for word in line.strip().split():
        if word.lower() in words:
            print('.', end=' ')
        else:
            words.add(word.lower())
            print(word, end=' ')
    print()    
    

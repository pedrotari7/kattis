import sys

max_n = 1000
min_n = 1

response = 'lower'

while 1:
    n = min_n + (max_n - min_n)/2

    print n

    response = next(sys.stdin).strip()

    if response == 'correct':
        break
    elif response == 'lower':
        max_n = n - 1
    elif response == 'higher':
        min_n = n + 1
    
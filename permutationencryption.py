import sys

while 1: 
    line = next(sys.stdin).strip()
    if line == '0': break
    
    numbers = map(int, line.split())[1:]
    message = next(sys.stdin).strip()

    final = ''

    r = len(message) / len(numbers) if len(message) % len(numbers) == 0 else len(message) / len(numbers) + 1

    for i in xrange(r):
        seg = message[i*len(numbers):i*len(numbers)+len(numbers)].ljust(len(numbers))           
        for j, c in enumerate(seg):
            final += seg[numbers[j]-1]
    print '\'' + final + '\''


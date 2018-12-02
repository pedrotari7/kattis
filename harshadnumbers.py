import sys

def harshad(number):
    return number % sum([int(_) for _ in str(number)]) == 0

n = int(next(sys.stdin).strip())

while not harshad(n):
    n += 1
print(n)
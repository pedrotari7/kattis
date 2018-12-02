import sys

N = next(sys.stdin)

numbers = sorted(map(int, next(sys.stdin).split()))

print numbers

groups = []

current = None

for i, num in enumerate(numbers[:-1]):
    print i, num, current, numbers[i+1]
    if not current:
        current = num

    if current - num == 1 and numbers[i+1] > num + 1:
        groups.append(str(current))
        groups.append(str(num))
        current = None
    if current - num > 1 and numbers[i+1] > num + 1:
        groups.append(str(current) + '-' + str(num))
        current = None

    print i, current

print ' '.join(groups)
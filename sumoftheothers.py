import sys

for line in sys.stdin:
    numbers = sorted(map(int, line.strip().split()))[::-1]

    for i, num in enumerate(numbers):
        if num == sum(numbers[:i] + numbers[i+1:]):
            print num
            break
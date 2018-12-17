import sys

n = next(sys.stdin)

numbers = [int(n) for n in map(str.strip, sys.stdin)]

mod = 1

while len(set([n % mod for n in numbers])) != len(numbers):
    mod += 1

print mod
import sys, math

P = next(sys.stdin)

for line in sys.stdin:
    K, N = map(int, line.split())

    positive_sum, positive = 0, 0
    odd_sum, odd = 0, 0
    even_sum, even = 0, 0

    i = 1

    while positive < N or odd < N or even < N:
        if positive < N : positive += 1; positive_sum += i
        if odd < N and i % 2 != 0: odd += 1; odd_sum += i
        if even < N and i % 2 == 0: even += 1; even_sum += i
        i+=1

    print K, positive_sum, odd_sum, even_sum

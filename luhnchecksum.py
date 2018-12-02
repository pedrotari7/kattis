import sys

T = next(sys.stdin)

output = ['FAIL', 'PASS']

for num in map(str.strip, sys.stdin):
    num = num[::-1]
    print(output[sum(int(d) if i%2==0 else sum([int(_) for _ in str(2*int(d))]) for i,d in enumerate(num)) % 10 == 0])
import sys, re

h = re.compile(r'0[xX][0-9a-fA-F]+')

for line in map(str.strip, sys.stdin):
    for num in h.findall(line):
        print num, int(num[2:10].upper(), 16)
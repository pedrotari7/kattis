import sys

d = dict()

d[('xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx')] = '0'
d[('....x','....x','....x','....x','....x','....x','....x')] = '1'
d[('xxxxx','....x','....x','xxxxx','x....','x....','xxxxx')] = '2'
d[('xxxxx','....x','....x','xxxxx','....x','....x','xxxxx')] = '3'
d[('x...x','x...x','x...x','xxxxx','....x','....x','....x')] = '4'
d[('xxxxx','x....','x....','xxxxx','....x','....x','xxxxx')] = '5'
d[('xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx')] = '6'
d[('xxxxx','....x','....x','....x','....x','....x','....x')] = '7'
d[('xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx')] = '8'
d[('xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx')] = '9'
d[('.....','..x..','..x..','xxxxx','..x..','..x..','.....')] = '+'

text = [line for line in map(str.strip,sys.stdin)]

numbers = str(eval(''.join([d[tuple([text[j][i*6:i*6+5] for j in xrange(7)])] for i in xrange((len(text[0])-1)//6+1)])))

final = [[[]]*7]

for j in xrange(7):
    final = []
    for i in xrange(len(numbers)):
        for num in d.iteritems():
            if num[1] == numbers[i]:
                final.append(num[0][j])
    print '.'.join(final)

import sys

cipher = []

key = next(sys.stdin).strip().replace(' ','').upper()
message = next(sys.stdin).strip().replace(' ','').upper()

for c in key:
    if c not in cipher and c != 'Q':
        cipher.append(c)

for l in xrange(ord('A'), ord('Z')+1):
    if chr(l) not in cipher and chr(l) != 'Q':
        cipher.append(chr(l))

cipher = [cipher[i*5:i*5+5] for i in xrange(5)]

cipher_dict = {cipher[i][j]:(i,j) for j in xrange(5) for i in xrange(5)}

final = ''
i = 0

while i < len(message):
    m = message[i:i+2]
    if len(m) == 1 or len(set(m)) == 1: 
        m = m[0] + 'X'
        i += 1
    else:
        i+= 2

    a, b = cipher_dict[m[0]], cipher_dict[m[1]]

    if a[0] == b[0]:
        final += cipher[a[0]][(a[1]+1)%5] + cipher[b[0]][(b[1]+1)%5]
    elif a[1] == b[1]:
        final += cipher[(a[0]+1)%5][a[1]] + cipher[(b[0]+1)%5][b[1]]
    else:
        final += cipher[a[0]][b[1]] + cipher[b[0]][a[1]]

print final
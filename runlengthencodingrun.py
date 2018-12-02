import sys

mode, s = next(sys.stdin).split()

final = ''

if mode == 'E':
    prev,count = s[0], 0
    for l in s:
        if l != prev:
            final += prev + str(count)
            prev = l
            count = 1
        else:
            count+=1
    final += prev + str(count)

elif mode == 'D':
    final = ''.join(s[i]*int(s[i+1]) for i in range(0,len(s),2))

print(final)
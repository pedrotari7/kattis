import sys

class TwoWayDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __len__(self):
        return dict.__len__(self) // 2

morse = TwoWayDict()

morse['A'] = '.-'
morse['B'] = '-...'
morse['C'] = '-.-.'
morse['D'] = '-..'
morse['E'] = '.'
morse['F'] = '..-.'
morse['G'] = '--.'
morse['H'] = '....'
morse['I'] = '..'
morse['J'] = '.---'
morse['K'] = '-.-'
morse['L'] = '.-..'
morse['M'] = '--'
morse['N'] = '-.'
morse['O'] = '---'
morse['P'] = '.--.'
morse['Q'] = '--.-'
morse['R'] = '.-.'
morse['S'] = '...'
morse['T'] = '-'
morse['U'] = '..-'
morse['V'] = '...-'
morse['W'] = '.--'
morse['X'] = '-..-'
morse['Y'] = '-.--'
morse['Z'] = '--..'

morse['_'] = '..--'
morse[','] = '.-.-'
morse['.'] = '---.'
morse['?'] = '----'

for line in sys.stdin:
    m = ''
    numbers = []
    final = ''

    for c in list(line.strip()):
        m += morse[c]
        numbers.append(len(morse[c]))

    i = 0

    while numbers:
        l = numbers.pop()
        if m[i:i+l] == '.':
            final += 'E'
        else:
            final += morse[m[i:i+l]]
        i += l


    print final.split('_')
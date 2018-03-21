import sys

dictionary = {
    'a' : '@',
    'b' : '8',
    'c' : '(',
    'd' : '|)',
    'e' : '3',
    'f' : '#',
    'g' : '6',
    'h' : '[-]',
    'i' : '|',
    'j' : '_|',
    'k' : '|<',
    'l' : '1',
    'm' : '[]\\/[]',
    'n' : '[]\\[]',
    'o' : '0',
    'p' : '|D',
    'q' : '(,)',
    'r' : '|Z',
    's' : '$',
    't' : '\'][\'',
    'u' : '|_|',
    'v' : '\\/',
    'w' : '\\/\\/',
    'x' : '}{',
    'y' : '`/',
    'z' : '2'
}

final = ''

for c in next(sys.stdin):
    c = c.lower() 
    if c.isalpha():
        final += dictionary[c]
    else:
        final += c

print final



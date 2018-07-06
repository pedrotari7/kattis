import sys

def lang2decimal(num, lang):
    return sum(len(lang)**(p)*lang.index(c) for p, c in enumerate(num[::-1]))

def decimal2lang(num, lang):
    result = ''
    n = len(lang)
    while num:
        result += lang[num % n]
        num = int(num / n)

    return result[::-1]

T = next(sys.stdin)

for i, (alien_number, source_language, target_language) in enumerate(map(lambda x: x.strip().split(), sys.stdin)):
    decimal = lang2decimal(alien_number, source_language)
    print('Case #'+str(i+1)+':', decimal2lang(decimal, target_language))

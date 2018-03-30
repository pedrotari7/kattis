import sys, re

deck = {'P': range(1,14),'K': range(1,14),'H': range(1,14),'T': range(1,14)}

cards = re.findall('...', next(sys.stdin))

greska = False

for card in cards:
    suit, value = card[0], int(card[1:])

    if value not in deck[suit]: greska = True; break
    
    deck[suit].remove(value)

if greska:
    print 'GRESKA'
else:
    print len(deck['P']),len(deck['K']),len(deck['H']),len(deck['T'])
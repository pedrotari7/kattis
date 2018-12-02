import sys

victory = {
    'Province': (8, 6),
    'Duchy': (5,3),
    'Estate': (2, 1)
}

treasure = {
    'Gold': (6,3),
    'Silver': (3,2),
    'Copper': (0,1)
}

G, S, C = map(int, next(sys.stdin).split())

buying = G*treasure['Gold'][1]+S*treasure['Silver'][1]+C*treasure['Copper'][1]

if buying < 2:
    print('Copper')
else:
    best_victory = (max([(victory[_][1],_) for _ in victory if victory[_][0] <= buying])[1])
    best_treasure = (max([(treasure[_][1],_) for _ in treasure if treasure[_][0] <= buying])[1])
    print(best_victory + ' or ' + best_treasure)
import sys

meas = dict()

meas['inch'] = (1000, 'th')
meas['in'] = (1000, 'th')

meas['foot'] = (12, 'in')
meas['ft'] = (12, 'in')

meas['yard'] = (3, 'ft')
meas['yd'] = (3, 'ft')

meas['chain'] = (22, 'yd')
meas['ch'] = (22, 'yd')

meas['furlong'] = (10, 'ch')
meas['fur'] = (10, 'ch')

meas['mile'] = (8, 'fur')
meas['mi'] = (8, 'fur')

meas['league'] = (3, 'fur')
meas['lea'] = (3, 'fur')


def normalize_measurements(value, units):
    if units != 'th':
        return normalize_measurements(meas[units][0]*value, meas[units][1])
    else:
        return (value, units)

for unit in meas:
    meas[unit] = normalize_measurements(meas[unit][0], meas[unit][1])

print meas

value, unit_from, _, unit_to = next(sys.stdin).strip().split()
value = int(value)

print value, meas[unit_from][0], meas[unit_to][0]

r = value * (meas[unit_from][0]) / float(meas[unit_to][0])

if int(r) == r: r = int(r)

print r






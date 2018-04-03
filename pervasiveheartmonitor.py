import sys

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

for patient in sys.stdin:
    patient = patient.strip().split()

    names, beat = [], []

    for info in patient:
        if isfloat(info):
            beat.append(float(info))
        else:
            names.append(info)

    print sum(beat)/len(beat) ,' '.join(names)


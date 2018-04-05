import sys

from datetime import datetime, timedelta
s1 = next(sys.stdin).strip()
s2 = next(sys.stdin).strip()

if s1 == s2:
    print '24:00:00'
else:
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

    if tdelta.days < 0:
        tdelta = timedelta(days=0,
                    seconds=tdelta.seconds, microseconds=tdelta.microseconds)

    print ':'.join([_.zfill(2) for _ in str(tdelta).split(':')])
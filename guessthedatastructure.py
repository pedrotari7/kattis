import sys

while 1:
    try:
        n = int(next(sys.stdin).strip())
    except:
        break

    data = []
    ds = ['stack', 'queue', 'priority queue']
    # print n
    for i in xrange(n):
        op, num = map(int, next(sys.stdin).strip().split())
        # print op, num, ds, data,
        if op == 1:
            data.append(num)
        if op == 2:
            if num not in data: ds = ['impossible']; break
            if 'priority queue' in ds and num != max(data):  ds.remove('priority queue')
            if 'stack' in ds and num != data[-1]: ds.remove('stack')
            if 'queue' in ds and num != data[0]: ds.remove('queue')
            data.remove(num)
        # print data, ds
    if len(ds) > 1:
        print 'not sure'
    else:
        print ds[0]
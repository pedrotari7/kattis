import sys

while 1:
    try: pattern = next(sys.stdin).strip()
    except: break
    text = next(sys.stdin).strip()

    try: print text.index(pattern),
    except: pass
    try: text[::-1].index(pattern[::-1]),
    except: pass
    print
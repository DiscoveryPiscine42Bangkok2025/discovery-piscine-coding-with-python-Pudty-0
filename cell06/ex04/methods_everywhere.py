
import sys


def shrink(s):
    print(s[:8])


def enlarge(s):
    print(s + 'Z' * (8 - len(s)))


params = sys.argv[1:]

if not params:
    print("none")
else:
    for p in params:
        if len(p) > 8:
            shrink(p)
        elif len(p) < 8:
            enlarge(p)
        else:  
            print(p)

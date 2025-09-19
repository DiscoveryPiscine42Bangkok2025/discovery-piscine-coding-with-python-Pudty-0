
import sys


def shrink(s):
    print(s[:8])


import sys

def enlarge(s):
    
    print(s + 'Z' * (8 - len(s)))

def shrink(s):
   
    print(s[:8])

def process_params(params):
    
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

def main():
    all_params = sys.argv[1:]
    process_params(all_params)

if __name__ == "__main__":
    main()


import sys


def shrink(s):
    print(s[:8])
import sys

class StringProcessor:

    def enlarge(s):
        print(s + 'Z' * (8 - len(s)))

    
    def shrink(s):
        print(s[:8])

    
    def process(cls, params):
        if not params:
            print("none")
        else:
            for p in params:
                if len(p) > 8:
                    cls.shrink(p)
                elif len(p) < 8:
                    cls.enlarge(p)
                else:
                    print(p)


def main():
    all_params = sys.argv[1:]
    StringProcessor.process(all_params)


if __name__ == "__main__":
    main()


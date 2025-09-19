import sys

class DowncaseIt:
    def process(params):
        if not params:
            print("none")
        else:
            for p in params:
                print(p.lower())


def main():
    all_params = sys.argv[1:]
    DowncaseIt.process(all_params)


if __name__ == "__main__":
    main()


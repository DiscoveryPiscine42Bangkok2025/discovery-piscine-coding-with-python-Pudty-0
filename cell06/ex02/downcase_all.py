
import sys

def downcase_it(params):
    if not params:
        print("none")
    else:
        for p in params:
            print(p.lower())


all_params = sys.argv[1:]


downcase_it(all_params)

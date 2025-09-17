import sys

if len(sys.argv) == 1:
    print("none")
else:
    print("parameters:", len(sys.argv) - 1)
    for p in sys.argv[1:]:
        print(p + ": " + str(len(p)))

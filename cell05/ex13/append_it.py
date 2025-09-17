import sys

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        match param.endswith("ism"):
            case True:
                pass  
            case False:
                print(param + "ism")

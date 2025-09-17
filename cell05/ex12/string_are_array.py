
import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    z_list = [] 

    for char in s:
        if char == "z":
            z_list.append("z")

    if len(z_list) == 0:
        print("none")
    else:
        print("".join(z_list))

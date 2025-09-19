


def add_one(x):
   
    x = x + 1
    print("Inside function:", x)


def main():
    num = 5
    print("Before function call:", num)

    add_one(num)

    print("After function call:", num)


if __name__ == "__main__":
    main()


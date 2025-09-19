


class NumberProcessor:
    def __init__(self, num):
        self.num = num

    def add_one(self):
        result = self.num + 1
        print("Inside method:", result)
        return result


def main():
    num = 5
    print("Before method call:", num)

    processor = NumberProcessor(num)
    processor.add_one()

    print("After method call:", num)


if __name__ == "__main__":
    main()



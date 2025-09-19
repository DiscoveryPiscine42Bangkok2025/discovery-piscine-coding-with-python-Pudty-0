
class Greetings:
    def greet(name="noble stranger"):
        if isinstance(name, str):
            print(f"Hello, {name}.")
        else:
            print("Error! It was not a name.")


def main():
    Greetings.greet('Alexandra')
    Greetings.greet('Wil')
    Greetings.greet()
    Greetings.greet(42)


if __name__ == "__main__":
    main()


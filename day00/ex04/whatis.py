import sys


def main():
    """This program prints whether the argument is even or odd."""
    try:
        assert len(sys.argv) < 3, \
            "AssertionError: more than one argument is provided"
        if len(sys.argv) == 2:
            try:
                int(sys.argv[1])
            except ValueError:
                print("AssertionError: argument is not an integer")
                return 1
            if int(sys.argv[1]) % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()

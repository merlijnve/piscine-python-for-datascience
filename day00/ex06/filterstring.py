import sys
from ft_filter import ft_filter


def main():
    "Main function."
    try:
        assert len(sys.argv) == 3 and sys.argv[2].isdigit() and \
            any(not c.isalnum() for c in sys.argv[1]), \
            "AssertionError: the arguments are bad"
        text = sys.argv[1].split()
        num = int(sys.argv[2])
        print(list(ft_filter(lambda s: len(s) > num, text)))
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()

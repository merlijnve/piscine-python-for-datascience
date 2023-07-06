import sys


def main():
    """Count the number of characters in a text."""
    upper_sum = 0
    lower_sum = 0
    punctuation_sum = 0
    digit_sum = 0
    space_sum = 0

    punctuation = [".", ",", ":", ";", "!", "?", "-", "_", "'",
                        "\"", "(", ")", "[", "]", "{", "}"]

    try:
        assert len(sys.argv) <= 2, "AssertionError: Too many arguments"
        if (len(sys.argv) == 1):
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]
        for char in text:
            if char.isupper():
                upper_sum += 1
            elif char.islower():
                lower_sum += 1
            elif char in punctuation:
                punctuation_sum += 1
            elif char.isdigit():
                digit_sum += 1
            elif char.isspace():
                space_sum += 1
        print(f"The text contains {len(text)} characters:")
        print(f"{upper_sum} upper letters")
        print(f"{lower_sum} lower letters")
        print(f"{punctuation_sum} punctuation marks")
        print(f"{space_sum} spaces")
        print(f"{digit_sum} digits")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()

import sys


def main():
    """Prints the Morse code of the given string."""
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        assert len(sys.argv) == 2 and sys.argv[1].isalnum(), \
            "AssertionError: the arguments are bad"
        morse = [NESTED_MORSE.get(c) for c in sys.argv[1].upper()]
        for i in range(len(morse) - 1):
            print(morse[i], end=" ")
        print(morse[-1])
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()

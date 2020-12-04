import sys
import string


def load_text(file):
    """Load a text file as a string."""
    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    """Solve null cipher based on number of letters after punctuation mark.

    message = null cipher text as string stripped of whitespace
    lookahead = endpoint of range of letters after punctuation mark to examine
    """
    for i in range(1, lookahead+1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}\n".format(i, plaintext))


def main():
    """Load text and solve null cipher"""
    filename = input("Enter full name and extension of file to translate: ")
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print("{}. Terminating program.".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nOriginal Message =")
    print("{}".format(loaded_message), "\n")
    print("\nList of punctuation marks to check = {}".format(string.punctuation), "\n")

    # remove whitespace:
    message = ''.join(loaded_message.split())
    # get range of possible cipher keys from user:
    while True:
        lookahead = input("\nHow many letters after punctuation do you check?: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)

    # run function to decode cipher
    solve_null_cipher(message, lookahead)


if __name__ == "__main__":
    main()

"""Decrypt text file to find hidden message

find nth letter in nth word to decrypt text file"""
import string
import re


def load_text(file):
    """Load text file as string"""
    with open(file) as f:
        return f.read().strip()


def solve_cipher(message_list, count):  # code message: drinkovaltine
    """Search for nth letter in nth words"""

    for i in range(0, count):
        results = ""
        # count every nth word
        word_list = message_list[i::i+1]
        # count every nth char
        for word in word_list:
            try:
                results += word[i]
            except IndexError:
                # word length too short
                pass
        print("Iteration: ", i+1, "\tPossible results: ", results)


def main():
    """Decipher coded text file"""
    message = load_text("colchester_message.txt")
    count = 0
    while True:
        user_input = input("Enter an integer for nth count: ")
        try:
            count = int(user_input)
            break
        except ValueError:
            print("Not a proper integer.")

    # strip punctuation, whitespace, and newlines from message
    message_list = re.split(r'[;,\s]\s*', message)

    solve_cipher(message_list, count)


if __name__ == "__main__":
    main()

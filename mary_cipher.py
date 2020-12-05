"""Hide MESSAGE string in a list of surnames."""
import sys
import string
import load_dictionary
from random import randint

# secret message to pass
MESSAGE = "Give your word and we rise"
FAKE_TEXT = "Merry Christmas from those named:\n"
name1 = "Jacob"
name2 = "Stuart"

# Hide the letters of MESSAGE in letter
# Alternate between second and third letter in every other word
# Include "Jacob" and "Stuart" into message but are null words
# Insert FAKE_TEXT into message but not used to hide MESSAGE


def main():
    """Generate names with MESSAGE embedded"""
    # open dictionary file
    name_list = load_dictionary.load("supporters.txt")
    # prep and parse MESSAGE for comparison process
    message = ''
    for char in MESSAGE.lower():
        if char in string.ascii_letters:
            message += char
    message = ''.join(message.split())
    output_names = []

    for letter in message:  # Breaks DRY, needs work
        is_even = True
        for name in name_list:
            if letter == name[1] and is_even is True and name not in output_names:
                output_names.append(name)
                print(letter, name)
                is_even = False
                break
            if letter == name[2] and is_even is False and name not in output_names:
                output_names.append(name)
                print(letter, name)
                is_even = True
                break


if __name__ == "__main__":
    main()

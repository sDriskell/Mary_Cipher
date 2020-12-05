"""Hide MESSAGE string in a list of surnames."""
import sys
import string
import load_dictionary
from random import randint

# secret message to pass
FAKE_TEXT = "Merry Christmas from those named:\n"
NAME1 = "JACOB"
NAME2 = "STUART"

# Hide the letters of MESSAGE in letter
# Alternate between second(even) and third(odd) letter in every other word
# Include "Jacob" and "Stuart" into message but are null words
# Insert FAKE_TEXT into message but not used to hide MESSAGE


def main():
    """Generate names with MESSAGE embedded"""
    user_message = input("What is your message to encrypt? ")
    # open dictionary file
    name_list = load_dictionary.load("supporters.txt")
    # prep and parse MESSAGE for comparison process
    message = ''
    for char in user_message.lower():
        if char in string.ascii_letters:
            message += char
    message = ''.join(message.split())
    output_names = []
    is_even = True  # tracks when to switch between odd/even for char comparison
    for letter in message:
        for i in range(0, len(name_list)):
            # grabs random name from list
            name = name_list[randint(0, len(name_list)-1)]
            # adds first name without starting process
            if len(output_names) == 0:
                pos = randint(0, len(name_list))
                output_names.append(name_list[pos])
            if is_even is True and letter == name[1] and name not in output_names:
                output_names.append(name)
                is_even = False
                break
            elif is_even is False and letter == name[2] and name not in output_names:
                output_names.append(name)
                is_even = True
                break
    # place null names in random index of output_names
    output_names.insert(randint(0, len(output_names)), NAME1)
    output_names.insert(randint(0, len(output_names)), NAME2)
    # display whole message
    print(FAKE_TEXT)
    for name in output_names:
        print(name)


if __name__ == "__main__":
    main()

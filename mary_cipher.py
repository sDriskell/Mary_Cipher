"""Hide MESSAGE string in a list of surnames."""
import sys
import string
import load_dictionary


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
    output_names = []
    for i in range(0, len(MESSAGE.split())+2):
        if i % 2 == 0:
            print(name_list[i][2])
        elif i / 2 != 0:
            print(name_list[i][3])


if __name__ == "__main__":
    main()

"""Decrypt text file to find hidden message

find nth letter in nth word to decrypt text file"""
import sys
import string


def load_text(file):
    """Load text file as string"""
    with open(file) as f:
        return f.read().strip()


def solve_cipher(message_list, count):  # code message: drinkovaltine
    """Search for nth letter in nth words"""
    results = ""
    # count every nth word
    word_list = message_list[count::count+1]
    print(word_list)
    # count every nth char
    for word in word_list:
        # combine into a string
        results += word[count]
    # print string
    print(results)


def main():
    """Decipher coded text file"""
    message = load_text("colchester_message.txt")
    count = int(input("How many steps to count word/char? "))
    # strip punctuation, whitespace, and newlines from message
    exclude = set(string.punctuation)
    message = ''.join(ch for ch in message if ch not in exclude)  # help from Ashish Cherian on Stack Overflow
    message = message.replace('\n', '').replace("  ", " ")  # yuck; need something better here
    message_list = message.split(" ")

    solve_cipher(message_list, count)


if __name__ == "__main__":
    main()

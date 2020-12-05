"""Decrypt text file to find hidden message

find nth letter in nth word to decrypt text file"""
import sys
import string


def load_text(file):
    """Load text file as string"""
    with open(file) as f:
        return f.read().strip()


def solve_cipher(message_list):  # code message: drinkovaltine
    """Search for nth letter in nth words"""
    for i in range(0, len(message_list)):
        count = 0
        text = ''
        for letter in message_list[i]:
            pass  # STUCK RIGHT HERE


def main():
    """Decipher coded text file"""
    message = load_text("colchester_message.txt")
    # strip punctuation, whitespace, and newlines from message
    exclude = set(string.punctuation)
    message = ''.join(ch for ch in message if ch not in exclude)  # help from Ashish Cherian on Stack Overflow
    message = message.replace('\n', '').replace("  ", " ")

    message_list = message.split(" ")
    print(message_list)

    solve_cipher(message_list)


if __name__ == "__main__":
    main()

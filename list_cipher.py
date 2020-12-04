from random import randint
import string
import load_dictionary

# write a short message that doesn't contain punctuation or numbers!
INPUT_MESSAGE = "Panel at the east end of chapel slides"


def main():
    """Create a message using INPUT_MESSAGE"""
    message = ''
    for char in INPUT_MESSAGE:
        if char in string.ascii_letters:
            message += char
    print(message, "\n")
    message = "".join(message.split())
    # open dictionary file
    word_list = load_dictionary.load("2of4brif.txt")
    # build vocabulary list with hidden message
    vocab_list = []
    for letter in message:
        size = randint(6, 10)
        for word in word_list:
            if len(word) == size and word[2].lower() == letter.lower() \
            and word not in vocab_list:
                vocab_list.append(word)
                break
    if len(vocab_list) < len(message):
        print("Word list too small; try larger dictionary or shorter message.")
    else:
        print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")


if __name__ == "__main__":
    main()

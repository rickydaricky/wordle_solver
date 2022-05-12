import collections
import csv
from words import WordsController
from tests import Tests


def retrieve_to_text(word_length, destination):
    """
    Tries every single word in the dictionary with length word_length 
    and appends the number of tries to get the result in the destination.

    Params:
    word_length: the length of the words to check
    destination: the file to put results in
    Returns: nothing
    """

    results = collections.defaultdict(list)
    wc = WordsController(word_length)

    for word in wc.word_options:
        results[Tests.test_word(word)].append(word)

    with open(destination, 'w') as f:
        for key, value in results.items():
            f.write(f'{key}: {value}\n\n')


def main():
    # Tests.test_word('slung')

    Tests.test_web()

    # retrieve_to_text(5, 'results.csv')


if __name__ == "__main__":
    main()

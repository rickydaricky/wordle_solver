from words import WordsController
from tests import Tests
import collections
import csv


def main():
    Tests.test_word('ascii')

    # results = collections.defaultdict(list)
    # wc = WordsController(5)
    # for word in wc.word_options:
    #     results[Tests.test_word(word)].append(word)

    # with open('results.csv', 'w') as f:
    #     for key, value in results.items():
    #         f.write(f'{key}: {value}\n\n')


    

if __name__ == "__main__":
    main()

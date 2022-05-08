from words import WordsController
from tests import Tests
import collections
import csv


def main():
    # Tests.test_word('zesty')

    results = collections.defaultdict(list)
    wc = WordsController(5)
    for word in wc.word_options:
        results[Tests.test_word(word)].append(word)

    csv_columns = ['Attempts', 'Words']

    with open('results.csv', 'w') as f:
        writer = csv.DictWriter()

    # c = collections.Counter(results)
    # print(c)

if __name__ == "__main__":
    main()

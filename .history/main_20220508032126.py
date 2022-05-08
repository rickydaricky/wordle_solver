from words import WordsController
from tests import Tests
import collections


def main():
    Tests.test_word('zesty')

    results = []
    wc = WordsController(5)
    for word in wc.word_options:
        results.append(Tests.test_word(word))

    c = collections.Counter(results)
    print()

if __name__ == "__main__":
    main()

from words import WordsController
from tests import Tests
import collections


def main():
    # Tests.test_word('zesty')

    results = []
    wc = WordsController(5)
    for word in wc.word_options:
        results.append(Tests.test_word(word))

    
    with open('')

    # c = collections.Counter(results)
    # print(c)

if __name__ == "__main__":
    main()

from words import WordsController
from tests import Tests
import collections


def main():
    # Tests.test_word('zesty')

    results = collections.defaultdict(list)
    wc = WordsController(5)
    for word in wc.word_options:
        results[Tests.test_word(word)].append(word)

    with open('results.csv', 'w') as f:
        f.write()

    # c = collections.Counter(results)
    # print(c)

if __name__ == "__main__":
    main()

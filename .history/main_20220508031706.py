from words import WordsController
from tests import Tests


def main():
    Tests.test_word('zesty')

    wc = WordsController(5)
    for word in wc.word_options:
        


if __name__ == "__main__":
    main()
